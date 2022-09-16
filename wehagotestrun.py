from typing import Tuple
import wehagotest, Android
import wehagoReport
import datetime, os, time, sys
from driver import chromeBrowser, serviceTest, serviceRun
import openpyxl

def serviceRun (browser, serviceObj, serviceFun) :
    print(serviceFun)
    result = wehagoReport.WehagoResult()
    global exer
    start = time.time()
    now = datetime.datetime.now()
    path = os.path.join(os.getcwd(), 'result/image/')
    fileName = now.strftime('%m-%d %Ih%Mm') + serviceFun + ' Fail.png'
    try :
        time.sleep(1)
        getattr(serviceObj, serviceFun)(browser)
        result.testSuccess(serviceFun)
    except Exception as ex :
        print(serviceFun)
        # 실패한 상황 캡쳐
        browser.save_screenshot(path + fileName)
        print(ex)
        exer = str(ex)
        result.testFailure(serviceFun, exer[:45], fileName)
    result.runTime(serviceFun, start)

def tabClose(browser) :
    count = len(browser.window_handles)
    if count != 1 :
        for i in range(count, 1, -1) :
            browser.switch_to.window(browser.window_handles[i-1])
            browser.close()
        browser.switch_to.window(browser.window_handles[0])

def getUrl(service, by=True) :
    url = 'https://www.wehago'
    if by :
        if wehagotest.wehagoBrand == 3 :
            url = url + 'v.com/#/'
        elif wehagotest.wehagoBrand == 2 :
            url = url + 't.com/#/'
        else:
            url = url + '.com/#/'
        url = url + service
    else :
        if wehagotest.wehagoBrand == 3 :
            url = url + 'v.com/'
        elif wehagotest.wehagoBrand == 2 :
            url = url + 't.com/'
        else:
            url = url + '.com/'
        url = url + service  + '/#/'
    return url

def browserTitle (browser, title) :
    if title in browser.title :
        return True
    else :
        return False

def appName (browser, service) :
    appName = browser.find_elements_by_class_name('app_name')
    for service in appName :
        if service.text == service :
            service.click()

def serviceFunction(service) :
    path = os.path.join(os.getcwd(), 'result')

    result = openpyxl.load_workbook(path + '/WEHAGO 결과 sample.xlsx')
    sheet = result.active

    # 엑셀의 함수명 열 리스트로 받기
    cellList = []
    col = sheet['D']
    for cell in col[:-2]:
        if service in cell.value:
            cellList.append(cell.value)
    return cellList

