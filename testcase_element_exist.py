"""
#-------------------------------------------------------------------
#                   CONFIDENTIAL --- JX FW Download Tool
#-------------------------------------------------------------------
#
#                   @Project Name : Sisyphus
#
#                   @File Name    : testcase_element_exist
#
#                   @Programmer   : Angus
#
#                   @Start Date   : 2021/02/25
#
#                   @Last Update  : 2023/05/23
#
#                   @Note: This file contains some judgement that about some website element if exist.
#-------------------------------------------------------------------
"""

def isElementExist(self,element):

    flag = True
    try:
        self.find_element_by_css_selector(element)
        return flag
    except:
        flag = False
        return flag

def isInputExist(self,element):
    try:
        self.find_element_by_css_selector(element)
        return True
    except:
        return False

def isUploadButton(self,element):
    try:
        self.find_element_by_css_selector(element)
        return True
    except:
        return False

def isLanguageSetExist(self,element):
    try:
        self.findElement_by_xpath_selector(element)
        return True
    except:
        return False
