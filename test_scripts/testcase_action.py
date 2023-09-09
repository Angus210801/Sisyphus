"""
#-------------------------------------------------------------------
#                   CONFIDENTIAL --- JX FW Download Tool
#-------------------------------------------------------------------
#
#                   @Project Name : Sisyphus
#
#                   @File Name    : testcase_action
#
#                   @Programmer   : Angus
#
#                   @Start Date   : 2021/02/25
#
#                   @Last Update  : 2023/05/23
#
#                   @Note: This file is contain the fuction that we want to do in the Xpress, it is for testcase_linux and test_windows call.
#-------------------------------------------------------------------
"""

import os
import random
import shutil
import sys
import zipfile
from telnetlib import EC
from time import sleep

import urllib3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from test_scripts.testcase_element_exist import isElementExist, isInputExist, isUploadButton


class BaseConfigure(object):
    def __init__(self, driver):
        self.driver = driver

    def click(self, *button):
        self.driver.find_element(*button).click()

    def click(self, *device):
        self.driver.find_element(*device).click()

    def window_position(self) -> object:
        self.update_idletasks()
        x = (self.winfo_screenwidth() - self.winfo_reqwidth()) / 2
        y = (self.winfo_screenheight() - self.winfo_reqheight()) / 2
        self.geometry("+%d+%d" % (x, y))
        self.mainloop()


class InitLinuxTrack(BaseConfigure):
    def __init__(self, driver):
        BaseConfigure.__init__(self, driver)
        # driver.get('http://dkcphweb15/')
        # test_address = driver.find_element(By.LINK_TEXT, 'Start Page').get_attribute("href")
        test_address = "http://dkcphweb15.corp.intra-gnn.com/Xpress/40.X.Development/MDCT"
        driver.get(test_address + '/thin-client')

    def click_next_button(self):
        button = (By.CLASS_NAME, 'button-container')
        self.click(*button)

    def select_device(self):
        fo = open("../config/device.txt", "rt")
        test_device_name = fo.read()
        device = (By.XPATH, "//label[contains(text(),'" + test_device_name + "')]")
        self.click(*device)
        self.driver.find_element(By.ID, 'btnAdd').send_keys(Keys.ENTER)
        self.driver.find_element(By.XPATH, "//input[@value='NEXT >']").click()


class InitWindowsTrack(BaseConfigure):

    def __init__(self, driver):
        BaseConfigure.__init__(self, driver)
        driver.get('http://dkcphweb15/')
        test_address = driver.find_element(By.LINK_TEXT, 'Start Page').get_attribute("href")
        # test_address="http://dkcphweb15.corp.intra-gnn.com/Xpress/40.X.Development/MDCT"
        driver.get(test_address + '/windows-desktop')

    def goto_selectdevice_page(self):
        """ Click the New button go to select device page """
        button = (By.CLASS_NAME, 'button-container')
        self.click(*button)

    def action_selectdevice_page(self):
        """ Select device and click next button """
        fo = open("../config/device.txt", "rt")
        test_device_name = fo.read()
        device = (By.XPATH, "//label[contains(text(),'" + test_device_name + "')]")
        self.click(*device)
        self.driver.find_element(By.ID, 'btnAdd').send_keys(Keys.ENTER)
        self.driver.find_element(By.XPATH, "//input[@value='NEXT >']").click()


def browser_configure():
    """ Configure the browser"""
    fo = open("../config/device.txt", "rt")
    test_device_name = fo.read()
    test_device_name = test_device_name.replace("Jabra", "").replace(" ", "").lower()
    file = get_save_dir()
    file = file.replace('\\\\', '\\')
    file = file + test_device_name
    options = webdriver.ChromeOptions()
    prefs = {"download.default_directory": file, "download.prompt_for_download": False, 'safebrowsing.enabled': True}
    options.add_experimental_option('prefs', prefs)
    options.add_argument('--headless')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    return options


def check_network_access():
    try:
        http = urllib3.PoolManager()
        http.request('GET', 'http://dkcphweb15.corp.intra-gnn.com/')
        return True
    except:
        return False


def get_save_dir():
    # 获取保存路径
    fo = open("../config/saveDir.txt", "rt")
    saveDir = fo.read() + "/"
    saveDir = saveDir.replace('/', '\\\\')
    return saveDir


def settings_default(driver):
    # 选择默认配置
    driver.find_element_by_xpath("//input[@value='SET ALL TO DEFAULT VALUES']").click()


