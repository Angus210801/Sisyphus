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
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon


def retranslateUi(label_chooseDevice, combox_chooseDevice, label_Windows, label_Linux, checkBox_checkAll_win,
                  checkBox_case3961, checkBox_case3965, checkBox_case3966, checkBox_case3968, checkBox_case3969,
                  checkBox_case4090, checkBox_case4128, checkBox_case4153, checkBox_case5509, checkBox_case7196,
                  checkBox_case5664, checkBox_case5665, checkBox_case7195, checkBox_case10449, checkBox_case10312,
                  checkBox_case3965_32b, checkBox_case3966_32b, checkBox_case4090_32b, checkBox_case5664_32b,
                  checkBox_case5509_32b, checkBox_case5665_32b, checkbox_selectAll_linux, checkBox_case6098,
                  checkBox_case6134, checkBox_case7555, checkBox_case7695, checkBox_case7692, checkBox_case7551,
                  checkBox_case7556, checkBox_case10312_2, checkBox_case16990, checkBox_case16991, button_start, label,
                  actionCheckall, JX_FW):
    _translate = QtCore.QCoreApplication.translate
    JX_FW.setWindowTitle(_translate("JX_FW", "Jabra Xpress Downlod tool"))

    label_chooseDevice.setText(_translate("JX_FW", "Choose Device   :"))
    combox_chooseDevice.setCurrentText(_translate("JX_FW", "Choose test device"))

    label_Windows.setText(_translate("JX_FW", "Windows Cases"))
    label_Linux.setText(_translate("JX_FW", "                                          Linux Cases "))
    checkBox_checkAll_win.setText(_translate("JX_FW", "Select All"))
    checkBox_checkAll_win.setStyleSheet("font-size: 16px;")
    checkBox_case3961.setText(_translate("JX_FW", "case3961"))
    checkBox_case3965.setText(_translate("JX_FW", "case3965"))
    checkBox_case3966.setText(_translate("JX_FW", "case3966"))
    checkBox_case3968.setText(_translate("JX_FW", "case3968"))
    checkBox_case3969.setText(_translate("JX_FW", "case3969"))
    checkBox_case4090.setText(_translate("JX_FW", "case4090"))
    checkBox_case4128.setText(_translate("JX_FW", "case4128"))
    checkBox_case4153.setText(_translate("JX_FW", "case4153"))
    checkBox_case5509.setText(_translate("JX_FW", "case5509"))
    checkBox_case7196.setText(_translate("JX_FW", "case7196"))
    checkBox_case5664.setText(_translate("JX_FW", "case5664"))
    checkBox_case5665.setText(_translate("JX_FW", "case5665"))
    checkBox_case7195.setText(_translate("JX_FW", "case7195"))
    checkBox_case10449.setText(_translate("JX_FW", "case10449"))
    checkBox_case10312.setText(_translate("JX_FW", "case10312"))
    checkBox_case3965_32b.setText(_translate("JX_FW", "case3965_32b"))
    checkBox_case3966_32b.setText(_translate("JX_FW", "case3966_32b"))
    checkBox_case4090_32b.setText(_translate("JX_FW", "case4090_32b"))
    checkBox_case5664_32b.setText(_translate("JX_FW", "case5664_32b"))
    checkBox_case5509_32b.setText(_translate("JX_FW", "case5509_32b"))
    checkBox_case5665_32b.setText(_translate("JX_FW", "case5665_32b"))

    checkbox_selectAll_linux.setText(_translate("JX_FW", "Select All"))
    checkbox_selectAll_linux.setStyleSheet("font-size: 16px;")
    checkBox_case6098.setText(_translate("JX_FW", "case6098"))
    checkBox_case6134.setText(_translate("JX_FW", "case6134"))
    checkBox_case7555.setText(_translate("JX_FW", "case7555"))
    checkBox_case7695.setText(_translate("JX_FW", "case7695"))
    checkBox_case7692.setText(_translate("JX_FW", "case7692"))
    checkBox_case7551.setText(_translate("JX_FW", "case7551"))
    checkBox_case7556.setText(_translate("JX_FW", "case7556"))
    checkBox_case10312_2.setText(_translate("JX_FW", "case10312l"))
    checkBox_case16990.setText(_translate("JX_FW", "case16990"))
    checkBox_case16991.setText(_translate("JX_FW", "case16991"))

    # 设置checkbox的名称显示字体的大小



    toolTip_dict = {
        "case3961": "FW:leaveunchage;Settings:All defualt value;JD install:Yes;Protect:Yes",
        "case3965": "FW:leaveunchage;Settings:leaveunchage;JD install:Yes;Protect:Yes",
        "case3966": "FW:higher version;Settings:leaveunchage;JD install:Yes;Protect:leaveunchage",
        "case3968": "manage by Jabra",
        "case3969": "FW:leaveunchage;Settings:random/default;JD install:Yes;Protect:Not",
        "case4090": "FW:higher version;Settings:diff from default;JD install:not;Protect:not",
        'case4128': "FW:leaveunchage;Settings:default/leaveunchage/diff from default;JD install:not.",
        'case4153': "2/3 packages FW:all available;Settings:leaveunchage;JD install:not;Protect:not",
        "case5509": "FW:higher version;Settings:leaveunchage;JD install:Yes;Protect:not",
        "case5664": "FW:leaveunchage;Settings:MAX;JD install:Yes;Protect:Yes",
        "case5665": "FW:leaveunchage;Settings:Min;JD install:Yes;Protect:Yes",
        "case7195": "FW:lower version;Settings:random;JD install:Yes;Protect:random",
        "case7196": "FW:higher version;Settings:random;DUT in power-off mode",
        "case10449": "FW:leaveunchage;Settings:leaveunchage;JD install:Yes;Protect:Yes",
        "case10312": "Language case,will download all language if device has languange setting",
        "case3965_32b": "FW:leaveunchage;Settings:leaveunchage;JD install:Yes;Protect:Yes",
        "case3966_32b": "FW:higher version;Settings:leaveunchage;JD install:Yes;Protect:leaveunchage",
        "case4090_32b": "FW:higher version;Settings:diff from default;JD install:not;Protect:not",
        "case5509_32b": "FW:higher version;Settings:leaveunchage;JD install:Yes;Protect:not",
        "case5664_32b": "FW:leaveunchage;Settings:MAX;JD install:Yes;Protect:Yes",
        "case5665_32b": "FW:leaveunchage;Settings:Min;JD install:Yes;Protect:Yes",
        "case6098": "Verify zip package content and JXDU version by creating a ZIP file.",
        "case6134": "FW:leaveunchage;Settings:leaveunchage;Protect:Yes",
        "case7555": "FW:higher version;Settings:leaveunchage;Protect:Yes",
        "case7695": "FW:leaveunchage;Settings:MAX;Protect:not",
        "case7692": "FW:leaveunchage;Settings:Min;Protect:Yes",
        "case7551": "FW:higher version;Settings:differ from default;Protect:Yes",
        "case7556": "FW:higher version;Settings:default value;Protect:not",
        "case10312_2": "Language case,will download all language if device has languange setting",
        "case16990": "FW:higher version;Settings:leaveunchage;Protect:not;Allow downgrade",
        "case16991": "FW:higher version;Settings:leaveunchage;Protect:not;not Allow downgrade",

    }
    toolTip_template = "<font color={color} size={size}>{text}</font>"
    checkBox_list = [checkBox_case3961, checkBox_case3965, checkBox_case3966, checkBox_case3968, checkBox_case3969, checkBox_case4090,
                     checkBox_case4128, checkBox_case4153, checkBox_case5509, checkBox_case5664, checkBox_case5665,
                     checkBox_case7195, checkBox_case7196, checkBox_case10449, checkBox_case10312, checkBox_case3965_32b,
                     checkBox_case3966_32b, checkBox_case4090_32b, checkBox_case5664_32b, checkBox_case5509_32b, checkBox_case5665_32b,
                     checkBox_case6098, checkBox_case6134, checkBox_case7555, checkBox_case7695, checkBox_case7692,
                     checkBox_case7551, checkBox_case7556, checkBox_case10312_2,checkBox_case16990, checkBox_case16991]
    for checkBox in checkBox_list:
        checkBox.setStyleSheet("font-size: 16px;")
        checkBox_name = "_".join(checkBox.objectName().split("_")[1:])
        toolTip_text = toolTip_dict[checkBox_name]
        toolTip_html = toolTip_template.format(color="red", size=4, text=toolTip_text)
        checkBox.setToolTip(_translate("JX_FW", toolTip_html))

    button_start.setText(_translate("JX_FW", "Start"))
    label.setText(_translate("JX_FW", "Download Progress"))
    actionCheckall.setText(_translate("JX_FW", "Checkall"))
    JX_FW.setWindowIcon(QIcon('../config/jabra.ico'))
