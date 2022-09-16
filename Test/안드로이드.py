from cgitb import text
from curses import A_COLOR, KEY_CLOSE, KEY_ENTER, KEY_F4
import curses
from email import message, message_from_binary_file
from inspect import modulesbyfile
from msilib.schema import Class
from operator import contains
from pydoc import classname
from select import select
import time, datetime
from tkinter import Checkbutton
from tkinter.font import names
from typing_extensions import Self
from unicodedata import name
import unittest
import os
from webbrowser import BaseBrowser
from appium import webdriver
from time import monotonic, sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from driver import browser_click, browser_sendKey, hasxpath, currentTime, btn_click
import mobileVarname
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

ID= 'id'; CSS='CSS'; CLASS_NAME='class'; TAG_NAME='tag_mobileVarname'


def initialScreen(browser) :
    confirmbtn = "com.duzon.android.lulubizpotal:id/tv_confirm_buttom"
    if hasxpath(browser, confirmbtn, ID) :
        browser_click(browser, mobileVarname.confirmbtn, ID)
        browser_click(browser, mobileVarname.allowbtn, ID)


def login(browser, id, pwd) :
    loginId = "com.duzon.android.lulubizpotal:id/et_login_insert_id"
    if hasxpath(browser, loginId, ID) : 
        browser_sendKey(browser, mobileVarname.loginId, id, ID)
        browser_sendKey(browser, mobileVarname.loginPw, pwd, ID)
        browser_click(browser, mobileVarname.loginButton, ID)


def loginError(browser) : 
    if hasxpath(browser, mobileVarname.loginError, ID) :
            browser_sendKey(browser, mobileVarname.loginId, 'yjjang_test3', ID)
            browser_sendKey(browser, mobileVarname.loginPw, '1q2w3e4r', ID)
            browser_click(browser, mobileVarname.loginButton, ID)
    else :
        print('로그인 성공!')


def start(browser) :
    startbtn = "com.duzon.android.lulubizpotal:id/btn_start"
    if hasxpath(browser, startbtn, ID) :
        browser_click(browser, startbtn, ID)


def sameText(browser, text) :
    if hasxpath(browser, mobileVarname.content, ID) :
        context = browser.find_element(By.ID, mobileVarname.content).text
        if text in context :
            return True
        else :
            return False
    elif hasxpath(browser, mobileVarname.dialogContent, ID) :
        context2 = browser.find_element(By.ID, mobileVarname.dialogContent).text
        if text in context2 :
            return True
        else :
            return False
    elif hasxpath(browser, mobileVarname.dialogTitle, ID) :
        context3 = browser.find_element(By.ID, mobileVarname.dialogTitle).text
        if text in context3 :
            return True
        else :
            return False    
    elif hasxpath(browser, mobileVarname.idMessage, ID) :
        context4 = browser.find_element(By.ID, mobileVarname.idMessage).text
        if text in context4 :
            return True
        else :
            return False
    elif hasxpath(browser, f'//android.widget.TextView[@text = "{text}"]') :
        context5 = browser.find_element(By.XPATH, f'//android.widget.TextView[@text = "{text}"]').text 
        if text in context5 :
            return True
        else :
            return False
    else :
        return False


def goService(browser, service) :
    if hasxpath(browser, f'//android.widget.TextView[@text = "{service}"]') :
        time.sleep(7)
        browser_click(browser, f'//android.widget.TextView[@text = "{service}"]')
        time.sleep(2)


def hideKeyboard(browser):
    time.sleep(1)
    browser.hide_keyboard()


def clickText(browser, text) : # 메시지 내용 전체 입력
    if hasxpath(browser, f'//android.widget.TextView[@text = "{text}"]') :
        browser_click(browser, f'//android.widget.TextView[@text = "{text}"]')
        time.sleep(2)
    """ elif hasxpath(browser,  f'//android.widget.CheckedTextView[@text = "{text}"]'):
        browser_click(browser, f'//android.widget.CheckedTextView[@text = "{text}"]')
        time.sleep(2) """


def goBack(browser, num):
    if not num : num = 2
    time.sleep(num)
    browser.back()


# 10초 이상 로딩 시, 뒤로가기 작업예정
def progress(browser) : 
    count = 1
    for i in range(0,10) :
        if count == 10 : 
            browser.back()
            time.sleep(5)
        else : 
            break


# 거래처 관리(1. 거래처 등록, 2. 거래처 수정, 3. 거래처 삭제, 4. 사용자 그룹 생성, 5. 사용자 그룹 삭제)            
class Account :
    def ac_registAccount(self, browser) :
        browser_click(browser, '//android.widget.TextView[@text = "거래처관리"]')
        time.sleep(3)
        browser_click(browser, mobileVarname.plusBtnAccounts, ID)
        browser_click(browser, mobileVarname.corporationAccounts, ID)
        time.sleep(2)
        browser_sendKey(browser, mobileVarname.accountsName, '(주)더존비즈온', ID)
        # 스크롤
        browser.swipe(400, 1500, 400, 400, 1000)
        #TouchAction().press(mobileVarname.enterpriseNumber).moveTo(mobileVarname.representativeName).release()
        browser_sendKey(browser, mobileVarname.representativeName, '김용우', ID)
        browser_click(browser, mobileVarname.checkBtn, ID)


    def ac_modifyAccount(self, browser) :
        browser_click(browser, '//android.widget.TextView[@text = "(주)더존비즈온"]')
        time.sleep(1)
        browser_click(browser, mobileVarname.detailbar, ID)
        browser_click(browser, mobileVarname.modifyAccounts)
        browser_click(browser, mobileVarname.enterpriseNumber, ID)
        browser_click(browser, mobileVarname.accountGroup, ID)
        time.sleep(1)
        browser_click(browser, mobileVarname.accountGroupCheckBtn)
        browser_click(browser, mobileVarname.accountGroupOkBtn, ID)
        browser_sendKey(browser, mobileVarname.enterpriseNumber, '2222222227', ID)
        time.sleep(1)
        browser_click(browser, mobileVarname.checkBtn, ID)
        time.sleep(3)
        browser.back()


    def ac_deleteAccount(self, browser) :
        browser_click(browser, mobileVarname.selectAccounts, ID)
        time.sleep(1)
        browser.find_element(By.XPATH, "//android.widget.TextView[@text = '(주)더존비즈온']").click()
        time.sleep(1)
        browser_click(browser, mobileVarname.deleteAccounts, ID)
        time.sleep(1)
        browser_click(browser, mobileVarname.OkayBtn, ID) 
        time.sleep(2)
        browser.back()


    def ac_createGroup(self, browser) :
        browser_click(browser, mobileVarname.allAccounts, ID)
        time.sleep(2)
        browser_click(browser, mobileVarname.addUserGroup) 
        browser_sendKey(browser, mobileVarname.inputBox,'거래처 그룹2',ID)
        browser_click(browser, mobileVarname.OkayBtn, ID)
        

    def ac_deleteGroup(self, browser) :
        if hasxpath(browser, mobileVarname.trashcanBtn):
            browser_click(browser, mobileVarname.trashcanBtn) # 주의) 두 번째 사용자 그룹 삭제
            browser_click(browser, mobileVarname.OkayBtn, ID)
        elif not hasxpath(browser, mobileVarname.trashcanBtn):
            print('삭제할 사용자 그룹 없음')


    def ac_search(self, browser, name) :
        browser_click(browser, mobileVarname.searchUser, ID)
        browser_sendKey(browser, mobileVarname.search, name ,ID)


    def ac_selectMember(self, browser) :
        browser_click(browser, mobileVarname.selectmember, ID)
        browser_click(browser, mobileVarname.checkBtn, ID)
         

    def ac_createSharedGroup(self, browser) :
        browser_click(browser, mobileVarname.addSharedGroup)
        browser_sendKey(browser, mobileVarname.inputBox, '공유 테스트2', ID)
        browser_click(browser, mobileVarname.OkayBtn, ID)
        self.ac_search(browser, '장윤주')
        hideKeyboard(browser)
        self.ac_selectMember(browser)


    def ac_deleteSharedGroup(self, browser) :
        browser_click(browser, mobileVarname.trashcanBtnSharedGroupAccount)
        browser_click(browser, mobileVarname.OkayBtn, ID)
        time.sleep(2) # 2초이상의 텀 필요 1초이하는 .back() 코드 실행 안됨
        browser.back()
        time.sleep(2)
        browser.back()
        