def config_the_protect_as_yes(driver):
    setting = driver.find_element_by_css_selector(
        "select[name='configurationViewModel.Devices[0].SelectedFirmware.Settings[0].SelectedValue']")
    Select(setting).select_by_index("1")


def config_the_protect_as_no(driver):
    setting = driver.find_element_by_css_selector(
        "select[name='configurationViewModel.Devices[0].SelectedFirmware.Settings[0].SelectedValue']")
    Select(setting).select_by_index("2")


def config_the_latest_FW(driver):
    fw_select = driver.find_element_by_css_selector(
        "select[name='configurationViewModel.Devices[0].SelectedFirmware.Id']")
    Select(fw_select).select_by_index("1")
    driver.find_element_by_css_selector("input[name='configurationViewModel.Devices[0].Downgrade']").click()


def config_the_FW_as_manage_by_jabra(driver):
    fw_select = driver.find_element_by_css_selector(
        "select[name='configurationViewModel.Devices[0].SelectedFirmware.Id']")
    Select(fw_select).select_by_value('2147457433')


def config_the_FW_as_lower_than_latest(driver):
    fw_select = driver.find_element_by_css_selector(
        "select[name='configurationViewModel.Devices[0].SelectedFirmware.Id']")
    fwList = Select(fw_select)
    fwNum = len(fwList.options)
    if fwNum == 4:
        i = fwNum - 2
        Select(fw_select).select_by_index(i)
        driver.find_element_by_css_selector("input[name='configurationViewModel.Devices[0].Downgrade']").click()
    elif fwNum == 3:
        i= fwNum - 1
        Select(fw_select).select_by_index(i)
        driver.find_element_by_css_selector("input[name='configurationViewModel.Devices[0].Downgrade']").click()


def config_allow_downgrade(driver):
    driver.find_element_by_css_selector("input[name='configurationViewModel.Devices[0].Downgrade']").click()


def config_settings_as_random(driver):
    set_table = driver.find_element_by_class_name('settings-table')
    td_content = set_table.find_elements_by_tag_name('tr')
    table_tr_number = len(td_content)
    i = 1
    while i < table_tr_number:
        flag = isElementExist(driver,
                              "select[name='configurationViewModel.Devices[0].SelectedFirmware.Settings[" + str(
                                  i) + "].SelectedValue']")
        if flag:
            setting = driver.find_element_by_css_selector(
                "select[name='configurationViewModel.Devices[0].SelectedFirmware.Settings[" + str(
                    i) + "].SelectedValue']")
            if Select(setting):
                select = Select(setting)
                selectlen = len(select.options)
                Select(setting).select_by_index(random.randint(1, selectlen - 1))
                i = i + 1
                continue
        elif isInputExist(driver,
                          "input[name='configurationViewModel.Devices[0].SelectedFirmware.Settings[" + str(
                              i) + "].SelectedValue']"):
            try:
                driver.find_element_by_css_selector(
                    "input[name='configurationViewModel.Devices[0].SelectedFirmware.Settings[" + str(
                        i) + "].SelectedValue']").send_keys('2021')
            except:
                i = i + 1
                continue
            i = i + 1
            continue
        else:
            i = i + 1
            continue

    nextButton = driver.find_element_by_xpath("//input[@value='NEXT >']")
    isNextButtonEnable = nextButton.is_enabled()

    if isNextButtonEnable == False:
        i = 0
        while i < table_tr_number:
            flag = isElementExist(driver,
                                  "select[name='configurationViewModel.Devices[0].SelectedFirmware.Settings[" + str(
                                      i) + "].SelectedValue']")
            if flag:
                setting = driver.find_element_by_css_selector(
                    "select[name='configurationViewModel.Devices[0].SelectedFirmware.Settings[" + str(
                        i) + "].SelectedValue']")
                if Select(setting):
                    i = i + 1
                    continue
            elif isInputExist(driver,
                              "input[name='configurationViewModel.Devices[0].SelectedFirmware.Settings[" + str(
                                  i) + "].SelectedValue']"):
                try:
                    driver.find_element_by_css_selector(
                        "input[name='configurationViewModel.Devices[0].SelectedFirmware.Settings[" + str(
                            i) + "].SelectedValue']").send_keys('2021')
                    i = i + 1
                    continue
                except Exception as e:
                    i = i + 1
                    continue
            elif isUploadButton(driver, "input[value='Upload']"):
                try:
                    driver.find_element_by_css_selector(
                        "input[id='configurationViewModel.Devices[0].SelectedFirmware.Settings[36].fileinputId']").send_keys(
                        "C:\\download\\bat.bmp")
                    sleep(5)
                    i = i + 1
                    continue
                except Exception as e:
                    print(e)
            else:
                i = i + 1
                continue


