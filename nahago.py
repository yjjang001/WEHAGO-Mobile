from cgitb import text
from curses import A_COLOR, KEY_CLOSE, KEY_ENTER, KEY_F4
import curses
from inspect import modulesbyfile
from msilib.schema import Class
from operator import contains
import time, datetime
from tkinter import Checkbutton
from tkinter.font import names
import mobileVarname
import driver
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
import varname_nahago
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
ID= 'id'; CSS='CSS'; CLASS_NAME='class'; TAG_NAME='tag_mobileVarname'

def start(browser) :
    startbtn = "com.duzon.android.lulubizpotal:id/btn_start"
    if hasxpath(browser, startbtn, ID) :
        browser_click(browser, startbtn, ID)

def sameText(browser, text) :
    # 팝업 창 문구
    if hasxpath(browser, mobileVarname.content, ID) :
        context = browser.find_element(By.ID, mobileVarname.content).text
        if text in context :
            return True
        else :
            return False
    else :
        return False

def goService(browser, service) :
    if hasxpath(browser, f'//android.widget.TextView[@text = "{service}"]') :
        time.sleep(4)
        browser_click(browser, f'//android.widget.TextView[@text = "{service}"]')
        time.sleep(2)

class Login :
    def login_nahago(self, browser, name) :
        print('나하고 로그인')
        # 스플래시 화면 대기
        splash = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.HorizontalScrollView'
        while True:
            if hasxpath(browser, splash):
                for i in range(0, 5):
                    browser.swipe(1000, 500, 300, 500, 100)
                    time.sleep(0.1)
                    btn_click(browser, 'android.view.View', '시작하기')
                break
            elif hasxpath(browser, varname_nahago.loginName):
                break
            else:
                time.sleep(3)

        # 이름, 휴대폰번호 입력
        browser_sendKey(browser, varname_nahago.loginName, name)
        browser_sendKey(browser, varname_nahago.loginNumber, '01045681896')
        browser_click(browser, varname_nahago.nahago_loginBtn)

        num = input('휴대폰인증번호')
        action = ActionChains(browser)
        action.send_keys(num).perform()
        time.sleep(3)
        if hasxpath(browser, varname_nahago.setPw) :
            btn_click(browser, 'android.widget.Button', '인증번호 재요청')
            num = input('휴대폰인증번호')
            action = ActionChains(browser)
            action.send_keys(num).perform()

        time.sleep(1)
        self.nahago_setPw(browser)

    def nahago_pw(self, browser) :
        browser_click(browser, '//android.widget.TextView[@text = "1"]')
        time.sleep(0.5)
        browser_click(browser, '//android.widget.TextView[@text = "2"]')
        time.sleep(0.5)
        browser_click(browser, '//android.widget.TextView[@text = "1"]')
        time.sleep(0.5)
        browser_click(browser, '//android.widget.TextView[@text = "2"]')
        time.sleep(0.5)
        browser_click(browser, '//android.widget.TextView[@text = "A"]')
        time.sleep(3)
    def nahago_setPw(self, browser) :
        browser_click(browser, varname_nahago.setPw)
        time.sleep(3)
        # 비밀번호 등록
        self.nahago_pw(browser)
        time.sleep(1)
        # 비밀번호 확인 등록
        self.nahago_pw(browser)
        # 시작하기 버튼 클릭
        browser_click(browser, varname_nahago.nahago_startBtn)

    def logout(self, browser) :
        browser_click(browser, varname_nahago.main_hamBtn)
        browser_click(browser, varname_nahago.main_setBtn)
        browser_click(browser, varname_nahago.logoutBtn)
        browser_click(browser, varname_nahago.logoutConfirmBtn)
        time.sleep(5)