# 연락처 (1. 연락처 등록, 2. 사용자그룹 생성, 3. 사용자그룹 수정, 4. 사용자 그룹 삭제, 5. 공유 그룹 생성, 6. 공유그룹 수정, 7. 연락처 정리(1), 8. 연락처 정리(2), 9. 연락처정리(3), 10. 연락처 가져오기
# 11. 연락처 내보내기, 12. 음성전화 13. 화상전화, 14. 링크설정 활성화, 15. 링크설정 비활성화, 16. 폰연락처에 자동저장 활성화, 17. 폰 연락처에 자동저장 비활성화)
# 연락처 삭제 추가 필요

class Contacts :
    def ct_addpeople(self, browser, name, name2, num): 
        browser_click(browser, mobileVarname.plusBtnContact, ID)
        browser_click(browser, mobileVarname.registerBtnContact, ID)
        time.sleep(1)
        browser_sendKey(browser, mobileVarname.inputfirstname, name, ID)
        browser_sendKey(browser, mobileVarname.inputlastname, name2, ID)
        browser_sendKey(browser, mobileVarname.inputTelephoneNumber, num, ID)
        

    def ct_registerContacts(self, browser) :
        browser_click(browser, '//android.widget.TextView[@text = "연락처"]')
        self.ct_addpeople(browser, '김', '더존', '01022223333')
        browser_sendKey(browser, mobileVarname.inputemail, 'aaaa@naver.com', ID)
        browser_click(browser, mobileVarname.workplaceInformation)
        browser_sendKey(browser, mobileVarname.inputAffiliation, '서비스QA', ID)
        browser_sendKey(browser, mobileVarname.inputPosition, '사원', ID)
        browser_sendKey(browser, mobileVarname.inputAssignedTask, '서비스QA', ID)
        browser_click(browser, mobileVarname.searchAddressContact)
        time.sleep(4)
        browser_sendKey(browser, mobileVarname.inputRegionName, '남산면 버들1길 130')
        browser_click(browser, mobileVarname.searchKey)
        browser_click(browser, mobileVarname.addressResults)
        time.sleep(3)
        browser_click(browser, mobileVarname.checkBtn, ID)


    def ct_registerContacts_add(self, browser) :
        self.ct_addpeople(browser, '이', '더존', '01011111111')
        browser_click(browser, mobileVarname.checkBtn, ID)
        self.ct_addpeople(browser, '이', '', '')
        browser_click(browser, mobileVarname.checkBtn, ID)


    def ct_createGroup(self, browser):
        browser_click(browser, mobileVarname.allContacts, ID)
        time.sleep(1)
        browser_click(browser, mobileVarname.addContactUserGroup)
        browser_sendKey(browser, mobileVarname.inputBox, '테스트 그룹',ID)
        browser_click(browser, mobileVarname.OkayBtn, ID)


    def ct_modifyGroup(self, browser):
        browser_click(browser, mobileVarname.modifyGroupName)
        browser_sendKey(browser, mobileVarname.inputBox, '테스트 그룹2',ID)
        browser_click(browser, mobileVarname.OkayBtn, ID)


    def ct_deleteGroup(self, browser):
        browser_click(browser, mobileVarname.trashcanBtnContact) # 주의) 두 번째 사용자 그룹 삭제
        browser_click(browser, mobileVarname.OkayBtn, ID)


    def ct_createSharedGroup(self, browser):
        browser_click(browser, mobileVarname.addContactSharingUserGroup)
        time.sleep(2)
        browser_click(browser, mobileVarname.searchUser, ID)
        browser_sendKey(browser, mobileVarname.search, "장윤주", ID)
        time.sleep(1)
        browser.back()
        browser_click(browser, mobileVarname.selectmember, ID)
        browser_click(browser, mobileVarname.checkBtn, ID)
        browser_sendKey(browser, mobileVarname.inputBox, '테스트 공유', ID)
        browser_click(browser, mobileVarname.OkayBtn, ID)


    def ct_modifySharedGroup(self, browser):
        browser_click(browser, mobileVarname.modifySharingGroupName) # 주의) 첫 번째 공유그룹 수정
        browser_sendKey(browser, mobileVarname.inputBox, '테스트 공유2',ID) 
        browser_click(browser, mobileVarname.OkayBtn, ID)


    def ct_deleteSharedGroup(self, browser):
        if hasxpath(browser, mobileVarname.trashcanBtnSharingContact):
            time.sleep(2)
            browser_click(browser, mobileVarname.trashcanBtnSharingContact) # 주의) 첫 번째 공유그룹 삭제
            browser_click(browser, mobileVarname.OkayBtn, ID)
        else :
            print('삭제할 공유그룹 없음!')
        time.sleep(3)
        browser.back()   


    def ct_contactExport(self, browser):
        browser_click(browser, mobileVarname.settingBtnContact, ID)
        browser_click(browser, mobileVarname.enterimportexportBtn, ID)
        if hasxpath(browser, mobileVarname.confirmbtn, ID):
            browser_click(browser, mobileVarname.confirmbtn, ID)
            browser_click(browser, mobileVarname.allowbtn, ID)
        browser_click(browser, mobileVarname.exportContacts, ID)
        browser_click(browser, mobileVarname.exportContactsListFirst) # 주의) 첫 번째 사람만 클릭
        browser_click(browser, mobileVarname.checkBtn, ID)
        time.sleep(3)
        browser_click(browser, mobileVarname.exportContacts, ID)


    def ct_contactImport(self, browser):
        browser_click(browser, mobileVarname.importContacts, ID)
        time.sleep(1)
        browser_click(browser, mobileVarname.exportContactsListFirst) # 주의) 첫 번째 사람만 클릭
        browser_click(browser, mobileVarname.checkBtn, ID)
        time.sleep(3)
        browser.back()
    

    def ct_organizeContact(self, browser):
        browser_click(browser, mobileVarname.OrganizeContactBtn, ID)
        time.sleep(1)
        for i in range(1, 4):
            organize = "//android.widget.LinearLayout["
            organize = organize + str(i+2) + ']'
            browser_click(browser, organize)
            time.sleep(1)
            if hasxpath(browser, mobileVarname.mergeListTitleAll, ID):
                browser_click(browser, mobileVarname.mergeListTitleAll, ID) # 주의) 모든 사람 선택 or 첫 번째 사람 전체 선택
                if hasxpath(browser, mobileVarname.mergeListTitleSecond): # 주의) 이름과 내용이 같은 연락처 네 번째 선택 - 이더존이 정리되어야 내용만 같은 연락처 가능..
                    browser_click(browser, mobileVarname.mergeListTitleSecond)
                    if hasxpath(browser, mobileVarname.OkayBtn, ID):
                        time.sleep(1)
                        browser_click(browser, mobileVarname.OkayBtn, ID)
                        time.sleep(1)
                browser_click(browser, mobileVarname.checkBtn, ID)
                if hasxpath(browser, mobileVarname.OkayBtn, ID):
                    browser_click(browser, mobileVarname.OkayBtn, ID)
            else:
                print(str(i) + "번째 연락처 정리 내용 없음")
                time.sleep(2)
                browser.back()
        time.sleep(2)
        browser.back()
        if hasxpath(browser, "//android.widget.TextView[@text = '연락처 정리']"):
            time.sleep(2)
            browser.back()


    def ct_LinkSetting(self, browser):
        browser_click(browser, mobileVarname.linkSettingBtn, ID)
        if hasxpath(browser, mobileVarname.OkayBtn, ID):
            browser_click(browser, mobileVarname.OkayBtn, ID)
            print('링크 설정 비활성화')
        elif not hasxpath(browser, mobileVarname.OkayBtn, ID):
            print('링크 설정 활성화')
    

    def ct_autosaveOnOff(self, browser):
        browser_click(browser, mobileVarname.autosaveBtn, ID)
        if hasxpath(browser, mobileVarname.confirmbtn, ID):
            browser_click(browser, mobileVarname.confirmbtn, ID)
            browser_click(browser, mobileVarname.allowbtn, ID)
        time.sleep(1)
        if hasxpath(browser, mobileVarname.OkayBtn, ID):
            browser_click(browser, mobileVarname.OkayBtn, ID)
            print('자동저장 활성화')
        elif not hasxpath(browser, mobileVarname.OkayBtn, ID):
            print('자동저장 비활성화')
        time.sleep(2)
        browser.back()
        time.sleep(2)
        browser.back()



