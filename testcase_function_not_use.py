"""
#-------------------------------------------------------------------
#                   CONFIDENTIAL --- JX FW Download Tool
#-------------------------------------------------------------------
#
#                   @Project Name : Sisyphus
#
#                   @File Name    : main windows
#
#                   @Programmer   : Angus
#
#                   @Start Date   : 2021/02/25
#
#                   @Last Update  : 2023/05/23
#
#                   @Note: This is the UI windows for download.
#-------------------------------------------------------------------
"""
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from selenium import webdriver

items_list=['Jabra BIZ 1500 MS USB Duo',
'Jabra BIZ 1500 MS USB Mono',
'Jabra BIZ 1500 USB Duo',
'Jabra BIZ 1500 USB Mono',
'Jabra BIZ 2300 USB Duo',
'Jabra BIZ 2300 USB Mono',
'Jabra BIZ 2400 II CC USB Mono',
'Jabra BIZ 2400 II CC USB Stereo',
'Jabra BIZ 2400 II Duo',
'Jabra EVOLVE2 75',
'Jabra BIZ 2400 II Mono',
'Jabra BIZ 2400 USB Duo',
'Jabra BIZ 2400 USB Mono',
'Jabra DIAL 550',
'Jabra Engage 40 Mono',
'Jabra Engage 40 Stereo',
'Jabra Engage 50 II Mono',
'Jabra Engage 50 II Stereo',
'Jabra Engage 50',
'Jabra PanaCast 20',
'Jabra Engage 65',
'Jabra Engage 75',
'Jabra EVOLVE 20 Mono',
'Jabra EVOLVE 20 SE Mono',
'Jabra EVOLVE 20 SE Stereo',
'Jabra EVOLVE 20 Stereo',
'Jabra EVOLVE 30 II Mono',
'Jabra EVOLVE 30 II Stereo',
'Jabra EVOLVE 30 Mono',
'Jabra EVOLVE 30 Stereo',
'Jabra EVOLVE 40 Mono',
'Jabra EVOLVE 40/80 Stereo',
'Jabra EVOLVE 65 Mono',
'Jabra EVOLVE 65 Stereo',
'Jabra Evolve 65e',
'Jabra Evolve 75',
'Jabra Evolve 75e',
'Jabra EVOLVE2 40',
'Jabra Evolve2 65 Deskstand',
'Jabra EVOLVE2 65 Mono',
'Jabra EVOLVE2 65 Stereo',
'Jabra EVOLVE2 85',
'Jabra Evolve2 85 Deskstand',
'Jabra GN2000 MS USB Mono / Duo',
'Jabra GN2000 USB Mono / Duo',
'Jabra GO 6470',
'Jabra HANDSET 450',
'Jabra LINK 220 QD to USB Adapter',
'Jabra LINK 220a QD to USB Adapter',
'Jabra LINK 230 QD to USB Adapter',
'Jabra LINK 260 MS QD to USB Adapter',
'Jabra LINK 260 QD to USB Adapter',
'Jabra LINK 265 QD to USB Training Adapter',
'Jabra LINK 280 QD to USB Adapter',
'Jabra LINK 350 (GO 6430)',
'Jabra LINK 360',
'Jabra LINK 370',
'Jabra LINK 370 MS Teams',
'Jabra Link 380a',
'Jabra LINK 380c',
'Jabra LINK 850',
'Jabra LINK 860',
'Jabra LINK 950',
'Jabra MOTION OFFICE',
'Jabra PanaCast 20',
'Jabra MOTION UC',
'Jabra PRO 925 Dual Connectivity',
'Jabra PRO 925 Single Connectivity',
'Jabra PRO 930',
'Jabra PRO 935 Dual Connectivity',
'Jabra PRO 935 Single Connectivity',
'Jabra PRO 9450 Series',
'Jabra PRO 9460 Series',
'Jabra PRO 9465 / 9470',
'Jabra SPEAK 410',
'Jabra SPEAK 450 Cisco',
'Jabra SPEAK 510',
'Jabra SPEAK 710',
'Jabra SPEAK 750 MS Teams',
'Jabra SPEAK 750 UC',
'Jabra SPEAK 810',
'Jabra STEALTH UC',
'Jabra SUPREME UC',
'Jabra UC VOICE 150a Duo (Version A)',
'Jabra UC VOICE 150a Mono (Version A)',
'Jabra UC VOICE 150a MS Duo (Version A)',
'Jabra UC VOICE 150a MS Mono (Version A)',
'Jabra UC VOICE 250a (Version A)',
'Jabra UC VOICE 250a MS (Version A)',
'Jabra UC VOICE 550a Duo (Version A)',
'Jabra UC VOICE 550a Mono (Version A)',
'Jabra UC VOICE 550a MS Duo (Version A)',
'Jabra UC VOICE 550a MS Mono (Version A)',
'Jabra UC VOICE 750a Duo (Version A)',
'Jabra UC VOICE 750a Mono (Version A)',
'Jabra UC VOICE 750a MS Duo (Version A)',
'Jabra UC VOICE 750a MS Mono (Version A)',
'Jabra EVOLVE2 30'
]