# 优化后的代码

def config_settings_as_not_default(driver):
    def build_selector(base, index):
        return f"configurationViewModel.Devices[0].SelectedFirmware.Settings[{index}].SelectedValue"

    def find_element_by_selector(base, index):
        return driver.find_element_by_css_selector(f"{base}[name='{build_selector(base, index)}']")

    def element_exists(base, index):
        try:
            find_element_by_selector(base, index)
            return True
        except:
            return False

    def random_select_option(select_element):
        options_len = len(select_element.options)
        while True:
            selected_option = select_element.options[random.randint(1, options_len - 1)]
            if '*' not in selected_option.text:
                selected_option.click()
                break

    set_table = driver.find_element_by_class_name('settings-table')
    rows = set_table.find_elements_by_tag_name('tr')
    total_rows = len(rows)

    for i in range(total_rows):
        if element_exists("select", i):
            setting = find_element_by_selector("select", i)
            select_elem = Select(setting)
            random_select_option(select_elem)
        elif element_exists("input", i):
            input_elem = find_element_by_selector("input", i)
            regex_val = input_elem.get_attribute('data-val-regex')
            if regex_val == '[\s\S]':
                try:
                    input_elem.send_keys('J2½§!"@#£$¤*%&/\<>[]()=?')
                except:
                    pass
            else:
                try:
                    input_elem.send_keys('1*#959932881')
                except:
                    pass
        elif element_exists("input[value='Upload']", i):
            try:
                driver.find_element_by_css_selector(
                    "input[id='configurationViewModel.Devices[0].SelectedFirmware.Settings[36].fileinputId']").send_keys(
                    "C:\\download\\bat.bmp")
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "some_id_to_wait_for")))
            except Exception as e:
                print(e)

    next_button = driver.find_element_by_xpath("//input[@value='NEXT >']")
    if not next_button.is_enabled():
        # 如果下一个按钮不可用，请按需要处理该情况。
        pass


def config_settings_as_MAX(driver):
    set_table = driver.find_element_by_class_name('settings-table')
    td_content = set_table.find_elements_by_tag_name('tr')
    table_tr_number = len(td_content)
    i = 1
    while i < table_tr_number:
        flag = isElementExist(driver,
                              "select[name='configurationViewModel.Devices[0].SelectedFirmware.Settings[" + str(
                                  i) + "].SelectedValue']")
        if flag:
            setting = driver.find_element_by_css_selector(
                "select[name='configurationViewModel.Devices[0].SelectedFirmware.Settings[" + str(
                    i) + "].SelectedValue']")
            if Select(setting):
                select = Select(setting)
                selectlen = len(select.options)
                Select(setting).select_by_index(selectlen - 1)
                i = i + 1
                continue
        elif isInputExist(driver,
                          "input[name='configurationViewModel.Devices[0].SelectedFirmware.Settings[" + str(
                              i) + "].SelectedValue']"):
            try:
                driver.find_element_by_css_selector(
                    "input[name='configurationViewModel.Devices[0].SelectedFirmware.Settings[" + str(
                        i) + "].SelectedValue']").send_keys('2023')
                i = i + 1
                continue
            except:
                i = i + 1
                continue
        else:
            i = i + 1
            continue

