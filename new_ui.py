import json
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from testcase_linux import *
from testcase_windows import *
import multiprocessing
from PyQt5.QtCore import QObject, pyqtSignal, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit
import sys
from testcase_chromedriver_update import *

def run_testcase(testcase_function):
    func = globals().get(testcase_function)
    if func is not None and callable(func):
        func()
    else:
        print(f"Function {testcase_function} not found or not callable.")

class TestcaseThread(multiprocessing.Process):
    output_signal = pyqtSignal(str)
    def __init__(self, testcase_function):
        super().__init__()
        self.testcase_function = testcase_function

    def run(self):
        run_testcase(self.testcase_function)

class checkGoogleDriver(QThread):
    def __init__(self):
        super().__init__()

    def run(self):
        checkChromeDriverUpdate()

class CheckNetworkThread(QThread):
    result_signal = pyqtSignal(bool)

    def run(self):
        try:
            http = urllib3.PoolManager()
            http.request('GET', 'http://dkcphweb15.corp.intra-gnn.com/')
            # http.request('GET', 'http://baidu.com/')
            self.result_signal.emit(True)
        except:
            self.result_signal.emit(False)

class TestcaseApp(QWidget):
    def __init__(self):
        super().__init__()

        self.save_location = None # To track if the user has selected a save location

        self.initUI()
        self.check_network_access()
        self.check_chromedriver()
        QTimer.singleShot(50, self.center)

    def load_device_values_from_json(self):
        with open('config.json', 'r') as file:
            data = json.load(file)
            return data['devices']

    def update_combobox_text(self):
        current_text = self.device_combobox.currentText()
        self.device_combobox.setEditText(current_text + " ▼")

        with open('config.json', 'r') as json_file:
            config_data = json.load(json_file)
        config_data['testdevice']=current_text;
        with open('config.json','w') as json_file:
            json.dump(config_data, json_file, indent=4)

    def load_testcase_data(self):
        with open('config.json', 'r') as file:
            data = json.load(file)
        return data['windows_testcases'], data['linux_testcases'], data['tooltips']

    def initUI(self):
        windows_testcases, linux_testcases, tooltips = self.load_testcase_data()

        layout = QVBoxLayout()
        testcases_layout = QHBoxLayout()  # This is the horizontal layout for the two testcases groups
        self.center()

        # Set the window icon
        self.setWindowIcon(QIcon('jabra.ico'))

        # Textbox to show program outputs
        self.output_textbox = QTextEdit(self)
        layout.addWidget(self.output_textbox)

        # Device selection
        self.device_combobox = QComboBox(self)
        self.device_combobox.addItem("Pls select test device")  # Add the placeholder text as the first item
        device_values = self.load_device_values_from_json()
        self.device_combobox.addItems(device_values)
        self.device_combobox.setCurrentIndex(0)  # Set the placeholder text as the current item
        self.device_combobox.setEditable(False)  # Ensure that the combobox is not editable
        layout.addWidget(self.device_combobox)
        self.device_combobox.currentTextChanged.connect(self.update_combobox_text)

        # Testcase groups
        # Windows Testcase checkboxes
        self.windows_group = QGroupBox('Windows Testcases')
        win_layout = QVBoxLayout()
        self.windows_checkboxes = {}
        for display_name, func_name in windows_testcases.items():
            cb = QCheckBox(display_name, self)
            cb.setToolTip(tooltips.get(func_name, ""))
            win_layout.addWidget(cb)
            self.windows_checkboxes[func_name] = cb
        self.windows_group.setLayout(win_layout)
        testcases_layout.addWidget(self.windows_group)

        # Linux Testcase checkboxes
        self.linux_group = QGroupBox('Linux Testcases')
        linux_layout = QVBoxLayout()
        self.linux_checkboxes = {}
        for display_name, func_name in linux_testcases.items():
            cb = QCheckBox(display_name, self)
            cb.setToolTip(tooltips.get(func_name, ""))
            linux_layout.addWidget(cb)
            self.linux_checkboxes[func_name] = cb
        self.linux_group.setLayout(linux_layout)
        testcases_layout.addWidget(self.linux_group)
        layout.addLayout(testcases_layout)

        # Create a horizontal layout for "Select All" buttons
        select_all_layout = QHBoxLayout()

        # Add a "Select All" button for Windows testcases
        select_all_win_button = QPushButton('Select All Windows Testcases', self)
        select_all_win_button.clicked.connect(self.select_all_windows_testcases)
        select_all_layout.addWidget(select_all_win_button)

        # Add a "Select All" button for Linux testcases
        select_all_linux_button = QPushButton('Select All Linux Testcases', self)
        select_all_linux_button.clicked.connect(self.select_all_linux_testcases)
        select_all_layout.addWidget(select_all_linux_button)

        # Add the buttons layout to the main layout
        layout.addLayout(select_all_layout)

        #Set the size of the UI
        self.resize(700, 700)


        # Directory selection
        self.dir_button = QPushButton('Select Directory', self)
        self.dir_button.clicked.connect(self.select_directory)
        layout.addWidget(self.dir_button)

        # Download button
        self.download_button = QPushButton('Download', self)
        layout.addWidget(self.download_button)
        self.download_button.setEnabled(False)
        self.download_button.clicked.connect(self.run_selected_testcases)

        self.setLayout(layout)
        self.setWindowTitle('JX1.0 package download tool')
        self.show()

        self.setStyleSheet("""
            QPushButton:hover {
                background-color: #FFFF52;
                border: 1px solid #EBEB00;
            }
        """)

    def center(self):
        screen_geometry = QDesktopWidget().availableGeometry()
        window_geometry = self.geometry()

        x = int((screen_geometry.width() - window_geometry.width()) / 2)
        y = int((screen_geometry.height() - window_geometry.height()) / 2)

        self.move(x, y)

    def select_all_windows_testcases(self):
        state = True if any([not cb.isChecked() for cb in self.windows_checkboxes.values()]) else False
        for cb in self.windows_checkboxes.values():
            cb.setChecked(state)

    def select_all_linux_testcases(self):
        state = True if any([not cb.isChecked() for cb in self.linux_checkboxes.values()]) else False
        for cb in self.linux_checkboxes.values():
            cb.setChecked(state)

    def run_selected_testcases(self):
        # 创建进程池
        pool = multiprocessing.Pool()

        for func, cb in self.windows_checkboxes.items():
            if cb.isChecked():
                thread = TestcaseThread(func)
                self.output_textbox.append(f"Running testcase: {func}")
                # thread.output_signal.connect(self.update_output)
                thread.start()

        # Repeat the same for Linux testcases
        for func, cb in self.linux_checkboxes.items():
            if cb.isChecked():
                thread = TestcaseThread(func)
                self.output_textbox.append(f"Running testcase: {func}")
                # thread.output_signal.connect(self.update_output)
                thread.start()

        pool.close()
        pool.join()

        print("All Downloads have completed.")

    def update_output(self, text):
        self.output_textbox.append(text)

    def select_directory(self):
        with open('config.json', 'r') as json_file:
            config_data = json.load(json_file)

        self.save_location = QFileDialog.getExistingDirectory(self, "Select Directory")
        if self.save_location:
            self.dir_button.setText(f"Directory: {self.save_location}")
            self.download_button.setEnabled(True)
            config_data['savedir'] = self.save_location
        with open('config.json','w') as json_file:
            json.dump(config_data, json_file, indent=4)

    def check_network_access(self):
        self.network_thread = CheckNetworkThread()
        self.network_thread.result_signal.connect(self.update_network_status)
        self.network_thread.start()

    def check_chromedriver(self):
        self.chromedriver_thread=checkGoogleDriver()
        self.chromedriver_thread.start()

    def update_network_status(self, result):
        if result:
            self.output_textbox.append("Network supports download.")
            self.output_textbox.append("Please choose the location you want to save the package")
        else:
            self.output_textbox.append("Network does not support download.")
            # Disable other components
            self.device_combobox.setDisabled(True)
            self.download_button.setDisabled(True)
            self.dir_button.setDisabled(True)

            # Optionally disable all testcases checkboxes
            for cb in self.windows_checkboxes.values():
                cb.setDisabled(True)
            for cb in self.linux_checkboxes.values():
                cb.setDisabled(True)

    def checkChromeDriverUpdate():
        chrome_version = getChromeVersion()
        driver_version = get_chromedriver_version()
        if chrome_version == driver_version:
            self.output_textbox.append("Same Version, No need to update.")
            return

        self.output_textbox.append("Lower Version for chromedriver detected, updating...")
        try:
            download_and_extract_chromedriver(chrome_version)
            self.output_textbox.append("Chromedriver updated successfully!")
        except requests.exceptions.Timeout:
            self.output_textbox.append("Chromedriver download failed. Check the network connection and try again.")
        except Exception as e:
            self.output_textbox.append(f"Chromedriver download failed due to: {e}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    with open('style.qss','r') as f:
        style = f.read()
        app.setStyleSheet(style)
    ex = TestcaseApp()
    sys.exit(app.exec_())
