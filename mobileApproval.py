from ast import And
from cgitb import text
from curses import A_COLOR, KEY_CLOSE, KEY_ENTER, KEY_F4
from lib2to3.pgen2 import driver
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
    time.sleep(6)
    Android.Approval().approvalInitialSetting(browser) # 앱 실행 후, 검정 화면 + 회전상태가 적용되어 뒤로가기 + 앱 재접속 과정 추가 / browser.refresh() 안먹힘.... -> ^p^ 해결~~ 위하고 앱에서 들어가면 됨 심지어 속도도 빠름 굿
    time.sleep(20) # 개선해야할 사항...
    Android.Approval().approvalLogin2(browser, id, pwd)
    browser.implicitly_wait(6)
    Android.Approval().approvalTest(browser)
    browser.implicitly_wait(6)
    






print('2')