def config_settings_as_Min(driver):
    set_table = driver.find_element_by_class_name('settings-table')
    td_content = set_table.find_elements_by_tag_name('tr')
    table_tr_number = len(td_content)

    i = 1
    while i < table_tr_number:
        flag = isElementExist(driver,
                              "select[name='configurationViewModel.Devices[0].SelectedFirmware.Settings[" + str(
                                  i) + "].SelectedValue']")
        if flag:
            setting = driver.find_element_by_css_selector(
                "select[name='configurationViewModel.Devices[0].SelectedFirmware.Settings[" + str(
                    i) + "].SelectedValue']")
            if Select(setting):
                Select(setting).select_by_index("1")
                i = i + 1
                continue
        elif isInputExist(driver,
                          "input[name='configurationViewModel.Devices[0].SelectedFirmware.Settings[" + str(
                              i) + "].SelectedValue']"):
            try:
                driver.find_element_by_css_selector(
                    "input[name='configurationViewModel.Devices[0].SelectedFirmware.Settings[" + str(
                        i) + "].SelectedValue']").send_keys('2020')
                i = i + 1
                continue
            except:
                i = i + 1
                continue
        else:
            i = i + 1
            continue

    # 判断按钮是否可用
    nextButton = driver.find_element_by_xpath("//input[@value='NEXT >']")
    isNextButtonEnable = nextButton.is_enabled()
    if isNextButtonEnable == False:
        i = 0
        while i < table_tr_number:
            flag = isElementExist(driver,
                                  "select[name='configurationViewModel.Devices[0].SelectedFirmware.Settings[" + str(
                                      i) + "].SelectedValue']")
            if flag:
                setting = driver.find_element_by_css_selector(
                    "select[name='configurationViewModel.Devices[0].SelectedFirmware.Settings[" + str(
                        i) + "].SelectedValue']")
                if Select(setting):
                    i = i + 1
                    continue
            elif isInputExist(driver,
                              "input[name='configurationViewModel.Devices[0].SelectedFirmware.Settings[" + str(
                                  i) + "].SelectedValue']"):
                try:
                    driver.find_element_by_css_selector(
                        "input[name='configurationViewModel.Devices[0].SelectedFirmware.Settings[" + str(
                            i) + "].SelectedValue']").send_keys('2021')
                    i = i + 1
                    continue
                except Exception as e:
                    i = i + 1
                    continue
            elif isUploadButton(driver, "input[value='Upload']"):
                try:
                    driver.find_element_by_css_selector(
                        "input[id='configurationViewModel.Devices[0].SelectedFirmware.Settings[36].fileinputId']").send_keys(
                        "C:\\download\\bat.bmp")
                    sleep(5)
                    i = i + 1
                    continue
                except Exception as e:
                    print(e)
            else:
                i = i + 1
                continue

def config_display_lanuage_settings_for_Engage75(driver):
    '''
    Engage75 has 4 options for language settings
    Update device to firmware version	5.11.0
    Language pack
    Display language
    Voice language pack
    Voice language
    '''
    print("Start config_lanuage_settings_for_Engage75")
    language_pack = driver.find_element_by_css_selector(
        "select[name='configurationViewModel.Devices[0].SelectedFirmware.RegionSettings.SelectedRegionId']")
    Select(language_pack).select_by_index("1")



def print_the_config_finish(currentTestcaseName, testDeviceName):
    print(testDeviceName + ' ' + currentTestcaseName + ' Configure finish')


def goto_pcsoftware_page(driver):
    # 跳转到PC Software下载页面
    driver.find_element_by_xpath("//input[@value='NEXT >']").click()


def action_download_jd(driver):
    # Choose JD
    driver.find_element_by_xpath("//input[@value='true']").click()


def config_random_sp(driver):
    """ Configure the SP randomly"""
    setting = driver.find_element_by_css_selector(
        "select[name='PcSoftwareViewModel.DeploymentOptionGroups[2].DeploymentOptions[19].Value']")
    if Select(setting):
        select = Select(setting)
        selectlen = len(select.options)
        Select(setting).select_by_index(random.randint(0, selectlen - 1))


def goto_summary_page_and_download(driver):
    driver.find_element_by_xpath("//input[@value='NEXT >']").click()
    # 跳转到Summary下载页面
    driver.find_element_by_xpath("//input[@value='NEXT >']").click()
    # 下载Summary
    driver.find_element_by_xpath("//input[@value='DOWNLOAD SUMMARY']").click()


def action_download_msi(driver):
    # Go back to download zip package
    driver.find_element_by_xpath("//input[@value='< PREVIOUS']").click()
    # check the agreement
    driver.find_element_by_id('eulaOk').click()
    # Click download
    driver.find_element_by_id('download64bit').click()


def action_download_msi_32bit(driver):
    # Go back to download zip package
    driver.find_element_by_xpath("//input[@value='< PREVIOUS']").click()
    # check the agreement
    driver.find_element_by_id('eulaOk').click()
    # Click download
    driver.find_element_by_id('download32bit').click()


