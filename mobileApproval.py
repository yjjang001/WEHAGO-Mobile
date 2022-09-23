from ast import And
from cgitb import text
from curses import A_COLOR, KEY_CLOSE, KEY_ENTER, KEY_F4
from operator import contains
import time, datetime
from tkinter import Checkbutton
import unittest
import os
from appium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from driver import browser_click, browser_sendKey, hasxpath, currentTime
import mobileVarname
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.action_chains import ActionChains
import Android
#import wehagotestrun

ID='id'; CSS='CSS'; CLASS_NAME='class'; TAG_NAME='tag_name'


def setting(apk):
    if apk == 'APPROVAL' :
        path = os.path.join(os.getcwd(), 'mobile')
        app = path + '/eapprovals.apk'
    
    device = {
        "platformName": "Android",
        "platformVersion": "11.0",
        "deviceName": "emulator-5554",
        "app": app,
        "automationName": "Appium",
        "newCommandTimeout": 300,
        "appPackage": "com.douzone.android.eapprovals",
        "appActivity": "host.exp.exponent.experience.TvActivity"
    }
    desired_caps = {
        'platformName': device['platformName'],
        'platformVersion': device['platformVersion'],
        'deviceName': device['deviceName'],
        'app': device['app'],
        'autoGrantPermissions': 'true',
        'automationName': 'UiAutomator2',
        'ignoreHiddenApiPolicyError': 'true',
        'appActivity': device['appActivity'],
        'noReset' : 'true'
    }
    return desired_caps

if __name__ == "__main__" :
    id = 'ptestjy_1719'; pwd = '1q2w3e4r'
    desired_caps = setting('APPROVAL')
    browser = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    






print('2')