class WehagoRun_web :
    result = wehagoReport.WehagoResult()
    def message(self, browser) :
        print('message s')
        browser.get(getUrl('communication2/message/inbox'))
        time.sleep(5)
        funlist = serviceFunction('ms_')
        # pms, sms 같이 조회되서 제거,
        for i in funlist[:] :
            if 'pms_' in i or 'sms_' in i:
                funlist.remove(i)
        for fun in funlist :
            serviceRun(browser, wehagotest.Message(), fun)

    def accounts(self, browser) :
        print('accounts s')
        browser.get(getUrl('accounts'))
        time.sleep(5)
        funlist = serviceFunction('ac_')
        for fun in funlist :
            serviceRun(browser, wehagotest.Accounts(), fun)

    def contacts(self, browser) :
        print('contacts s')
        funlist = serviceFunction('ct_')
        browser.get(getUrl('contacts'))
        time.sleep(5)
        # pms 같이 조회되서 제거,
        for i in funlist[:] :
            if 'pms_' in i :
                funlist.remove(i)
        for fun in funlist :
            serviceRun(browser, wehagotest.Contacts(), fun)

    def schedule(self, browser) :
        print('schedule s')
        browser.get(getUrl('schedule'))
        time.sleep(5)
        funlist = serviceFunction('sc_')
        for fun in funlist :
            serviceRun(browser, wehagotest.Schedule(), fun)

    def communication(self, browser) :
        print('communication s')
        browser.get(getUrl('communication2'))
        time.sleep(5)
        funlist = serviceFunction('cc_')
        for fun in funlist :
            serviceRun(browser, wehagotest.Communication(), fun)

    def mail(self, browser) :
        print('mail s')
        browser.get(getUrl('mail'))
        time.sleep(5)
        funlist = serviceFunction('ma_')
        for fun in funlist :
            serviceRun(browser, wehagotest.Mail(), fun)

    def todo(self, browser) :
        print('todo s')
        browser.get(getUrl('todo', False))
        time.sleep(5)
        funlist = serviceFunction('td_')
        for fun in funlist :
            serviceRun(browser, wehagotest.Todo(), fun)

    def wecrm(self, browser) :
        print('wecrm s')
        browser.get(getUrl('wecrm'))
        time.sleep(5)
        funlist = serviceFunction('crm_')
        for fun in funlist :
            serviceRun(browser, wehagotest.Wecrm(), fun)

    def wepms(self, browser) :
        print('wepms s')
        browser.get(getUrl('wepms'))
        time.sleep(5)
        funlist = serviceFunction('pms_')
        for fun in funlist :
            serviceRun(browser, wehagotest.Wepms(), fun)

    def note(self, browser) :
        print('note s')
        browser.get(getUrl('note', False))
        time.sleep(5)
        funlist = serviceFunction('nt_')
        # 회사게시판 같이 조회되서 제거,
        for i in funlist[:] :
            if 'cb_' in i :
                funlist.remove(i)
        for fun in funlist :
            serviceRun(browser, wehagotest.Note(), fun)

    def approval(self, browser) :
        print('approval s')
        browser.get(getUrl('eapprovals'))
        time.sleep(5)
        funlist = serviceFunction('ap_')
        for fun in funlist :
            serviceRun(browser, wehagotest.Approval(), fun)

    def corporateCard(self, browser) :
        print('corporateCard s')
        browser.get(getUrl('expense'))
        time.sleep(5)
        funlist = (['cca_setAdminstor', 'cca_unsetAdminstor','cca_settingUse', 'cca_scraping', 'cca_expenseClaim', 'cca_requestApproval',
                    'cca_settingUnuse', 'ex_request', 'cca_expenseClaimRequest', 'ex_approve', 'ex_approveCancel', 'ex_reject', 'ex_rejectCancel', 'cca_returnCard'])
        for fun in funlist :
            if fun == 'ex_request' or fun == 'cca_expenseClaimRequest' :
                if wehagotest.wehagoBrand != 3 :
                    serviceRun(browser, wehagotest.CorporateCard(), fun)
            else :
                serviceRun(browser, wehagotest.CorporateCard(), fun)
        # serviceRun(browser, wehagotest.CorporateCard(), 'cca_setAdminstor')
        # serviceRun(browser, wehagotest.CorporateCard(), 'cca_unsetAdminstor')
        # serviceRun(browser, wehagotest.CorporateCard(), 'cca_settingUse')
        # serviceRun(browser, wehagotest.CorporateCard(), 'cca_scraping')
        # serviceRun(browser, wehagotest.CorporateCard(), 'cca_expenseClaim')
        # serviceRun(browser, wehagotest.CorporateCard(), 'cca_requestApproval')
        # serviceRun(browser, wehagotest.CorporateCard(), 'cca_settingUnuse')
        # if wehagotest.wehagoBrand != 3:
        #     serviceRun(browser, wehagotest.CorporateCard(), 'ex_request')
        #     serviceRun(browser, wehagotest.CorporateCard(), 'cca_expenseClaimRequest')
        # serviceRun(browser, wehagotest.CorporateCard(), 'ex_approve')
        # serviceRun(browser, wehagotest.CorporateCard(), 'ex_approveCancel')
        # serviceRun(browser, wehagotest.CorporateCard(), 'ex_reject')
        # serviceRun(browser, wehagotest.CorporateCard(), 'ex_rejectCancel')
        # serviceRun(browser, wehagotest.CorporateCard(), 'cca_returnCard')

    def personalCard(self, browser) :
        print('personalCard s')
        browser.get(getUrl('expensepersonalcard'))
        time.sleep(5)
        funlist = (['pca_settingUse', 'pca_scraping', 'pca_transmitExpenseClaim', 'pca_excludeDetails', 'pca_directInput', 'pca_expenseClaim',
                    'pca_requestApproval', 'ex_request', 'pca_settingUnuse', 'pca_expenseClaimRequest', 'ex_approve', 'ex_approveCancel', 'ex_reject', 'ex_rejectCancel'])
        for fun in funlist :
            serviceRun(browser, wehagotest.PersonalCard(), fun)
        # serviceRun(browser, wehagotest.PersonalCard(), 'pca_settingUse')
        # serviceRun(browser, wehagotest.PersonalCard(), 'pca_scraping')
        # serviceRun(browser, wehagotest.PersonalCard(), 'pca_transmitExpenseClaim')
        # serviceRun(browser, wehagotest.PersonalCard(), 'pca_excludeDetails')
        # serviceRun(browser, wehagotest.PersonalCard(), 'pca_directInput')
        # serviceRun(browser, wehagotest.PersonalCard(), 'pca_expenseClaim')
        # serviceRun(browser, wehagotest.PersonalCard(), 'pca_requestApproval')
        # serviceRun(browser, wehagotest.PersonalCard(), 'ex_request')
        # serviceRun(browser, wehagotest.PersonalCard(), 'pca_settingUnuse')
        # serviceRun(browser, wehagotest.PersonalCard(), 'pca_expenseClaimRequest')
        # serviceRun(browser, wehagotest.PersonalCard(), 'ex_approve')
        # serviceRun(browser, wehagotest.PersonalCard(), 'ex_approveCancel')
        # serviceRun(browser, wehagotest.PersonalCard(), 'ex_reject')
        # serviceRun(browser, wehagotest.PersonalCard(), 'ex_rejectCancel')

    def companyboard(self, browser) :
        print('companyboard s')
        browser.get(getUrl('companyboard', False))
        time.sleep(5)
        funlist = serviceFunction('cb_')
        for fun in funlist :
            serviceRun(browser, wehagotest.Companyboard(), fun)

    def meet(self, browser) :
        print('meet s')
        browser.get(getUrl('wehagomeet', False))
        time.sleep(5)
        funlist = serviceFunction('meet_')
        for fun in funlist :
            serviceRun(browser, wehagotest.Meet(), fun)

    def attendance(self, browser) :
        print('attendance s')
        browser.get(getUrl('attendance'))
        time.sleep(5)
        funlist = serviceFunction('at_')
        for fun in funlist :
            serviceRun(browser, wehagotest.Attendance(), fun)

    def invoice(self, browser) :
        print('invoice s')
        browser.get(getUrl('invoice'))
        time.sleep(5)
        # 전자세금 계산서
        funlist = serviceFunction('tax_')
        for fun in funlist :
            serviceRun(browser, wehagotest.Invoice(), fun)

        # 거래명세서
        funlist = serviceFunction('tr_')
        for fun in funlist :
            serviceRun(browser, wehagotest.Invoice(), fun)

        # 입금표
        funlist = serviceFunction('de_')
        for fun in funlist :
            serviceRun(browser, wehagotest.Invoice(), fun)
        # 영수증
        funlist = serviceFunction('re_')
        for fun in funlist :
            serviceRun(browser, wehagotest.Invoice(), fun)

    def fax(self, browser) :
        print('fax s')
        funlist = serviceFunction('fax_')
        browser.get(getUrl('fax'))
        time.sleep(5)
        for fun in funlist :
            serviceRun(browser, wehagotest.Fax(), fun)

    def sms(self, browser) :
        print('sms s')
        browser.get(getUrl('sms'))
        time.sleep(5)
        funlist = serviceFunction('sms_')
        for fun in funlist :
            serviceRun(browser, wehagotest.Sms(), fun)

    def westudio(self, browser) :
        print('westudio s')
        browser.get('https://www.wehago.com/westudio')
        time.sleep(5)
        funlist = serviceFunction('ws_')
        for fun in funlist :
            serviceRun(browser, wehagotest.WeStudio(), fun)

    def webot(self, browser) :
        # 위봇 확인필요
        print('webot s')
        browser.get(getUrl('webot', False))
        time.sleep(5)
        funlist = serviceFunction('wb_')
        guestbrowser = chromeBrowser()
        for fun in funlist :
            if fun == 'wb_user' or fun == 'wb_userSendMessage' :
                serviceRun(guestbrowser, wehagotest.Webot(), fun)
            else :
                serviceRun(browser, wehagotest.Webot(), fun)
        guestbrowser.quit()

    def wehagoRun(self, browser, id, version, brand) :
        wehagotest.Common().set_wehagoBrand(version, brand)
        #로그인 테스트
        wehagotest.Login().login(browser, id)
        #메시지 테스트
        if serviceTest['message'] : self.message(browser)
        #거래처 테스트
        if serviceTest['accounts'] : self.accounts(browser)
        #연락처 테스트
        if serviceTest['contacts'] : self.contacts(browser)
        #일정 테스트
        if serviceTest['schedule'] : self.schedule(browser)
        #메신저 테스트
        if serviceTest['communication'] : self.communication(browser)
        #메일 테스트
        if serviceTest['mail'] : self.mail(browser)
        #할일 테스트
        if serviceTest['todo'] : self.todo(browser)
        #CRM 테스트
        if serviceTest['wecrm'] : self.wecrm(browser)
        #PMS 테스트
        if serviceTest['wepms'] : self.wepms(browser)
        #노트 테스트
        if serviceTest['note'] : self.note(browser)
        #전자결재 테스트
        if serviceTest['approval'] : self.approval(browser)
        #법인카드 테스트
        if serviceTest['corporateCard'] : self.corporateCard(browser)
        #개인카드 테스트
        if serviceTest['personalCard'] : self.personalCard(browser)
        #근태관리 테스트
        if serviceTest['attendance'] : self.attendance(browser)
        #회사게시판 테스트
        if serviceTest['companyboard'] : self.companyboard(browser)
        # 화상회의 테스트
        if serviceTest['meet'] : self.meet(browser)
        # # 다른 사용자 테스트
        # if serviceTest['other'] : UserCheck().userCheck(browser, version)
        self.invoiceRun(browser, version)
        self.result.savexl(version)

    def invoiceRun(self, browser, version) :
        if version == 2 or version == 3:
            wehagotest.Login().logout(browser)
            wehagotest.Login().login(browser, 'iqatest')
            if serviceTest['invoice'] : self.invoiceUpdate(browser)
        else :
            # 전자세금계산서 테스트
            if serviceTest['invoice'] : self.invoice(browser)
        # 팩스 테스트
        if serviceTest['fax'] : self.fax(browser)
        # 문자 테스트
        if serviceTest['sms'] : self.sms(browser)
        # WEstudio 테스트
        if serviceTest['westudio'] : self.westudio(browser)
        # 위봇 테스트
        if serviceTest['webot'] : self.webot(browser)

    # 회원가입~가입완료
    def wehagoJoinRun(self, browser, id, name, pay) :
        # wehago 회원가입
        wehagotest.Join().wehagoJoin(browser, id, name, pay)
        # 초기설정 진행
        wehagotest.Plan().plan(browser, pay, name)
        # 마켓 구매
        service = {'법인카드':'구매O', '개인카드':'구매O', '할일':'구매O', 'WE CRM':'구매O', 'WE PMS':'구매O','근태관리':'구매O', '전자결재':'구매O'}
        wehagotest.Market().market(browser, pay, name, service)
        # 정기결제 수단 등록, 도메인 구매, 직원초대
        CompanyRun().companySetting(browser)
        # # qatest123으로 가입
        # wehagotest.Join().employeeJoin(wehago)

    # 초기설정 팝업 노출되는 부분 작업
    def wehagoSetting(self, browser, id, version, brand) :
        wehagotest.Common().set_wehagoBrand(version, brand)
        #로그인 테스트
        wehagotest.Login().login(browser, id)
        try:
            # 개인설정 - 기본이메일 수정
            wehagotest.Personal().pe_setMail(browser, id)
        except: pass
        try :
            #회사설정 (서비스배포, 관리자권한 부여)
            CompanyRun().company(browser)
        except: pass
        try:
            #PMS 테스트 (초기설정 팝업창 입력)
            WepmsRun().wepmsSetting(browser)
        except: pass
        try:
            #CRM 테스트 (초기설정 팝업창 입력)
            WecrmRun().wecrmSetting(browser)
        except: pass
        try:
            #전자결재 자주쓰는 결재 등록
            ApprovalRun().approvalSetting(browser)
        except: pass
        try:
            #법인카드 등록
            CorporateCardRun().corporateCardSetting(browser)
        except: pass
        try:
            #개인카드 카드등록
            PersonalCardRun().personalCardSetting(browser)
        except: pass
        try:
            #근태관리 직원휴가일설정
            AttendanceRun().attendanceSetting(browser)
        except : pass
        wehagotest.Login().logout(browser)
        print('logout s')
        time.sleep(3)

