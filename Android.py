from cgitb import text
from curses import KEY_ENTER
import time
from tkinter import Checkbutton
import unittest
import os
from appium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from driver import browser_click, browser_sendKey, hasxpath
import name
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.action_chains import ActionChains

def run() :
    desired_caps = setting()
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    time.sleep(5)
    initialScreen(driver)
    time.sleep(2)
    login(driver)
    time.sleep(6)
    start(driver)
    time.sleep(5)
    Account.ac_registerAccount(driver)
    time.sleep(2)
    Account.ac_modifyAccount(driver)

    # driver.switch_to.context('NATIVE_APP')
    # #python test script
    # findElementClickByID(driver, "element ID")
    # driver.quit()

def setting():
    device = {
     "platform_name" : "Android",
        "platform_version" : "11.0",
        "device_name" : "emulator-5554",
        "app_activity" : "com.duzon.android.lulubizpotal.intro.SplashActivity",
        "app" : "C:/mobile/wehago1.apk"
    }
    desired_caps = {
        'platformName': device['platform_name'],
        'platformVersion': device['platform_version'],
        'deviceName': device['device_name'],
        'app': device['app'],
        'autoGrantPermissions': 'true',
        'automationName': 'UiAutomator2',
        'ignoreHiddenApiPolicyError': 'true',
        'appActivity': device['app_activity']
    }
    return desired_caps



def initialScreen(driver) :
    confirmbtn = "com.duzon.android.lulubizpotal:id/tv_confirm_buttom"
    if hasxpath(driver, confirmbtn, 'id') :
        browser_click(driver, name.confirmbtn, 'id')
        browser_click(driver, name.allowbtn, 'id')





def login(driver) :
    browser_sendKey(driver, name.loginId, 'ptestjy_1719', 'id')
    browser_sendKey(driver, name.loginPw, '1q2w3e4r', 'id')
    browser_click(driver, name.loginButton, 'id')
    if hasxpath(driver, name.loginError, 'id') :
        browser_sendKey(driver, name.loginId, 'yjjang_test3', 'id')
        browser_sendKey(driver, name.loginPw, '1q2w3e4r', 'id')
        browser_click(driver, name.loginButton, 'id')

    


def start(driver) :
    startbtn = "com.duzon.android.lulubizpotal:id/btn_start"
    if hasxpath(driver, startbtn, 'id') :
        browser_click(driver, startbtn, 'id')




            
class Account :
    def ac_registerAccount(driver) :
        browser_click(driver, name.enterAccounts, 'xpath')
        browser_click(driver, name.plusBtnAccounts, 'id')
        browser_click(driver, name.corporationAccounts, 'id')
        time.sleep(2)
        browser_sendKey(driver, name.accountsName, '(주)더존비즈온', 'id')
        # 스크롤
        driver.swipe(400, 1500, 100, 400, 1000)
        #TouchAction().press(name.enterpriseNumber).moveTo(name.representativeName).release()
        browser_sendKey(driver, name.representativeName, '김용우', 'id')
        browser_click(driver, name.checkBtn, 'id')
    
    def ac_modifyAccount(driver) :
        #browser_sendKey(driver,name.search, '(주)더존비즈온', 'id').send_keys(KEY_ENTER).perform()
        #browser_click(driver, )
        #driver.find_elements(By.ACCESSIBILITY_ID,'SomeAccessibilityID').click()
        #driver.find_elements(By.ID, '(주)더존비즈온').click()
        ActionChains(driver.find_elements(By.ID, '(주)더존비즈온')).click()



    def ac_deleteAccount(driver) :
        browser_click(driver, name.selectAccounts, 'id')
        

run()
print('1')