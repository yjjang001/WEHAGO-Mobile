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
from webbrowser import BackgroundBrowser, BaseBrowser
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

# 초기화면
def initialScreen(browser) :
    confirmbtn = "com.duzon.android.lulubizpotal:id/tv_confirm_buttom"
    if hasxpath(browser, confirmbtn, ID) :
        browser_click(browser, mobileVarname.confirmbtn, ID)
        browser_click(browser, mobileVarname.allowbtn, ID)


# 로그인
def login(browser, id, pwd) :
    loginId = "com.duzon.android.lulubizpotal:id/et_login_insert_id"
    if hasxpath(browser, loginId, ID) : 
        browser_sendKey(browser, mobileVarname.loginId, id, ID)
        browser_sendKey(browser, mobileVarname.loginPw, pwd, ID)
        browser_click(browser, mobileVarname.loginButton, ID)


# 로그인 에러시, 타계정 접속
def loginError(browser) : 
    if hasxpath(browser, mobileVarname.loginError, ID) :
            browser_sendKey(browser, mobileVarname.loginId, 'yjjang_test3', ID)
            browser_sendKey(browser, mobileVarname.loginPw, '1q2w3e4r', ID)
            browser_click(browser, mobileVarname.loginButton, ID)
    else :
        print('로그인 성공!')

# 시작하기
def start(browser) :
    startbtn = "com.duzon.android.lulubizpotal:id/btn_start"
    if hasxpath(browser, startbtn, ID) :
        browser_click(browser, startbtn, ID)


# 문구 여부
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

def context(browser, xpath, by=None) :
    if by == CLASS_NAME :
        text = browser.find_element(By.CLASS_NAME, xpath).text
    elif by == ID :
        text = browser.find_element(By.ID, xpath).text
    else :
        text = browser.find_element(By.XPATH, xpath).text
    return text



# 서비스 선택
def goService(browser, service) :
    if hasxpath(browser, f'//android.widget.TextView[@text = "{service}"]') :
        time.sleep(6)
        browser_click(browser, f'//android.widget.TextView[@text = "{service}"]')
        time.sleep(2)


# 키보드 숨기기
def hideKeyboard(browser):
    time.sleep(1)
    browser.hide_keyboard()


# 텍스트 클릭
def clickText(browser, text) : # 메시지 내용 전체 입력
    if hasxpath(browser, f'//android.widget.TextView[@text = "{text}"]') :
        browser_click(browser, f'//android.widget.TextView[@text = "{text}"]')
        time.sleep(2)
    """ elif hasxpath(browser,  f'//android.widget.CheckedTextView[@text = "{text}"]'):
        browser_click(browser, f'//android.widget.CheckedTextView[@text = "{text}"]')
        time.sleep(2) """


# 뒤로가기
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

    # 거래처 등록
    def ac_registAccount(self, browser) :
        browser_click(browser, '//android.widget.TextView[@text = "거래처관리"]')
        time.sleep(3)
        browser_click(browser, mobileVarname.plusBtnAccounts, ID)
        browser_click(browser, mobileVarname.corporationAccounts, ID)
        time.sleep(2)
        browser_sendKey(browser, mobileVarname.accountsName, '(주)더존비즈온', ID)
        # 스크롤
        browser.swipe(500, 1500, 500, 500, 500)
        #TouchAction().press(mobileVarname.enterpriseNumber).move_to(mobileVarname.representativeName).release()
        browser_sendKey(browser, mobileVarname.representativeName, '김용우', ID)
        browser_click(browser, mobileVarname.checkBtn, ID)


    # 거래처 수정
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


    # 거래처 삭제
    def ac_deleteAccount(self, browser) :
        browser_click(browser, mobileVarname.selectAccounts, ID)
        time.sleep(1)
        #browser.find_element(By.XPATH, "//android.widget.TextView[@text = '(주)더존비즈온']").click()
        clickText(browser, '(주)더존비즈온')
        time.sleep(1)
        browser_click(browser, mobileVarname.deleteAccounts, ID)
        time.sleep(1)
        browser_click(browser, mobileVarname.OkayBtn, ID) 
        time.sleep(2)
        browser.back()


    # 사용자 그룹 생성
    def ac_createGroup(self, browser) :
        browser_click(browser, mobileVarname.allAccounts, ID)
        time.sleep(2)
        browser_click(browser, mobileVarname.addUserGroup) 
        browser_sendKey(browser, mobileVarname.inputBox,'거래처 그룹2',ID)
        browser_click(browser, mobileVarname.OkayBtn, ID)
        

    # 사용자 그룹 삭제
    def ac_deleteGroup(self, browser) :
        if hasxpath(browser, mobileVarname.trashcanBtn):
            browser_click(browser, mobileVarname.trashcanBtn) # 주의) 두 번째 사용자 그룹 삭제
            browser_click(browser, mobileVarname.OkayBtn, ID)
        elif not hasxpath(browser, mobileVarname.trashcanBtn):
            raise Exception('[거래처관리] 삭제할 사용자 그룹 없음. 확인 필요')


    # 조직도 사용자 검색
    def ac_search(self, browser, name) :
        browser_click(browser, mobileVarname.searchUser, ID)
        browser_sendKey(browser, mobileVarname.search, name ,ID)


    # 조직도 사용자 선택
    def ac_selectMember(self, browser) :
        browser_click(browser, mobileVarname.selectmember, ID)
        browser_click(browser, mobileVarname.checkBtn, ID)
         

    # 공유 그룹 생성
    def ac_createSharedGroup(self, browser) :
        browser_click(browser, mobileVarname.addSharedGroup)
        browser_sendKey(browser, mobileVarname.inputBox, '공유 테스트2', ID)
        browser_click(browser, mobileVarname.OkayBtn, ID)
        self.ac_search(browser, '장윤주')
        hideKeyboard(browser)
        self.ac_selectMember(browser)


    # 공유 그룹 삭제
    def ac_deleteSharedGroup(self, browser) :
        browser_click(browser, mobileVarname.trashcanBtnSharedGroupAccount)
        browser_click(browser, mobileVarname.OkayBtn, ID)
        goBack(browser, 2) # 2초이상의 텀 필요
        goBack(browser, 2)
        


