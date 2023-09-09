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
import os
import shutil
import threading
import time
from concurrent.futures import ThreadPoolExecutor

from test_scripts.testcase_action import *

'''
Group01 : FW Update case:

    16990 JXDU:Disconnect the DUT during the FW update.[Use JX Package][Allow downgrade]
    16991 JXDU:Disconnect the DUT during the FW udpate.[Use JX Package][Not allow downgrade]
    16992 JXDU:Disconnect the DUT during the FW update,for all individual components.[Use FW File]
    17950 JXDU:Normal FW update without Interruption.[Use FW File](Linux JXDU 6.x or above)
    17951 JXDU:Normal FW Update without Interruption.[Use JX Package](Linux JXDU 6.x or Above)

Group02 :FW Update & Settings Configure case:
    
    6098 JX-ThinC: Verify zip package content and JXDU version by creating a ZIP file. - - It is a check test case, not need tu run code so dont need another prepare pakcage for this.
    6134 JX-ThinC:All device settings and FW set to "Leave Unchange",all settings set to Protected.
    7692 JX-ThinC:All settings in the device can be change from default value to min.value with installation of .zip file at the end user PC,no FW change.
    7695 JX-ThinC:All settings in the device can be change from default value to max.value with installation of .zip file at the end user PC,no FW change.
    7551 JX-ThinC:Install a ZIP file on end user environment with a later FW and set all settings are changed.
    7555 JX-ThinC:Install a ZIP file on end user environment with a later FW and no setting change.
    7556 JX-ThinC:Install a ZIP file on end user environment with a later FW and set all settings set to default.

Group03 :Prepare package for 01:
    16990p: Lower FW and not settings change,downgrade==allow.
    16991p: same with 16990p
    16992p: same with 16990p
    17950p: same with 16990p
    17951p:same with 16990p

Group04 :Prepare testcase for 02:
    6134p: Latest FW and Random settings, Protect = Not.
    7692p: Use the pacakge == 7556.
    7695p: Use the pacakge == 7556.
    7551p: Lower FW and Random settigns.
    7555p: Lower FW and settings = Max value.
    7556p: Lower FW and not default settings.
'''


def testcase6098():
    """ 6098: JX-ThinC: Verify zip package content and JXDU version by creating a ZIP file."""
    # Get current function name
    currentTestcaseName = sys._getframe().f_code.co_name
    driver, linuxtrack, test_deviceName, file = setup_driver_linux(currentTestcaseName)
    # Go to select device page
    linuxtrack.click_next_button()
    # Input device name
    linuxtrack.select_device()
    # Go to select firmware page
    config_the_latest_FW(driver)
    # Print configure finish
    print_the_config_finish(currentTestcaseName, test_deviceName)
    # Download summary
    goto_summary_page_and_download(driver)
    # Rename summary file
    rename_summary(currentTestcaseName, file, test_deviceName)
    # Go to download page
    action_download_zip_file(driver)

    # Download zip file and rename
    testcaseName = currentTestcaseName[len('testcase'):]
    zipFile = file + '\\JabraXpressFiles.zip'
    while os.path.exists(zipFile) == False:
        sleep(10)
    zipFile_rename = file + '\\' + testcaseName
    os.rename(zipFile, zipFile_rename)
    print(test_deviceName + ' ' + testcaseName + '  download successful')


def testcase6134():
    """ 6134: JX-ThinC: All device settings and FW set to "Leave Unchange", all settings set to Protected."""
    # Get current function name
    currentTestcaseName = sys._getframe().f_code.co_name
    driver, linuxtrack, test_deviceName, file = setup_driver_linux(currentTestcaseName)
    # Go to select device page
    linuxtrack.click_next_button()
    # Input device name
    linuxtrack.select_device()
    # Configure protect as yes
    config_the_protect_as_yes(driver)
    # Configure the latest FW
    config_the_latest_FW(driver)
    # Print configure finish
    print_the_config_finish(currentTestcaseName, test_deviceName)
    # Download summary
    goto_summary_page_and_download(driver)
    # Rename summary file
    rename_summary(currentTestcaseName, file, test_deviceName)
    # Go to download page
    action_download_zip_file(driver)
    # Download zip file and rename
    rename_linux_zip(driver, file, currentTestcaseName, test_deviceName)



