import yaml

import os
import sys
from appium import webdriver


class readyamlConfig:
    def readyamlConfig(self,filename):

        file = open(filename,"r")
        data =yaml.load(file)

        desired_caps={}
        desired_caps["platformName"] = data["platformName"]
        desired_caps["platVersion"] = data["platVersion"]
        desired_caps["devicesName"] = data["devicesName"]
        desired_caps["appPackage"] = data["appPackage"]
        desired_caps["appActivity"] = data["appActivity"]
        desired_caps["unicodeKeyboard"] = data["unicodeKeyboard"]
        desired_caps["aotuGrantPermissions"] = data["aotuGrantPermissions"]

        driver = webdriver.Remote("http://127.0.0.1:4372/wd/hub",desired_caps)

if __name__ =="__main__":
    operation = readyamlConfig
    operation.readyamlConfig("driver_config.yaml")










