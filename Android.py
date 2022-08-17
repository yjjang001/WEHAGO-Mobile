from cgitb import text
from curses import A_COLOR, KEY_CLOSE, KEY_ENTER, KEY_F4
from operator import contains
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
ID='id'; CSS='CSS'; CLASS_NAME='class'; TAG_NAME='tag_name'


def run() :
    desired_caps = setting()
    browser = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    browser.implicitly_wait(5)
    #time.sleep(5)
    initialScreen(browser)
    time.sleep(3)
    login(browser)
    time.sleep(5)
    start(browser)
    time.sleep(5)
    #Account.ac_registerAccount(browser)
    #time.sleep(4)
    #Account.ac_modifyAccount(browser)
    #time.sleep(3)
    #Account.ac_deleteAccount(browser)
    #time.sleep(3)
    #Account.ac_addUserGroup(browser)
    #time.sleep(1)
    #Account.ac_deleteUserGroup(browser)
    #time.sleep(2)
    #Contacts.ct_registerContacts(browser)
    #time.sleep(2)
    #Contacts.ct_addUserGroup(browser)
    #time.sleep(2)
    #Contacts.ct_modifyUserGroup(browser)
    #time.sleep(2)
    #Contacts.ct_deleteUserGroup(browser)
    #time.sleep(2)
    Contacts.ct_addSharingUserGroup(browser)
    time.sleep(2)
    Contacts.ct_modifySharingUserGroup(browser)
    time.sleep(2)
    Contacts.ct_deleteSharingUserGroup(browser)
    #time.sleep(2)
    #Contacts.ct_organizeContact1(browser)
    #time.sleep(2)
    #Contacts.ct_organizeContact2(browser)
    #time.sleep(2)
    #Contacts.ct_organizeContact3(browser)
    #time.sleep(3)
    #Contacts.ct_exportContact(browser)
    #time.sleep(2)
    #Contacts.ct_importContact(browser)
    #time.sleep(2)

    
    





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
        'appActivity': device['app_activity'],
        'noReset' : 'true'
    }
    return desired_caps



def initialScreen(browser) :
    confirmbtn = "com.duzon.android.lulubizpotal:id/tv_confirm_buttom"
    if hasxpath(browser, confirmbtn, 'id') :
        browser_click(browser, name.confirmbtn, 'id')
        browser_click(browser, name.allowbtn, 'id')





def login(browser) :
    loginId = "com.duzon.android.lulubizpotal:id/et_login_insert_id"
    if hasxpath(browser, loginId, 'id') : 
        browser_sendKey(browser, name.loginId, 'ptestjy_1719', 'id')
        browser_sendKey(browser, name.loginPw, '1q2w3e4r', 'id')
        browser_click(browser, name.loginButton, 'id')
    elif hasxpath(browser, name.loginError, 'id') :
        browser_sendKey(browser, name.loginId, 'yjjang_test3', 'id')
        browser_sendKey(browser, name.loginPw, '1q2w3e4r', 'id')
        browser_click(browser, name.loginButton, 'id')

    


def start(browser) :
    startbtn = "com.duzon.android.lulubizpotal:id/btn_start"
    if hasxpath(browser, startbtn, 'id') :
        browser_click(browser, startbtn, 'id')