class WehagoRun_Mobile :
    # 앱 없는 것은 일단 제외
    # todo, crm, pms, note, cca, pca, attendance, invoice, fax, sms
    result = wehagoReport.WehagoResult()
    def message(self, browser) :
        print('message s')
        funlist = serviceFunction('ms_')
        # pms, sms 같이 조회되서 제거,
        for i in funlist[:] :
            if 'pms_' in i or 'sms_' in i:
                funlist.remove(i)
        for fun in funlist :
            serviceRun(browser, Android.Message(), fun)

    def accounts(self, browser) :
        print('accounts s')
        funlist = serviceFunction('ac_')
        for fun in funlist :
            serviceRun(browser, Android.Accounts(), fun)

    def contacts(self, browser) :
        print('contacts s')
        funlist = serviceFunction('ct_')
        # pms 같이 조회되서 제거,
        for i in funlist[:] :
            if 'pms_' in i :
                funlist.remove(i)
        for fun in funlist :
            serviceRun(browser, Android.Contacts(), fun)

    def schedule(self, browser) :
        print('schedule s')
        funlist = serviceFunction('sc_')
        for fun in funlist :
            serviceRun(browser, Android.Schedule(), fun)

    def communication(self, browser) :
        print('communication s')
        funlist = serviceFunction('cc_')
        for fun in funlist :
            serviceRun(browser, Android.Communication(), fun)

    def mail(self, browser) :
        print('mail s')
        funlist = serviceFunction('ma_')
        for fun in funlist :
            serviceRun(browser, Android.Mail(), fun)

    def approval(self, browser) :
        print('approval s')
        funlist = serviceFunction('ap_')
        for fun in funlist :
            serviceRun(browser, Android.Approval(), fun)

    def meet(self, browser) :
        print('meet s')
        funlist = serviceFunction('meet_')
        for fun in funlist :
            serviceRun(browser, Android.Meet(), fun)

    def wehagoRun(self, browser, id) :
        #로그인 테스트
        Android.login(browser, id)
        #메시지 테스트
        self.message(browser)
        #거래처 테스트
        self.accounts(browser)
        #연락처 테스트
        self.contacts(browser)
        #일정 테스트
        self.schedule(browser)
        #메신저 테스트
        self.communication(browser)
        #메일 테스트
        self.mail(browser)
        #전자결재 테스트
        self.approval(browser)
        # 화상회의 테스트
        self.meet(browser)
        # #메시지 테스트
        # if serviceTest['message'] : self.message(browser)
        # #거래처 테스트
        # if serviceTest['accounts'] : self.accounts(browser)
        # #연락처 테스트
        # if serviceTest['contacts'] : self.contacts(browser)
        # #일정 테스트
        # if serviceTest['schedule'] : self.schedule(browser)
        # #메신저 테스트
        # if serviceTest['communication'] : self.communication(browser)
        # #메일 테스트
        # if serviceTest['mail'] : self.mail(browser)
        # #전자결재 테스트
        # if serviceTest['approval'] : self.approval(browser)
        # # 화상회의 테스트
        # if serviceTest['meet'] : self.meet(browser)
        # # 다른 사용자 테스트
        # if serviceTest['other'] : UserCheck().userCheck(browser, version)