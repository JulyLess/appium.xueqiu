from appium import webdriver
import time

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


"""定位与操作的代码示例"""
caps ={ }
caps["platformName"] = "android"
caps["deviceName"] = "127.0.0.1:62001"
caps["appPackage"] = "com.xueqiu.android"
caps["appActivity"] = ".view.WelcomeActivityAlias"
caps["autoGrantPermissions"] = True

driver = webdriver.Remote("http://localhost:4273/wd/hub",caps)