# 메일 (1. 메일쓰기(1), 2. 메일쓰기(2), 3. 메일쓰기(3), 4. 메일쓰기(4), 5. 메일쓰기(5), 6. 답장(1), 7. 답장(2), 8. 전달, 9. 읽음 설정, 10. 삭제(1), 11. 삭제(2))
class Mail :
    normal='일반'; reserve='예약'; security='보안'; individual='개별전송'; reply='답장'; replyAll='전체답장'; forward='전달'; reading='읽음처리' ; delete = '삭제'; temporary = '임시저장'
   
    def ma_recipient(self, browser, address) :
        browser_click(browser, mobileVarname.dropdownBtn, ID)
        time.sleep(1)
        browser_click(browser, mobileVarname.recipientMail)
        browser_sendKey(browser, mobileVarname.recipientMail, address)
        browser.press_keycode(66)
        time.sleep(1)
        self.ma_receivercc(browser)
        time.sleep(2)


    def ma_receivercc(self, browser) :
        browser_click(browser, mobileVarname.referenceMail)
        browser_sendKey(browser, mobileVarname.referenceMail, "yjjang_test1@wehago.com")
        browser.press_keycode(66)
        browser_click(browser, mobileVarname.hiddenReferenceMail)
        browser_sendKey(browser, mobileVarname.hiddenReferenceMail, "yjjang_test2@wehago.com")
        browser.press_keycode(66)
        time.sleep(2)
        browser.hide_keyboard()


    def ma_hasMailTitle(self, browser):
        # 메일 제목이 없는 경우
        if sameText(browser, '제목이 지정되지 않았습니다.\n제목없이 메일을 보내시겠습니까?') :
            browser_click(browser, mobileVarname.OkayBtn, ID)
            print('메일 제목 입력안됨')
            time.sleep(4)


    def ma_wedriveUpload(self, browser) :
        browser_click(browser, mobileVarname.attachfileBtn, ID)
        browser_click(browser, mobileVarname.uploadBtn, ID)
        time.sleep(2)
        browser_click(browser, mobileVarname.uploadfromWedrive)
        time.sleep(5)
        if hasxpath(browser, mobileVarname.selectWedrive):
            browser_click(browser, mobileVarname.selectWedrive) # 첫 번째 파일 선택
        else :
            print('선택할 웹스토리지 파일 없음')
        time.sleep(4)
        browser_click(browser, mobileVarname.checkBtn, ID)
        time.sleep(4)
        browser.back()


    def ma_selectLocalFile(self, browser) :
        if not hasxpath(browser, mobileVarname.cameraBtn):
            browser_click(browser, mobileVarname.selectPhoneAlbum, ID)
            time.sleep(5)
            if hasxpath(browser, mobileVarname.selectPhoneAlbum, ID):
                browser_click(browser, mobileVarname.selectPhoneAlbum, ID)
        else :
            print('선택할 파일 없음. 앨범에 파일 다운로드 필요')
            goBack(browser, 2)


    def ma_localUpload(self, browser) :
        browser_click(browser, mobileVarname.attachfileBtnMessage, ID)
        browser_click(browser, mobileVarname.uploadBtn, ID)
        time.sleep(2)
        browser_click(browser, mobileVarname.uploadfromAlbum)
        time.sleep(5)
        self.ma_selectLocalFile(browser)
        goBack(browser, 5)


    def ma_sendMailTitle(self, browser, name) :
        browser_sendKey(browser, mobileVarname.mailTitle, "메일 제목 -- "+ name, ID)
        time.sleep(2)


    def ma_sendMailContent(self, browser) :
        browser_sendKey(browser, mobileVarname.mailContent, "테스트입니다", ID)
        time.sleep(2)


    def ma_clickOption(self, browser, mail) :
        browser_click(browser, mobileVarname.mailOptionLayout, ID)
        if mail == self.reserve :
            browser_click(browser, mobileVarname.mailReservationBtn, ID)
            browser_click(browser, mobileVarname.TimeBtn, ID)
            browser_click(browser, mobileVarname.textModeBtn, ID)
            time.sleep(2)        
            browser_sendKey(browser, mobileVarname.inputHour, currentTime().strftime('%I'), ID)
            time.sleep(4)
            browser_sendKey(browser, mobileVarname.inputMinute, currentTime().strftime('%M'), ID)
            time.sleep(2)
            browser_click(browser, mobileVarname.MailOkBtn, ID)
            time.sleep(4)
            if sameText(browser, '예약 시간은 현재 시간 이후부터 설정 가능합니다.'):
                browser_click(browser, mobileVarname.OkayBtn, ID)
                print('1분뒤 다시 보내기')
                time.sleep(60)
                browser_sendKey(browser, mobileVarname.inputHour, currentTime().strftime('%I'), ID)
                browser_sendKey(browser, mobileVarname.inputMinute, currentTime().strftime('%M'), ID)
                browser_click(browser, mobileVarname.MailOkBtn, ID)
                time.sleep(4)              
        elif mail == self.security :
            browser_click(browser, mobileVarname.mailSecurityBtn, ID)
        elif mail == self.individual :
            browser_click(browser, mobileVarname.mailIndividualBtn, ID)          


    def ma_clickSendButton(self, browser, mail) :
        if mail == self.reserve :
            self.ma_clickOption(browser, mail)
            time.sleep(2)
            browser_click(browser, mobileVarname.checkBtn, ID)
            self.ma_hasMailTitle(browser)
            goBack(browser, 6)

        elif mail == self.security:
            self.ma_clickOption(browser, mail)
            time.sleep(2)
            browser_click(browser, mobileVarname.checkBtn, ID)
            self.ma_hasMailTitle(browser)
            time.sleep(2)
            browser_click(browser, mobileVarname.mailStoragePeriodDate, ID)
            browser_click(browser, mobileVarname.OkayBtn, ID)    
            browser_sendKey(browser, mobileVarname.mailSecurityPwd, '1111', ID)
            browser_sendKey(browser, mobileVarname.mailSecurityPwdCheck, '1111', ID)
            browser_click(browser, mobileVarname.checkBtn, ID)
            goBack(browser, 6)

        elif mail == self.individual :
            self.ma_clickOption(browser, mail)
            browser_click(browser, mobileVarname.checkBtn, ID)
            self.ma_hasMailTitle(browser)
            goBack(browser, 6)

        elif mail == self.temporary :
            goBack(browser, 6)
            browser_click(browser, mobileVarname.OkayBtn, ID)
            browser_click(browser, mobileVarname.allMail, ID)
            browser_click(browser, mobileVarname.mailTemporaryStorageBox)
            time.sleep(2)
            browser_click(browser, mobileVarname.firstMail,'xpath')
            time.sleep(3)
            browser_click(browser, mobileVarname.checkBtn, ID)
            self.ma_hasMailTitle(browser)
            goBack(browser, 6)
            browser_click(browser, mobileVarname.allMail, ID)
            browser_click(browser, mobileVarname.fullMailBox)

        elif mail == self.replyAll :
            browser_click(browser, mobileVarname.checkBtn, ID)
            if sameText(browser, '받는 사람을 입력해 주세요.') :
                browser_click(browser, mobileVarname.OkayBtn, ID)
                self.ma_recipient(browser, 'yjjang1_@naver.com')
                browser_click(browser, mobileVarname.checkBtn, ID)
                self.ma_hasMailTitle(browser)
            goBack(browser, 6)

        else :
           browser_click(browser, mobileVarname.checkBtn, ID)
           self.ma_hasMailTitle(browser)
           goBack(browser, 6)

        goService(browser, '메일')
        

    def ma_sendMailDetail(self, browser, address, name, local= None, wedrive= None) :
        browser_click(browser, mobileVarname.plusBtnMail, ID)
        self.ma_recipient(browser, address)
        time.sleep(2)
        self.ma_sendMailTitle(browser, name)
        self.ma_sendMailContent(browser)
        if local :
            self.ma_localUpload(browser)
            time.sleep(2)
        if wedrive :
            self.ma_wedriveUpload(browser)
            time.sleep(2)        


    def ma_sendMail(self, browser) :
        browser_click(browser, '//android.widget.TextView[@text = "메일"]')
        time.sleep(2)
        self.ma_sendMailDetail(browser, 'yjjang1_@naver.com',self.normal)
        self.ma_clickSendButton(browser, self.normal)


    def ma_sendMailWedrive(self, browser) :
        self.ma_sendMailDetail(browser, 'yjjang1_@naver.com', '웹스토리지 파일 첨부', wedrive=True)
        self.ma_clickSendButton(browser, self.normal)


    def ma_sendMailLocalWedrive(self, browser) :
        self.ma_sendMailDetail(browser, 'yjjang1_@naver.com', '로컬 파일 첨부', local=True)
        self.ma_clickSendButton(browser, self.normal)

    def ma_sendReservedMail(self, browser) :
        self.ma_sendMailDetail(browser, 'yjjang1_@naver.com', self.reserve)
        self.ma_clickSendButton(browser, self.reserve)


    def ma_sendSecureMail(self, browser) :
        self.ma_sendMailDetail(browser, 'yjjang1_@naver.com', self.security)
        self.ma_clickSendButton(browser, self.security)


    def ma_temporarySave(self, browser) :
        self.ma_sendMailDetail(browser, 'yjjang1_@naver.com', self.temporary)
        self.ma_clickSendButton(browser , self.temporary)


    def ma_individualTransfer(self, browser) :
        self.ma_sendMailDetail(browser, 'yjjang1_@naver.com', self.individual)
        self.ma_clickSendButton(browser, self.individual)


    def ma_sendMore(self, browser, mail) :
        if hasxpath(browser, mobileVarname.emptyMail, ID):
                self.ma_sendMailDetail(browser, 'ptestjy_1719@wehago.com','답장용')
                self.ma_clickSendButton(browser, self.normal)
                time.sleep(1)
                browser_click(browser, mobileVarname.firstMail)
        else: 
            browser_click(browser, mobileVarname.firstMail)
        browser_click(browser, mobileVarname.mailReplyDetailTitlebar, ID)
        if mail == self.reply :
            browser_click(browser, mobileVarname.mailReplyBtn)
        elif mail == self.replyAll :
            browser_click(browser, mobileVarname.mailAllReplyBtn)
        elif mail == self.forward :
            browser_click(browser, mobileVarname.mailDeliveryBtn)
            self.ma_recipient(browser, 'yjjang1_@naver.com')
        else :
            goBack(browser, 6)
            goBack(browser, 6)
            print('답장 or 전체답장 or 전달 이상있음')


    def ma_replyMail(self, browser) :
        self.ma_sendMore(browser, self.reply)
        self.ma_clickSendButton(browser, self.reply)


    def ma_replyMailAll(self, browser) :
        self.ma_sendMore(browser, self.replyAll)
        self.ma_clickSendButton(browser, self.replyAll)


    def ma_deliveryMail(self, browser) :
        self.ma_sendMore(browser, self.forward)
        self.ma_clickSendButton(browser, self.forward)


    def ma_selectMail(self, browser, mail) :
        if hasxpath(browser, mobileVarname.selectMailFirstCheckBox) :
            browser_click(browser, mobileVarname.selectMailFirstCheckBox)
            if mail == self.reading :
                browser_click(browser, mobileVarname.mailListReadBtn, ID)
            else :
                browser_click(browser, mobileVarname.mailListDeleteBtn, ID)
                browser_click(browser, mobileVarname.OkayBtn, ID)
                goBack(browser, 6) # 확인 필요 - 뒤로가기 적용이 안되고 있었음. 
        else :
            print('선택할 메일 없음')


    def ma_readProcessing(self, browser) :
        browser_click(browser, mobileVarname.mailEditBtn, ID)
        time.sleep(2)
        self.ma_selectMail(browser, self.reading)


    def ma_deleteMail(self, browser) : 
        self.ma_selectMail(browser, self.delete)
        goBack(browser, 6)


    def ma_emptyTrash(self, browser) :
        browser_click(browser, mobileVarname.allMail, ID)
        time.sleep(3)
        if hasxpath(browser,mobileVarname.mailEmptyTrashBtn) :
            browser_click(browser,mobileVarname.mailEmptyTrashBtn)
            browser_click(browser, mobileVarname.OkayBtn, ID)         
        else :
            print("휴지통 비우기 버튼 없음")
        goBack(browser, 6)
    


