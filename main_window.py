"""
#-------------------------------------------------------------------
#                   CONFIDENTIAL --- Linux JDU auto test script
#-------------------------------------------------------------------
#
#                   @Project Name : Sisyphus
#
#                   @File Name    : main windows
#
#                   @Programmer   : Angus
#
#                   @Start Date   : 2022/03/25
#
#                   @Last Update  : 2023/05/23
#
#                   @Note: This is the UI windows for download.
#-------------------------------------------------------------------
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QFileDialog, QWidget, QPushButton
from config.devices_name_list import items_list
from log.logs import *
from test_scripts.testcase_chromedriver_update import checkChromeDriverUpdate
from test_scripts.testcase_linux import *
from ui.controller import retranslateUi
from test_scripts.testcase_linux import *
from test_scripts.testcase_windows import *


class DownloadComplete(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Download Complete')

        button = QPushButton('OK', self)
        button.move(85, 100)
        button.clicked.connect(self.close)

        self.show()


class EmittingStr(QtCore.QObject):
    textWritten = QtCore.pyqtSignal(str)  # 定义一个发送str的信号

    def write(self, text):
        self.textWritten.emit(str(text))


class EmittingStr2(QtCore.QObject):
    textWritten2 = QtCore.pyqtSignal(str)  # 定义一个发送str的信号

    def write(self, text):
        self.textWritten2.emit(str(text))


class checkGoogleDriver(QThread):
    def __init__(self):
        super().__init__()

    def run(self):
        checkChromeDriverUpdate()
        print("\n")
        print("Now, Please click the 1st button to choose the location that test package should save.")
        print("\n")
        print("Then click the 2nd button to the main windows - Download the test package！")


class startdownloadThread(QThread):
    def __init__(self):
        super().__init__()

    def run(self):
        testcaselist = Ui_JX_FW.excuteTestCase
        threads = []
        try:
            for testcase in testcaselist:
                testcase = "test" + testcase
                print('Start configure ' + testcase)
                thread = threading.Thread(target=eval(testcase))
                threads.append(thread)
                thread.start()

            for thread in threads:
                thread.join()
            print("All the test package that you choose is downloaded!")

        except Exception as e:
            print("Error")
            print(f"{e}")


class Ui_TesteEnviromentCheck(object):

    def __init__(self):
        sys.stdout = EmittingStr(textWritten=self.onUpdateText)
        sys.stderr = EmittingStr(textWritten=self.onUpdateText)

    def onUpdateText(self, text):
        cursor = self.textBrowser.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.textBrowser.setTextCursor(cursor)
        self.textBrowser.ensureCursorVisible()


    def slot_btn_chooseDir(self):
        print("\nWait a few seconds...")

        dir_choose = QFileDialog.getExistingDirectory()

        file = dir_choose if dir_choose else "/"

        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, 'config/saveDir.txt')

        try:
            with open(file_path, 'wt') as saveDir:
                saveDir.write(file)
            print(f"You have chosen this location that test package will keep: {file}")
            if dir_choose:
                self.chooseSaveDir2.setEnabled(True)
        except Exception as e:
            print(f"Error: {e}")

    def gotomainwindow(self):
        TesteEnviromentCheck.close()
        time.sleep(0.5)
        jx = Ui_JX_FW()
        jx.setupUi(JX_FW)
        JX_FW.show()

    def setupUi(self, TesteEnviromentCheck):
        TesteEnviromentCheck.setObjectName("TesteEnviromentCheck")
        # TesteEnviromentCheck.setStyleSheet("background-color: rgb(255, 255, 222);")
        # TesteEnviromentCheck.setPalette(palette)
        TesteEnviromentCheck.resize(600, 600)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(TesteEnviromentCheck)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.textBrowser = QtWidgets.QTextBrowser(TesteEnviromentCheck)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.chooseSaveDir = QtWidgets.QPushButton(TesteEnviromentCheck)
        self.chooseSaveDir.setMinimumSize(QtCore.QSize(0, 40))
        self.chooseSaveDir.setObjectName("next")
        self.chooseSaveDir2 = QtWidgets.QPushButton(TesteEnviromentCheck)
        self.chooseSaveDir2.setMinimumSize(QtCore.QSize(0, 40))
        self.chooseSaveDir2.setObjectName("chooseSaveDir")
        self.verticalLayout.addWidget(self.chooseSaveDir)
        self.verticalLayout.addWidget(self.chooseSaveDir2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.chooseSaveDir.clicked.connect(lambda: self.slot_btn_chooseDir())
        self.chooseSaveDir2.clicked.connect(lambda: self.gotomainwindow())
        self.chooseSaveDir2.setEnabled(False)
        self.font = QtGui.QFont()
        # Setup Font_size and Font Family
        self.font.setPointSize(12)
        self.font.setFamily("Arial")
        self.textBrowser.setFont(self.font)
        self.retranslateUi(TesteEnviromentCheck)
        QtCore.QMetaObject.connectSlotsByName(TesteEnviromentCheck)

    def retranslateUi(self, TesteEnviromentCheck):
        _translate = QtCore.QCoreApplication.translate
        TesteEnviromentCheck.setWindowTitle(
            _translate("TesteEnviromentCheck", "Xpress Package Download Tool - Test Enviroment check"))
        TesteEnviromentCheck.setWindowIcon(QIcon('config/jabra.ico'))
        self.chooseSaveDir.setText(_translate("TesteEnviromentCheck", "Select the folder to save test package"))
        self.chooseSaveDir2.setText(_translate("TesteEnviromentCheck", "Go to the Main Window"))
        TesteEnviromentCheck.setWindowIcon(QIcon('config/jabra.ico'))


class Ui_JX_FW(object):
    def __init__(self):
        sys.stdout = EmittingStr2(textWritten2=self.onUpdateText2)
        sys.stderr = EmittingStr2(textWritten2=self.onUpdateText2)

    def onUpdateText2(self, text):
        cursor = self.textbox_progress.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.textbox_progress.setTextCursor(cursor)
        self.textbox_progress.ensureCursorVisible()

    excuteTestCase = []

    # Add test case that user select to Ui_JX_FW.excuteTestCase.
    def add_testcase(self, testcase):
        testcase = testcase
        if testcase in Ui_JX_FW.excuteTestCase:
            Ui_JX_FW.excuteTestCase.remove(testcase)
            # print(Ui_JX_FW.excuteTestCase)
        elif (testcase == 'case4128'):
            if 'case4128_1' in Ui_JX_FW.excuteTestCase:
                Ui_JX_FW.excuteTestCase.remove('case4128_1')
                Ui_JX_FW.excuteTestCase.remove('case4128_2')
                Ui_JX_FW.excuteTestCase.remove('case4128_3')
                # print(Ui_JX_FW.excuteTestCase)
            else:
                Ui_JX_FW.excuteTestCase.append('case4128_1')
                Ui_JX_FW.excuteTestCase.append('case4128_2')
                Ui_JX_FW.excuteTestCase.append('case4128_3')
        elif (testcase == 'case4153'):
            if ('case4153_1' in Ui_JX_FW.excuteTestCase):
                Ui_JX_FW.excuteTestCase.remove('case4153_1')
                Ui_JX_FW.excuteTestCase.remove('case4153_2')
            else:
                Ui_JX_FW.excuteTestCase.append('case4153_1')
                Ui_JX_FW.excuteTestCase.append('case4153_2')
        elif (testcase == 'case10312'):
            if ('case10312w' in Ui_JX_FW.excuteTestCase):
                Ui_JX_FW.excuteTestCase.remove('case10312w')
            else:
                Ui_JX_FW.excuteTestCase.append('case10312w')
        elif (testcase == 'case6134'):
            Ui_JX_FW.excuteTestCase.append('case6134p')
            Ui_JX_FW.excuteTestCase.append(testcase)
        elif (testcase == 'case7551'):
            Ui_JX_FW.excuteTestCase.append('case7551p')
            Ui_JX_FW.excuteTestCase.append(testcase)
        elif (testcase == 'case7555'):
            Ui_JX_FW.excuteTestCase.append('case7555p')
            Ui_JX_FW.excuteTestCase.append(testcase)
        elif (testcase == 'case7556'):
            Ui_JX_FW.excuteTestCase.append('case7556p')
            Ui_JX_FW.excuteTestCase.append(testcase)
        elif (testcase == 'case16990'):
            Ui_JX_FW.excuteTestCase.append('case16990p')
            Ui_JX_FW.excuteTestCase.append(testcase)
        else:
            Ui_JX_FW.excuteTestCase.append(testcase)

    # Define the download function - - Start the new Thread.
    def startNewThread(self):
        self.startNewThread = startdownloadThread()
        # print("thread created")
        self.startNewThread.start()

    def saveDeviceName(self):
        DeviceName = self.combox_chooseDevice.currentText()
        print("Test device is " + DeviceName)
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, 'config/device.txt')
        try:
            with open(file_path, 'wt') as saveDir:
                saveDir.write(DeviceName)
        except Exception as e:
            print(script_dir,file_path)
            print(f"Error: {e}")

    def startbuttonevent(self):
        try:
            self.button_start.setEnabled(False)
            self.saveDeviceName()
            print("Download will start......")
            self.startNewThread()
        except Exception as e:
            print("Save device name failed:")
            print(f"{e}")

    def setupUi(self, JX_FW):
        JX_FW.setObjectName("JX_FW")
        JX_FW.resize(800, 1000)
        self.Layout_global = QtWidgets.QVBoxLayout(JX_FW)
        self.Layout_global.setObjectName("Layout_global")
        self.HLayout_first = QtWidgets.QHBoxLayout()
        self.HLayout_first.setObjectName("HLayout_first")
        self.label_theCurrentVersion = QtWidgets.QLabel(JX_FW)
        font = QtGui.QFont()
        font.setPointSize(12)

        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)

        self.HLayout_second = QtWidgets.QHBoxLayout()
        self.HLayout_second.setObjectName("HLayout_second")
        self.label_empty_1 = QtWidgets.QLabel(JX_FW)
        self.label_empty_1.setText("")
        self.label_empty_1.setObjectName("label_empty_1")
        self.HLayout_second.addWidget(self.label_empty_1)
        self.label_empty_2 = QtWidgets.QLabel(JX_FW)
        self.label_empty_2.setText("")
        self.label_empty_2.setObjectName("label_empty_2")
        self.HLayout_second.addWidget(self.label_empty_2)
        self.Layout_global.addLayout(self.HLayout_second)
        self.HLayout_third = QtWidgets.QHBoxLayout()
        self.HLayout_third.setObjectName("HLayout_third")
        self.label_empty_3 = QtWidgets.QLabel(JX_FW)
        self.label_empty_3.setEnabled(False)
        self.label_empty_3.setText("")
        self.label_empty_3.setObjectName("label_empty_3")
        self.HLayout_third.addWidget(self.label_empty_3)
        self.label_chooseDevice = QtWidgets.QLabel(JX_FW)
        font = QtGui.QFont()
        font.setPointSize(16)

        self.label_chooseDevice.setFont(font)
        self.label_chooseDevice.setWordWrap(True)
        self.label_chooseDevice.setObjectName("label_chooseDevice")
        self.HLayout_third.addWidget(self.label_chooseDevice)

        self.combox_chooseDevice = QtWidgets.QComboBox(JX_FW)
        self.combox_chooseDevice.setMinimumSize(QtCore.QSize(0, 35))
        self.combox_chooseDevice.setEditable(True)
        self.combox_chooseDevice.setObjectName("combox_chooseDevice")
        self.HLayout_third.addWidget(self.combox_chooseDevice)
        self.combox_chooseDevice.setStyleSheet("font-size: 16px;background-color: grey;")

        self.label_empty_4 = QtWidgets.QLabel(JX_FW)
        self.label_empty_4.setEnabled(False)
        self.label_empty_4.setText("")
        self.label_empty_4.setObjectName("label_empty_4")
        self.HLayout_third.addWidget(self.label_empty_4)
        self.Layout_global.addLayout(self.HLayout_third)
        self.HLayout_forth = QtWidgets.QGridLayout()
        self.HLayout_forth.setContentsMargins(-1, -1, 200, -1)
        self.HLayout_forth.setObjectName("HLayout_forth")
        self.label_Windows = QtWidgets.QLabel(JX_FW)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_Windows.sizePolicy().hasHeightForWidth())
        self.label_Windows.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_Windows.setFont(font)
        self.label_Windows.setToolTipDuration(0)
        self.label_Windows.setObjectName("label_Windows")
        self.HLayout_forth.addWidget(self.label_Windows, 0, 0, 1, 1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        self.label_Linux = QtWidgets.QLabel(JX_FW)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_Linux.sizePolicy().hasHeightForWidth())
        self.label_Linux.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_Linux.setFont(font)
        self.label_Linux.setToolTipDuration(0)
        self.label_Linux.setObjectName("label_Linux")
        self.HLayout_forth.addWidget(self.label_Linux, 0, 1, 1, 1)
        self.HLayout_forth.setColumnMinimumWidth(0, 5)
        self.HLayout_forth.setColumnMinimumWidth(1, 1)
        self.HLayout_forth.setColumnMinimumWidth(2, 5)
        self.HLayout_forth.setColumnStretch(0, 3)
        self.HLayout_forth.setColumnStretch(1, 1)
        self.HLayout_forth.setColumnStretch(2, 3)
        self.Layout_global.addLayout(self.HLayout_forth)
        self.HLayout_fifth = QtWidgets.QHBoxLayout()
        self.HLayout_fifth.setObjectName("HLayout_fifth")

        self.VLayout_win = QtWidgets.QVBoxLayout()
        self.VLayout_win.setObjectName("VLayout_win")
        # windows button - check all
        self.checkBox_checkAll_win = QtWidgets.QCheckBox(JX_FW)
        self.checkBox_checkAll_win.setObjectName("checkBox_checkAll_win")
        self.VLayout_win.addWidget(self.checkBox_checkAll_win)
        # testcase3961 -
        self.checkBox_case3961 = QtWidgets.QCheckBox(JX_FW)
        self.checkBox_case3961.setObjectName("checkBox_case3961")
        self.VLayout_win.addWidget(self.checkBox_case3961)
        self.checkBox_case3965 = QtWidgets.QCheckBox(JX_FW)
        self.checkBox_case3965.setObjectName("checkBox_case3965")
        self.VLayout_win.addWidget(self.checkBox_case3965)
        self.checkBox_case3966 = QtWidgets.QCheckBox(JX_FW)
        self.checkBox_case3966.setObjectName("checkBox_case3966")
        self.VLayout_win.addWidget(self.checkBox_case3966)
        self.checkBox_case3968 = QtWidgets.QCheckBox(JX_FW)
        self.checkBox_case3968.setObjectName("checkBox_case3968")
        self.VLayout_win.addWidget(self.checkBox_case3968)
        self.checkBox_case3969 = QtWidgets.QCheckBox(JX_FW)
        self.checkBox_case3969.setObjectName("checkBox_case3969")
        self.VLayout_win.addWidget(self.checkBox_case3969)
        self.checkBox_case4090 = QtWidgets.QCheckBox(JX_FW)
        self.checkBox_case4090.setObjectName("checkBox_case4090")
        self.VLayout_win.addWidget(self.checkBox_case4090)
        self.checkBox_case4128 = QtWidgets.QCheckBox(JX_FW)
        self.checkBox_case4128.setObjectName("checkBox_case4128")
        self.VLayout_win.addWidget(self.checkBox_case4128)
        self.checkBox_case4153 = QtWidgets.QCheckBox(JX_FW)
        self.checkBox_case4153.setObjectName("checkBox_case4153")
        self.VLayout_win.addWidget(self.checkBox_case4153)

        self.checkBox_case5509 = QtWidgets.QCheckBox(JX_FW)
        self.checkBox_case5509.setObjectName("checkBox_case5509")
        self.VLayout_win.addWidget(self.checkBox_case5509)

        self.checkBox_case5664 = QtWidgets.QCheckBox(JX_FW)
        self.checkBox_case5664.setObjectName("checkBox_case5664")
        self.VLayout_win.addWidget(self.checkBox_case5664)

        self.checkBox_case5665 = QtWidgets.QCheckBox(JX_FW)
        self.checkBox_case5665.setObjectName("checkBox_case5665")
        self.VLayout_win.addWidget(self.checkBox_case5665)
        self.checkBox_case7195 = QtWidgets.QCheckBox(JX_FW)
        self.checkBox_case7195.setObjectName("checkBox_case7195")
        self.VLayout_win.addWidget(self.checkBox_case7195)

        self.checkBox_case7196 = QtWidgets.QCheckBox(JX_FW)
        self.checkBox_case7196.setObjectName("checkBox_case7196")
        self.VLayout_win.addWidget(self.checkBox_case7196)

        self.checkBox_case10449 = QtWidgets.QCheckBox(JX_FW)
        self.checkBox_case10449.setObjectName("checkBox_case10449")
        self.VLayout_win.addWidget(self.checkBox_case10449)

        self.checkBox_case10312 = QtWidgets.QCheckBox(JX_FW)
        self.checkBox_case10312.setObjectName("checkBox_case10312")
        self.VLayout_win.addWidget(self.checkBox_case10312)

        self.checkBox_case3965_32b = QtWidgets.QCheckBox(JX_FW)
        self.checkBox_case3965_32b.setObjectName("checkBox_case3965_32b")
        self.VLayout_win.addWidget(self.checkBox_case3965_32b)

        self.checkBox_case3966_32b = QtWidgets.QCheckBox(JX_FW)
        self.checkBox_case3966_32b.setObjectName("checkBox_case3966_32b")
        self.VLayout_win.addWidget(self.checkBox_case3966_32b)

        self.checkBox_case4090_32b = QtWidgets.QCheckBox(JX_FW)
        self.checkBox_case4090_32b.setObjectName("checkBox_case4090_32b")
        self.VLayout_win.addWidget(self.checkBox_case4090_32b)

        self.checkBox_case5664_32b = QtWidgets.QCheckBox(JX_FW)
        self.checkBox_case5664_32b.setObjectName("checkBox_case5664_32b")
        self.VLayout_win.addWidget(self.checkBox_case5664_32b)

        self.checkBox_case5509_32b = QtWidgets.QCheckBox(JX_FW)
        self.checkBox_case5509_32b.setObjectName("checkBox_case5509_32b")
        self.VLayout_win.addWidget(self.checkBox_case5509_32b)

        self.checkBox_case5665_32b = QtWidgets.QCheckBox(JX_FW)
        self.checkBox_case5665_32b.setObjectName("checkBox_case5665_32b")
        self.VLayout_win.addWidget(self.checkBox_case5665_32b)

        self.HLayout_fifth.addLayout(self.VLayout_win)
        self.VLayout_linux = QtWidgets.QVBoxLayout()
        self.VLayout_linux.setObjectName("VLayout_linux")

        self.checkbox_selectAll_linux = QtWidgets.QCheckBox(JX_FW)
        self.checkbox_selectAll_linux.setObjectName("checkbox_selectAll_linux")
        self.VLayout_linux.addWidget(self.checkbox_selectAll_linux)

        self.checkBox_case6098 = QtWidgets.QCheckBox(JX_FW)
        self.checkBox_case6098.setObjectName("checkBox_case6098")
        self.VLayout_linux.addWidget(self.checkBox_case6098)

        self.checkBox_case6134 = QtWidgets.QCheckBox(JX_FW)
        self.checkBox_case6134.setObjectName("checkBox_case6134")
        self.VLayout_linux.addWidget(self.checkBox_case6134)

        self.checkBox_case7555 = QtWidgets.QCheckBox(JX_FW)
        self.checkBox_case7555.setObjectName("checkBox_case7555")
        self.VLayout_linux.addWidget(self.checkBox_case7555)

        self.checkBox_case7695 = QtWidgets.QCheckBox(JX_FW)
        self.checkBox_case7695.setObjectName("checkBox_case7695")
        self.VLayout_linux.addWidget(self.checkBox_case7695)

        self.checkBox_case7692 = QtWidgets.QCheckBox(JX_FW)
        self.checkBox_case7692.setObjectName("checkBox_case7692")
        self.VLayout_linux.addWidget(self.checkBox_case7692)

        self.checkBox_case7551 = QtWidgets.QCheckBox(JX_FW)
        self.checkBox_case7551.setObjectName("checkBox_case7551")
        self.VLayout_linux.addWidget(self.checkBox_case7551)

        self.checkBox_case7556 = QtWidgets.QCheckBox(JX_FW)
        self.checkBox_case7556.setObjectName("checkBox_case7556")
        self.VLayout_linux.addWidget(self.checkBox_case7556)

        self.checkBox_case10312_2 = QtWidgets.QCheckBox(JX_FW)
        self.checkBox_case10312_2.setObjectName("checkBox_case10312_2")
        self.VLayout_linux.addWidget(self.checkBox_case10312_2)

        self.checkBox_case16990 = QtWidgets.QCheckBox(JX_FW)
        self.checkBox_case16990.setObjectName("checkBox_case16990")
        self.VLayout_linux.addWidget(self.checkBox_case16990)

        self.checkBox_case16991 = QtWidgets.QCheckBox(JX_FW)
        self.checkBox_case16991.setObjectName("checkBox_case16991")
        self.VLayout_linux.addWidget(self.checkBox_case16991)

        self.HLayout_fifth.addLayout(self.VLayout_linux)
        self.Layout_global.addLayout(self.HLayout_fifth)
        self.HLayout_sixth = QtWidgets.QHBoxLayout()
        self.HLayout_sixth.setObjectName("HLayout_sixth")
        self.label_8 = QtWidgets.QLabel(JX_FW)
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.HLayout_sixth.addWidget(self.label_8)
        self.button_start = QtWidgets.QPushButton(JX_FW)
        self.button_start.setMinimumSize(QtCore.QSize(10, 40))
        self.button_start.setObjectName("button_start")
        self.HLayout_sixth.addWidget(self.button_start)
        self.label_9 = QtWidgets.QLabel(JX_FW)
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.HLayout_sixth.addWidget(self.label_9)
        self.Layout_global.addLayout(self.HLayout_sixth)
        self.HLayout_seventh = QtWidgets.QVBoxLayout()
        self.HLayout_seventh.setObjectName("HLayout_seventh")
        self.label = QtWidgets.QLabel(JX_FW)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.HLayout_seventh.addWidget(self.label)
        self.textbox_progress = QtWidgets.QTextBrowser(JX_FW)
        self.textbox_progress.setObjectName("textbox_progress")
        self.textbox_progress.resize(800, 300)
        self.HLayout_seventh.addWidget(self.textbox_progress)
        self.Layout_global.addLayout(self.HLayout_seventh)
        self.actionCheckall = QtWidgets.QAction(JX_FW)
        self.actionCheckall.setObjectName("actionCheckall")
        self.font = QtGui.QFont()
        self.font.setPointSize(12)
        self.font.setFamily("SimHei")
        self.textbox_progress.setFont(self.font)
        retranslateUi(self.label_chooseDevice, self.combox_chooseDevice, self.label_Windows, self.label_Linux,
                      self.checkBox_checkAll_win, self.checkBox_case3961, self.checkBox_case3965,
                      self.checkBox_case3966, self.checkBox_case3968, self.checkBox_case3969, self.checkBox_case4090,
                      self.checkBox_case4128, self.checkBox_case4153, self.checkBox_case5509, self.checkBox_case7196,
                      self.checkBox_case5664, self.checkBox_case5665, self.checkBox_case7195, self.checkBox_case10449,
                      self.checkBox_case10312, self.checkBox_case3965_32b, self.checkBox_case3966_32b,
                      self.checkBox_case4090_32b, self.checkBox_case5664_32b, self.checkBox_case5509_32b,
                      self.checkBox_case5665_32b, self.checkbox_selectAll_linux, self.checkBox_case6098,
                      self.checkBox_case6134, self.checkBox_case7555, self.checkBox_case7695, self.checkBox_case7692,
                      self.checkBox_case7551, self.checkBox_case7556, self.checkBox_case10312_2,
                      self.checkBox_case16990, self.checkBox_case16991, self.button_start, self.label,
                      self.actionCheckall, JX_FW)
        QtCore.QMetaObject.connectSlotsByName(JX_FW)

        # Define widget function
        i = 0
        while i < len(items_list):
            self.combox_chooseDevice.addItem(items_list[i])
            i = i + 1
        # Define check all button - windows
        self.checkBox_checkAll_win.clicked.connect(self.checkBox_case3961.click)
        self.checkBox_checkAll_win.clicked.connect(self.checkBox_case3965.click)
        self.checkBox_checkAll_win.clicked.connect(self.checkBox_case3966.click)
        self.checkBox_checkAll_win.clicked.connect(self.checkBox_case3969.click)
        self.checkBox_checkAll_win.clicked.connect(self.checkBox_case4090.click)
        self.checkBox_checkAll_win.clicked.connect(self.checkBox_case4128.click)
        self.checkBox_checkAll_win.clicked.connect(self.checkBox_case3968.click)
        self.checkBox_checkAll_win.clicked.connect(self.checkBox_case4153.click)
        self.checkBox_checkAll_win.clicked.connect(self.checkBox_case5509.click)
        self.checkBox_checkAll_win.clicked.connect(self.checkBox_case5664.click)
        self.checkBox_checkAll_win.clicked.connect(self.checkBox_case5665.click)
        self.checkBox_checkAll_win.clicked.connect(self.checkBox_case7195.click)
        self.checkBox_checkAll_win.clicked.connect(self.checkBox_case7196.click)
        self.checkBox_checkAll_win.clicked.connect(self.checkBox_case10449.click)
        self.checkBox_checkAll_win.clicked.connect(self.checkBox_case10312.click)
        self.checkBox_checkAll_win.clicked.connect(self.checkBox_case3965_32b.click)
        self.checkBox_checkAll_win.clicked.connect(self.checkBox_case3966_32b.click)
        self.checkBox_checkAll_win.clicked.connect(self.checkBox_case4090_32b.click)
        self.checkBox_checkAll_win.clicked.connect(self.checkBox_case5664_32b.click)
        self.checkBox_checkAll_win.clicked.connect(self.checkBox_case5509_32b.click)
        self.checkBox_checkAll_win.clicked.connect(self.checkBox_case5665_32b.click)

        # # Define check all button - Linux
        self.checkbox_selectAll_linux.clicked.connect(self.checkBox_case6098.click)
        self.checkbox_selectAll_linux.clicked.connect(self.checkBox_case6134.click)
        self.checkbox_selectAll_linux.clicked.connect(self.checkBox_case7555.click)
        self.checkbox_selectAll_linux.clicked.connect(self.checkBox_case7695.click)
        self.checkbox_selectAll_linux.clicked.connect(self.checkBox_case7692.click)
        self.checkbox_selectAll_linux.clicked.connect(self.checkBox_case7551.click)
        self.checkbox_selectAll_linux.clicked.connect(self.checkBox_case7556.click)
        self.checkbox_selectAll_linux.clicked.connect(self.checkBox_case10312_2.click)
        self.checkbox_selectAll_linux.clicked.connect(self.checkBox_case16990.click)
        self.checkbox_selectAll_linux.clicked.connect(self.checkBox_case16991.click)

        # Define function for Windows case checkbox
        self.checkBox_case3961.clicked.connect(lambda: self.add_testcase(self.checkBox_case3961.text()))
        self.checkBox_case3965.clicked.connect(lambda: self.add_testcase(self.checkBox_case3965.text()))
        self.checkBox_case3966.clicked.connect(lambda: self.add_testcase(self.checkBox_case3966.text()))
        self.checkBox_case3969.clicked.connect(lambda: self.add_testcase(self.checkBox_case3969.text()))
        self.checkBox_case3968.clicked.connect(lambda: self.add_testcase(self.checkBox_case3968.text()))
        self.checkBox_case4153.clicked.connect(lambda: self.add_testcase(self.checkBox_case4153.text()))
        self.checkBox_case4090.clicked.connect(lambda: self.add_testcase(self.checkBox_case4090.text()))
        self.checkBox_case4128.clicked.connect(lambda: self.add_testcase(self.checkBox_case4128.text()))
        self.checkBox_case5509.clicked.connect(lambda: self.add_testcase(self.checkBox_case5509.text()))
        self.checkBox_case5664.clicked.connect(lambda: self.add_testcase(self.checkBox_case5664.text()))
        self.checkBox_case5665.clicked.connect(lambda: self.add_testcase(self.checkBox_case5665.text()))
        self.checkBox_case7195.clicked.connect(lambda: self.add_testcase(self.checkBox_case7195.text()))
        self.checkBox_case10449.clicked.connect(lambda: self.add_testcase(self.checkBox_case10449.text()))
        self.checkBox_case10312.clicked.connect(lambda: self.add_testcase(self.checkBox_case10312.text()))
        self.checkBox_case3965_32b.clicked.connect(lambda: self.add_testcase(self.checkBox_case3965_32b.text()))
        self.checkBox_case3966_32b.clicked.connect(lambda: self.add_testcase(self.checkBox_case3966_32b.text()))
        self.checkBox_case4090_32b.clicked.connect(lambda: self.add_testcase(self.checkBox_case4090_32b.text()))
        self.checkBox_case5664_32b.clicked.connect(lambda: self.add_testcase(self.checkBox_case5664_32b.text()))
        self.checkBox_case5509_32b.clicked.connect(lambda: self.add_testcase(self.checkBox_case5509_32b.text()))
        self.checkBox_case5665_32b.clicked.connect(lambda: self.add_testcase(self.checkBox_case5664_32b.text()))
        # Define function for Linux case checkbox
        self.checkBox_case6098.clicked.connect(lambda: self.add_testcase(self.checkBox_case6098.text()))
        self.checkBox_case6134.clicked.connect(lambda: self.add_testcase(self.checkBox_case6134.text()))
        self.checkBox_case7555.clicked.connect(lambda: self.add_testcase(self.checkBox_case7555.text()))
        self.checkBox_case7695.clicked.connect(lambda: self.add_testcase(self.checkBox_case7695.text()))
        self.checkBox_case7692.clicked.connect(lambda: self.add_testcase(self.checkBox_case7692.text()))
        self.checkBox_case7551.clicked.connect(lambda: self.add_testcase(self.checkBox_case7551.text()))
        self.checkBox_case7556.clicked.connect(lambda: self.add_testcase(self.checkBox_case7556.text()))
        self.checkBox_case10312_2.clicked.connect(lambda: self.add_testcase(self.checkBox_case10312_2.text()))
        self.checkBox_case16990.clicked.connect(lambda: self.add_testcase(self.checkBox_case16990.text()))
        self.checkBox_case16991.clicked.connect(lambda: self.add_testcase(self.checkBox_case16991.text()))

        self.button_start.clicked.connect(lambda: self.startbuttonevent())


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    TesteEnviromentCheck = QtWidgets.QWidget()
    ui = Ui_TesteEnviromentCheck()
    ui.setupUi(TesteEnviromentCheck)
    TesteEnviromentCheck.setStyleSheet("background-image: url(Background.png);color: white;")
    TesteEnviromentCheck.show()

    # Recall the function that record the logs
    log = createLogger()
    log.info("Start the APP")

    # Define the Main Window
    app2 = QtWidgets.QApplication(sys.argv)
    JX_FW = QtWidgets.QWidget()
    JX_FW.setStyleSheet("background-image: url(Background.png);color: white;")
    # Check network
    ipaddress = check_network_access()
    print("INTRODUCE:")
    print("     THIS TEST TOOL to help Tester download the Xpress package")
    print("\n")
    print("Before downlaod,we need check the running environment:")
    print("Check Network : ")

    if ipaddress == True:
        print("  Supported network")
        print("\n")
        print("Start check Google Chrome driver....")
        checkDriver = checkGoogleDriver()
        checkDriver.start()

    else:
        print("     Unsupported netwrok")
        print("     Please Switch to the Supported network and restart the APP:")
        print("     -Intra-gnn.com")
        print("     -GN-Wifi")
        print("\n")
        print("Start check Google Chrome driver....")
        checkDriver = checkGoogleDriver()
        checkDriver.start()


    sys.exit(app.exec_())
    sys.exit(app2.exec_())