# 연락처 (1. 연락처 등록, 2. 사용자그룹 생성, 3. 사용자그룹 수정, 4. 사용자 그룹 삭제, 5. 공유 그룹 생성, 6. 공유그룹 수정, 7. 연락처 정리(1), 8. 연락처 정리(2), 9. 연락처정리(3), 10. 연락처 가져오기
# 11. 연락처 내보내기, 12. 음성전화 13. 화상전화, 14. 링크설정 활성화, 15. 링크설정 비활성화, 16. 폰연락처에 자동저장 활성화, 17. 폰 연락처에 자동저장 비활성화)
# 연락처 삭제 추가 필요

class Contacts :
    
    # 연락처 등록 기본 틀
    def ct_addpeople(self, browser, name, name2, num): 
        browser_click(browser, mobileVarname.plusBtnContact, ID)
        browser_click(browser, mobileVarname.registerBtnContact, ID)
        time.sleep(1)
        browser_sendKey(browser, mobileVarname.inputfirstname, name, ID)
        browser_sendKey(browser, mobileVarname.inputlastname, name2, ID)
        browser_sendKey(browser, mobileVarname.inputTelephoneNumber, num, ID)
        

    # 연락처 등록 상세
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


    # 연락처 정리용 연락처 등록
    def ct_registerContacts_add(self, browser) :
        self.ct_addpeople(browser, '이', '더존', '01011111111')
        browser_click(browser, mobileVarname.checkBtn, ID)
        self.ct_addpeople(browser, '이', '', '')
        browser_click(browser, mobileVarname.checkBtn, ID)


    # 내 그룹 생성
    def ct_createGroup(self, browser):
        browser_click(browser, mobileVarname.allContacts, ID)
        time.sleep(1)
        browser_click(browser, mobileVarname.addContactUserGroup)
        browser_sendKey(browser, mobileVarname.inputBox, '테스트 그룹',ID)
        browser_click(browser, mobileVarname.OkayBtn, ID)


    # 내 그룹 수정
    def ct_modifyGroup(self, browser):
        browser_click(browser, mobileVarname.modifyGroupName)
        browser_sendKey(browser, mobileVarname.inputBox, '테스트 그룹2',ID)
        browser_click(browser, mobileVarname.OkayBtn, ID)


    # 내 그룹 삭제
    def ct_deleteGroup(self, browser):
        browser_click(browser, mobileVarname.trashcanBtnContact) # 주의) 두 번째 사용자 그룹 삭제
        browser_click(browser, mobileVarname.OkayBtn, ID)


    # 공유 그룹 '테스트 공유' 생성
    def ct_createSharedGroup(self, browser):
        if sameText(browser, '공유 그룹') :
            action = ActionChains(browser)
            sharedGroup = browser.find_element(By.XPATH, '//android.widget.TextView[@text = "공유 그룹"]')
            action.move_to_element_with_offset(sharedGroup, 1050, 0).click().perform()
        time.sleep(2)
        Account().ac_search(browser, '장윤주')
        hideKeyboard(browser)
        Account().ac_selectMember(browser)
        browser_sendKey(browser, mobileVarname.inputBox, '테스트 공유', ID)
        browser_click(browser, mobileVarname.OkayBtn, ID)


    # '테스트 공유' -> '테스트 공유2' 수정
    def ct_modifySharedGroup(self, browser):
        #browser_click(browser, mobileVarname.modifySharingGroupName) # 주의) 첫 번째 공유그룹 수정
        if sameText(browser, '테스트 공유') :
                action = ActionChains(browser)
                modifySharedGroup = browser.find_element(By.XPATH, '//android.widget.TextView[@text = "테스트 공유"]')
                action.move_to_element_with_offset(modifySharedGroup, 950, 0).click().perform()
                time.sleep(2)
        browser_sendKey(browser, mobileVarname.inputBox, '테스트 공유2',ID) 
        browser_click(browser, mobileVarname.OkayBtn, ID)


    # '테스트 공유2' 공유그룹 삭제
    def ct_deleteSharedGroup(self, browser):
        #if hasxpath(browser, mobileVarname.trashcanBtnSharingContact):
            #time.sleep(2)
            #browser_click(browser, mobileVarname.trashcanBtnSharingContact) # 주의) 첫 번째 공유그룹 삭제
        if sameText(browser, '테스트 공유2') :
            action = ActionChains(browser)
            deleteSharedGroup = browser.find_element(By.XPATH, '//android.widget.TextView[@text = "테스트 공유2"]')
            action.move_to_element_with_offset(deleteSharedGroup, 1000, 0).click().perform()
            time.sleep(2)
            browser_click(browser, mobileVarname.OkayBtn, ID) # 얼랏창 확인 과정 생략 - cf. 에러

        else :
            raise Exception('[연락처] 삭제할 공유그룹 없음. 확인 필요')
        goBack(browser, 3)


    # 연락처 내보내기
    def ct_contactExport(self, browser):
        # test
        browser_click(browser, '//android.widget.TextView[@text = "연락처"]')
        # test
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


    # 연락처 가져오기
    def ct_contactImport(self, browser):
        browser_click(browser, mobileVarname.importContacts, ID)
        time.sleep(1)
        browser_click(browser, mobileVarname.exportContactsListFirst) # 주의) 첫 번째 사람만 클릭
        browser_click(browser, mobileVarname.checkBtn, ID)
        goBack(browser, 3)
    

    # 연락처 정리하기
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
                if sameText(browser, '이더존') :
                    time.sleep(2)
                    action = ActionChains(browser)
                    secondPeople = browser.find_element(By.XPATH, '//android.widget.TextView[@text = "이더존"]')
                    action.move_to_element_with_offset(secondPeople, -150, 0).click().perform()
                    time.sleep(2)
                    if hasxpath(browser, mobileVarname.OkayBtn, ID):
                        time.sleep(1)
                        browser_click(browser, mobileVarname.OkayBtn, ID)
                        time.sleep(1)
                browser_click(browser, mobileVarname.checkBtn, ID)
                if hasxpath(browser, mobileVarname.OkayBtn, ID):
                    browser_click(browser, mobileVarname.OkayBtn, ID)
            else:
                print("[연락처] " + str(i) + "번째 연락처 정리 내용 없음")
                goBack(browser, 2)
        goBack(browser, 2)
        if sameText(browser, '정리가 필요한 연락처'):
            goBack(browser, 2)


    # 링크 설정
    def ct_LinkSetting(self, browser):
        browser_click(browser, mobileVarname.linkSettingBtn, ID)
        if hasxpath(browser, mobileVarname.OkayBtn, ID):
            browser_click(browser, mobileVarname.OkayBtn, ID)
            print('[연락처] 링크 설정 비활성화')
        elif not hasxpath(browser, mobileVarname.OkayBtn, ID):
            print('[연락처] 링크 설정 활성화')
    

    # 자동저장 활성화 / 비활성화
    def ct_autosaveOnOff(self, browser):
        browser_click(browser, mobileVarname.autosaveBtn, ID)
        if hasxpath(browser, mobileVarname.confirmbtn, ID):
            browser_click(browser, mobileVarname.confirmbtn, ID)
            browser_click(browser, mobileVarname.allowbtn, ID)
        time.sleep(1)
        if hasxpath(browser, mobileVarname.OkayBtn, ID):
            browser_click(browser, mobileVarname.OkayBtn, ID)
            print('[연락처] 자동저장 활성화')
        elif not hasxpath(browser, mobileVarname.OkayBtn, ID):
            print('[연락처] 자동저장 비활성화')
        goBack(browser, 2)
        goBack(browser, 2)



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
        hideKeyboard(browser)


    def ma_hasMailTitle(self, browser):
        # 메일 제목이 없는 경우
        if sameText(browser, '제목이 지정되지 않았습니다.\n제목없이 메일을 보내시겠습니까?') :
            browser_click(browser, mobileVarname.OkayBtn, ID)
            print('[메일] 메일 제목 입력안됨. 메일 제목 없이 전송')
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
            print('[메일] 선택할 웹스토리지 파일 없음. 파일추가 작업 필요')
        time.sleep(4)
        browser_click(browser, mobileVarname.checkBtn, ID)
        goBack(browser, 4)


    def ma_selectLocalFile(self, browser) :
        if not hasxpath(browser, mobileVarname.cameraBtn):
            browser_click(browser, mobileVarname.selectPhoneAlbum, ID)
            time.sleep(5)
            if hasxpath(browser, mobileVarname.selectPhoneAlbum, ID):
                browser_click(browser, mobileVarname.selectPhoneAlbum, ID)
        else :
            print('[메일] 앨범에서 선택할 파일 없음. 앨범에 파일 업로드 작업 필요')
            goBack(browser, 2)


    def ma_localUpload(self, browser) :
        browser_click(browser, mobileVarname.attachfileBtn, ID)
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
            """ if sameText(browser, '예약 시간은 현재 시간 이후부터 설정 가능\n합니다.'):
                browser_click(browser, mobileVarname.OkayBtn, ID)
                print('[메일] 예약 메일 1분뒤 다시 보내기')
                time.sleep(60)
                browser_sendKey(browser, mobileVarname.inputHour, currentTime().strftime('%I'), ID)
                browser_sendKey(browser, mobileVarname.inputMinute, currentTime().strftime('%M'), ID)
                browser_click(browser, mobileVarname.MailOkBtn, ID)
                time.sleep(4)       """    
        elif mail == self.security :
            browser_click(browser, mobileVarname.mailSecurityBtn, ID)
        elif mail == self.individual :
            browser_click(browser, mobileVarname.mailIndividualBtn, ID)          


    """ # 메일 전송 실패
    def ma_sendMailFail(self, browser) :
        if not sameText(browser, '메일이 정상적으로 전송되었습니다.') :
            time.sleep(2)
            raise Exception('[메일] 메일 전송 이상있음. 확인필요')
        elif not sameText(browser, '메일이 전송 예약이 완료 되었습니다.') :
            time.sleep(2)
            raise Exception('[메일] 예약 메일 전송 이상있음. 확인필요') """


    def ma_clickSendButton(self, browser, mail) :
        if mail == self.reserve :
            self.ma_clickOption(browser, mail)
            time.sleep(2)
            browser_click(browser, mobileVarname.checkBtn, ID)
            self.ma_hasMailTitle(browser)
            goBack(browser, 4)

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
            goBack(browser, 4)

        elif mail == self.individual :
            self.ma_clickOption(browser, mail)
            browser_click(browser, mobileVarname.checkBtn, ID)
            self.ma_hasMailTitle(browser)
            goBack(browser, 4)

        elif mail == self.temporary :
            goBack(browser, 6)
            browser_click(browser, mobileVarname.OkayBtn, ID)
            browser_click(browser, mobileVarname.allMail, ID)
            browser_click(browser, mobileVarname.mailTemporaryStorageBox)
            time.sleep(2)
            browser_click(browser, mobileVarname.firstMail,'xpath')
            time.sleep(4)
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
            goBack(browser, 4)

        else :
           browser_click(browser, mobileVarname.checkBtn, ID)
           self.ma_hasMailTitle(browser)
           goBack(browser, 4)

        goService(browser, '메일')
        

    def ma_sendMailDetail(self, browser, address, name, local= None, wedrive= None) :
        browser_click(browser, mobileVarname.plusBtnMail, ID)
        self.ma_recipient(browser, address)
        time.sleep(2)
        self.ma_sendMailTitle(browser, name)
        self.ma_sendMailContent(browser)
        if local :
            time.sleep(2)
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
            goBack(browser, 4)
            goBack(browser, 4)
            raise Exception('[메일] 답장 or 전체답장 or 전달 이상있음. 확인필요')


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
        else :
            raise Exception('[메일] 선택할 메일 없음. 확인 필요')


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
            raise Exception('[메일] 휴지통 비우기 버튼 없음. 확인 필요')
        goBack(browser, 4)
    


