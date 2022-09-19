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

def initialScreen(browser) :
    confirmbtn = "com.duzon.android.lulubizpotalIDtv_confirm_buttom"
    if hasxpath(browser, confirmbtn, ID) :
        browser_click(browser, mobileVarname.confirmbtn, ID)
        browser_click(browser, mobileVarname.allowbtn, ID)

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
    browser.implicitly_wait(3)

    # 거래처
    #Android.Account().ac_registAccount(browser)
    #browser.implicitly_wait(3)
    #Android.Account().ac_modifyAccount(browser)
    #browser.implicitly_wait(3)
    #Android.Account().ac_deleteAccount(browser)
    #browser.implicitly_wait(3)
    #Android.Account().ac_createGroup(browser)
    #browser.implicitly_wait(3)
    #Android.Account().ac_deleteGroup(browser)
    #browser.implicitly_wait(3)
    #Android.Account().ac_createSharedGroup(browser)
    #browser.implicitly_wait(3)
    #Android.Account().ac_deleteSharedGroup(browser)
    #browser.implicitly_wait(5)

    # 연락처
    #Android.Contacts().ct_registerContacts(browser)
    #browser.implicitly_wait(3)
    #Android.Contacts().ct_registerContacts_add(browser)
    #browser.implicitly_wait(3)
    #Android.Contacts().ct_createGroup(browser)
    #browser.implicitly_wait(3)
    #Android.Contacts().ct_modifyGroup(browser)
    ##browser.implicitly_wait(3)
    #Android.Contacts().ct_deleteGroup(browser) 
    #browser.implicitly_wait(4)
    #Android.Contacts().ct_createSharedGroup(browser)
    #browser.implicitly_wait(3)
    #Android.Contacts().ct_modifySharedGroup(browser)
    #browser.implicitly_wait(3)
    #Android.Contacts().ct_deleteSharedGroup(browser)
    #browser.implicitly_wait(3)
    #Android.Contacts().ct_contactExport(browser)
    #browser.implicitly_wait(4)
    #Android.Contacts().ct_contactImport(browser)
    #browser.implicitly_wait(4)
    #Android.Contacts().ct_organizeContact(browser)
    #browser.implicitly_wait(3)
    #Android.Contacts().ct_LinkSetting(browser)
    #browser.implicitly_wait(3)
    #Android.Contacts().ct_autosaveOnOff(browser)
    #browser.implicitly_wait(4)
    

    # 메일 
    #Android.Mail().ma_sendMail(browser)
    #browser.implicitly_wait(4)
    #Android.Mail().ma_sendReservedMail(browser)
    #browser.implicitly_wait(4)
    #Android.Mail().ma_sendSecureMail(browser)
    #browser.implicitly_wait(4)
    #Android.Mail().ma_temporarySave(browser)
    #browser.implicitly_wait(5)
    #Android.Mail().ma_individualTransfer(browser)
    #browser.implicitly_wait(5)
    #Android.Mail().ma_sendMailWedrive(browser)
    #browser.implicitly_wait(5)
    #Android.Mail().ma_sendMailLocalWedrive(browser)
    #browser.implicitly_wait(5)
    #Android.Mail().ma_replyMail(browser)
    #browser.implicitly_wait(4)
    #Android.Mail().ma_replyMailAll(browser)
    #browser.implicitly_wait(4)
    #Android.Mail().ma_deliveryMail(browser)
    #browser.implicitly_wait(4)
    #Android.Mail().ma_readProcessing(browser)
    #browser.implicitly_wait(4)
    #Android.Mail().ma_deleteMail(browser)
    #browser.implicitly_wait(4)
    #Android.Mail().ma_emptyTrash(browser)
    #browser.implicitly_wait(4)
    

    # 메시지
    """ Android.Message().ms_sendMessage(browser)
    browser.implicitly_wait(4)
    Android.Message().ms_sendImportantMessage(browser)
    browser.implicitly_wait(4)
    Android.Message().ms_sendSecurityMessage(browser)
    browser.implicitly_wait(4)
    Android.Message().ms_sendReservationMessage(browser)
    time.sleep(8)
    Android.Message().ms_replyMessage(browser)
    time.sleep(8) # browser.implicitly_wait(8)로 하면 에러. 
    Android.Message().ms_replyAllMessage(browser)
    time.sleep(8) 
    Android.Message().ms_forwardMessage(browser)
    time.sleep(8)
    Android.Message().ms_resendMessage(browser)
    time.sleep(8)
    Android.Message().ms_readMessage(browser)
    time.sleep(8)
    Android.Message().ms_downdloadFile(browser)
    time.sleep(8)
    Android.Message().ms_readSecureMessage(browser, pwd)
    browser.implicitly_wait(4)
    Android.Message().ms_bookmark(browser)
    browser.implicitly_wait(4)
    Android.Message().ms_deleteReceiveMessage(browser)
    browser.implicitly_wait(5)
    Android.Message().ms_deleteSendMessage(browser)
    browser.implicitly_wait(4) """


    # 메신저
    """ Android.Communication().cc_createGroupChat(browser)
    time.sleep(8)

    Android.Communication().cc_appendingLocalFile(browser)
    time.sleep(5) # err
    Android.Communication().cc_appendingCamera(browser)
    time.sleep(5)
    Android.Communication().cc_appendingWedriveFile(browser)
    time.sleep(5)
    Android.Communication().cc_appendingContacts(browser)
    time.sleep(5)
    
    Android.Communication().cc_sendChat(browser) # 순서 주의 입력파트 이전에 넣을 것. 파일 첨부 이전에 넣으면 위로 밀림
    browser.implicitly_wait(4)
    Android.Communication().cc_searchChat(browser) # 검색한 키워드 클릭 시, 로딩 발생
    browser.implicitly_wait(6)

    Android.Communication().cc_copyChat(browser) # 붙여넣기 실패...
    browser.implicitly_wait(4)
    Android.Communication().cc_commentChat(browser)
    browser.implicitly_wait(4)
    Android.Communication().cc_reactionChat(browser)
    browser.implicitly_wait(4)
    Android.Communication().cc_deleteChat(browser) # 삭제 메시지 테스트
    browser.implicitly_wait(4)
    
    Android.Communication().cc_downloadFileTab(browser)
    browser.implicitly_wait(4)
    Android.Communication().cc_settingPrivateGroup(browser)
    browser.implicitly_wait(4)
    Android.Communication().cc_settingPublicGroup(browser) # goBack() 과정에서 로딩 발생. 옵션에서 뒤로가기 과정으로 빠져나올 때 로딩발생 확인. 
    browser.implicitly_wait(8)
    Android.Communication().cc_favoriteConversation(browser)
    browser.implicitly_wait(4)

    Android.Communication().cc_checkUserProfile(browser)
    browser.implicitly_wait(4)
    Android.Communication().cc_setAsMaster(browser) # sameText 에러
    browser.implicitly_wait(4)
    Android.Communication().cc_exportUser(browser) # sameText 에러
    browser.implicitly_wait(4)
    Android.Communication().cc_leaveChatRoom(browser)
    browser.implicitly_wait(4)
    
    Android.Communication().cc_createChat(browser) # 1:1 채팅방 생성
    browser.implicitly_wait(4) """


    # 일정관리
    """ Android.Schedule().sc_createCalendar(browser)
    time.sleep(6)
    Android.Schedule().sc_createSharedCalendar(browser)
    time.sleep(6)
    Android.Schedule().sc_modifyCalendar(browser)
    time.sleep(6) # time.sleep(5)로 안하면 err
    Android.Schedule().sc_deleteCalendar(browser)
    browser.implicitly_wait(5)

    Android.Schedule().sc_registerSchedule1(browser)
    browser.implicitly_wait(5)
    Android.Schedule().sc_registerSchedule2(browser)
    browser.implicitly_wait(5)

    Android.Schedule().sc_searchSchedule(browser)
    browser.implicitly_wait(5)
    Android.Schedule().sc_addComment(browser)
    browser.implicitly_wait(5)
    Android.Schedule().sc_modifySchedule(browser) # 같은 캘린더명이 여러개 있을 때, 선택 안됨 주의
    time.sleep(5)
    Android.Schedule().sc_deleteSchedule(browser)
    browser.implicitly_wait(5)

    Android.Schedule().sc_clickCalendar(browser)
    browser.implicitly_wait(5) """


    
    

    #wehagotestrun.WehagoRun_Mobile().wehagoRun(browser, id)

print('2')