class Communication :
    def cc_createGroupChat(self, browser) :
        browser_click(browser, varname_nahago.cc_createBtn)
        browser_click(browser, varname_nahago.cc_addGroupChat)
        time.sleep(3)
        browser_sendKey(browser, varname_nahago.cc_groupChatName, '안드1')
        # input
        browser_sendKey(browser, varname_nahago.cc_addChatUser, '한초희')
        browser_click(browser, varname_nahago.cc_addUserInput)
        # # 조직도
        # browser_click(browser, varname_nahago.cc_addChatUserBtn)
        # mobile_click(browser, '선택')
        time.sleep(1)
        browser_click(browser, varname_nahago.cc_createConfirm)
        time.sleep(3)
        # 대화방 생성 안된경우 (동일대화방일때)
        if not hasxpath(browser, varname_nahago.cc_backBtn) :
            browser_sendKey(browser, varname_nahago.cc_groupChatName, currentTime().strftime('%H%M'))
            browser_click(browser, varname_nahago.cc_createConfirm)
            time.sleep(3)
        browser_click(browser, varname_nahago.cc_backBtn)

    def cc_leaveGroupChat(self, browser) :
        # 스와이프로
        # mobile_click(browser, '그룹채팅')
        # 내보내기 이슈 있음
        # browser_click(browser, varname_nahago.cc_chat)
        # browser_click(browser, varname_nahago.cc_hamburgerBtn)
        # for i in range(0,2) :
        #     browser_click(browser, varname_nahago.cc_userList)
        #     browser_click(browser, varname_nahago.cc_exportUser)
        #     btn_click(browser, 'android.widget.Button', '확인')
        # browser_click(browser, varname_nahago.cc_backBtn)
        # browser_click(browser, varname_nahago.cc_backBtn)
        time.sleep(3)
        # 그룹 채팅 화면인지 확인해보기
        browser.execute_script('mobile: swipeGesture', {'direction': 'left', 'element': varname_nahago.cc_chat})
        browser_click(browser, varname_nahago.cc_swipeLeaveBtn)
        #mobile_click(browser, '확인')

    def cc_createChat(self, browser) :
        browser_click(browser, varname_nahago.cc_createBtn)
        browser_click(browser, varname_nahago.cc_addChat)
        time.sleep(3)
        browser_sendKey(browser, varname_nahago.searchUser, '한초희')
        browser_click(browser, varname_nahago.selectUser)
        #mobile_click(browser, '선택')
        time.sleep(3)
        if not hasxpath(browser, varname_nahago.cc_backBtn) :
            raise Exception('1:1 대화방 생성 확인필요')
        browser_click(browser, varname_nahago.cc_backBtn)

    def cc_leaveChat(self, browser) :
        # 나가기 버튼으로
        browser_click(browser, varname_nahago.cc_oneChatList)
        browser_click(browser, varname_nahago.cc_chat)
        browser_click(browser, varname_nahago.cc_hamburgerBtn)
        browser_click(browser, varname_nahago.cc_leaveBtn)
        browser_click(browser, varname_nahago.cc_leaveCheckBtn)
        time.sleep(3)
        browser_click(browser, varname_nahago.cc_chatList)

    def cc_sendChat(self, browser) :
        browser_click(browser, varname_nahago.cc_groupChatList)
        browser_click(browser, varname_nahago.cc_chat)
        browser_click(browser, varname_nahago.cc_sendChat)
        action = ActionChains(browser)
        action.send_keys('nonono').perform()
        browser_click(browser, varname_nahago.cc_sendChatBtn)
        time.sleep(1)
        # 멘션입력
        browser_click(browser, varname_nahago.cc_mentionBtn)
        browser_click(browser, varname_nahago.cc_mentionList)
        browser_click(browser, varname_nahago.cc_sendChatBtn)
        # 이모지 입력
        browser_click(browser, varname_nahago.cc_emojiBtn)
        browser_click(browser, varname_nahago.cc_emoji1)
        browser_click(browser, varname_nahago.cc_emoji2)
        browser_click(browser, varname_nahago.cc_sendChatBtn)
        browser_click(browser, varname_nahago.cc_backBtn)
        browser_click(browser, varname_nahago.cc_chatList)

    def cc_bookmarkChat(self, browser) :
        browser_click(browser, varname_nahago.cc_groupChatList)
        # browser.execute_script('mobile: swipe', {direction: 'right', element: varname_nahago.cc_chat});
        # browser_click(browser, varname_nahago.cc_swipeBookmarkBtn)
        # time.sleep(3)
        browser_click(browser, varname_nahago.cc_chat)
        browser_click(browser, varname_nahago.cc_hamburgerBtn)
        browser_click(browser, varname_nahago.cc_bookmarkBtn)
        browser_click(browser, varname_nahago.cc_backBtn)
        browser_click(browser, varname_nahago.cc_backBtn)
        browser_click(browser, varname_nahago.cc_chatList)

