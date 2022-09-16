from cgitb import text
from curses import A_COLOR, KEY_CLOSE, KEY_ENTER, KEY_F4
import curses
from inspect import modulesbyfile
from msilib.schema import Class
from operator import contains
import time, datetime
from tkinter import Checkbutton
from tkinter.font import names
from unicodedata import name
import unittest
import os
from webbrowser import BaseBrowser
from appium import webdriver
from time import monotonic, sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from driver import browser_click, browser_sendKey, hasxpath, currentTime, btn_click, mobile_click
import varname_nahago
import mobileVarname
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.action_chains import ActionChains

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
    def login_nahago(self, browser) :
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
        browser_sendKey(browser, varname_nahago.loginName, '안태자')
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
        mobile_click(browser, '확인')

    def cc_createChat(self, browser) :
        browser_click(browser, varname_nahago.cc_createBtn)
        browser_click(browser, varname_nahago.cc_addChat)
        time.sleep(3)
        browser_sendKey(browser, varname_nahago.cc_searchUser, '한초희')
        browser_click(browser, varname_nahago.cc_selectUser)
        mobile_click(browser, '선택')
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