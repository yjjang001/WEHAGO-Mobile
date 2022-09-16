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
    if apk == 'WEHAGO' :
        path = os.path.join(os.getcwd(), 'mobile')
        app = path + '/wehago1.apk'
    
    device = {
        "platformName": "Android",
        "platformVersion": "11.0",
        "deviceName": "emulator-5554",
        "app": app,
        "automationName": "Appium",
        "newCommandTimeout": 300,
        "appPackage": "com.duzon.android.lulubizpotal",
        "appActivity": "com.duzon.android.lulubizpotal.intro.SplashActivity"
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

def test(browser) : 
    a = "//android.widget.LinearLayout[2]/android.widget.RelativeLayout/android.widget.TextView[1]"
    context = browser.find_element(By.XPATH, a).text
    print(context)

def test1(browser) : 
    b = "com.duzon.android.lulubizpotal:id/tv_main_toolbar_company"
    context1 = browser.find_element(By.ID, b).text
    print(context1)

def test2(browser) :
    c = "//android.widget.LinearLayout[8]"
    browser_click(browser, c)

def test3(browser) :
    print('time.sleep(20)초 테스트 시작~!')
    time.sleep(20)

def test4(browser) :
    c = "//android.widget.LinearLayout[8]"
    if hasxpath(browser, c) :
        print('없어도 된당')

if __name__ == "__main__" :
    id = 'ptestjy_1719'; pwd = '1q2w3e4r'
    desired_caps = setting('WEHAGO')
    browser = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    browser.implicitly_wait(5)
    Android.initialScreen(browser)
    browser.implicitly_wait(4)
    Android.login(browser, id, pwd)
    browser.implicitly_wait(5)
    Android.loginError(browser)
    browser.implicitly_wait(5)
    Android.start(browser)
    browser.implicitly_wait(4)

    test4(browser) # 텍스트 추출 테스트