class Attendance :
    # 결재자 선택
    def at_selectAssign(self, browser, userName) :
        browser_click(browser, varname_nahago.at_selectAssign)
        time.sleep(3)
        browser_sendKey(browser, varname_nahago.at_searchUser, userName)
        browser_click(browser, varname_nahago.at_selectUser)
        browser_click(browser, varname_nahago.selectBtn)

    def at_assign(self, browser, userName) :
        time.sleep(3)
        if hasxpath(browser, varname_nahago.at_deleteUserBtn) :
            browser_click(browser, varname_nahago.at_deleteUserBtn)
            time.sleep(1)

        self.at_selectAssign(browser, userName)
        browser_click(browser, varname_nahago.at_doneBtn)
        time.sleep(3)
        if hasxpath(browser, varname_nahago.duplicationVacation):
            browser_click(browser, varname_nahago.duplicationVacation)
            time.sleep(3)
            browser_click(browser, varname_nahago.at_closeApproval)
        else :
            browser_click(browser, varname_nahago.at_confirmBtn)
        time.sleep(5)

    def at_vacationApplication(self, browser, userName):
        browser_click(browser, varname_nahago.at_vacation)
        browser_click(browser, varname_nahago.at_alldayVacation)
        time.sleep(1)
        browser_click(browser, varname_nahago.at_nextBtn)
        self.at_assign(browser, userName)

    def at_vacationApplicationCancel(self, browser, userName) :
        time.sleep(1)
        # 휴가취소
        browser_click(browser, varname_nahago.at_vacation)
        browser_click(browser, varname_nahago.at_vacationCancel)
        time.sleep(1)
        print(hasxpath(browser, varname_nahago.at_findVacationApplication))
        browser_click(browser, varname_nahago.at_findVacationApplication)
        if hasxpath(browser, varname_nahago.at_emptyFindVaction) :
            browser_click(browser, varname_nahago.at_emptyConfirmBtn)
            browser_click(browser, varname_nahago.at_closeVacationApplication)
            raise Exception('휴가 신청 확인 필요')
        else :
            browser_click(browser, varname_nahago.at_selectVactionApplication)
            time.sleep(1)
            browser_click(browser, varname_nahago.at_selectVactionConfirmBtn)
            time.sleep(3)
            browser_sendKey(browser, varname_nahago.at_vacationCancelReason, '휴가취소')
            browser_click(browser, varname_nahago.at_nextBtn)
            self.at_assign(browser, userName)