global xpress_version
class Widget(QWidget):
  def __init__(self, *args, **kwargs):

    super(Widget, self).__init__(*args, **kwargs)
    layout = QVBoxLayout(self)
    self.lineedit = QLineEdit(self, minimumWidth=200)

#Choose what platform need to downlood
    self.linuxButton=QRadioButton("     Linux")
    self.linuxButton.move(10,10)
    self.winButton  =QRadioButton("     Windows")
    self.bothButton =QRadioButton("     Both")

    self.submitButton=QPushButton("Submit",minimumWidth=200)

    layout.addWidget(QLabel("Choose Device：", self))
    layout.addWidget(self.lineedit)
    layout.addItem(QSpacerItem(20, 5, QSizePolicy.Expanding, QSizePolicy.Minimum))

    layout.addWidget(QLabel("Choose Platform：", self))

  #Create a button group
    self.buttonGroup=QButtonGroup(self)
    self.buttonGroup.addButton(self.linuxButton,11)
    self.buttonGroup.addButton(self.winButton,12)
    self.buttonGroup.addButton(self.bothButton,13)
    self.infor1=''

    self.buttonGroup.buttonClicked.connect(self.choosePlat)

    layout.addWidget(self.linuxButton,0,Qt.AlignTop)
    layout.addWidget(self.winButton,0,Qt.AlignTop)
    layout.addWidget(self.bothButton,0,Qt.AlignTop)


    layout.addWidget(self.submitButton)
    #初始化combobox
    self.initUI()
    self.init_lineedit()
    # self.init_combobox()
    self.setGeometry(850, 300, 300, 100)

    #增加选中事件
    #self.combobox.activated.connect(self.on_combobox_Activate)
    self.submitButton.clicked.connect(self.submitEvent)
    self.submitButton.clicked.connect(self.close)

  def init_lineedit(self):
    # 增加自动补全

    self.completer = QCompleter(items_list)
    # 设置匹配模式 有三种： Qt.MatchStartsWith 开头匹配（默认） Qt.MatchContains 内容匹配 Qt.MatchEndsWith 结尾匹配
    self.completer.setFilterMode(Qt.MatchContains)
    # 设置补全模式 有三种： QCompleter.PopupCompletion（默认） QCompleter.InlineCompletion  QCompleter.UnfilteredPopupCompletion
    self.completer.setCompletionMode(QCompleter.PopupCompletion)
    # 给lineedit设置补全器
    self.lineedit.setCompleter(self.completer)

  def submitEvent(self):
    #设置点击按钮时的事件：提交device name、platform、关闭窗口
    self.saveDeviceName()
    self.getPlatForm()


  def saveDeviceName(self):
      DeviceName=self.lineedit.text().capitalize()
      print("Test device is " + DeviceName)
      fo = open("config/device.txt", "wt")
      fo.write(DeviceName)
      fo.close()


  def getPlatForm(self):
     if self.infor1=='Windows' or self.infor1=='Linux':
         print("Start download "+self.infor1+" cases")
     else:
         print("Start downlaod ALL case")
     plat=self.infor1
     platformFile = open("config/platform.txt", "wt")
     platformFile.write(plat)
     platformFile.close()



  def choosePlat(self):
     sender=self.sender()
     if sender==self.buttonGroup:
         if self.buttonGroup.checkedId()==11:
             self.infor1='Linux'
         elif self.buttonGroup.checkedId()==12:
             self.infor1='Windows'
         else:
             self.infor1='Both'

  def initUI(self):
    self.setWindowTitle('JX_FW_DOWNLOAD')
    self.setWindowIcon(QIcon('config/jabra.ico'))
    self.show()


def getXpressVersion():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(chrome_options=options)

    concurrentversion="hello"

    xpress_version = concurrentversion
    xpress_version = xpress_version[13:21]
    return xpress_version

if __name__ == '__main__':
    test=getXpressVersion()
    print(test)