def testcase6134p():
    """
    It is prepared for the testcase 6134.Latest FW and Random settings, Protect = Not.
    6134: JX-ThinC: All device settings and FW set to "Leave Unchange", all settings set to Protected.
    """
    # Get current function name
    currentTestcaseName = sys._getframe().f_code.co_name
    driver, linuxtrack, testDeviceName, file = setup_driver_linux(currentTestcaseName)
    # Go to select device page
    linuxtrack.click_next_button()
    # Input device name
    linuxtrack.select_device()
    # Configure the latest FW
    config_the_latest_FW(driver)
    # Configure all settings as random
    config_settings_as_random(driver)
    # Configure protect as yes
    try:
        config_the_protect_as_no(driver)
    except Exception as e:
        print(e)
    # Print configure finish
    print_the_config_finish(currentTestcaseName, testDeviceName)
    # Download summary
    goto_summary_page_and_download(driver)
    # Rename summary file
    rename_summary(currentTestcaseName, file, testDeviceName)
    # Go to download page
    action_download_zip_file(driver)
    # Download zip file and rename
    rename_linux_zip(driver, file, currentTestcaseName, testDeviceName)


def testcase7551():
    """ 7551: JX-ThinC: Install a ZIP file on end user environment with a later FW and set all settings are changed."""
    # Get current function name
    currentTestcaseName = sys._getframe().f_code.co_name
    driver, linuxtrack, testDeviceName, file = setup_driver_linux(currentTestcaseName)
    # Go to select device page
    linuxtrack.click_next_button()
    # Input device name
    linuxtrack.select_device()
    # Configure the latest FW
    config_the_latest_FW(driver)
    # Configure all settings as random
    config_settings_as_random(driver)
    # Print configure finish
    print_the_config_finish(currentTestcaseName, testDeviceName)
    # Download summary
    goto_summary_page_and_download(driver)
    # Rename summary file
    rename_summary(currentTestcaseName, file, testDeviceName)
    # Go to download page
    action_download_zip_file(driver)
    # Download zip file and rename
    rename_linux_zip(driver, file, currentTestcaseName, testDeviceName)


def testcase7551p():
    """ 7551: JX-ThinC: Install a ZIP file on end user environment with a later FW and set all settings are changed."""
    # Get current function name
    currentTestcaseName = sys._getframe().f_code.co_name
    driver, linuxtrack, testDeviceName, file = setup_driver_linux(currentTestcaseName)
    # Go to select device page
    linuxtrack.click_next_button()
    # Input device name
    linuxtrack.select_device()
    # Configure the latest FW
    config_the_FW_as_lower_than_latest(driver)
    # Configure all settings as random
    config_settings_as_random(driver)
    # Print configure finish
    print_the_config_finish(currentTestcaseName, testDeviceName)
    # Download summary
    goto_summary_page_and_download(driver)
    # Rename summary file
    rename_summary(currentTestcaseName, file, testDeviceName)
    # Go to download page
    action_download_zip_file(driver)
    # Download zip file and rename
    rename_linux_zip(driver, file, currentTestcaseName, testDeviceName)


def testcase7555():
    """ 7555:JX-ThinC: Install a ZIP file on end user environment with a later FW and no setting change. """
    # Configure the basic function
    currentTestcaseName = sys._getframe().f_code.co_name
    driver, linuxtrack, testDeviceName, file = setup_driver_linux(currentTestcaseName)
    # Go to select device page
    linuxtrack.click_next_button()
    # Input device name
    linuxtrack.select_device()
    # Go to select firmware page
    config_the_latest_FW(driver)
    # Print configure finish
    print_the_config_finish(testDeviceName, currentTestcaseName)
    # Download summary
    goto_summary_page_and_download(driver)
    # Rename summary file
    rename_summary(currentTestcaseName, file, testDeviceName)
    # Go to download page
    action_download_zip_file(driver)
    # Download zip file and rename
    rename_linux_zip(driver, file, currentTestcaseName, testDeviceName)


