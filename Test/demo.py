from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import pytest

"""控件知识体系"""
"""DOM:Document Object Model文档对象模型"""
"""DOM应用：最早应用于HTML和Javascript的交互。界面"""

"""findElementByXXX"""
"""findElement(by,value)"""
"""findElement主要用于Page Object模式"""

"""常见自动化动作支持"""
"""click"""
"""sendKeys"""
"""swipe"""   """driver.swipe(start_x=75,start_y=500)"""
"""touch action"""

"""手势操作TouchAction"""
"""press release longPress"""
"""tap wait"""
"""moveTo"""
"""perform"""


"""定位与操作的代码示例"""
class TestDemo:
    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "127.0.0.1:62001"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["autoGrantPermissions"] = True

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",caps)
        self.driver.implicitly_wait(10)

    def test_Login(self):
        pass

    def teardown(self):
        pass