# 메시지 (1. 일반메시지 보내기, 2. 보안메시지 보내기, 3. 중요메시지 보내기, 4. 예약 메시지 보내기, 5. 답장/전체답장/전달/다시 보내기 보내기, 6. 모두 읽음 처리, 7. 메시지 검색, 8. 첨부파일 다운받기
# 9. 보안 메시지 확인, 10. 즐겨찾기 설정 11. 받은 메시지 삭제, 12. 보낸 메시지 삭제)
class Message :
    normal='일반'; reserve='예약'; security='보안'; importance='중요'; reply='답장'; replyAll='전체답장'; forward='전달'; resend = '다시 보내기'

    def ms_recipient(self, browser, name) :
        if hasxpath(browser, '//android.widget.MultiAutoCompleteTextView[@text = "이름 또는 아이디를 입력해주세요."]') :
            browser_click(browser, mobileVarname.userSelectBtn, ID)
            time.sleep(2)
            Account().ac_search(browser, name)
            time.sleep(1)
            browser.hide_keyboard()
            Account().ac_selectMember(browser)


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
            print('[메시지] 선택할 웹스토리지 파일 없음')
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
            """ if sameText(browser, '예약 시간은 현재 시간 이후부터 설정 가능합니다.'):
                browser_click(browser, mobileVarname.OkayBtn, ID)
                print('[메시지] 예약 메시지 1분뒤 다시 보내기')
                time.sleep(60)
                browser_sendKey(browser, mobileVarname.inputHour, currentTime().strftime('%I'), ID)
                browser_sendKey(browser, mobileVarname.inputMinute, currentTime().strftime('%M'), ID)
                browser_click(browser, mobileVarname.MailOkBtn, ID)
                time.sleep(3)     """          
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
        browser_sendKey(browser, mobileVarname.messageContent, message + ' 메시지 입력 테스트', ID)
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
            print('[메시지] 읽음처리 되어있음')
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
            #print('[메시지] 첨부파일 없음! 확인 필요')
            raise Exception('[메시지] 첨부파일 없음. 확인 필요')
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
                    print('[메시지] 보안 메시지 비밀번호 오류')
                    goBack(browser, 2)
            goBack(browser, 2)
        else :
            raise Exception('[메시지] 보안 메시지 선택 안됨. 확인 필요')


    def ms_bookmark(self, browser) :
        browser_click(browser, mobileVarname.firstMessage) # 첫 번째 메일 클릭
        browser_click(browser, mobileVarname.messageBookmark, ID)
        goBack(browser, 2)
    

    def ms_deleteMessage(self, browser, option) :
        if option == 'receive' :
            self.ms_enterReceivedMessage(browser)
        elif option == 'send' :
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
            #print('메시지 삭제 확인 필요')
            raise Exception('[메시지] 메시지 삭제 확인 필요')
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
                    time.sleep(2)
                    action.move_to_element_with_offset(plusBtn, 500, 400).click().perform() # 이번만 허용을 누르면, 카메라를 누르기 이전 화면으로 전환되어 다시 카메라 앱 눌러야 함. 
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
            #print('[메신저] 파일첨부파트 확인필요')
            raise Exception('[메신저] 파일첨부파트 확인 필요')
        

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
                        #print('메신저 채팅 삭제 확인 필요')
                        raise Exception('[메신저] 채팅 삭제 확인 필요')                
                else :
                    #print('메신저 채팅 삭제 얼럿창 확인 필요')
                    raise Exception('[메신저] 메신저 채팅 삭제 얼럿창 확인 필요')
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
            #print('해당 대화내용 없음. 입력내용 파트 확인 필요')
            raise Exception('[메신저] 해당 대화내용없음. 입력내용 파트 확인 필요')


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
            #print('[메신저] 파일 모아보기 탭에 파일 없음. 확인 필요')
            raise Exception('[메신저] 파일 모아보기 탭에 파일없음. 확인 필요')
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
        #browser_click(browser, '//android.widget.TextView[@text = "일정관리"]')
        #time.sleep(6)
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
        time.sleep(1)
        browser_click(browser, mobileVarname.sc_selectCalendar, ID)
        time.sleep(2)
        browser_click(browser, '//android.widget.TextView[@text = "캘린더 생성1"]') 
        time.sleep(2)
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