def testcase7555p():
    """
        7555p:JX-ThinC: Prepare package for the 7555. Lower FW and not default settings.
        7555:JX-ThinC: Install a ZIP file on end user environment with a later FW and no setting change.

    """
    # Configure the basic function
    currentTestcaseName = sys._getframe().f_code.co_name
    driver, linuxtrack, testDeviceName, file = setup_driver_linux(currentTestcaseName)
    # Go to select device page
    linuxtrack.click_next_button()
    # Input device name
    linuxtrack.select_device()
    # Go to select firmware page
    config_the_FW_as_lower_than_latest(driver)
    # Configure all settings as default
    config_settings_as_MAX(driver)
    # Print configure finish
    print_the_config_finish(testDeviceName, currentTestcaseName)
    # Download summary
    goto_summary_page_and_download(driver)
    # Rename summary file
    rename_summary(currentTestcaseName, file, testDeviceName)
    # Go to download page
    action_download_zip_file(driver)
    # Download zip file and rename
    rename_linux_zip(driver, file, currentTestcaseName, testDeviceName)


def testcase7556():
    """ 7556: JX-ThinC: Install a ZIP file on end user environment with a later FW and set all settings set to default."""
    # Get current function name
    currentTestcaseName = sys._getframe().f_code.co_name
    driver, linuxtrack, testDeviceName, file = setup_driver_linux(currentTestcaseName)
    # Go to select device page
    linuxtrack.click_next_button()
    # Input device name
    linuxtrack.select_device()
    # Configure the latest FW
    config_the_latest_FW(driver)
    # Configure all settings as default
    settings_default(driver)
    # Print configure finish
    print_the_config_finish(currentTestcaseName, testDeviceName)
    # Download summary
    goto_summary_page_and_download(driver)
    # Rename summary file
    rename_summary(currentTestcaseName, file, testDeviceName)
    # Go to download page
    action_download_zip_file(driver)
    # Download zip file and rename
    rename_linux_zip(driver, file, currentTestcaseName, testDeviceName)


def testcase7556p():
    """ 7556p:prepare package for
    7556 JX-ThinC: Install a ZIP file on end user environment with an old FW and set all settings set not default value."""
    # Get current function name
    currentTestcaseName = sys._getframe().f_code.co_name
    driver, linuxtrack, testDeviceName, file = setup_driver_linux(currentTestcaseName)
    # Go to select device page
    linuxtrack.click_next_button()
    # Input device name
    linuxtrack.select_device()
    # Configure the latest FW
    config_the_FW_as_lower_than_latest(driver)
    # Configure all settings as default
    config_settings_as_not_default(driver)
    # Print configure finish
    print_the_config_finish(currentTestcaseName, testDeviceName)
    # Download summary
    goto_summary_page_and_download(driver)
    # Rename summary file
    rename_summary(currentTestcaseName, file, testDeviceName)
    # Go to download page
    action_download_zip_file(driver)
    # Download zip file and rename
    rename_linux_zip(driver, file, currentTestcaseName, testDeviceName)


def testcase7692():
    """JX-ThinC: All settings in the device can be changed from default value to min. value with installation of .zip file at the end user PC, no FW change."""
    # Get current function name
    currentTestcaseName = sys._getframe().f_code.co_name
    driver, linuxtrack, testDeviceName, file = setup_driver_linux(currentTestcaseName)
    # Go to select device page
    linuxtrack.click_next_button()
    # Input device name
    linuxtrack.select_device()
    # Configure the latest FW
    config_the_latest_FW(driver)
    # Configure all settings as default
    config_settings_as_Min(driver)
    # Print configure finish
    print_the_config_finish(currentTestcaseName, testDeviceName)
    # Download summary
    goto_summary_page_and_download(driver)
    # Rename summary file
    rename_summary(currentTestcaseName, file, testDeviceName)
    # Go to download page
    action_download_zip_file(driver)
    # Download zip file and rename
    rename_linux_zip(driver, file, currentTestcaseName, testDeviceName)


