import sys
import threading
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QCheckBox, QLabel, QGroupBox, QComboBox, \
    QHBoxLayout, QTextEdit, QFileDialog

# 导入您的测试用例函数
from test_scripts.testcase_windows import (
    testcase3961, testcase3965, testcase3966, testcase3968, testcase3969, testcase4090, testcase4128_1,
    testcase4128_2, testcase4128_3, testcase4153_1, testcase4153_2, testcase5509, testcase5664,
    testcase5665, testcase7195, testcase7196, testcase10449, testcase10312w, testcase3965_32b,
    testcase3966_32b, testcase4090_32b, testcase5509_32b, testcase5664_32b, testcase5665_32b,

)
from test_scripts.testcase_linux import(
    testcase6134, testcase7555, testcase7692, testcase7695, testcase7551, testcase7556,
    testcase10312l, testcase16990, testcase16991, testcase6098
)

class TestRunnerApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Test Runner")
        self.setGeometry(100, 100, 800, 400)

        layout = QHBoxLayout()

        # 创建设备选择下拉框
        self.device_combo = QComboBox()
        self.device_combo.addItem("Select Device")
        device_list = [
            'Jabra SPEAK2 40',
            'Jabra SPEAK2 55',
            # 添加其他设备名称
        ]
        self.device_combo.addItems(device_list)

        # 创建 Windows 部分的组
        windows_group = QGroupBox("Windows Test Cases")
        windows_layout = QVBoxLayout()
        self.add_checkboxes(windows_layout, [
            ("Test Case 3961", testcase3961),
            ("Test Case 3965", testcase3965),
            # 添加其他 Windows 测试用例
        ])
        windows_group.setLayout(windows_layout)

        # 创建 Linux 部分的组
        linux_group = QGroupBox("Linux Test Cases")
        linux_layout = QVBoxLayout()
        self.add_checkboxes(linux_layout, [
            ("Test Case 6134", testcase6134),
            ("Test Case 7555", testcase7555),
            # 添加其他 Linux 测试用例
        ])
        linux_group.setLayout(linux_layout)

        # 创建文本输出框1，用于显示check_network_access()和checkGoogleDriver()的结果
        self.result_output = QTextEdit()
        self.result_output.setReadOnly(True)

        # 创建文本输出框2，用于显示程序运行过程中的输出
        self.log_output = QTextEdit()
        self.log_output.setReadOnly(True)

        # 创建保存文件按钮
        self.save_button = QPushButton("Save Output to File")
        self.save_button.clicked.connect(self.save_output_to_file)

        # 创建开始按钮
        self.start_button = QPushButton("Start")
        self.start_button.clicked.connect(self.start_tests)

        # 左侧布局
        left_layout = QVBoxLayout()
        left_layout.addWidget(QLabel("Select Device:"))
        left_layout.addWidget(self.device_combo)
        left_layout.addWidget(QLabel("Test Case Selection:"))
        left_layout.addWidget(windows_group)
        left_layout.addWidget(linux_group)

        # 中间布局
        middle_layout = QVBoxLayout()
        middle_layout.addWidget(QLabel("Test Results:"))
        middle_layout.addWidget(self.result_output)

        # 右侧布局
        right_layout = QVBoxLayout()
        right_layout.addWidget(QLabel("Program Log:"))
        right_layout.addWidget(self.log_output)
        right_layout.addWidget(self.save_button)
        right_layout.addWidget(self.start_button)

        # 将左侧、中间和右侧布局添加到水平布局中
        layout.addLayout(left_layout)
        layout.addLayout(middle_layout)
        layout.addLayout(right_layout)

        self.setLayout(layout)

    def add_checkboxes(self, layout, test_cases):
        for name, func in test_cases:
            checkbox = QCheckBox(name)
            setattr(self, f"{name}_checkbox", checkbox)
            layout.addWidget(checkbox)

    def start_tests(self):
        selected_device = self.device_combo.currentText()
        if selected_device == "Select Device":
            self.result_output.append("Please select a device.")
            return

        selected_cases = []
        for name, func in selected_cases:
            checkbox = getattr(self, f"{name}_checkbox")
            if checkbox.isChecked():
                selected_cases.append(func)

        if not selected_cases:
            self.result_output.append("Please select at least one test case.")
            return

        # 启动多线程运行选定的测试用例
        threads = []
        for selected_case in selected_cases:
            thread = threading.Thread(target=selected_case)
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        self.result_output.append("Test cases completed.")

    def save_output_to_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_name, _ = QFileDialog.getSaveFileName(self, "Save Output to File", "", "Text Files (*.txt);;All Files (*)", options=options)
        if file_name:
            with open(file_name, 'w') as file:
                file.write(self.log_output.toPlainText())
                self.result_output.append(f"Output saved to {file_name}")

def main():
    app = QApplication(sys.argv)
    window = TestRunnerApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()