# 메시지 (1. 일반메시지 보내기, 2. 보안메시지 보내기, 3. 중요메시지 보내기, 4. 예약 메시지 보내기, 5. 답장/전체답장/전달/다시 보내기 보내기, 6. 모두 읽음 처리, 7. 메시지 검색, 8. 첨부파일 다운받기
# 9. 보안 메시지 확인, 10. 즐겨찾기 설정 11. 받은 메시지 삭제, 12. 보낸 메시지 삭제)
class Message :
    normal='일반'; reserve='예약'; security='보안'; importance='중요'; reply='답장'; replyAll='전체답장'; forward='전달'; resend = '다시 보내기'

    def ms_recipient(self, browser, name) :
        if hasxpath(browser, '//android.widget.MultiAutoCompleteTextView[@text = "이름 또는 아이디를 입력해주세요."]') :
            browser_click(browser, mobileVarname.userSelectBtn, ID)
            time.sleep(2)
            browser_click(browser, mobileVarname.searchUser, ID)
            browser_sendKey(browser, mobileVarname.search, name, ID)
            time.sleep(1)
            browser.hide_keyboard()
            browser_click(browser, mobileVarname.selectmember, ID)
            browser_click(browser, mobileVarname.checkBtn, ID)


    def ms_hascontents(self, browser) :
        time.sleep(2)
        if hasxpath(browser, '//android.widget.TextView[@text = "메시지 보내기"]') :
            browser_sendKey(browser, mobileVarname.messageContent, '메시지 내용입력 오류', ID)
            browser_click(browser, mobileVarname.checkBtn, ID)
            time.sleep(2)
    

    def ms_wedriveUpload(self, browser) :
        browser_click(browser, mobileVarname.attachfileBtnMessage, ID)
        browser_click(browser, mobileVarname.uploadBtn, ID)
        time.sleep(2)
        browser_click(browser, mobileVarname.uploadfromWedrive)
        time.sleep(5)
        if hasxpath(browser, mobileVarname.selectWedrive):
            browser_click(browser, mobileVarname.selectWedrive) # 첫 번째 파일 선택
        else :
            print('선택할 웹스토리지 파일 없음')
        time.sleep(4)
        browser_click(browser, mobileVarname.checkBtn, ID)
        time.sleep(4)
        browser.back()


    def ms_localUpload(self, browser) :
        browser_click(browser, mobileVarname.attachfileBtnMessage, ID)
        browser_click(browser, mobileVarname.uploadBtn, ID)
        time.sleep(2)
        browser_click(browser, mobileVarname.uploadfromAlbum)
        time.sleep(5)
        Mail().ma_selectLocalFile(browser)
        goBack(browser, 5)
    

    def ms_clickOption(self, browser, message) :
        browser_click(browser, mobileVarname.messageOptionBtn, ID)
        if message == self.reserve :
            browser_click(browser, mobileVarname.messageReservationBtn, ID)
            browser_click(browser, mobileVarname.TimeBtn, ID)
            browser_click(browser, mobileVarname.textModeBtn, ID)
            time.sleep(2)        
            browser_sendKey(browser, mobileVarname.inputHour, currentTime().strftime('%I'), ID)
            time.sleep(4)
            browser_sendKey(browser, mobileVarname.inputMinute, currentTime().strftime('%M'), ID)
            time.sleep(2)
            browser_click(browser, mobileVarname.MailOkBtn, ID)
            time.sleep(3)
            if sameText(browser, '예약 시간은 현재 시간 이후부터 설정 가능합니다.'):
                browser_click(browser, mobileVarname.OkayBtn, ID)
                print('1분뒤 다시 보내기')
                time.sleep(60)
                browser_sendKey(browser, mobileVarname.inputHour, currentTime().strftime('%I'), ID)
                browser_sendKey(browser, mobileVarname.inputMinute, currentTime().strftime('%M'), ID)
                browser_click(browser, mobileVarname.MailOkBtn, ID)
                time.sleep(3)              
        elif message == self.security :
            browser_click(browser, mobileVarname.messageSecurityBtn, ID)
        elif message == self.importance :
            browser_click(browser, mobileVarname.messageImportantBtn, ID)


    def ms_sendBtn(self, browser, message) :
        if message == self.importance :
            self.ms_clickOption(browser, message)            
        elif message == self.reserve :
            self.ms_clickOption(browser, message)            
        elif message == self.security :
            self.ms_clickOption(browser, message)           
        browser_click(browser, mobileVarname.checkBtn, ID)
        time.sleep(2)
    
    
    def ms_sendMessageDetail(self, browser, name, message, local= None, wedrive= None) :
        browser_click(browser, mobileVarname.plusBtnMessage, ID)
        time.sleep(3)
        self.ms_recipient(browser, name)
        browser_sendKey(browser, mobileVarname.messageContent, message + '메시지 입력 테스트', ID)
        time.sleep(1)
        if local :
            self.ms_localUpload(browser)
            time.sleep(2)
        if wedrive :
            self.ms_wedriveUpload(browser)
            time.sleep(2)
        self.ms_sendBtn(browser, message)


    def ms_sendMessage(self, browser) :
        browser_click(browser, '//android.widget.TextView[@text = "메시지"]')
        time.sleep(2)
        self.ms_sendMessageDetail(browser, '문지영', self.normal, local = True, wedrive = True)


    def ms_sendSecurityMessage(self, browser) :
        self.ms_sendMessageDetail(browser, '문지영', self.security) 


    def ms_sendImportantMessage(self, browser) :
        self.ms_sendMessageDetail(browser,'문지영', self.importance)


    def ms_sendReservationMessage(self, browser) :
        #test
        #browser_click(browser, '//android.widget.TextView[@text = "메시지"]')
        #time.sleep(2)
        #test
        self.ms_sendMessageDetail(browser, '문지영', self.reserve)

    """ def ms_searchMessage(self, browser, content) : # 포기 클릭 > 입력 > 엔터가 안됨 
        #test
        browser_click(browser, '//android.widget.TextView[@text = "메시지"]')
        time.sleep(2)
        #test
        browser_click(browser, mobileVarname.searchUser, ID)
        browser_click(browser, mobileVarname.search, ID)
        browser_sendKey(browser, mobileVarname.search, content, ID)
       
        #browser.press_keycode(84)
        hideKeyboard(browser) """


    def ms_sendMore(self, browser, message, name) :
        clickText(browser, '일반메시지 입력 테스트')
        #browser_click(browser, mobileVarname.firstMessage) # 첫 번째 메일 클릭 -> 상황따라 clickText(browser, '일반메시지 입력 테스트')와 바꿔쓰기
        browser_click(browser, mobileVarname.right3Btn, ID)
        if message == self.reply :
            clickText(browser, '답장')
        elif message == self.replyAll :
            clickText(browser, '전체답장')
        elif message == self.forward :
            clickText(browser, '전달')
        elif message == self.resend :
            clickText(browser, '다시보내기')
        time.sleep(3)
        self.ms_recipient(browser, name)
        browser_sendKey(browser, mobileVarname.messageContent, message + '메시지 입력 테스트', ID)
        time.sleep(1)
        self.ms_sendBtn(browser, message)
        time.sleep(6) # 6초 이상 필요


    def ms_replyMessage(self, browser) :
        self.ms_sendMore(browser, self.reply, '문지영')


    def ms_replyAllMessage(self, browser) :
        self.ms_sendMore(browser, self.replyAll, '문지영')


    def ms_forwardMessage(self, browser) :
        self.ms_sendMore(browser, self.forward, '문지영')


    def ms_enterSendMessage(self, browser) :
        browser_click(browser, mobileVarname.messageDropDownSelectBar, ID)
        time.sleep(8)      
        browser_click(browser, mobileVarname.enterSendMessage)
        time.sleep(8)


    def ms_enterReceivedMessage(self, browser) :
        browser_click(browser, mobileVarname.messageDropDownSelectBar, ID)
        time.sleep(10)
        browser_click(browser, mobileVarname.enterReceivedMessage)
        time.sleep(8)   


    def ms_resendMessage(self, browser) :
        self.ms_enterSendMessage(browser)
        self.ms_sendMore(browser, self.resend, '문지영')
        self.ms_enterReceivedMessage(browser)
    

    def ms_selectMessage(self, browser) :
        browser_click(browser, mobileVarname.selectMessage, ID)
        time.sleep(2)
        browser_click(browser, mobileVarname.selectAllMessageChckBox, ID)


    def ms_readMessage(self, browser) : # 일회용...
        self.ms_selectMessage(browser)
        if hasxpath(browser, '//android.widget.TextView[@text = "읽음"]'):
            browser_click(browser, '//android.widget.TextView[@text = "읽음"]')
        else :
            print('읽음처리 되어있음')
        goBack(browser, 2)


    def ms_downdloadFile(self, browser) :
        clickText(browser, '일반메시지 입력 테스트')
        browser_click(browser, mobileVarname.receiveMessageAttachmentBtn, ID)
        time.sleep(3)
        if hasxpath(browser, mobileVarname.messageFileDetail):
            browser_click(browser, mobileVarname.messageFileDetail)
            time.sleep(2)
            clickText(browser, '웹스토리지 저장')
        else :
            print('첨부파일 없음! 확인 필요')
        goBack(browser, 2) 
        goBack(browser, 4) 


    def ms_readSecureMessage(self, browser, pwd) :
        if hasxpath(browser, '//android.widget.TextView[@text = "보안 메시지"]') :
            #clickText(browser, '보안 메시지')
            browser_click(browser, '//android.widget.TextView[@text = "보안 메시지"]')
            time.sleep(4)
            if hasxpath(browser, mobileVarname.dialogEditText, ID) :
                browser_sendKey(browser, mobileVarname.dialogEditText, pwd, ID)
                browser_click(browser, mobileVarname.dialogOkBtn, ID)
                if hasxpath(browser, mobileVarname.messageError, ID):
                    print('비밀번호 오류')
                    goBack(browser, 2)
            goBack(browser, 2)
        else :
            print('보안메시지 없음')


    def ms_bookmark(self, browser) :
        browser_click(browser, mobileVarname.firstMessage) # 첫 번째 메일 클릭
        browser_click(browser, mobileVarname.messageBookmark, ID)
        goBack(browser, 2)
    

    def ms_deleteMessage(self, browser, send) :
        if send == 'receive' :
            self.ms_enterReceivedMessage(browser)
        elif send == 'send' :
            self.ms_enterSendMessage(browser)
        browser_click(browser, mobileVarname.selectMessage, ID)
        time.sleep(2)
        
        for i in range(0, 5) :
            browser_click(browser, mobileVarname.selectAllMessageChckBox, ID)
            if hasxpath(browser,  '//android.widget.TextView[@text = "삭제"]') :
                clickText(browser, '삭제')
                browser_click(browser, mobileVarname.dialogOkBtn, ID)
                time.sleep(9)
            else : break
        time.sleep(2)
        
        if hasxpath(browser,  '//android.widget.TextView[@text = "삭제"]') :
            print('메시지 삭제 확인 필요')
        goBack(browser, 2)


    def ms_deleteReceiveMessage(self, browser) :
        self.ms_deleteMessage(browser, 'receive')


    def ms_deleteSendMessage(self, browser) : # 마지막 화면
        self.ms_deleteMessage(browser, 'send')
        goBack(browser, 2) # 메뉴탭으로 고고