class Approval :
    def ap_selectAssign(self, browser, userName) :
        browser_click(browser, varname_nahago.ap_selectAssign)
        time.sleep(3)
        browser_sendKey(browser, varname_nahago.searchUser, userName)
        browser_click(browser, varname_nahago.selectUser)
        browser_click(browser, varname_nahago.selectBtn)

    def ap_assign(self, browser, userName) :
        time.sleep(3)
        if hasxpath(browser, varname_nahago.ap_deleteUserBtn) :
            browser_click(browser, varname_nahago.ap_deleteUserBtn)
            time.sleep(1)

        self.ap_selectAssign(browser, userName)
        browser_click(browser, varname_nahago.ap_doneBtn)
        time.sleep(3)
        if hasxpath(browser, varname_nahago.duplicationVacation):
            browser_click(browser, varname_nahago.duplicationVacation)
            time.sleep(3)
            browser_click(browser, varname_nahago.ap_closeApproval)
        else :
            browser_click(browser, varname_nahago.ap_nextBtn)
        browser_click(browser, varname_nahago.ap_homeBackBtn)
        time.sleep(5)
    def ap_vacationApplication(self, browser, userName) :
        # 전자결재에서 휴가신청
        browser_click(browser, varname_nahago.approvalBtn)
        time.sleep(10)
        browser_click(browser, varname_nahago.ap_vacation)
        time.sleep(3)
        browser_click(browser, varname_nahago.ap_nextBtn)
        self.ap_assign(browser, userName)

    def ap_vacationApplicationCancel(self, browser, userName) :
        # 전자결재에서 휴가취소
        browser_click(browser, varname_nahago.approvalBtn)
        time.sleep(10)
        browser_click(browser, varname_nahago.ap_vacationCancel)
        time.sleep(3)
        browser_click(browser, varname_nahago.ap_findVacationApplication)
        if hasxpath(browser, varname_nahago.at_emptyFindVaction):
            browser_click(browser, varname_nahago.at_emptyConfirmBtn)
            browser_click(browser, varname_nahago.at_closeVacationApplication)
            raise Exception('휴가 신청 확인 필요')
        else:
            browser_click(browser, varname_nahago.at_selectVactionApplication)
            time.sleep(1)
            browser_click(browser, varname_nahago.at_selectVactionConfirmBtn)
            time.sleep(3)
            browser_sendKey(browser, varname_nahago.ap_vacationCancelReason, '휴가취소')
            browser_click(browser, varname_nahago.ap_nextBtn)
            self.ap_assign(browser, userName)

    def ap_clickApproval(self, browser) :
        time.sleep(10)
        browser_click(browser, varname_nahago.approvalBtn)
        time.sleep(10)
        if not hasxpath(browser, varname_nahago.ap_clickApproval) :
            raise Exception('결재 상신 확인 필요')
        browser_click(browser, varname_nahago.ap_clickApproval)
        time.sleep(5)

    def ap_approve(self, browser) :
        self.ap_clickApproval(browser)
        browser_click(browser, varname_nahago.ap_approveBtn)
        time.sleep(1)
        browser_click(browser, varname_nahago.ap_confirmBtn)
        time.sleep(1)
        browser_click(browser, varname_nahago.ap_backBtn)
        time.sleep(5)

    def ap_reject(self, browser) :
        self.ap_clickApproval(browser)
        browser_click(browser, varname_nahago.ap_rejectBtn)
        browser_sendKey(browser, varname_nahago.ap_rejectReason, '반려합니다')
        browser_click(browser, varname_nahago.ap_rejectBtn2)
        browser_click(browser, varname_nahago.ap_rejectConfirmBtn)
        time.sleep(1)
        browser_click(browser, varname_nahago.ap_backBtn)

    def ap_modifyApporve(self, browser) :
        self.ap_clickApproval(browser)
        browser_click(browser, varname_nahago.ap_modify)
        browser_click(browser, varname_nahago.ap_nextBtn)
        browser_click(browser, varname_nahago.ap_doneBtn)