def testcase7695():
    """JX-ThinC: All settings in the device can be changed from default value to max. value with installation of .zip file at the end user PC, no FW change."""
    # Get current function name
    currentTestcaseName = sys._getframe().f_code.co_name
    driver, linuxtrack, testDeviceName, file = setup_driver_linux(currentTestcaseName)
    # Go to select device page
    linuxtrack.click_next_button()
    # Input device name
    linuxtrack.select_device()
    # Configure the latest FW
    config_the_latest_FW(driver)
    # Configure all settings as default
    config_settings_as_MAX(driver)
    # Print configure finish
    print_the_config_finish(currentTestcaseName, testDeviceName)
    # Download summary
    goto_summary_page_and_download(driver)
    # Rename summary file
    rename_summary(currentTestcaseName, file, testDeviceName)
    # Go to download page
    action_download_zip_file(driver)
    # Download zip file and rename
    rename_linux_zip(driver, file, currentTestcaseName, testDeviceName)

def download_language(driver, language_select, currentTestcaseName, file, testDeviceName):
    # Check if language_select is an option element
    if language_select.tag_name == 'option':
        # Find parent select element
        language_select = language_select.find_element_by_xpath('..')
    # Select language
    Select(language_select).select_by_visible_text(language_select.text)
    language_select = language_select.text
    # Print configure finish
    currentTestcaseName = currentTestcaseName + language_select
    print_the_config_finish(currentTestcaseName, testDeviceName)
    # Download summary
    goto_summary_page_and_download(driver)
    # Rename summary file
    rename_summary(currentTestcaseName, file, testDeviceName)
    # Go to download page
    action_download_zip_file(driver)
    # Download zip file and rename
    rename_linux_zip(driver, file, currentTestcaseName, testDeviceName)

def testcase10312l():
    i = 1
    while i <= 6:
        # Get current function name
        currentTestcaseName = sys._getframe().f_code.co_name
        driver, linuxtrack, testDeviceName, file = setup_driver_linux(currentTestcaseName)
        # Go to select device page
        linuxtrack.click_next_button()
        # Input device name
        linuxtrack.select_device()
        # Configure the latest FW
        config_the_latest_FW(driver)
        # According to the different device make different settings
        if testDeviceName == "Jabra Engage 75":
            config_display_lanuage_settings_for_Engage75(driver)
        # 判断是否存在Language setting
        try:
            language_region_select = driver.find_element_by_css_selector(
                "select[name='configurationViewModel.Devices[0].SelectedFirmware.VoicePromptSettings.SelectedLanguageId']")
            if language_region_select is not None:
                print("Language setting is exist")
            language_select = driver.find_element_by_css_selector(
                "select[name='configurationViewModel.Devices[0].SelectedFirmware.VoicePromptSettings.SelectedLanguageId']")
            languageList = Select(language_select)
            languageNum = len(languageList.options)
            print(testDeviceName+ " has " + str(languageNum) + " language setting")

            # Download each language in a separate thread
            threads = []
            for option in languageList.options:
                t = threading.Thread(target=download_language, args=(driver, option, currentTestcaseName, file, testDeviceName))
                threads.append(t)
                t.start()

            # Wait for all threads to finish
            for t in threads:
                t.join()

            i += 1

        except:
            print("There is no language setting for this device")
            driver.close()
            break

