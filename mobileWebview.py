# 모바일 웹뷰 진입 코드 1
""" from selenium import webdriver
mobile_emulation = { "deviceName": "Nexus 5" }
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"]) # USB: usb_device_handle_win.cc:1048 Failed to read descriptor from node connescriptor from node connection: 시스템에 부착된 장치가 작동하지 않습니다. (0x1F) 에러 안뜨게 하는 용도 - 다음주에 정리해야지
driver = webdriver.Chrome(options=chrome_options) #sometimes you have to insert your execution path
driver.get('https://wehago.com/#/login') """

# 모바일 웹뷰 진입 코드 2
""" from selenium import webdriver
from selenium.webdriver.chrome.options import Options

mobile_emulation = {
    "deviceMetrics": { "width": 375, "height": 812, "pixelRatio": 3.0 },
    "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"
}

chrome_options = Options()
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(
    executable_path="./chromedriver", options=chrome_options
) """
import time, datetime, platform
from driver import browser_click, browser_sendKey, hasxpath, currentTime, btn_click, chromeBrowser, wehagoID
import varname
import wehagotest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import os





ID= 'id'; CSS='CSS'; CLASS_NAME='class'; TAG_NAME='tag_mobileVarname'
path = os.getcwd()





def getUrl(service, by=True) :
    url = 'https://www.wehago.com/#/'
    url = url + service
    return url


def progress(browser) :
    count = 1
    for i in range(0,60) :
        if count == 60 : 
            browser.refresh()
            time.sleep(5)
            raise Exception('60초 동안 무한로딩중,,')
        if hasxpath(browser, 'WSC_LUXCircularProgress', CLASS_NAME) :
            time.sleep(1)
            count = count + 1
        else : 
            break
    time.sleep(1)

def enter (browser, xpath, text, by=None, sec=None) :
    if not sec : sec = 1
    browser_sendKey(browser, xpath, text, by)
    time.sleep(sec)
    browser_sendKey(browser, xpath, Keys.ENTER, by)
    time.sleep(1)

def textClear(browser, xpath) :
    text = browser.find_element(By.XPATH, xpath)

    if platform.system() == 'Windows' :
        text.send_keys(Keys.CONTROL + "a")
    elif platform.system() == 'Darwin' :
        text.send_keys(Keys.COMMAND, "a")
    text.send_keys(Keys.DELETE)
    time.sleep(0.5)

def inputUser(browser, xpath, by=None, sec=None) :
    name = usersName(browser)
    if name == '문지영' :
        enter(browser, xpath, '장윤주', by, sec)
    else :
        enter(browser, xpath, '문지영', by, sec)

def usersName (browser) :
    name = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, 'btn_userprofile'))).text
    return name[0:3]

def context(browser, xpath, by=None) :
    if by == CLASS_NAME :
        text = browser.find_element(By.CLASS_NAME, xpath).text
    elif by == ID :
        text = browser.find_element(By.ID, xpath).text
    else :
        text = browser.find_element(By.XPATH, xpath).text
    return text

def sameText(browser, text) :
    # 중복 팝업 창 문구
    if hasxpath(browser, varname.duplicatePopup) :
        context = browser.find_element(By.XPATH, varname.duplicatePopup).text
        if text in context :
            return True
        else :
            return False
    else :
        return False


class Common :
    def set_wehagoBrand(self, version, brand) :
        global wehagoBrand
        global userid
        wehagoBrand = brand
        userid = wehagoID(version, brand)

    def fileUpload(self, browser, fileName) :
        f = path + '/' + fileName
        browser.find_element(By.CSS_SELECTOR, 'input[type="file"]').send_keys(f)
        time.sleep(3)

    def setPassword(self, browser) :
        browser.find_element(By.XPATH, '//button[text()="1"]').click()
        browser.find_element(By.XPATH, '//button[text()="2"]').click()
        browser.find_element(By.XPATH, '//button[text()="1"]').click()
        browser.find_element(By.XPATH, '//button[text()="2"]').click()
        browser.find_element(By.XPATH, '//button[text()="1"]').click()
        browser.find_element(By.XPATH, '//button[text()="2"]').click()
        time.sleep(1)
    
    def close(self, browser) :
        action = ActionChains(browser)
        action.send_keys(Keys.ESCAPE).perform()
        action.reset_actions()
        time.sleep(1)


    def tabClose(self, browser) :
        count = len(browser.window_handles)
        if count != 1 :
            for i in range(count, 1, -1) :
                browser.switch_to.window(browser.window_handles[i-1])
                browser.close()
            browser.switch_to.window(browser.window_handles[0])
        browser.refresh()
        time.sleep(5)


    def canvasClick(self, browser, xpath, xoffset, yoffset, by=None) :
        # x,y 선택하는 canvas
        action = ActionChains(browser)
        if by == CLASS_NAME :
            service = browser.find_element(By.CLASS_NAME, xpath)
        else :
            service = browser.find_element(By.XPATH, xpath)
        action.move_to_element_with_offset(service, xoffset, yoffset).click().perform()
        action.reset_actions()
        time.sleep(3)