# 메신저 (01. 그룹 대화방 생성, 02. 대화내용 입력(1) - 복붙, 03. 대화내용 입력(2) - 삭제, 04. 대화내용 입력(3) - 댓글, 05. 대화내용 입력(4) -이모티콘,
#         06. 연락처 첨부, 07. 파일 모아보기, 08. 공개 / 비공개 그룹 설정 09. 대화내용 검색, 10. 파일 첨부 11. 즐겨찾는 대화방 설정, 12. 참여자 목록 확인(1) - 프로필 클릭, 
#         13. 참여자 목록 확인(2) - 마스터 설정, 14. 참여자 목록 확인(3) - 내보내기 및 나가기, 15. 그룹 대화방 상대 내보내기, 16. 1:1 대화방 생성)

class Communication : 
    album = '사진첩' ; camera = '카메라' ; wedrive = '웹스토리지' ; contacts = '연락처'; webconference = '화상회의'
    copy = '복사' ; delete = '삭제' ; comment = '댓글' ; reaction = '리액션'; one = '1인용'; group = '그룹용'; private = '비공개'; allow = '검색 허용'
    
    def cc_createRoom(self, browser, people, name, private = None, allow = None) :
        browser_click(browser, '//android.widget.TextView[@text = "메신저"]') # 그룹 대화방 첫번째에만 놓기
        time.sleep(3)
        browser_click(browser, mobileVarname.plusBtnContact, ID)
        # 1:1대화
        if people == self.one :
            browser_click(browser, mobileVarname.newChat, ID)
            time.sleep(2)
            Account().ac_search(browser, name)
            hideKeyboard(browser)
            Account().ac_selectMember(browser)
        # 그룹대화
        elif people == self.group :
            browser_click(browser, mobileVarname.newGorupChat, ID)
            # 그룹 참여자 - 조직도
            browser_click(browser, mobileVarname.userSelectBtn, ID)
            Account().ac_search(browser, name)
            hideKeyboard(browser)
            Account().ac_selectMember(browser)
        
        # 그룹 이름
            browser_sendKey(browser, mobileVarname.groupChatName, '자동화 테스트', ID)
        
        # 비공개 그룹
            if private :
                browser_click(browser, mobileVarname.privateChat, ID)
            # 검색 허용
                if allow :
                    browser_click(browser, mobileVarname.allowSearchBtn, ID)
            browser_click(browser, mobileVarname.checkBtn, ID)
            if sameText(browser, '동일한 그룹이름이 존재합니다.') :
                browser_click(browser, mobileVarname.dialogOkBtn, ID)
                time.sleep(2)
                browser_sendKey(browser, mobileVarname.groupChatName, '자동화 테스트 ' + str(currentTime())[5:16], ID)
                browser_click(browser, mobileVarname.checkBtn, ID)


    # 그룹 대화방 생성
    def cc_createGroupChat(self, browser) :
        self.cc_createRoom(browser, self.group, '장윤주')
    

    # 1:1 대화방 생성
    def cc_createChat(self, browser) :
        self.cc_createRoom(browser, self.one, '장윤주')
        goBack(browser, 3)
        goBack(browser, 3) # 메인 화면으로 돌아가기


    # 채팅 전송
    def cc_sendChat(self, browser) :
        # test
        #browser_click(browser, '//android.widget.TextView[@text = "메신저"]')
        #time.sleep(6)
        #clickText(browser, '자동화 테스트')
        #test
        
        # 멘션
        browser_sendKey(browser, mobileVarname.inputChat,'@', ID)
        clickText(browser, '@장윤주') 
        browser_click(browser, mobileVarname.cc_sendBtn, ID)

        # 채팅
        browser_sendKey(browser, mobileVarname.inputChat,'test', ID)
        browser_click(browser, mobileVarname.cc_sendBtn, ID)


    # 채팅 검색
    def cc_searchChat(self, browser) :
        # test
        #browser_click(browser, '//android.widget.TextView[@text = "메신저"]')
        #time.sleep(6)
        #clickText(browser, '자동화 테스트')
        #test
        browser_click(browser, mobileVarname.right2Btn, ID)
        browser_sendKey(browser, mobileVarname.searchEditText, 'test', ID)
        action = ActionChains(browser)
        rightBtn = browser.find_element(By.XPATH, '//android.widget.TextView[@text = "취소"]')
        action.move_to_element_with_offset(rightBtn, 0, 2570).click().perform()
        #browser_click(browser, mobileVarname.talkChatContent, ID) # 텍스트 클릭 시, 로딩 발생
        goBack(browser, 2)



    # 파일 첨부옵션(사진첩, 카메라, 위드라이브, 연락처) - 화상회의 제외
    def cc_appendingOption(self, browser, option) : # cc_attachFileOption
        # test
        #browser_click(browser, '//android.widget.TextView[@text = "메신저"]')
        #time.sleep(2)
        #clickText(browser, 'testtest')
        #time.sleep(2)
        # test
        action = ActionChains(browser)
        plusBtn = browser.find_element(By.ID, 'com.duzon.android.lulubizpotal:id/interactive_attach_file_button')     
        # 사진첩 선택 -> 메일 로컬 첨부와 동일 (o)
        if option == self.album :
            action.move_to_element_with_offset(plusBtn, 60, 400).click().perform()
            Mail().ma_selectLocalFile(browser)
        # 카메라 선택 (o)
        elif option == self.camera :
            action.move_to_element_with_offset(plusBtn, 500, 400).click().perform()
            # 위하고 내에서 카메라 앱 초기 실행 얼럿창
            if sameText(browser, "카메라권한 - 프로필 등록 및 서비스 내 사진 첨부시와 QR코드 스캔에 사용됩니다.") :
                browser_click(browser, 'android.widget.Button', CLASS_NAME)
                time.sleep(4)
                if sameText(browser, "WEHAGO에서 사진을 촬영하고 동영상을 녹화하도록 허용하시겠습니까?") :
                    time.sleep(2)
                    browser_click(browser, mobileVarname.permissionAllowBtn, ID)
                else :
                    print('[메신저] 채팅 파일첨부_카메라 두 번째 얼럿창 확인 필요')
            else :
                print('[메신저] 채팅 파일첨부_카메라 초기 설정을 하지 않았았다면, 첫 번째 얼럿창 확인 필요')
            browser_click(browser, mobileVarname.shutterBtn, ID)
            browser_click(browser, mobileVarname.cameraDoneBtn, ID)
            
        # 웹스토리지 선택 (o)
        elif option == self.wedrive :
            action.move_to_element_with_offset(plusBtn, 830, 400).click().perform()
            browser_click(browser, mobileVarname.selectFirstWedriveFile)
            browser_click(browser, mobileVarname.checkBtn, ID)

        # 연락처 선택 (o)
        elif option == self.contacts :
            name = '김더존'
            action.move_to_element_with_offset(plusBtn, 1300, 400).click().perform()
            Account().ac_search(browser, name)
            leftBtn = browser.find_element(By.ID, 'com.duzon.android.lulubizpotal:id/btn_left')
            # 돋보기 버튼 클릭 성고오오오오오옹
            action.move_to_element_with_offset(leftBtn, 1240, 2570).click().perform()
            hideKeyboard(browser)
            clickText(browser, name)
            if sameText(browser, name + ' 전송하시겠습니까?') :
                browser_click(browser, mobileVarname.OkayBtn, ID)
        
        else :
            print('[메신저] 파일첨부파트 확인필요')
        

        # 화상회의 선택 - 앱 별도 설치 필요 -> 보류
        #action.move_to_element_with_offset(plusBtn, 60, 500).click().perform()
    

    def cc_appendingLocalFile(self, browser) :
        browser_click(browser, mobileVarname.cc_attachFileBtn, ID)
        time.sleep(2)
        self.cc_appendingOption(browser, self.album)


    def cc_appendingCamera(self, browser) :
        self.cc_appendingOption(browser, self.camera)


    def cc_appendingWedriveFile(self, browser) : 
        self.cc_appendingOption(browser, self.wedrive)
    

    def cc_appendingContacts(self, browser) :
        self.cc_appendingOption(browser, self.contacts)
        goBack(browser, 2)


    def cc_addOption(self, browser, text, option) :
        # test
        #browser_click(browser, '//android.widget.TextView[@text = "메신저"]')
        #time.sleep(2)
        #clickText(browser, 'testtest')
        #time.sleep(2)
        # test
        action = ActionChains(browser)
        if sameText(browser, text) :
            text2 = browser.find_element(By.XPATH, f'//android.widget.TextView[@text = "{text}"]')
            action.click_and_hold(text2).perform() 
            time.sleep(5)
            # 채팅 복사
            if option == self.copy :
                browser_click(browser, mobileVarname.cc_chatCopyBtn)
                """ time.sleep(4)
                browser_click(browser, mobileVarname.inputChat, ID)
                inputChat = browser.find_element(By.ID, "com.duzon.android.lulubizpotal:id/interactive_input_edit_text")
                touch = TouchAction(browser)
                touch.long_press(inputChat, duration = 3000).perform() """
            # 채팅 삭제
            elif option == self.delete :
                browser_click(browser, mobileVarname.cc_chatDeleteBtn)
                if sameText(browser, '삭제한 대화는 복원할 수 없습니다. 선택한 대화를 삭제 하시겠습니까?') :
                    browser_click(browser, mobileVarname.dialogOkBtn, ID)
                    time.sleep(7)
                    if not sameText(browser, '삭제된 메시지 입니다.') :
                        print('메신저 채팅 삭제 확인 필요')                  
                else :
                    print('메신저 채팅 삭제 얼럿창 확인 필요')
            # 채팅 댓글
            elif option == self.comment :
                browser_click(browser, mobileVarname.cc_chatCommentBtn)
                browser_sendKey(browser, mobileVarname.inputChat, '댓글 테스트', ID)
                browser_click(browser, mobileVarname.cc_sendBtn, ID)
            # 채팅 리액션
            elif option == self.reaction :
                browser_click(browser, mobileVarname.cc_chatReactionBtn)
                time.sleep(3)
                browser_click(browser, mobileVarname.cc_selectReactionTab)
                browser_click(browser, mobileVarname.cc_selectFirstReaciton)
        else : 
            print('해당 대화내용 없음. 입력내용 파트 확인 필요')


    def cc_copyChat(self, browser) : 
        self.cc_addOption(browser, 'test', self.copy)


    def cc_deleteChat(self, browser) : 
        self.cc_addOption(browser, 'test', self.delete)


    def cc_commentChat(self, browser) : 
        self.cc_addOption(browser, 'test', self.comment)


    def cc_reactionChat(self, browser) :
        self.cc_addOption(browser, 'test', self.reaction)


    def cc_downloadFileTab(self, browser) : # 첫 번째 파일 다운
        # test
        #browser_click(browser, '//android.widget.TextView[@text = "메신저"]')
        #time.sleep(2)
        #clickText(browser, 'testtest')
        #test
        browser_click(browser, mobileVarname.checkBtn, ID)
        browser_click(browser, mobileVarname.cc_fileTab, ID)
        time.sleep(2)
        if hasxpath(browser, mobileVarname.cc_firstFileDetail) :
            browser_click(browser, mobileVarname.cc_firstFileDetail)
            clickText(browser, '다운로드')
            time.sleep(4)
        # xlsx 같은 확장자의 경우 고려
            if sameText(browser, '해당 확장자는 뷰어 설치 후 첨부파일 열람이 가능합니다. 뷰어를 설치해 주세요.') :
                browser_click(browser, 'android.widget.Button', CLASS_NAME)
            else :
                goBack(browser, 3)
        else :
            print('[메신저] 파일 모아보기 탭에 파일 없음. 확인 필요')
        goBack(browser, 3)
    

    def cc_settingGroup(self, browser, option) :
        # test
        #browser_click(browser, '//android.widget.TextView[@text = "메신저"]')
        #time.sleep(6)
        #clickText(browser, '자동화 테스트')
        #test
        browser_click(browser, mobileVarname.cc_selectGroupSetting, ID)
        time.sleep(2)
        if option == '공개' :
            clickText(browser, '공개 그룹')
            browser_click(browser, '//android.widget.CheckedTextView[@text = "공개 그룹"]')
            
        else :
            clickText(browser, '비공개 그룹')
            browser_click(browser, '//android.widget.CheckedTextView[@text = "비공개 그룹"]')
           
        browser_click(browser, mobileVarname.dialogOkBtn, ID)
        

    def cc_settingPublicGroup(self, browser) : # 어떤식으로 할지 고려
        self.cc_settingGroup(browser, '공개')
        goBack(browser,2)
        if not hasxpath(browser, mobileVarname.cc_chatBookmarkBtn, ID) : # 무한 로딩 임시방편..
            goBack(browser, 2)


    def cc_settingPrivateGroup(self, browser):
        browser_click(browser, mobileVarname.cc_chatSettingBtn, ID)
        self.cc_settingGroup(browser, '비공개')
 

    def cc_favoriteConversation(self, browser):
        browser_click(browser, mobileVarname.cc_chatBookmarkBtn, ID)


    def cc_checkUserProfile(self, browser):
        browser_click(browser, mobileVarname.cc_userDetail)
        time.sleep(2)
        clickText(browser, '프로필')
        goBack(browser, 5)


    def cc_setAsMaster(self, browser) :
        browser_click(browser, mobileVarname.cc_userDetail)
        time.sleep(2)
        clickText(browser, '마스터로 설정')
        time.sleep(2)
        if hasxpath(browser, "//android.widget.TextView[@text = '마스터 설정']") : # sameText err
            browser_click(browser, mobileVarname.dialogOkBtn, ID)
    

    # 그룹 참여자 내보내기
    def cc_exportUser(self, browser) :
        browser_click(browser, mobileVarname.cc_userDetail)
        time.sleep(2)
        clickText(browser, '내보내기')
        if hasxpath(browser, "//android.widget.TextView[@text = '그룹 대화방에서 내보내기']") : # sameText err
            browser_click(browser, mobileVarname.dialogOkBtn, ID)


    # 그룹 대화방 나가기
    def cc_leaveChatRoom(self, browser) :
        browser_click(browser, mobileVarname.cc_leaveChatBtn, ID)
        if sameText(browser, '대화방을 정말로 나가시겠습니까?') :
            browser_click(browser, mobileVarname.dialogOkBtn, ID)


  
