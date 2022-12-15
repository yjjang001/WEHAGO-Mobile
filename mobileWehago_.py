#-*- coding: utf-8 -*-
#from pathos.multiprocessing import ProcessingPool
import numpy as np
import time, datetime, os, platform
import wehagotestrun, wehagotest, varname
import wehagoReport
from driver import wehagoID, chromeBrowser, checkSerivce
from appium import webdriver
import Android
ID='id'; CSS='CSS'; CLASS_NAME='class'; TAG_NAME='tag_name'

# 에뮬레이터
# def setting(apk):
#     if apk == 'WEHAGO' :
#         path = os.path.join(os.getcwd(), 'mobile')
#         app = path + '/wehago1.apk'
#
#     device = {
#         "platformName": "Android",
#         "platformVersion": "11.0",
#         "deviceName": "emulator-5554",
#         "app": app,
#         "automationName": "Appium",
#         "newCommandTimeout": 300,
#         "appPackage": "com.duzon.android.lulubizpotal",
#         "appActivity": "com.duzon.android.lulubizpotal.intro.SplashActivity"
#     }
#     desired_caps = {
#         'platformName': device['platformName'],
#         'platformVersion': device['platformVersion'],
#         'deviceName': device['deviceName'],
#         'app': device['app'],
#         'autoGrantPermissions': 'true',
#         'automationName': 'UiAutomator2',
#         'ignoreHiddenApiPolicyError': 'true',
#         'appActivity': device['appActivity'],
#         'noReset' : 'true'
#     }
#     return desired_caps

# Galaxy S20 Ultra 5G
# def setting(apk):
#     if apk == 'WEHAGO' :
#         path = os.path.join(os.getcwd(), 'mobile')
#         app = path + '/wehago1.apk'
#
#     device = {
#         "platformName": "Android",
#         "platformVersion": "12.0",
#         "deviceName": "Galaxy S20 Ultra 5G",
#         "app": app,
#         "automationName": "Appium",
#         "newCommandTimeout": 300,
#         "appPackage": "com.duzon.android.lulubizpotal",
#         "appActivity": "com.duzon.android.lulubizpotal.intro.SplashActivity",
#         "udid": "R3CN20TE8KM"
#     }
#     desired_caps = {
#         'platformName': device['platformName'],
#         'platformVersion': device['platformVersion'],
#         'deviceName': device['deviceName'],
#         'app': device['app'],
#         'autoGrantPermissions': 'true',
#         'automationName': 'UiAutomator2',
#         'ignoreHiddenApiPolicyError': 'true',
#         'appActivity': device['appActivity'],
#         'noReset' : 'true'
#
#     }
#     return desired_caps


