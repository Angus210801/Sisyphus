"""
#-------------------------------------------------------------------
#                   CONFIDENTIAL --- JX FW Download Tool
#-------------------------------------------------------------------
#
#                   @Project Name : Sisyphus
#
#                   @File Name    : testcase_runner
#
#                   @Programmer   : Angus
#
#                   @Start Date   : 2021/02/25
#
#                   @Last Update  : 2023/05/23
#
#                   @Note: This is for debug testcase but not imtroduce the multi-procedure, will imporvement.
#-------------------------------------------------------------------
"""

from testcase_linux import *
from testcase_windows import *


def Windows_cases():
    case3961 = testcase3961()
    case3965 = testcase3965()
    case3966 = testcase3966()
    case3968 = testcase3968()
    case3969 = testcase3969()
    case4090 = testcase4090()
    case4128_1 = testcase4128_1()
    case4128_2 = testcase4128_2()
    case4128_3 = testcase4128_3()
    case4153_1 = testcase4153_1()
    case4153_2 = testcase4153_2()
    case5509 = testcase5509()
    case5664 = testcase5664()
    case5665 = testcase5665()
    case7195 = testcase7195()
    case7196 = testcase7196()
    case10449 = testcase10449()
    testcase10312 = testcase10312w()
    case3965_32b = testcase3965_32b()
    case3966_32b = testcase3966_32b()
    case4090_32b = testcase4090_32b()
    case5509_32b = testcase5509_32b()
    case5664_32b = testcase5664_32b()
    case5665_32b = testcase5665_32b()


def Linux_cases():
    case6134 = testcase6134()
    case7555 = testcase7555()
    case7692 = testcase7692()
    case7695 = testcase7695()
    case7551 = testcase7551()
    case7556 = testcase7556()
    case10312 = testcase10312l()
    case16990 = testcase16990()
    case16991 = testcase16991()
    case6098 = testcase6098()


if __name__ == '__main__':
    Linux_cases()
    Windows_cases()
