import subprocess,os
import time
import psutil


def judgeProcess(devices_name):
    """查看程序是否运行"""
    p = psutil.pids()
    for pid in p:
        if psutil.Process(pid).name() == devices_name
            return  True
        else:
            print ("not found")
            return False

def connect_devices():
    """连接设备"""
    os.system(r".\ConnectDevices.bat")

def start_NOX(devices_name):
    """启动夜神"""
    os.system(r".\start_NOX.bat")

# def start_appium(host,port)
#     """启动appium服务器"""
#     bootstrap_port = str(port)