# 일정관리 (1. 캘린더 생성, 2. 공유 캘린더 생성, 3. 캘린더 수정, 4. 캘린더 삭제, 5. 일정등록(1 - 기본) , 6. 일정등록(2 - 예약), 7. 일정 검색, 
#           8. 일정 수정(캘린더 변경) + 일정 이동, 9. 일정 삭제, 10. 댓글 등록, 11. 캘린더 보기방식 변경)

class Schedule :
    def sc_createCalendarOption(self, browser, option) :
        calendarName1 = '캘린더 생성1' ; calendarName2 = '공유캘린더 생성1' ; name1 = '장윤주'

        browser_click(browser, mobileVarname.sc_dropDownSelectBar, ID)
        time.sleep(5)
        browser_click(browser, mobileVarname.createCalendar, ID)
        time.sleep(2)
        hideKeyboard(browser)
        browser_click(browser, mobileVarname.calendarColor, ID)
        time.sleep(2)
        browser_click(browser, mobileVarname.calendarRedColor)
        browser_click(browser, mobileVarname.calendarOkBtn)

        if option == '캘린더 생성' :
            browser_sendKey(browser, mobileVarname.calendarName, calendarName1, ID)
            time.sleep(2)
            browser_sendKey(browser, mobileVarname.calendarExplain, '기본 캘린더 생성중입니다', ID)

        elif option == '공유캘린더 생성' :
            browser_click(browser, mobileVarname.userSelectBtn, ID)
            Account().ac_search(browser, name1)
            hideKeyboard(browser)
            Account().ac_selectMember(browser)
            browser_sendKey(browser, mobileVarname.calendarName, calendarName2, ID)
            browser_sendKey(browser, mobileVarname.calendarExplain, '공유 캘린더 생성중입니다', ID)

        hideKeyboard(browser)
        browser_click(browser, mobileVarname.checkBtn, ID)


    # 캘린더 생성
    def sc_createCalendar(self, browser) :
        browser_click(browser, '//android.widget.TextView[@text = "일정관리"]')
        time.sleep(6)
        self.sc_createCalendarOption(browser, '캘린더 생성')
    

    # 공유 캘린더 생성
    def sc_createSharedCalendar(self, browser) :
        self.sc_createCalendarOption(browser, '공유캘린더 생성')


    # 공유 캘린더 편집
    def sc_modifyCalendar(self, browser) :
        calendarName = '공유캘린더 생성'
        browser_click(browser, mobileVarname.sc_dropDownSelectBar, ID)
        time.sleep(2)
        if hasxpath(browser, '//android.widget.TextView[@text = "공유캘린더 생성1"]') :
            clickText(browser, '공유캘린더 생성1')
        else :
            browser.swipe(400, 1500, 400, 400, 1000)
            clickText(browser, '공유캘린더 생성1')
        
        time.sleep(2)
        
        if not hasxpath(browser, mobileVarname.checkBtn, ID) :
            raise Exception('[일정관리] 공유캘린더 생성 안됨. 확인 필요')
        
        browser_click(browser, mobileVarname.checkBtn, ID)
        clickText(browser, '수정')
        browser_sendKey(browser, mobileVarname.calendarName, calendarName, ID)
        browser_click(browser, mobileVarname.checkBtn, ID)


    # 공유 캘린더 삭제
    def sc_deleteCalendar(self, browser) :
        browser_click(browser, mobileVarname.checkBtn, ID)
        clickText(browser, '삭제')
        time.sleep(3)
        if sameText(browser, '공유한 캘린더 삭제 시, 전체 공유멤버의 공유가 해제되며\n등록된 일정은 영구 삭제됩니다. 삭제하시겠습니까?') :
            time.sleep(2)
            browser_click(browser, mobileVarname.calendarOkBtn)
        else :
            raise Exception('[일정관리] 캘린더 삭제문구 없음. 확인 필요')


    # 일정 생성 옵션
    def sc_registerScheduleOption(self, browser, option) :
        scheduleName1 = '일정 생성1' ; scheduleName2 = '일정 생성2'
        browser_click(browser, mobileVarname.plusBtnContact, ID)
        time.sleep(1)
        hideKeyboard(browser)
        clickText(browser, '장소')
        time.sleep(1)
        clickText(browser, '초대')
        time.sleep(1)
        clickText(browser, '첨부파일')
        time.sleep(1)
        clickText(browser, '설명')
        time.sleep(1)
        browser_sendKey(browser, mobileVarname.sc_scheduleLocation, '더존비즈온', ID)
        browser_click(browser, mobileVarname.inputName, ID)
        browser_sendKey(browser, mobileVarname.inputName, 'yjjang_test1@wehago.com', ID)
        browser.press_keycode(66)
        hideKeyboard(browser)
        browser_click(browser, mobileVarname.sc_scheduleAttachFile, ID)
        browser_click(browser, mobileVarname.uploadBtn, ID)
        clickText(browser, '앨범에서 사진 업로드')
        Mail().ma_selectLocalFile(browser)
        goBack(browser, 2)

        if option == '일정 생성1' :
            browser_sendKey(browser, mobileVarname.sc_scheduleTitleName, scheduleName1, ID)
            browser_click(browser, mobileVarname.sc_scheduleAllday, ID)
            browser_sendKey(browser, mobileVarname.sc_scheduleExplain, '초대일정1 일정을 등록중입니다.', ID)

        elif option == '일정 생성2' :
            browser_sendKey(browser, mobileVarname.sc_scheduleTitleName, scheduleName2, ID)
            browser_click(browser, mobileVarname.sc_scheduleAlert, ID)
            clickText(browser, '정시 알림')
            time.sleep(1)
            clickText(browser, '10분전')
            browser_sendKey(browser, mobileVarname.sc_scheduleExplain, '초대일정2 일정을 등록중입니다.', ID)

        browser_click(browser, mobileVarname.checkBtn, ID)


    # 일정등록 1
    def sc_registerSchedule1(self, browser) :
        # test
        browser_click(browser, '//android.widget.TextView[@text = "일정관리"]')
        time.sleep(6)
        # test
        self.sc_registerScheduleOption(browser, '일정 생성1')


    # 일정등록 2
    def sc_registerSchedule2(self, browser) :
        self.sc_registerScheduleOption(browser, '일정 생성2')


    # 일정 검색
    def sc_searchSchedule(self, browser) :
        # test
        browser_click(browser, '//android.widget.TextView[@text = "일정관리"]')
        time.sleep(6)
        # test
        browser_click(browser, mobileVarname.sc_searchScheduleBtn, ID)
        browser_sendKey(browser, mobileVarname.sc_searchScheduleText, '일정 생성1', ID)
        action = ActionChains(browser)
        leftBtn = browser.find_element(By.ID, 'com.duzon.android.lulubizpotal:id/btn_search_left')
        action.move_to_element_with_offset(leftBtn, 1230, 2550).click().perform()
        hideKeyboard(browser)

        if sameText(browser, '일정 생성1') :
            clickText(browser, '일정 생성1')
        else :
            raise Exception('[일정관리] 일정 검색 확인 필요')


    # 일정 댓글달기
    def sc_addComment(self, browser) :
        clickText(browser, '댓글')
        browser_sendKey(browser, mobileVarname.sc_inputComment, '테스트입니다',ID)
        btn_click(browser, 'android.widget.Button', '전송')
        time.sleep(2)
        
        if not sameText(browser, '테스트입니다') :
            raise Exception('[일정관리] 일정 댓글 확인 필요')
        goBack(browser, 2)


    # 일정 수정(캘린더 변경, 날짜 1일 뒤로 변경)
    def sc_modifySchedule(self, browser) : # 일정 이동 추가. currentTime으로 고고
        browser_click(browser, mobileVarname.checkBtn, ID)
        time.sleep(1)
        clickText(browser, '수정')
        browser_click(browser, mobileVarname.sc_selectCalendar, ID)
        time.sleep(1)
        clickText(browser, '캘린더 생성1')
        if sameText(browser, '캘린더 변경 시, 기존캘린더에서 해당 일정은 삭제됩니다.') :
            browser_click(browser, '//android.widget.Button[@text = "확인"]')
        else :
            raise Exception('[일정관리] 일정 수정 확인 필요')

        browser_click(browser, mobileVarname.sc_scheduleStartDate, ID)
        time.sleep(2)
        
        now = datetime.datetime.now()
        now = now + datetime.timedelta(days = 1)
        now = now.strftime('%d %#m월 %Y')
        
        browser_click(browser, f'//android.view.View[@content-desc="{now}"]') # //android.view.View[@content-desc="15 9월 2022"]
        browser_click(browser, mobileVarname.MailOkBtn, ID)
        browser_click(browser, mobileVarname.checkBtn, ID)


    # 일정 삭제
    def sc_deleteSchedule(self, browser) :
        browser_click(browser, mobileVarname.checkBtn, ID)
        time.sleep(1)
        clickText(browser, '삭제')
        goBack(browser, 2)


    # 캘린더 보기방식 변경 (주간, 목록, 연간)
    def sc_clickCalendar(self, browser) :
        
        browser_click(browser, mobileVarname.sc_dropDownSelectBar, ID)
        time.sleep(1)
        clickText(browser, '주간')
        if not sameText(browser, '주간') :
            raise Exception('[일정관리] 일정 주간 클릭 확인 필요')

        browser_click(browser, mobileVarname.sc_dropDownSelectBar, ID)
        time.sleep(1)
        clickText(browser, '목록')
        if not sameText(browser, '목록') :
            raise Exception('[일정관리] 일정 목록 클릭 확인 필요')
        
        browser_click(browser, mobileVarname.sc_dropDownSelectBar, ID)
        time.sleep(1)
        clickText(browser, '연간')
        if not sameText(browser, '연간') :
            raise Exception('[일정관리] 일정 연간 클릭 확인 필요')

        goBack(browser, 2)

        



print('1')