def action_download_zip_file(driver):
    # Go back to download zip package
    driver.find_element_by_xpath("//input[@value='< PREVIOUS']").click()
    # check the agreement
    driver.find_element_by_id('eulaOk').click()
    # Input the website
    driver.find_element_by_css_selector("input[name='localServerUrl']").send_keys('http://my.gn.com/')
    # Click download
    driver.find_element_by_id('downloadZip').click()


def configure_finish():
    print(os.path.basename(sys.argv[0]).split('.')[0])


def rename_summary(testcase, file, testDeviceName):
    summary = file + '\\summary.html'
    summary_rename = file + '\\' + testcase + '.html'
    try:
        while not os.path.exists(summary):
            sleep(8)
        os.rename(summary, summary_rename)
        print(testDeviceName + ' ' + testcase + ' summary download successful')
    except:
        os.remove(summary_rename)
        os.rename(summary, summary_rename)


def rename_msi_file(self, file, testcaseName, testDeviceName):
    msiFile = file + '\\JabraXPRESSx64.msi'
    msiFile_rename = file + '\\' + testcaseName + '.msi'

    try:
        while not os.path.exists(msiFile):
            sleep(8)
        os.rename(msiFile, msiFile_rename)
        self.close()

    except Exception as e:
        print(e)
        self.close()
    print(testDeviceName + ' ' + testcaseName + ' download successful.')
    print('\n')


def rename_msi_file_32bit(self, file, testcaseName, testDeviceName):
    msiFile = file + '\\JabraXPRESSx86.msi'
    msiFile_rename = file + '\\' + testcaseName + '.msi'
    try:
        while not os.path.exists(msiFile):
            sleep(8)
        os.rename(msiFile, msiFile_rename)
        self.close()
    except Exception as e:
        print(e)
        self.close()
    print(testDeviceName + ' ' + testcaseName + ' download successful.')
    print('\n')


def rename_linux_zip(self, file, testcaseName, testDeviceName):
    testcaseName = testcaseName[len('testcase'):]
    zipFile = file + '\\JabraXpressFiles.zip'
    zipFile_rename = file + '\\' + testcaseName
    try:
        while os.path.exists(zipFile) == False:
            sleep(10)
        with zipfile.ZipFile(zipFile, "r") as zip_ref:
            zip_ref.extractall(file)
        local_server_dir = file + '\\Files_to_place_on_local_server'
        os.rename(local_server_dir, zipFile_rename)
        shutil.rmtree(file + '\\Files_to_install_on_end-user_computers')
        os.remove(file + '\\JabraXpressFiles.zip')
        os.remove(file + '\\readme.txt')
        print(testDeviceName + ' ' + testcaseName + '  download successful')
        self.close()

    except Exception as e:
        print(e)


def setup_driver_windows(testcasename):
    with open("../config/device.txt", "rt") as f:
        testDeviceName = f.read()

    # 获取文件位置并构建选项
    file = get_save_dir() + testDeviceName
    options = browser_configure()

    with open("../config/saveDir.txt", "rt") as f:
        file = f.read()
        file = file.replace('/', '\\') + '\\' + testDeviceName.replace("Jabra", "").replace(" ", "").lower() + '\\' + testcasename

    chromedriver_path = setup_chromedriver()
    driver = webdriver.Chrome(executable_path=chromedriver_path,options=options)
    driver.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
    params = {'cmd': 'Page.setDownloadBehavior',
              'params': {'behavior': 'allow', 'downloadPath': file}}
    driver.execute("send_command", params=params)

    windowsTrack = InitWindowsTrack(driver)
    return driver, windowsTrack, testDeviceName, file


def setup_driver_linux(testcasename):
    with open("../config/device.txt", "rt") as f:
        testDeviceName = f.read()

    options = browser_configure()

    with open("../config/saveDir.txt", "rt") as f:
        file = f.read()
        file = file.replace('/', '\\') + '\\' + testDeviceName.replace("Jabra", "").replace(" ", "").lower() + '\\' + testcasename

    driver = webdriver.Chrome(chrome_options=options)
    driver.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
    params = {'cmd': 'Page.setDownloadBehavior',
              'params': {'behavior': 'allow', 'downloadPath': file}}
    driver.execute("send_command", params=params)

    linuxtrack = InitLinuxTrack(driver)
    return driver, linuxtrack, testDeviceName, file

def setup_chromedriver():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    parent_directory = os.path.dirname(current_directory)
    chromedriver_path = os.path.join(parent_directory, 'chromedriver.exe')
    return chromedriver_path
