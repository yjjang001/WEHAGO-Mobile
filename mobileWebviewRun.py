
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
from driver import browser_click, browser_sendKey, hasxpath, currentTime, chromeBrowser, mobileBrowser
import mobileVarname
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.action_chains import ActionChains
import Android
import mobileWebview
import wehagotest
#import wehagotestrun
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

ID='id'; CSS='CSS'; CLASS_NAME='class'; TAG_NAME='tag_name'





if __name__ == "__main__" :
    id = 'ptestjy_1719'; pwd = '1q2w3e4r' ; id2 = 'stestjy_20195'
    

    # 모바일 웹뷰 테스트_에러나는 pc 있음. 
    # 1
    #mobile_emulation = { "deviceName": "Nexus 5" }
    #mobile_emulation = { "deviceName": "Samsung Galaxy S20 Ultra" }
    #chrome_options = webdriver.ChromeOptions()
    #chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    #chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"]) 
    #browser = webdriver.Chrome(options=chrome_options) 
    #1-2
    #browser = mobileBrowser() # driver.py 파일


    # 2 : 모바일 웹 호출
    """ mobile_emulation = {
        #"deviceMetrics": { "width": 375, "height": 812, "pixelRatio": 3.0 },
        "deviceMetrics": { "width": 412, "height": 915, "pixelRatio": 3.0 },
        "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"
    }

    chrome_options = Options()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
    chrome_options.add_argument('--start-maximized')
    browser = webdriver.Chrome(
        executable_path="./chromedriver", options=chrome_options
    ) """

    
    


    browser = mobileBrowser()
    # 로그인
    mobileWebview.Login().login(browser, id)

    # 거래처
    """ browser.get(wehagotest.getUrl('accounts', 1))
    wehagotest.Accounts().ac_registAccount(browser) 
    wehagotest.Accounts().ac_modifyAccount(browser) # 그룹 선택은 안됨. 
    wehagotest.Accounts().ac_deleteAccount(browser)
    wehagotest.Accounts().ac_createGroup(browser) # 수정, 삭제는 err
    wehagotest.Accounts().ac_createSharedGroup(browser) """ # 수정, 삭제는 err
    


    # 연락처
    """ browser.get(wehagotest.getUrl('contacts', 1))
    wehagotest.Contacts().ct_deleteContact(browser)
    wehagotest.Contacts().ct_registerContacts(browser)
    wehagotest.Contacts().ct_modifyContact(browser)
    wehagotest.Contacts().ct_deleteContact(browser)
    wehagotest.Contacts().ct_createGroup(browser)
    wehagotest.Contacts().ct_modifyGroup(browser)
    wehagotest.Contacts().ct_deleteGroup(browser)
    wehagotest.Contacts().ct_createSharedGroup(browser)
    wehagotest.Contacts().ct_modifySharedGroup(browser)
    wehagotest.Contacts().ct_deleteSharedGroup(browser) """
    
    

    # 메일
    """ browser.get(wehagotest.getUrl('mail', 1))
    wehagotest.Mail().ma_sendMail(browser)
    browser.refresh()
    #wehagotest.Mail().ma_replyMail(browser) # err - 웹에서는 오류 x
    wehagotest.Mail().ma_sendMailWedrive(browser)
    browser.refresh()
    #wehagotest.Mail().ma_replyMailAll(browser) #  err
    wehagotest.Mail().ma_sendReservedMail(browser)
    wehagotest.Mail().ma_sendSecureMail(browser)
    #wehagotest.Mail().ma_deliveryMail(browser) # err
    wehagotest.Mail().ma_automaticClassification(browser)
    wehagotest.Mail().ma_deleteAutomatic(browser)
    wehagotest.Mail().ma_deleteMail(browser)
    wehagotest.Mail().ma_emptyTrash(browser) """


    # 메시지
    """ browser.get(wehagotest.getUrl('communication2/message/inbox', 1))

    wehagotest.Message().ms_sendMessage(browser)
    wehagotest.Message().ms_sendSecurityMessage(browser)
    wehagotest.Message().ms_sendImportantMessage(browser)
    wehagotest.Message().ms_sendReservationMessage(browser)
    
    
    #wehagotest.Message().ms_resendMessage(browser) # err 2개 메시지 선택되는 현상
    #wehagotest.Message().ms_replyMessage(browser) # err 
    #wehagotest.Message().ms_replyAllMessage(browser) # err
    #wehagotest.Message().ms_forwardMessage(browser) # err
    #wehagotest.Message().ms_readSecurityMessage(browser) # err
    wehagotest.Message().ms_readMessageAll(browser)
    browser.refresh()
    #wehagotest.Message().ms_searchMessage(browser) # err 메시지 내용 클릭 안됨
    #wehagotest.Message().ms_bookmark(browser) # 두 개 메시지 선택됨
    #wehagotest.Message().ms_deleteReceiveMessage(browser) # err  선택 안됨 - 전체 선택이 아닌 그 옆 드랍다운 버튼이 클림됨 _ 웹에서는 정상
    #wehagotest.Message().ms_deleteSendMessage(browser) # err 선택 안됨 - 전체 선택이 아닌 그 옆 드랍다운 버튼이 클림됨 _ 웹에서는 정상
    wehagotest.Message().ms_addBoilerplate(browser)
    wehagotest.Message().ms_applyBoilerplate(browser)
    browser.refresh()
    wehagotest.Message().ms_readBoilerplate(browser) # 새로고침 안하면 err
    wehagotest.Message().ms_delBoilerplate(browser) """

    """ browser.get(wehagotest.getUrl('communication2/message/inbox', 1))
    wehagotest.Message().ms_sendMessage(browser)
    wehagotest.Message().ms_sendSecurityMessage(browser)
    wehagotest.Message().ms_sendImportantMessage(browser)
    wehagotest.Message().ms_sendReservationMessage(browser)

    #wehagotest.Message().ms_resendMessage(browser) # err 2개 메시지 선택되는 현상
    #wehagotest.Message().ms_replyMessage(browser) # err 
    #wehagotest.Message().ms_replyAllMessage(browser) # err
    #wehagotest.Message().ms_forwardMessage(browser) # err
    #wehagotest.Message().ms_readSecurityMessage(browser) # err

    browser.refresh()
    wehagotest.Message().ms_readSecurityMessage(browser)
    print('1')
    wehagotest.Message().ms_readMessageAll(browser)
    print('2')
    browser.refresh()
    wehagotest.Message().ms_searchMessage(browser)
    print('3')
    browser.refresh()
    #wehagotest.Message().ms_bookmark(browser) # 두 개 메시지 선택됨
    print('4')
    #wehagotest.Message().ms_deleteReceiveMessage(browser) # err  선택 안됨 - 전체 선택이 아닌 그 옆 드랍다운 버튼이 클림됨 _ 웹에서는 정상
    print('5')
    #wehagotest.Message().ms_deleteSendMessage(browser) # err  선택 안됨 - 전체 선택이 아닌 그 옆 드랍다운 버튼이 클림됨 _ 웹에서는 정상
    print('6')
    wehagotest.Message().ms_addBoilerplate(browser)
    print('7')
    wehagotest.Message().ms_applyBoilerplate(browser)
    print('8')
    wehagotest.Message().ms_readBoilerplate(browser)
    print('9')
    wehagotest.Message().ms_delBoilerplate(browser)
    print('10') """

    # 메신저


    # 모바일 웹뷰 종료
    #browser.quit()
    

    # 웹 자동화 테스트
    browser2 = chromeBrowser() # 웹 호출

    # 로그인
    mobileWebview.Login().login(browser2, id)

    # 거래처
    """ browser2.get(wehagotest.getUrl('accounts', 1))
    time.sleep(3)
    wehagotest.Accounts().ac_registAccount(browser2)
    wehagotest.Accounts().ac_modifyAccount(browser2)
    wehagotest.Accounts().ac_deleteAccount(browser2) """
    """ wehagotest.Accounts().ac_createGroup(browser2)
    wehagotest.Accounts().ac_deleteGroup(browser2)
    wehagotest.Accounts().ac_createSharedGroup(browser2)
    wehagotest.Accounts().ac_deleteSharedGroup(browser2) """
    

    # 연락처
    """ browser2.get(wehagotest.getUrl('contacts', 1))
    wehagotest.Contacts().ct_deleteContact(browser2)
    wehagotest.Contacts().ct_registerContacts(browser2)
    wehagotest.Contacts().ct_modifyContact(browser2)
    wehagotest.Contacts().ct_deleteContact(browser2)
    wehagotest.Contacts().ct_createGroup(browser2)
    wehagotest.Contacts().ct_modifyGroup(browser2)
    wehagotest.Contacts().ct_deleteGroup(browser2)
    wehagotest.Contacts().ct_createSharedGroup(browser2)
    wehagotest.Contacts().ct_modifySharedGroup(browser2)
    wehagotest.Contacts().ct_deleteSharedGroup(browser2)
    """


    # 메일
    """ browser2.get(wehagotest.getUrl('mail', 1))
    wehagotest.Mail().ma_sendMail(browser2)
    wehagotest.Mail().ma_replyMail(browser2) # 순서 구성 잘하기
    wehagotest.Mail().ma_sendMailWedrive(browser2)
    wehagotest.Mail().ma_replyMailAll(browser2) # 순서 구성 잘하기
    wehagotest.Mail().ma_sendReservedMail(browser2)
    wehagotest.Mail().ma_sendSecureMail(browser2)
    wehagotest.Mail().ma_deliveryMail(browser2)
    wehagotest.Mail().ma_automaticClassification(browser2)
    wehagotest.Mail().ma_deleteAutomatic(browser2)
    wehagotest.Mail().ma_deleteMail(browser2)
    wehagotest.Mail().ma_emptyTrash(browser2) """


    # 메시지
    """ browser2.get(wehagotest.getUrl('communication2/message/inbox', 1))
    wehagotest.Message().ms_sendMessage(browser2)
    wehagotest.Message().ms_sendSecurityMessage(browser2)
    wehagotest.Message().ms_sendImportantMessage(browser2)
    wehagotest.Message().ms_sendReservationMessage(browser2)
    
    
    wehagotest.Message().ms_resendMessage(browser2)
    wehagotest.Message().ms_replyMessage(browser2)
    wehagotest.Message().ms_replyAllMessage(browser2)
    wehagotest.Message().ms_forwardMessage(browser2)
    wehagotest.Message().ms_readSecurityMessage(browser2)
    wehagotest.Message().ms_readMessageAll(browser2)
    wehagotest.Message().ms_searchMessage(browser2)
    wehagotest.Message().ms_bookmark(browser2)
    wehagotest.Message().ms_deleteReceiveMessage(browser2)
    wehagotest.Message().ms_deleteSendMessage(browser2)
    wehagotest.Message().ms_addBoilerplate(browser2)
    wehagotest.Message().ms_applyBoilerplate(browser2)
    wehagotest.Message().ms_readBoilerplate(browser2)
    wehagotest.Message().ms_delBoilerplate(browser2) """
    
    # 메신저
    browser.get(wehagotest.getUrl('communication2', 1))



    wehagotest.Communication().cc_acceptParticipation(browser2)

    wehagotest.Communication().cc_acceptInvitedUser(browser2)

    wehagotest.Communication().cc_refusalParticipation(browser2)

    wehagotest.Communication().cc_exportUser(browser2)
    wehagotest.Communication().cc_leaveChatRoom(browser2)
    wehagotest.Communication().cc_createRoomByContacts(browser2)
    wehagotest.Communication().cc_createRoomByInput(browser2)

    wehagotest.Communication().cc_createRoomByOrganization(browser2)
    wehagotest.Communication().cc_sendChat(browser2)
    wehagotest.Communication().cc_deleteChat(browser2)
    wehagotest.Communication().cc_copyChat(browser2)
    wehagotest.Communication().cc_addComment(browser2)
    wehagotest.Communication().cc_uploadLocal(browser2)
    wehagotest.Communication().cc_uploadWedrive(browser2)
    wehagotest.Communication().cc_uploadFileTab(browser2)
    wehagotest.Communication().cc_collectFile(browser2)
    wehagotest.Communication().cc_openWebOffice(browser2)
    wehagotest.Communication().cc_appendingSchedule(browser2)

    wehagotest.Communication().cc_appendingAccount(browser2)
    wehagotest.Communication().cc_appendingContact(browser2)
    wehagotest.Communication().cc_appendingMeet(browser2)
    wehagotest.Communication().cc_appendingVote(browser2)
    wehagotest.Communication().cc_listVote(browser2)
    wehagotest.Communication().cc_recentChat(browser2)
    wehagotest.Communication().cc_searchChat(browser2)
    wehagotest.Communication().cc_sharedChat(browser2)
    wehagotest.Communication().cc_settingGroup(browser2)
    wehagotest.Communication().cc_favoriteConversation(browser2)
    wehagotest.Communication().cc_unfavoriteConversation(browser2)
    wehagotest.Communication().cc_searchMention(browser2)
    wehagotest.Communication().cc_checkUserProfile(browser2)
    wehagotest.Communication().cc_setAsMaster(browser2)
    wehagotest.Communication().cc_createChat(browser2)
    wehagotest.Communication().cc_leaveChat(browser2)

    # 전자결재
    #browser2.get(wehagotest.getUrl('eapprovals', 1))
    #wehagotest.Approval().ap_deleteApprove(browser2)
    #mobileWebview.Approval().ap_deleteApprove(browser2)

    # 브라우저 종료
    #browser2.quit() 

print('3')