# def testcase10312l():
#     i = 1
#     while i <= 6:
#         # Get current function name
#         currentTestcaseName = sys._getframe().f_code.co_name
#         driver, linuxtrack, testDeviceName, file = setup_driver_linux(currentTestcaseName)
#         # Go to select device page
#         linuxtrack.click_next_button()
#         # Input device name
#         linuxtrack.select_device()
#         # Configure the latest FW
#         config_the_latest_FW(driver)
#         # According to the different device make different settings
#         if testDeviceName == "Jabra Engage 75":
#             config_display_lanuage_settings_for_Engage75(driver)
#         # 判断是否存在Language setting
#         try:
#             language_region_select = driver.find_element_by_css_selector(
#                 "select[name='configurationViewModel.Devices[0].SelectedFirmware.VoicePromptSettings.SelectedLanguageId']")
#             if language_region_select is not None:
#                 print("Language setting is exist")
#             Select(language_region_select).select_by_index("1")
#             language_select = driver.find_element_by_css_selector(
#                 "select[name='configurationViewModel.Devices[0].SelectedFirmware.VoicePromptSettings.SelectedLanguageId']")
#             languageList = Select(language_select)
#             languageNum = len(languageList.options)
#             print(testDeviceName+ " has " + str(languageNum) + " language setting")
#             Select(language_select).select_by_index(i)
#             language_select = Select(language_select).first_selected_option.text
#             # Print configure finish
#             currentTestcaseName = currentTestcaseName + language_select
#             print_the_config_finish(currentTestcaseName, testDeviceName)
#             # Download summary
#             goto_summary_page_and_download(driver)
#             # Rename summary file
#             rename_summary(currentTestcaseName, file, testDeviceName)
#             # Go to download page
#             action_download_zip_file(driver)
#             # Download zip file and rename
#             rename_linux_zip(driver, file, currentTestcaseName, testDeviceName)
#             i += 1
#
#
#         except:
#             print("There is no language setting for this device")
#             driver.close()
#             break


def testcase16990():
    # Get current function name
    currentTestcaseName = sys._getframe().f_code.co_name
    driver, linuxtrack, testDeviceName, file = setup_driver_linux(currentTestcaseName)
    # Go to select device page
    linuxtrack.click_next_button()
    # Input device name
    linuxtrack.select_device()

    # Configure the latest FW
    config_the_latest_FW(driver)
    # Configure all settings as default
    config_allow_downgrade(driver)
    # Print configure finish
    print_the_config_finish(currentTestcaseName, testDeviceName)
    # Download summary
    goto_summary_page_and_download(driver)
    # Rename summary file
    rename_summary(currentTestcaseName, file, testDeviceName)
    # Go to download page
    action_download_zip_file(driver)
    # Download zip file and rename
    rename_linux_zip(driver, file, currentTestcaseName, testDeviceName)

def testcase16990p():
    # Get current function name
    currentTestcaseName = sys._getframe().f_code.co_name
    driver, linuxtrack, testDeviceName, file = setup_driver_linux(currentTestcaseName)
    # Go to select device page
    linuxtrack.click_next_button()
    # Input device name
    linuxtrack.select_device()
    # Configure the latest FW
    config_the_FW_as_lower_than_latest(driver)
    # Print configure finish
    print_the_config_finish(currentTestcaseName, testDeviceName)
    # Download summary
    goto_summary_page_and_download(driver)
    # Rename summary file
    rename_summary(currentTestcaseName, file, testDeviceName)
    # Go to download page
    action_download_zip_file(driver)
    # Download zip file and rename
    rename_linux_zip(driver, file, currentTestcaseName, testDeviceName)



def testcase16991():
    # Get current function name
    currentTestcaseName = sys._getframe().f_code.co_name
    driver, linuxtrack, testDeviceName, file = setup_driver_linux(currentTestcaseName)
    # Go to select device page
    linuxtrack.click_next_button()
    # Input device name
    linuxtrack.select_device()
    # Configure the latest FW
    config_the_latest_FW(driver)
    # Print configure finish
    print_the_config_finish(currentTestcaseName, testDeviceName)
    # Download summary
    goto_summary_page_and_download(driver)
    # Rename summary file
    rename_summary(currentTestcaseName, file, testDeviceName)
    # Go to download page
    action_download_zip_file(driver)
    # Download zip file and rename
    rename_linux_zip(driver, file, currentTestcaseName, testDeviceName)

def testcase16992():
    # Get current function name
    currentTestcaseName = sys._getframe().f_code.co_name
    driver, linuxtrack, testDeviceName, file = setup_driver_linux(currentTestcaseName)
    # Go to select device page
    linuxtrack.click_next_button()
    # Input device name
    linuxtrack.select_device()
    # Configure the latest FW
    config_the_latest_FW(driver)
    # Print configure finish
    print_the_config_finish(currentTestcaseName, testDeviceName)
    # Download summary
    goto_summary_page_and_download(driver)
    # Rename summary file
    rename_summary(currentTestcaseName, file, testDeviceName)
    # Go to download page
    action_download_zip_file(driver)
    # Download zip file and rename
    rename_linux_zip(driver, file, currentTestcaseName, testDeviceName)