# 거래처 관리(1. 거래처 등록, 2. 거래처 수정, 3. 거래처 삭제, 4. 사용자 그룹 생성, 5. 사용자 그룹 삭제)            
class Account :
    def ac_registerAccount(browser) :
        browser_click(browser, "//android.widget.LinearLayout[8]", 'xpath')
        browser_click(browser, name.plusBtnAccounts, 'id')
        browser_click(browser, name.corporationAccounts, 'id')
        time.sleep(2)
        browser_sendKey(browser, name.accountsName, '(주)더존비즈온', 'id')
        # 스크롤
        browser.swipe(400, 1500, 100, 400, 1000)
        #TouchAction().press(name.enterpriseNumber).moveTo(name.representativeName).release()
        browser_sendKey(browser, name.representativeName, '김용우', 'id')
        browser_click(browser, name.checkBtn, 'id')

    
    def ac_modifyAccount(browser) :
        browser.find_element(By.XPATH, "//android.widget.TextView[@text = '(주)더존비즈온']").click()
        browser_click(browser, name.detailbar, 'id')
        browser_click(browser, name.modifyAccounts, 'xpath')
        browser_click(browser, name.enterpriseNumber, 'id')
        browser_click(browser, name.accountGroup, 'xpath')
        browser_click(browser, name.accountGroupCheckBtn, 'xpath')
        browser_click(browser, name.accountGroupOkBtn, 'id')
        browser_sendKey(browser, name.enterpriseNumber, '2222222227' ,'id')
        browser_click(browser, name.checkBtn, 'id')
        time.sleep(1)
        browser.back() 
        

    def ac_deleteAccount(browser) :
        browser_click(browser, name.selectAccounts, 'id')
        time.sleep(1)
        browser.find_element(By.XPATH, "//android.widget.TextView[@text = '(주)더존비즈온']").click()
        time.sleep(1)
        browser_click(browser, name.deleteAccounts, 'id')
        time.sleep(1)
        accountOkayBtn  = "com.duzon.android.lulubizpotal:id/tv_ok"
        browser_click(browser, accountOkayBtn, 'id') 
        time.sleep(2)
        browser.back()
        #browser_click(browser, name.returnBtn, 'id')

    def ac_addUserGroup(browser) :
        browser_click(browser, name.allAccounts, 'id')
        time.sleep(2)
        browser_click(browser, name.addUserGroup, 'xpath') 
        browser_sendKey(browser, name.inputBox,'거래처 그룹2','id')
        browser_click(browser, name.accountOkayBtn, 'id')

        
    def ac_deleteUserGroup(browser) :
        browser_click(browser, name.trashcanBtn, 'xpath') # 주의) 두 번째 사용자 그룹 삭제
        browser_click(browser, name.accountOkayBtn, 'id')
        time.sleep(2)
        browser.back()
        browser_click(browser, name.returnHome, 'id')


# 연락처 (1. 연락처 등록, 2. 사용자그룹 생성, 3. 사용자그룹 수정, 4. 사용자 그룹 삭제, 5. 공유 그룹 생성, 6. 공유그룹 수정, 7. 연락처 정리(1), 8. 연락처 정리(2), 9. 연락처정리(3), 10. 연락처 가져오기
# 11. 연락처 내보내기, 12. 음성전화 13. 화상전화, 14. 링크설정 활성화, 15. 링크설정 비활성화, 16. 폰연락처에 자동저장 활성화, 17. 폰 연락처에 자동저장 비활성화)