# 전자결재 (1. 전자결재 작성 - 휴가 신청서, 2. 전자결재 작성 - 연장근무 신청서, 3. 전자결재 작성 - 출장 신청서, 4. 전자결재 작성 - 휴가취소신청서, 5. 수신참조 수정, 6. 기안 보관함 이동,
#          7. 댓글작성, 8. 전자결재 진행 - 시행 정보 입력, 9. 전자결재 진행 - 승인, 10. 전자결재 진행 - 반려, 11. 전자결재 진행 - 검토 클릭 12. 웹에서 상신된 결재 확인 - 승인,
#          13. 웹에서 상신된 결재 확인 - 반려, 14. 웹에서 상신된 결재 확인 - 검토, 15. 웹에서 상신된 결재 확인 - 삭제, 16. 웹에서 상신된 결재 확인 - 전결 승인, 17. 웹에서 상신된 결재 확인 - 후결 승인
#          18. 보관함 이동 - 웹에서 상신된 기안 이동, 19. 보관함 이동 - 기안 보관함 이동

class Approval :

    # 앱 실행 후, 검정 화면 + 회전상태가 적용되어 뒤로가기 + 앱 재접속 과정 추가
    def approvalInitialSetting(self, browser) :
        goBack(browser, 0)
        browser_click(browser, '//android.widget.TextView[@content-desc="전자결재"]')


    # WEHAGO 앱으로 로그인
    def approvalLogin1(self, browser, id, pwd) :
        if hasxpath(browser, mobileVarname.ap_loginBtn1) :
            browser_click(browser, mobileVarname.ap_loginBtn1)
            time.sleep(3)
            if hasxpath(browser, mobileVarname.ap_inputIdBtn) :
                browser_sendKey(browser, mobileVarname.ap_inputIdBtn, id)
                browser_sendKey(browser, mobileVarname.ap_inputPwdBtn, pwd)
                browser_click(browser, mobileVarname.ap_loginBtn2)
            print('로그인 성공!')
    

    # 직접 입력해서 로그인
    def approvalLogin2(self, browser, id, pwd) :
        if hasxpath(browser, mobileVarname.ap_directLoginBtn) :
            browser_click(browser, mobileVarname.ap_directLoginBtn)
            browser_sendKey(browser, mobileVarname.ap_inputIdBtn, id)
            browser_sendKey(browser, mobileVarname.ap_inputPwdBtn, pwd)
            browser_click(browser, mobileVarname.ap_loginBtn2)
            print('로그인 성공!')
    

    # 위하고앱 -> 전자결재 앱 연동
    def enterApproval(self, browser) :
        browser.swipe(500, 1500, 500, 500, 100)
        browser_click(browser, '//android.widget.TextView[@text = "전자결재"]')
        if hasxpath(browser, mobileVarname.ap_alertTitle2) :
            browser_click(browser, "android:id/button1", ID)
            time.sleep(2)


    # 연동 테스트
    def approvalTest(self, browser) :
        clickText(browser, '수신결재')


    # 결재 작성
    def ap_createApproval(self, browser, type, reference = None, enforcementer = None, vacation = None, file = None) :
        clickText(browser, '결재작성')
        time.sleep(2)
        if type == "휴가신청서" :
            clickText(browser, '휴가신청서')
        elif type == "연장근무신청서" :
            clickText(browser, '연장근무신청서')
        elif type == "출장신청서" :
            clickText(browser, '출장신청서')
        elif type == "휴가취소신청서" :
            clickText(browser, '휴가취소신청서')
        
        time.sleep(4)
        
        # test
        """ browser.swipe(500, 1500, 500, 1000, 100)
        time.sleep(5)
        action = ActionChains(browser)
        date1 = browser.find_element(By.XPATH, '//android.widget.TextView[@text = "연장근무일자"]')
        action.move_to_element_with_offset(date1, 1150, 100).click().perform() 
        print('눌렀당') """
        # test

        self.ap_approvalTitle(browser, type)

        if reference :
            self.ap_receivingReference(browser)
        if enforcementer :
            time.sleep(1)
            self.ap_enforcementer(browser)

        if vacation :
            self.ap_vacationCancelFile(browser)
        if file :
            self.ap_appendFile(browser)

        clickText(browser, '다음')
        self.ap_approver(browser, option = "결재")
        time.sleep(3)
        self.ap_approval(browser)
 

    # 신청서 제목
    def ap_approvalTitle(self, browser, type) :
        approveTitle = currentTime().strftime('%m%d') + ' ' + type + ' 테스트'
        browser_sendKey(browser, mobileVarname.ap_inputTitle, approveTitle)
    
    # 수신참조, 결재자 선택
    def ap_searchUser(self, browser, name) :
        browser_sendKey(browser, mobileVarname.ap_searchUser, name)
        browser_click(browser, mobileVarname.ap_userCheckbox)
        browser_click(browser, mobileVarname.ap_checkBtn)


    # 수신참조
    def ap_receivingReference(self, browser) :
        browser_click(browser, mobileVarname.ap_receivingReference)
        self.ap_searchUser(browser, '문지영')


    # 참조문서(검색어 입력시 앱이 다운되는 이슈로 업데이트 이후 추가 예정)
    
    
    # 첨부파일
    def ap_appendFile(self, browser) :
        browser.swipe(500, 1500, 500, 500, 100)
        browser_click(browser, "//android.widget.EditText[@text = '첨부파일을 추가해주세요.']")
        browser_click(browser, mobileVarname.ap_plusBtn)
        time.sleep(1)
        clickText(browser, '앨범에서 사진 업로드')
        if sameText(browser, '전자결재에서 기기의 사진 및 미디어에 액세스하도록 허용하시겠습니까?'):
            btn_click(browser, 'android.widget.Button', '허용')
        browser_click(browser, mobileVarname.ap_albumFirstFile)
        clickText(browser, '확인')
        clickText(browser, '확인')


    # 시행자 - xpath 위치가 각각 달라서 actionchain으로 작업예정
    def ap_enforcementer(self, browser) :
        action = ActionChains(browser)
        people = browser.find_element(By.XPATH, '//android.widget.TextView[@text = "시행자"]')
        action.move_to_element_with_offset(people, 1200, 90).click().perform()
        #browser_click(browser, mobileVarname.ap_vacationCancelFile) # 연장근무 시행자 xpath 클릭
        self.ap_searchUser(browser, '문지영')


    # 결재자 지정
    def ap_approver(self, browser, option) :
        browser_click(browser, mobileVarname.ap_approver)
        self.ap_searchUser(browser, '문지영')
        if option == '합의':
            browser_click(browser, mobileVarname.ap_agreementBtn)


    # 기안
    def ap_approval(self, browser) :
        clickText(browser, '기안')
        # 이미 기안 있는 경우 이전 -> 날짜 변경(2일 뒤로) for 구문 써서 3번 반복
        time.sleep(3)
        # 중복일시, 휴가 신청 불가 얼럿창
        """ if hasxpath(browser, mobileVarname.ap_alertTitle) : 
            browser_click(browser, "android:id/button1", ID)
            self.ap_attendanceHoliday(browser) """
        self.ap_attendanceHoliday(browser)

    # 휴일
    """ def ap_attendanceHoliday(self, browser) :
        clickText(browser, '이전')
        time.sleep(1)
        
        # 휴가신청, 출장신청
        if not sameText(browser, '연장근무일자') :
            browser.swipe(500, 1500, 500, 1000, 100)
            action = ActionChains(browser)
            date = browser.find_element(By.XPATH, '//android.widget.TextView[@text = "시작일자-종료일자"]')
            action.move_to_element_with_offset(date, 390, 90).click().perform()

        # 연장근무 신청
        elif sameText(browser, '연장근무일자') :
            #browser_click(browser, mobileVarname.ap_enforcementerBtn) # 코드 실행할 때마다 actionChain 클릭이 안돼서 우선 xpath로 작업
            action = ActionChains(browser)
            date1 = browser.find_element(By.XPATH, '//android.widget.TextView[@text = "연장근무일자"]')
            action.move_to_element_with_offset(date1, 1150, 114).click().perform() # 지속적으로 에러 발생함 수시로 확인 필요.. 스와이프를 바꿔야할까
            #action.move_to_element_with_offset(date1, 1155, 119).click().perform() # y: 119

        day = (currentTime() + datetime.timedelta(days=2)).strftime('%#d') # 1의 단위 날짜, 임시로 날짜 1일 설정. 
        currentmonth = currentTime().strftime('%m')
        month = (currentTime() + datetime.timedelta(days=2)).strftime('%m')
        

        # 3일 뒤가 다음달로 넘어갈 경우 다음달로 넘어가기
        if month > currentmonth :
            browser_click(browser, mobileVarname.ap_nextMonth)
            time.sleep(1)
            browser_click(browser, f'//android.widget.TextView[@text = "{day}"]')
        else :
            browser_click(browser, f'//android.widget.TextView[@text = "{day}"]')

        clickText(browser, '적용')
        time.sleep(1)
        clickText(browser, '다음')
        time.sleep(1)
        clickText(browser, '기안')
        time.sleep(2)


        # 휴일에 연장근무 신청을 할 경우 - 휴일근무 적용
        # hasxpath(browser, mobileVarname.ap_alertTitle2)
        if sameText(browser, "휴일에 연장근무를 신청할 경우연장근무 구분내용을 '휴일근무'로 지정해야 합니다.근태구분을 재입력해주세요."):
            browser_click(browser, "android:id/button1", ID)
            clickText(browser, '이전')
            time.sleep(1)
            action = ActionChains(browser)
            sort = browser.find_element(By.XPATH, '//android.widget.TextView[@text = "근태구분"]')
            action.move_to_element_with_offset(sort, 1200, 90).click().perform()
            clickText(browser, '휴일근무')
            clickText(browser, '적용')
            clickText(browser, '다음')
            clickText(browser, '기안') """


    # 휴일
    def ap_attendanceHoliday(self, browser) :
        for i in range(1, 4) :
            if sameText(browser, '입력한 일시의 중복신청건이 존재합니다.일시를 다시 입력해주세요') or sameText(browser, '등록된 휴일 일자에 휴가신청이 불가합니다.시작/종료 일자를 재입력해주세요.') or sameText(browser, '등록된 휴일 일자에 출장신청이 불가합니다.시작/종료 일자를 재입력해주세요.'): 
                browser_click(browser, "android:id/button1", ID)
                clickText(browser, '이전')
                
                # 휴가신청, 출장신청
                if not sameText(browser, '연장근무일자') :
                    browser.swipe(500, 1500, 500, 1000, 100)
                    action = ActionChains(browser)
                    date = browser.find_element(By.XPATH, '//android.widget.TextView[@text = "시작일자-종료일자"]')
                    action.move_to_element_with_offset(date, 390, 90).click().perform()

                # 연장근무 신청
                elif sameText(browser, '연장근무일자') :
                    #browser_click(browser, mobileVarname.ap_enforcementerBtn) # 코드 실행할 때마다 actionChain 클릭이 안돼서 우선 xpath로 작업
                    action = ActionChains(browser)
                    date1 = browser.find_element(By.XPATH, '//android.widget.TextView[@text = "연장근무일자"]')
                    action.move_to_element_with_offset(date1, 1150, 114).click().perform() # 지속적으로 에러 발생함 수시로 확인 필요.. 스와이프를 바꿔야할까
                    #action.move_to_element_with_offset(date1, 1155, 119).click().perform() # y: 119

                day = (currentTime() + datetime.timedelta(days = i + 1)).strftime('%#d') # 1의 단위 날짜, 임시로 날짜 1일 설정. 
                currentmonth = currentTime().strftime('%m')
                month = (currentTime() + datetime.timedelta(days = i + 1)).strftime('%m')
                currentmonth = int(currentmonth)
                month = int(month)
                # 달력 월 비교용
                month2 = (currentTime() + datetime.timedelta(days = i + 1)).strftime('%Y.%m')


                # 3일 뒤가 다음달로 넘어갈 경우 다음달로 넘어가기
                if month - currentmonth == 1 :
                    # 반복문으로 인해 이미 다음달로 넘어간 경우
                    print(month - currentmonth)
                    print(context(browser, mobileVarname.ap_date))
                    print(mobileVarname.ap_date)
                    print(type(month2))
                    print(type(context(browser, mobileVarname.ap_date)))
                    print(month2 == context(browser, mobileVarname.ap_date))
                    # context = xpath.text 작업
                    if month2 == context(browser, mobileVarname.ap_date) :
                        browser_click(browser, f'//android.widget.TextView[@text = "{day}"]')
                        
                    # 첫 반복문 실행 시 다음달로 넘어가야 하는 경우
                    else :
                        browser_click(browser, mobileVarname.ap_nextMonth)
                        time.sleep(2)
                        browser_click(browser, f'//android.widget.TextView[@text = "{day}"]')

                else :
                    browser_click(browser, f'//android.widget.TextView[@text = "{day}"]')

                clickText(browser, '적용')
                time.sleep(1)
                clickText(browser, '다음')
                time.sleep(1)
                clickText(browser, '기안')
                time.sleep(2)


                # 휴일에 연장근무 신청을 할 경우 - 휴일근무 적용
                # hasxpath(browser, mobileVarname.ap_alertTitle2)
                if sameText(browser, "휴일에 연장근무를 신청할 경우연장근무 구분내용을 '휴일근무'로 지정해야 합니다.근태구분을 재입력해주세요."):
                    browser_click(browser, "android:id/button1", ID)
                    clickText(browser, '이전')
                    time.sleep(1)
                    action = ActionChains(browser)
                    sort = browser.find_element(By.XPATH, '//android.widget.TextView[@text = "근태구분"]')
                    action.move_to_element_with_offset(sort, 1200, 90).click().perform()
                    clickText(browser, '휴일근무')
                    clickText(browser, '적용')
                    clickText(browser, '다음')
                    clickText(browser, '기안')
            else : break


    # 휴가신청서 참조
    def ap_vacationCancelFile(self, browser) :
        browser_click(browser, mobileVarname.ap_vacationCancelFile)
        if not sameText(browser, '참조할 결재문서가 없습니다.') :
            browser_click(browser, mobileVarname.ap_vacationCancelFirstFile)
            time.sleep(2)
            clickText(browser, '확인')
            browser.swipe(500, 1500, 500, 500, 100)
            browser_sendKey(browser, mobileVarname.ap_vacationCancelReason, '테스트입니다')

        # 참조할 결재문서가 없을 때, 메인화면으로 돌아가 휴가신청서 승인 - 아직 작업 안해둠... 다음에 고고 + 순서를 바꿔야할듯.... 휴가신청서 > 연장근무 > 출장신청 > 휴가신청서 승인 > 연장근무 승인 > 출장신청 반려 > 휴가취소 신청서 고고
        else :
            goBack(browser, 2)
            goBack(browser, 2)
            goBack(browser, 4)
            self.ap_attendanceVacation(browser)
            time.sleep(5)
            clickText(browser, '결재작성')
            clickText(browser, '휴가취소신청서')
            time.sleep(2)
            self.ap_approvalTitle(browser, type)


    # 휴가신청서
    def ap_attendanceVacation(self, browser) :
        self.ap_createApproval(browser, '휴가신청서')
    
    # 연장근무신청서
    def ap_attendanceExtensionWork(self, browser) :
        self.ap_createApproval(browser, '연장근무신청서', enforcementer = True)
    
    # 출장신청서
    def ap_attendanceBusinessTrip(self, browser) :
        self.ap_createApproval(browser, '출장신청서')

    # 휴가취소신청서
    def ap_attendanceVacationCancel(self, browser) :
        self.ap_createApproval(browser, '휴가취소신청서', vacation=True)


    def ap_clickApproval(self, browser, text) :
        clickText(browser, '수신결재')
        clickText(browser, text)

    def ap_modifyApproval(self, browser) :
        title = currentTime().strftime('%m%d') + ' 휴가신청서' + type + ' 테스트'
        self.ap_clickApproval(browser, title)
        

    




print('1')