class Login :
    def login(self, browser, id) :
            print("login s")
            if id == 'hancho1' :
                browser.get('https://www.wehago.com/#/login')
            else :
                browser.get(getUrl('login'))
            time.sleep(3)
            if '로그인 : WEHAGO' in browser.title :
                #아이디,비밀번호 입력
                browser_sendKey(browser, 'inputId', id, ID)
                if id == 'ptestjy_1719' or 'yjjang_test3' in id : pwd = '1q2w3e4r'
                browser_sendKey(browser, 'inputPw', pwd, ID)
                browser_sendKey(browser, 'inputPw', Keys.ENTER, ID)
                time.sleep(1)

                #중복 로그인 창 뜨면 확인 버튼 클릭
                if hasxpath(browser, varname.duplicateBtn) :
                    browser_click(browser, varname.duplicateBtn)
                time.sleep(5)

                # 로그아웃 하고 세션 만료 된 경우 새로고침 추가
                if id != browser.get_cookie('h_portal_id')['value'] :
                    browser.refresh()
                    time.sleep(5)
            else :
                print('로그인 상태')

class Approval :
    # Web 전자결재 파트 시작
    def ap_basicset(self, browser) :
        browser_click(browser, varname.createApproval)
        browser_click(browser, varname.setFrequentlyApproval)
        enter(browser, varname.serachFormname, '명함')
        browser_click(browser, varname.approvalForm)
        browser_click(browser, varname.saveApproval)
        text = '자주쓰는 결재를 등록하지 않은 경우'
        if wehagotest.sameText(browser, text) :
            browser_click(browser, varname.cancel)
            browser_click(browser, varname.cancelApproval)
        progress(browser)


    def ap_unsavedInformation(self, browser) :
        text = '결재문서에 입력된 정보가 존재합니다.'
        if wehagotest.sameText(browser, text) :
            browser_click(browser, varname.confirm)
    
   
    

    # 모듈화 고민 - 제목, self.ap_webApprover 빼고 다 겹치는데...ㅠㅠ for문이 걸린다
    def ap_createWebApproval(self, browser, num, type) :
        #browser.get(getUrl('eapprovals'))
        time.sleep(3)
        if type == "일반":
            for i in range(1, 6):
                self.ap_unsavedInformation(browser)
                browser_click(browser, varname.createApproval)
                progress(browser)
                if not hasxpath(browser, varname.createApprovalForm) :
                    self.ap_basicset(browser)
                browser_click(browser, varname.createApprovalForm)
                progress(browser)
                time.sleep(1)
                approveTitle = '웹전자결재 테스트' + str(i)
                browser_sendKey(browser, varname.approvalName, approveTitle)
                self.ap_webApprover(browser, type)
                time.sleep(1)
                browser_click(browser, 'LUX_basic_btn.Confirm.basic2', CLASS_NAME)
                progress(browser)
        
        elif type == "후결" or "전결" :
            self.ap_unsavedInformation(browser)
            browser_click(browser, varname.createApproval)
            progress(browser)
            if not hasxpath(browser, varname.createApprovalForm) :
                self.ap_basicset(browser)
            browser_click(browser, varname.createApprovalForm)
            progress(browser)
            time.sleep(1)
            approveTitle = '웹전자결재 테스트' + num
            browser_sendKey(browser, varname.approvalName, approveTitle)
            self.ap_webApprover(browser, type)
            time.sleep(1)
            browser_click(browser, 'LUX_basic_btn.Confirm.basic2', CLASS_NAME)
            progress(browser)


    # 웹 결재자 지정
    def ap_webApprover(self, browser, type) :
        browser_click(browser, varname.approvalUser)
        progress(browser)
        if type == '일반' :
            enter(browser, '//*[@id="inputSearch-TK"]', '문지영')
            time.sleep(2) # 테스트용 추가
            browser_click(browser, 'point_color', CLASS_NAME)
            browser_click(browser, varname.approvalAddUser)
            time.sleep(1)
            if '중복 지정' in context(browser, varname.ap_duplicatePopup) :
                browser_click(browser, varname.ap_duplicateConfirm)
        else :
            if type == '후결' :
                browser_click(browser, varname.postApprovalButton)
            elif type == '전결' :
                browser_click(browser, varname.preApprovalButton)
            time.sleep(1)
            if '프로세스 변경 시' in context(browser, varname.duplicatePopup) :
                browser_click(browser, varname.confirm)
                time.sleep(1)
            enter(browser, '//*[@id="inputSearch-TK"]', '문지영')
            browser_click(browser, 'point_color', CLASS_NAME)
            browser_click(browser, varname.approvalAddUser1)
            textClear(browser, '//*[@id="inputSearch-TK"]')
            inputUser(browser, '//*[@id="inputSearch-TK"]')
            browser_click(browser, 'point_color', CLASS_NAME)
            browser_click(browser, varname.approvalAddUser2)
        browser_click(browser, varname.registApprover)
        time.sleep(3)
        # if '후결 일 경우' in context(browser, varname.duplicatePopup) :
        #     browser_click(browser, varname.confirm)
        #     Common().close(browser)


    # 웹 기안 상신 1 ~ 3
    def ap_webApproval1(self, browser) :
        #self.ap_createWebApproval1(browser)
        browser.get(getUrl('eapprovals'))
        self.ap_createWebApproval(browser, None,'일반')
 
    # 웹 기안 상신 4 - 전결
    def ap_webApproval2(self, browser) :
        #self.ap_createWebApproval2(browser,'4', '전결')
        self.ap_createWebApproval(browser, '6', '전결')
    
    # 웹 기안 상신 5 - 후결
    def ap_webApproval3(self, browser) :
        #self.ap_createWebApproval2(browser,'5', '후결')
        self.ap_createWebApproval(browser, '7', '후결')

    

    # 웹에서 보관함 삭제
    def ap_deleteArchive(self, browser): 
        browser.get(getUrl('eapprovals'))
        #time.sleep(3)
        progress(browser)
        while hasxpath(browser, varname.archiveList) :
            browser_click(browser, varname.archiveList)
            time.sleep(1)
            browser_click(browser, varname.archiveOption)
            time.sleep(1) # 테스트
            browser_click(browser, varname.archiveDelete)
            if '보관함을 삭제' in context(browser, varname.archivePopup) :
                browser_click(browser, varname.archiveConfirm)
            time.sleep(1)
        if context(browser, varname.archiveCount) != '0' :
            raise Exception('보관함 삭제 확인 필요')

    # 웹에서 보관함 생성
    def ap_createArchive(self, browser) :
        browser_click(browser, 'add_group', CLASS_NAME)
        time.sleep(1)
        action = ActionChains(browser)
        action.send_keys('보관함 하나').send_keys(Keys.ENTER).perform()
        action.reset_actions()
        time.sleep(1)
        if context(browser, varname.archiveCount) == '0' :
            raise Exception('보관함 추가 확인 필요')