class Contacts :
    def ct_registerContacts(browser) :
        enterContact = "//android.widget.LinearLayout[7]"
        browser_click(browser, enterContact, 'xpath')
        browser_click(browser, name.plusBtContact, 'id')
        browser_click(browser, name.registerBtnContact, 'id')
        time.sleep(1)
        browser_sendKey(browser, name.inputfirstname, '김', 'id')
        browser_sendKey(browser, name.inputlastname, '더존', 'id')
        browser_sendKey(browser, name.inputTelephoneNumber, '01022223333', 'id')
        browser_sendKey(browser, name.inputemail, 'aaaa@naver.com', 'id')
        browser_click(browser, name.workplaceInformation, 'xpath')
        browser_sendKey(browser, name.inputAffiliation, '서비스QA', 'id')
        browser_sendKey(browser, name.inputPosition, '사원', 'id')
        browser_sendKey(browser, name.inputAssignedTask, '서비스QA', 'id')
        browser_click(browser, name.searchAddressContact, 'xpath')
        time.sleep(3)
        browser_sendKey(browser, name.inputRegionName, '남산면 버들1길 130', 'xpath')
        browser_click(browser, name.searchKey, 'xpath')
        browser_click(browser, name.addressResults, 'xpath')
        time.sleep(3)
        browser_click(browser, name.checkBtn, 'id')


    def ct_addUserGroup(browser):
        browser_click(browser, name.allContacts, 'id')
        browser_click(browser, name.addContactUserGroup, 'xpath')
        browser_sendKey(browser, name.inputBox, '테스트 그룹','id')
        browser_click(browser, name.accountOkayBtn, 'id')

    def ct_modifyUserGroup(browser):
        browser_click(browser, name.modifyGroupName, 'xpath')
        browser_sendKey(browser, name.inputBox, '테스트 그룹2','id')
        browser_click(browser, name.accountOkayBtn, 'id')


    def ct_deleteUserGroup(browser):
        browser_click(browser, name.trashcanBtnContact, 'xpath') # 주의) 두 번째 사용자 그룹 삭제
        browser_click(browser, name.accountOkayBtn, 'id')




    def ct_addSharingUserGroup(browser):
        # test
        enterContact = "//android.widget.LinearLayout[7]"
        browser_click(browser, enterContact, 'xpath')
        browser_click(browser, name.allContacts, 'id')
        time.sleep(1)
        # test
        browser_click(browser, name.addContactSharingUserGroup, 'xpath')
        time.sleep(2)
        browser_click(browser, name.searchUser, 'id')
        browser_sendKey(browser, name.search, "장윤주",'id')
        time.sleep(1)
        browser.back()
        browser_click(browser, name.selectmember, 'id')
        browser_click(browser, name.checkBtn, 'id')
        browser_sendKey(browser, name.inputBox, '테스트 공유', 'id')
        browser_click(browser, name.accountOkayBtn, 'id')


    def ct_modifySharingUserGroup(browser):
        browser_click(browser, name.modifySharingGroupName, 'xpath') # 주의) 첫 번째 공유그룹 수정
        browser_sendKey(browser, name.inputBox, '테스트 공유2','id') 
        browser_click(browser, name.accountOkayBtn, 'id')


    def ct_deleteSharingUserGroup(browser):
        if hasxpath(browser, name.trashcanBtnSharingContact, 'xpath'):
            browser_click(browser, name.trashcanBtnSharingContact, 'xpath') # 주의) 첫 번째 공유그룹 삭제
            browser_click(browser, name.accountOkayBtn, 'id')
        else :
            print('삭제할 공유그룹 없음!')
        time.sleep(2)
        browser.back()


    def ct_organizeContact1(browser):
        browser_click(browser, name.settingBtnContact, 'id')
        browser_click(browser, name.OrganizeContactBtn, 'id')
        browser_click(browser, name.mergeSelectAllNum1, 'id')
        if hasxpath(browser, name.mergeListTitleAll, 'id'):
            browser_click(browser, name.mergeListTitleAll, 'id') # 주의) 모든 사람 선택
            browser_click(browser, name.checkBtn, 'id')
            time.sleep(1)
        else:
            print("이름과 내용이 같은 연락처 정리 내용 없음")
            time.sleep(1)

    def ct_organizeContact2(browser):
        browser_click(browser, name.mergeSelectSameContactsNum2, 'id')
        if hasxpath(browser, name.mergeListTitleAll, 'id'):           
            browser_click(browser, name.mergeListTitleAll, 'id') # 주의) 모든 사람 선택
            browser_click(browser, name.checkBtn, 'id')
            time.sleep(1)
        else:
            print("내용만 같은 연락처 정리 내용 없음")
            time.sleep(1)

    def ct_organizeContact3(browser):
        browser_click(browser, name.mergeSelectNoneAllNum3, 'id')
        if hasxpath(browser, name.mergeListTitleAll, 'id'):
            browser_click(browser, name.mergeListTitleAll, 'id') # 주의) 모든 사람 선택
            browser_click(browser, name.checkBtn, 'id')
            browser_click(browser, name.accountOkayBtn, 'id')
            time.sleep(2)
        else:
            print("이름 또는 내용이 없는 연락처 정리 내용 없음")
            time.sleep(2)
        browser.back()
        time.sleep(1)
        browser.back()

    
    def ct_exportContact(browser):
        ## test
        enterContact = "//android.widget.LinearLayout[7]"
        browser_click(browser, enterContact, 'xpath')
        browser_click(browser, name.settingBtnContact, 'id')
        # test
        browser_click(browser, name.enterimportexportBtn, 'id')
        if hasxpath(browser, name.confirmbtn, 'id'):
            browser_click(browser, name.confirmbtn, 'id')
            browser_click(browser, name.allowbtn, 'id')
        browser_click(browser, name.exportContacts, 'id')
        browser_click(browser, name.exportContactsListAll, 'id')
        browser_click(browser, name.checkBtn, 'id')
        time.sleep(3)
        browser_click(browser, name.exportContacts, 'id')


    def ct_importContact(browser):
        if hasxpath(browser, name.confirmbtn, 'id'):
            browser_click(browser, name.confirmbtn, 'id')
            browser_click(browser, name.allowbtn, 'id')
        browser_click(browser, name.importContacts, 'id')
        time.sleep(2)
        browser_click(browser, name.exportContactsListAll, 'id')
        browser_click(browser, name.checkBtn, 'id')
        time.sleep(1)
        browser.back()
        time.sleep(1)
        browser.back()
       
        
       
        
        

run()
print('1')
