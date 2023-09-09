"""
#-------------------------------------------------------------------
#                   CONFIDENTIAL --- JX FW Download Tool
#-------------------------------------------------------------------
#
#                   @Project Name : Sisyphus
#
#                   @File Name    : logs.py
#
#                   @Programmer   : Angus
#
#                   @Start Date   : 2022/02/25
#
#                   @Last Update  : 2023/05/23
#
#                   @Note: Not complete yet.
#-------------------------------------------------------------------
"""


import logging

import os


def createLogFolder():

    if not os.path.exists("log"):
        os.mkdir("log")



def createLogFile():


    createLogFolder()


    if not os.path.exists("log/log.txt"):
        with open("log/log.txt", "w") as f:
            f.write("")
    else:
        with open("log/log.txt", "a") as f:
            f.write(" ")


def createLogger():

    createLogFile()


    logger = logging.getLogger()

    logger.setLevel(logging.DEBUG)

    fh = logging.FileHandler("log/log.txt", encoding="utf-8")

    fmt = "%(asctime)s - %(levelname)s - %(message)s"

    formatter = logging.Formatter(fmt)

    fh.setFormatter(formatter)

    logger.addHandler(fh)

    return logger