delete = '삭제'
class Accounts :
    
    def ac_registAccount (self, browser) :
        browser.get(wehagotest.getUrl('accounts', 1))
        time.sleep(3) # 추가
        #progress(browser)
        browser_click(browser, varname.registerAccount)
        time.sleep(3)
        browser_sendKey(browser, varname.accountName, '(주)더존비즈온')
        browser_sendKey(browser, varname.representativeName, '김용우')
        time.sleep(1) # 추가
        browser_click(browser, varname.register)
        progress(browser)
        enter(browser, varname.searchAccount, '더존비즈온')
        count = '//*[@id="BODY_CLASS"]/div[3]/div/div/div/div/div/div[3]/div[1]/h2'
        if '검색결과0' == context(browser, count) :
            raise Exception('거래처 등록 확인 필요')

    def ac_modifyAccount (self, browser) :
        textClear(browser, varname.searchAccount)
        enter(browser, varname.searchAccount, '더존비즈온')
        browser_click(browser, varname.modifyAccount)
        browser_sendKey(browser, varname.enterpriseNumber, '1348108473')
        time.sleep(1)

        #사용자 그룹 추가
        browser_click(browser, varname.accountGroupSelect)
        Common().canvasClick(browser, varname.accountGroup, 15, 15) # (16, 16) (20, 20) (10)
        time.sleep(1)
        browser_click(browser, varname.accountConfirm)
        time.sleep(6) # test
        browser_click(browser, varname.register)
        progress(browser)
    
    def ac_deleteAccount (self, browser) :
        while True :
            textClear(browser, varname.searchAccount)
            enter(browser, varname.searchAccount, '더존')
            time.sleep(1)
            if not hasxpath(browser, 'data_none', CLASS_NAME) :
                browser_click(browser, varname.clickAccount)
                browser_click(browser, varname.deleteAccount)
                browser_click(browser, varname.confirm_ac)
                progress(browser)
            else :
                break
    
    def ac_createGroup (self, browser) :
        browser_click(browser, varname.accountAddUserGroup)
        time.sleep(1)
        action = ActionChains(browser)
        action.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).send_keys(Keys.BACK_SPACE).send_keys('거래처그룹').send_keys(Keys.ENTER).perform()
        time.sleep(3)
        if not hasxpath(browser, varname.accountList) :
            raise Exception('거래처 사용자 그룹 생성 확인 필요')

    def ac_deleteGroup (self, browser) :
        time.sleep(1)
        while hasxpath(browser, varname.accountList) :
            time.sleep(1)
            browser_click(browser, varname.accountList)
            time.sleep(3)
            browser_click(browser, varname.accountOption)
            time.sleep(1)
            browser_click(browser, varname.accountDeleteGroup)
            browser_click(browser, varname.confirm)
            browser.refresh()
            time.sleep(3)
        time.sleep(1)
        if hasxpath(browser, varname.accountList) :
            raise Exception('거래처 사용자 그룹 생성 확인 필요')

    def ac_createSharedGroup (self, browser) :
        browser_click(browser, varname.accountAddSharedGroup)
        time.sleep(1)
        browser_click(browser, varname.accountSharedGroupName)
        action = ActionChains(browser)
        action.send_keys('공유거래처그룹').send_keys(Keys.TAB).send_keys('한초희').pause(1).send_keys(Keys.ENTER).perform()
        action.reset_actions()
        time.sleep(1)
        browser_click(browser, varname.accountCreateGroup)
        if sameText(browser, '공유그룹의 참여자를 추가해주세요.') :
            browser_click(browser, varname.confirm)
            browser_click(browser, varname.accountCloseButton)
            raise Exception('사용자 미초대!!')

    def ac_deleteSharedGroup(self, browser) :
        time.sleep(3)
        while hasxpath(browser, varname.accountSharedList) :
            time.sleep(1)
            browser_click(browser, varname.accountSharedList)
            time.sleep(1)
            browser_click(browser, varname.accountSharedOption)
            browser_click(browser, varname.accountDeleteSharedGroup)
            browser_click(browser, varname.confirm)
            time.sleep(1)

class Approval : 

    def clickApproalSetting(self, browser) :
        browser_click(browser, varname.approvalSetting)
        time.sleep(5)
        browser.switch_to.window(browser.window_handles[1])
        while not hasxpath(browser, varname.documentForm) :
            time.sleep(1)

    def ap_deleteApprove(self, browser) :
        time.sleep(3)
        self.clickApproalSetting(browser)
        enter(browser, varname.serachApproval, '전자결재')
        progress(browser)
        while True :
            Common().canvasClick(browser, '//*[@id="gridAdminCheckBox"]/div/canvas', -650, 170)
            #Common().canvasClick(browser, '//*[@id="gridAdminCheckBox"]/div/canvas', 45, 170) # (45, 170) 60 80 200 -700부터 선택이 안되네 여기서 조정 ㄱ 
            if context(browser, varname.deleteApprove) == delete :
                browser_click(browser, varname.deleteApprove)
                browser_click(browser, varname.confirm)
            else :
                break
        #browser.close()
        browser.switch_to.window(browser.window_handles[0])
        time.sleep(3)