class Run(Approval, Attendance, Login) :
    def ap_1(self, browser) :
        name = '일자동'
        self.logout(browser)
        self.login_nahago(browser, name)
        # 일반근로제 - 자동 시간 기록 메인 > 전자결재 상신 후 승인
        # print('')
        self.at_vacationApplication(browser, name)
        time.sleep(5)
        self.ap_approve(browser)
        self.at_vacationApplicationCancel(browser, name)
        time.sleep(5)
        self.ap_approve(browser)

    def ap_2(self, browser) :
        # 일반근로제 - 실시간 체크 / 메인 > 전자결재 상신 후 반려
        name = '일실시'
        self.logout(browser)
        self.login_nahago(browser, name)
        self.at_vacationApplication(browser, name)
        time.sleep(5)
        self.ap_reject(browser)

    def ap_3(self, browser) :
        # 일반근로제 - 직접입력 / 메인 > 전자결재 상신 후 수정 후 승인
        # !! 현재 버전 전자결재 수정 시 이슈
        name = '일직접'
        self.logout(browser)
        self.login_nahago(browser, name)
        self.at_vacationApplication(browser, name)
        time.sleep(5)
        self.ap_approve(browser)
        self.at_vacationApplicationCancel(browser, name)
        time.sleep(5)
        self.ap_approve(browser)

    def ap_4(self, browser) :
        # 시차출퇴근제 - 자동 시간 기록 / 결재 > 자결재 상신 후 수정 후 반려
        # !! 현재 버전 전자결재 수정 시 이슈
        name = '시자동'
        self.logout(browser)
        self.login_nahago(browser, name)
        self.ap_vacationApplication(browser, name)
        time.sleep(5)
        self.ap_reject(browser)

    def ap_5(self, browser) :
        # 시차출퇴근제 - 실시간 체크 / 결재 > 전자결재 상신 후 승인
        name = '시실시'
        self.logout(browser)
        self.login_nahago(browser, name)
        self.ap_vacationApplication(browser, name)
        time.sleep(5)
        self.ap_approve(browser)
        self.ap_vacationApplicationCancel(browser, name)
        time.sleep(5)
        self.ap_approve(browser)

    def ap_6(self, browser):
        # 시차출퇴근제 - 직접입력 / 결재 > 전자결재 상신 후 반려
        name = '시직접'
        self.logout(browser)
        self.login_nahago(browser, name)
        self.ap_vacationApplication(browser, name)
        time.sleep(5)
        self.ap_reject(browser)

class Certificate :
    def setCertificate(self, browser) :
        time.sleep(10)
        browser_click(browser, varname_nahago.main_hamBtn)
        time.sleep(5)
        action = ActionChains(browser)
        test = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.View'
        action.move_to_element_with_offset(browser.find_element(By.XPATH, test), 150, 1900).click().perform()
        time.sleep(5)
        # KT 본인인증
        browser_click(browser, varname_nahago.certificateBtn)
        Login().nahago_pw(browser)

        browser_click(browser, varname_nahago.certificateDoneBtn)
        time.sleep(5)
        browser_click(browser, varname_nahago.kt)
        browser_click(browser, varname_nahago.agreeBtn)
        browser_click(browser, varname_nahago.smsSendBtn)
        time.sleep(1)
        secureText = input('보안문자 입력')
        browser_sendKey(browser, varname_nahago.username, '문지영')
        browser_sendKey(browser, varname_nahago.mynum1, '950209')
        browser_sendKey(browser, varname_nahago.mynum2, '2')
        browser_sendKey(browser, varname_nahago.mobileno, '01045681896')
        browser_sendKey(browser, varname_nahago.answer, secureText)
        browser_click(browser, varname_nahago.btnSubmit)
        time.sleep(3)
        number = input('인증번호 입력')
        browser_sendKey(browser, varname_nahago.authnumber, number)
        browser_click(browser, varname_nahago.btnSubmit2)
        time.sleep(3)
        browser_click(browser, varname_nahago.certificateCheck)
        browser_click(browser, varname_nahago.certificateDoneBtn)
        browser_click(browser, varname_nahago.notuseBtn)
        while True :
            count = 0
            if hasxpath(browser, varname_nahago.certificateDoneBtn) :
                break
            elif count == 60 :
                break
            else :
                time.sleep(3)
                count = count + 1

        if not hasxpath(browser, varname_nahago.certificationSetBtn) :
            raise Exception('인증서 발급 확인 필요')

        browser_click(browser, varname_nahago.certificateBackBtn)

    def deleteCertificate(self, browser) :
        browser_click(browser, varname_nahago.main_hamBtn)
        time.sleep(5)
        action = ActionChains(browser)
        test = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.View'
        action.move_to_element_with_offset(browser.find_element(By.XPATH, test), 150, 1900).click().perform()
        time.sleep(5)
        browser_click(browser, varname_nahago.certificationSetBtn)
        browser_click(browser, varname_nahago.deleteCertificate)
        browser_click(browser, varname_nahago.deleteCertificateBtn)
        if hasxpath(browser, varname_nahago.certificationSetBtn) :
            raise Exception('인증서 발급 확인 필요')