def testcase17950():
    # Get current function name
    currentTestcaseName = sys._getframe().f_code.co_name
    driver, linuxtrack, testDeviceName, file = setup_driver_linux(currentTestcaseName)
    # Go to select device page
    linuxtrack.click_next_button()
    # Input device name
    linuxtrack.select_device()
    # Configure the latest FW
    config_the_latest_FW(driver)
    # Print configure finish
    print_the_config_finish(currentTestcaseName, testDeviceName)
    # Download summary
    goto_summary_page_and_download(driver)
    # Rename summary file
    rename_summary(currentTestcaseName, file, testDeviceName)
    # Go to download page
    action_download_zip_file(driver)
    # Download zip file and rename
    rename_linux_zip(driver, file, currentTestcaseName, testDeviceName)

def testcase17951():
    # Get current function name
    currentTestcaseName = sys._getframe().f_code.co_name
    driver, linuxtrack, testDeviceName, file = setup_driver_linux(currentTestcaseName)
    # Go to select device page
    linuxtrack.click_next_button()
    # Input device name
    linuxtrack.select_device()
    # Configure the latest FW
    config_the_latest_FW(driver)
    # Print configure finish
    print_the_config_finish(currentTestcaseName, testDeviceName)
    # Download summary
    goto_summary_page_and_download(driver)
    # Rename summary file
    rename_summary(currentTestcaseName, file, testDeviceName)
    # Go to download page
    action_download_zip_file(driver)
    # Download zip file and rename
    rename_linux_zip(driver, file, currentTestcaseName, testDeviceName)

def run_linux_tests_in_threads():
    with ThreadPoolExecutor(max_workers=5) as executor:
        # executor.submit(testcase6098)
        # executor.submit(testcase6134)
        # executor.submit(testcase7551)
        # executor.submit(testcase7555)
        # executor.submit(testcase7556)
        # executor.submit(testcase7692)
        # executor.submit(testcase7695)
        # executor.submit(testcase6134p)
        # executor.submit(testcase7551p)
        # executor.submit(testcase7555p)
        # executor.submit(testcase7556p)
        # executor.submit(testcase16990)
        # executor.submit(testcase16991)
        # executor.submit(testcase16992)
        # executor.submit(testcase17950)
        # executor.submit(testcase17951)
        # executor.submit(testcase16990p)
        executor.submit(testcase10312l)
        print("Download start!")

if __name__ == '__main__':

    start_time = time.time()

    # Ask user what device to test, and save its name to the device.txt file
    test_device_name = input("Please input the device name: ")
    with open("../config/device.txt", "wt") as f:
        f.write(test_device_name)

    # run_linux_tests_in_threads()
    run_linux_tests_in_threads()

    time.sleep(3)
    print("Download finish!")
    #
    with open("../config/device.txt", "rt") as f:
        testDeviceName = f.read()

    with open("../config/saveDir.txt", "rt") as f:
        file = f.read()
        folder = file.replace('/', '\\') + '\\' + testDeviceName.replace("Jabra", "").replace(" ", "").lower()

    for root, dirs, files in os.walk(folder):
        for subdir in dirs:
            subdir_path = os.path.join(root, subdir)
            for subroot, subdirs, subfiles in os.walk(subdir_path):
                for subfile in subfiles:
                    src_file = os.path.join(subroot, subfile)
                    dst_file = os.path.join(folder, subfile)
                    shutil.move(src_file, dst_file)
                for subsubdir in subdirs:
                    src_dir = os.path.join(subroot, subsubdir)
                    dst_dir = os.path.join(folder, subsubdir)
                    shutil.move(src_dir, dst_dir)

    print("Please also prepare the lowerfw and higherfw for the test device and upload them to the server too.")


    end_time = time.time()
    total_time = end_time - start_time
    # Transfer the time to minutes
    total_time = round(total_time / 60, 1)
    print("Test finish, the test run time is: "+ str(total_time))