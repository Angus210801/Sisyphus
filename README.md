# JX FW Download Tool
This tool is for Tester to auto download the Xpress package in Jabra Xpress 1.0 test.
## config directory


#### The .bmp file is for Engage75 to upload the image.
#### The device.txt is store the test device name.
#### The platform.txt is store what platform user select, Winodws or Linux.
#### The saveDir.txt is store what address user want to put the package.
#### The devices_name_list is store all device name, and if there is a new device support,we need to add the device name in the list.


## log

Record the log info.

## test_script

#### For this dirctory,

#### It contains all auto action.

#### testcase_action : All operations on website elements
#### testcase_chromedriver_update: Update the chromdrive if we need
#### testcase_element_exist: Judgement if website elements
#### testcase_linux: All testcaase of Linux platform
#### testcase_runner: Debug the testcase, if we don't want use UI we can use this.
#### testcase_windows: All testcaase of Windows platform

## UI

#### A UI window integrate the testcase_linux & testcase_Windows.
