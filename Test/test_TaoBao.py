# coding=utf-8
 # 3.导入模块
from appium import webdriver
import time
desired_caps = {}
desired_caps['platformName'] = 'Android'   #android的apk还是IOS的ipa
desired_caps['platformVersion'] = '8.0'  #android系统的版本号
desired_caps['deviceName'] = '127.0.0.1:62001'    #手机设备名称，通过adb devices  查看
desired_caps['appPackage'] = 'com.xueqiu.android'  #apk的包名
desired_caps['appActivity'] = '.view.WelcomeActivityAlias'  #apk的launcherActivity
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps) #启动服务器地址，后面跟的是手机信息
# 休眠五秒等待页面加载完成
time.sleep(15)

driver.find_element_by_id("com.xueqiu.android:id/home_search").click()
time.sleep(4)
driver.find_element_by_id("com.xueqiu.android:id/home_search").send_keys("琵琶")
time.sleep(2)