class UserInfo :
    def info_modifyInfo(self, browser) :
        browser_click(browser, varname_nahago.basicInfo)
        action = ActionChains(browser)
        info = varname_nahago.modifyBasicInfo
        action.move_to_element_with_offset(browser.find_element(By.XPATH, info), 250, 300).click().perform()
        time.sleep(1)
        browser_sendKey(browser, varname_nahago.numberInfo, '0262333301')
        browser_sendKey(browser, varname_nahago.mailInfo, 'aass@naver.com')
        browser_click(browser, varname_nahago.modifyInfoBtn)
        time.sleep(1)
        browser_click(browser, varname_nahago.infoBackBtn)

    def info_deleteInfo(self, browser) :
        browser_click(browser, varname_nahago.basicInfo)
        action = ActionChains(browser)
        info = varname_nahago.modifyBasicInfo
        action.move_to_element_with_offset(browser.find_element(By.XPATH, info), 250, 300).click().perform()
        time.sleep(1)
        browser_click(browser, varname_nahago.numberInfo)
        browser_click(browser, varname_nahago.delNumberInfo)
        browser_click(browser, varname_nahago.mailInfo)
        browser_click(browser, varname_nahago.delMailInfo)
        browser_click(browser, varname_nahago.modifyInfoBtn)
        time.sleep(1)
        browser_click(browser, varname_nahago.infoBackBtn)

    def info_account(self, browser) :
        browser_click(browser, varname_nahago.accountInfo)
        action = ActionChains(browser)
        info = varname_nahago.addAccountInfo
        action.move_to_element_with_offset(browser.find_element(By.XPATH, info), 500, 800).click().perform()
        time.sleep(1)
        Login().nahago_pw(browser)
        time.sleep(3)
        browser_sendKey(browser, varname_nahago.info_user, '문지영')
        browser_click(browser, varname_nahago.selectBank)
        browser_click(browser, '//android.widget.TextView[@text = "신한은행"]')
        browser_sendKey(browser, varname_nahago.accountNumber, '110436254029')
        browser_click(browser, varname_nahago.registerAccountBtn)
        browser_click(browser, varname_nahago.info_doneBtn)
        time.sleep(3)
        action = ActionChains(browser)
        action.move_to_element_with_offset(browser.find_element(By.XPATH, varname_nahago.info), 500, 1100).click().perform()
        time.sleep(3)
        browser_click(browser, varname_nahago.cancelBtn)
        time.sleep(5)

    def info_dependent(self, browser) :
        browser_click(browser, varname_nahago.dependentInfo)
        action = ActionChains(browser)
        action.move_to_element_with_offset(browser.find_element(By.XPATH, varname_nahago.info), 500, 1100).click().perform()
        time.sleep(1)
        browser_click(browser, varname_nahago.addDependent)
        browser_click(browser, '//android.widget.TextView[@text = "직접 입력"]')
        time.sleep(1)
        browser_sendKey(browser, varname_nahago.dependentName, '김수한무')
        browser_click(browser, varname_nahago.dependentRelations)
        time.sleep(1)
        browser_click(browser, varname_nahago.selectDependentRelations)
        browser_click(browser, varname_nahago.dependentNumber)
        action = ActionChains(browser)
        action.pause(1).send_keys('921111').send_keys(Keys.TAB).pause(1).send_keys('1111111').send_keys(Keys.TAB).perform()
        browser.hide_keyboard()
        time.sleep(1)
        # browser_sendKey(browser, varname_nahago.dependentNumber, '9211111111111')

        browser_click(browser, varname_nahago.dependentDoneBtn)
        browser_click(browser, varname_nahago.dependentNextBtn)
        browser_click(browser, varname_nahago.dependentNextBtn)
        browser_click(browser, varname_nahago.info_doneBtn)
        time.sleep(5)
        action = ActionChains(browser)
        action.move_to_element_with_offset(browser.find_element(By.XPATH, varname_nahago.info), 500, 1100).click().perform()
        browser_click(browser, varname_nahago.cancelDependent)