# Galaxy S20 Ultra 5G
def setting(apk):
    if apk == 'WEHAGO' :
        path = os.path.join(os.getcwd(), 'mobile')
        app = path + '/wehago1.apk'

    device = {
        "platformName": "Android",
        "platformVersion": "13.0",
        "deviceName": "Galaxy S20 Ultra 5G",
        "app": app,
        "automationName": "Appium",
        "newCommandTimeout": 300,
        "appWaitForLaunch": "false",
        "appPackage": "com.duzon.android.lulubizpotal",
        "appActivity": "com.duzon.android.lulubizpotal.intro.SplashActivity",
        "udid": "R3CN20TE8KM"
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





# V20
# def setting(apk):
#     if apk == 'WEHAGO' :
#         path = os.path.join(os.getcwd(), 'mobile')
#         app = path + '/wehago1.apk'
#
#     device = {
#         "platformName": "Android",
#         "platformVersion": "8.0",
#         "deviceName": "V20",
#         "app": app,
#         "automationName": "Appium",
#         "newCommandTimeout": 300,
#         "appPackage": "com.duzon.android.lulubizpotal",
#         "appActivity": "com.duzon.android.lulubizpotal.intro.SplashActivity",
#         "udid": "LGF800S2e7e8e4"
#     }
#     desired_caps = {
#         'platformName': device['platformName'],
#         'platformVersion': device['platformVersion'],
#         'deviceName': device['deviceName'],
#         'app': device['app'],
#         'autoGrantPermissions': 'true',
#         'automationName': 'UiAutomator2',
#         'ignoreHiddenApiPolicyError': 'true',
#         'appActivity': device['appActivity'],
#         'noReset' : 'true'
#
#     }
#     return desired_caps

# S20 노트 울트라 너 왜 이상해 버전 12라 그러니?
# def setting(apk):
#     if apk == 'WEHAGO' :
#         path = os.path.join(os.getcwd(), 'mobile')
#         app = path + '/wehago1.apk'
#
#     device = {
#         "platformName": "Android",
#         "platformVersion": "12.0",
#         "deviceName": "Galaxy Note20 5G",
#         "app": app,
#         "automationName": "Appium",
#         "newCommandTimeout": 300,
#         "appPackage": "com.duzon.android.lulubizpotal",
#         "appActivity": "com.duzon.android.lulubizpotal.intro.SplashActivity",
#         "udid": "R3CN806H3CB"
#     }
#     desired_caps = {
#         'platformName': device['platformName'],
#         'platformVersion': device['platformVersion'],
#         'deviceName': device['deviceName'],
#         'app': device['app'],
#         'autoGrantPermissions': 'true',
#         'automationName': 'UiAutomator2',
#         'ignoreHiddenApiPolicyError': 'true',
#         'appActivity': device['appActivity'],
#         'noReset' : 'true'
#
#     }
#     return desired_caps

# 노트20울트라 안이상한거
# def setting(apk):
#     if apk == 'WEHAGO' :
#         path = os.path.join(os.getcwd(), 'mobile')
#         app = path + '/wehago1.apk'
#
#     device = {
#         "platformName": "Android",
#         "platformVersion": "13.0",
#         "deviceName": "Galaxy Note20 5G",
#         "app": app,
#         "automationName": "Appium",
#         "newCommandTimeout": 300,
#         "appPackage": "com.duzon.android.lulubizpotal",
#         "appActivity": "com.duzon.android.lulubizpotal.intro.SplashActivity",
#         "udid": "R3CN806RLER"
#     }
#     desired_caps = {
#         'platformName': device['platformName'],
#         'platformVersion': device['platformVersion'],
#         'deviceName': device['deviceName'],
#         'app': device['app'],
#         'autoGrantPermissions': 'true',
#         'automationName': 'UiAutomator2',
#         'ignoreHiddenApiPolicyError': 'true',
#         'appActivity': device['appActivity'],
#         'noReset' : 'true'
#
#     }
#     return desired_caps


# 갤럭시 노트9
# def setting(apk):
#     if apk == 'WEHAGO' :
#         path = os.path.join(os.getcwd(), 'mobile')
#         app = path + '/wehago1.apk'
#
#     device = {
#         "platformName": "Android",
#         "platformVersion": "10.0",
#         "deviceName": "Galaxy Note9",
#         "app": app,
#         "automationName": "Appium",
#         "newCommandTimeout": 300,
#         "appPackage": "com.duzon.android.lulubizpotal",
#         "appActivity": "com.duzon.android.lulubizpotal.intro.SplashActivity",
#         "udid": "27d9484837217ece"
#     }
#     desired_caps = {
#         'platformName': device['platformName'],
#         'platformVersion': device['platformVersion'],
#         'deviceName': device['deviceName'],
#         'app': device['app'],
#         'autoGrantPermissions': 'true',
#         'automationName': 'UiAutomator2',
#         'ignoreHiddenApiPolicyError': 'true',
#         'appActivity': device['appActivity'],
#         'noReset' : 'true'
#
#     }
#     return desired_caps



def web(browser2) :
    # 웹 로그인
    Android.Login().webLogin(browser2, id)
    # 웹 전자결재 기안 작성
    Android.Approval().ap_webApproval1(browser2)
    Android.Approval().ap_webApproval2(browser2)
    Android.Approval().ap_webApproval3(browser2)
    # 웹에서 보관함 삭제 및 생성
    Android.Approval().ap_deleteArchive(browser2)
    Android.Approval().ap_createArchive(browser2)
    # 브라우저 종료
    browser2.quit()


if __name__ == "__main__" :
    #id = 'ptestjy_1719' ; pwd = '1q2w3e4r';
    # 현재 폴더 경로 받아옴
    path = os.getcwd()
    version = int(input('2- 체크리스트 / 3- 특정서비스 '))
    id = wehagoID(version)
    if version == 2 :
        checkSerivce(invoice=False)
    elif version == 3 :
        # 특정 서비스만 실행
        print('0-메시지/1-거래처/2-연락처/3-일정/4-메신저/5-메일/10-전자결재')
        number = map(int, input('\n숫자만 입력 ').split()) # type : map
        # number1 = list(number)
        number1 = int(input('한번 더 입력 ')) # number나 기존의 number를 list화 시킬 경우 에러발생
        checkSerivce(num=number)

    else:
        pass


    if version == 2 :
        # 체크리스트
        print('Android Wehago 체크리스트 시작!')
        # 웹 호출
        browser2 = chromeBrowser()
        web(browser2)
        desired_caps = setting('WEHAGO')
        browser = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        time.sleep(5)
        wehagotestrun.WehagoRun_Mobile().wehagoRun(browser, id, version)
        wehagoReport.reportRun(version, 1, False)
        print('Android Wehago 체크리스트 끝!')
    elif version == 3 :
        # 특정 서비스
        if number1 == 10 :
            # 웹 호출
            print('gogo')
            browser2 = chromeBrowser()
            web(browser2)
        desired_caps = setting('WEHAGO')
        browser = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        time.sleep(5)
        wehagotestrun.WehagoRun_Mobile().wehagoRun(browser, id, version)
    else :
        print('BYE')



