from typing import Tuple
import wehagotest
import wehagoReport
import datetime, os, time, sys
from driver import chromeBrowser, serviceTest, browser_click
import openpyxl
from wehagotest import getUrl

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

def browserTitle (browser, title) :
    if title in browser.title :
        return True
    else :
        return False

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
    def dev_message(self, browser) :
        print('message s')
        browser.get(getUrl('communication2/message/inbox', 0))
        time.sleep(5)
        funlist = ['ms_sendImportantMessage', 'ms_searchMessage', 'ms_deleteReceiveMessage']
        for fun in funlist :
            serviceRun(browser, wehagotest.Message(), fun)

    def message(self, browser) :
        print('message s')
        browser.get(getUrl('communication2/message/inbox', 1))
        time.sleep(5)
        funlist = (['ms_sendMessage', 'ms_sendSecurityMessage', 'ms_addBoilerplate', 'ms_applyBoilerplate', 'ms_readBoilerplate',
                    'ms_delBoilerplate','ms_sendImportantMessage', 'ms_sendReservationMessage', 'ms_resendMessage', 'ms_replyAllMessage',
                    'ms_replyMessage', 'ms_forwardMessage', 'ms_readMessageAll', 'ms_readSecurityMessage', 'ms_searchMessage', 'ms_bookmark',
                    'ms_deleteReceiveMessage', 'ms_deleteSendMessage'])
        for fun in funlist :
            serviceRun(browser, wehagotest.Message(), fun)

    def dev_accounts(self, browser) :
        print('accounts s')
        browser.get(getUrl('accounts', 0))
        time.sleep(5)
        funlist = ['ac_registAccount', 'ac_deleteAccount']
        for fun in funlist :
            serviceRun(browser, wehagotest.Accounts(), fun)

    def accounts(self, browser) :
        print('accounts s')
        browser.get(getUrl('accounts', 1))
        time.sleep(5)
        funlist = ['ac_createGroup', 'ac_registAccount', 'ac_modifyAccount', 'ac_deleteAccount', 'ac_deleteGroup', 'ac_createSharedGroup', 'ac_deleteSharedGroup']
        for fun in funlist :
            serviceRun(browser, wehagotest.Accounts(), fun)

    def dev_contacts(self, browser) :
        print('contacts s')
        browser.get(getUrl('contacts', 0))
        time.sleep(5)
        funlist = ['ct_registerContacts', 'ct_contactImport', 'ct_organizeContact', 'ct_deleteGroup']
        # 전화 수락, 거절 보류
        for fun in funlist :
            serviceRun(browser, wehagotest.Contacts(), fun)

    def contacts(self, browser) :
        print('contacts s')
        browser.get(getUrl('contacts', 1))
        time.sleep(5)
        # 'ct_agreeVoiceCall', 'ct_refuseVoiceCall', 'ct_agreeVideoCall', 'ct_refuseVideoCall'
        funlist = (['ct_deleteContact', 'ct_registerContacts', 'ct_bookmarkContact', 'ct_modifyContact', 'ct_createGroup',
                   'ct_modifyGroup', 'ct_createSharedGroup', 'ct_modifySharedGroup', 'ct_contactImport', 'ct_organizeContact', 'ct_deleteGroup',
                    'ct_deleteSharedGroup'])
        # 전화 수락, 거절 보류
        for fun in funlist :
            serviceRun(browser, wehagotest.Contacts(), fun)

    def dev_schedule(self, browser) :
        print('schedule s')
        browser.get(getUrl('schedule', 0))
        time.sleep(5)
        funlist = ['sc_deleteSchedule', 'sc_createSharedCalendar', 'sc_deleteCalendar', 'sc_registerSchedule']
        for fun in funlist :
            serviceRun(browser, wehagotest.Schedule(), fun)

    def schedule(self, browser) :
        print('schedule s')
        browser.get(getUrl('schedule', 1))
        time.sleep(5)
        funlist = (['sc_deleteSchedule', 'sc_createCalendar', 'sc_createSharedCalendar', 'sc_modifyCalendar', 'sc_dragCalender', 'sc_deleteCalendar',
                   'sc_registerSchedule', 'sc_addComment', 'sc_clickCalendar', 'sc_searchSchedule'])
        for fun in funlist :
            serviceRun(browser, wehagotest.Schedule(), fun)

    def dev_communication(self, browser) :
        print('communication s')
        browser.get(getUrl('communication2', 0))
        time.sleep(5)
        # cc_addNotice 제외
        funlist = ['cc_leaveChatRoom', 'cc_createRoomByOrganization', 'cc_sendChat', 'cc_searchMention']
        for fun in funlist :
            serviceRun(browser, wehagotest.Communication(), fun)

    def communication(self, browser) :
        print('communication s')
        browser.get(getUrl('communication2', 1))
        time.sleep(5)
        # cc_addNotice 제외
        funlist = (['cc_acceptParticipation', 'cc_acceptInvitedUser', 'cc_refusalParticipation', 'cc_exportUser', 'cc_leaveChatRoom', 'cc_createRoomByContacts',
                    'cc_createRoomByInput', 'cc_createRoomByOrganization', 'cc_sendChat', 'cc_deleteChat', 'cc_copyChat', 'cc_addComment', 'cc_uploadLocal',
                    'cc_uploadWedrive','cc_uploadFileTab', 'cc_collectFile', 'cc_openWebOffice', 'cc_appendingSchedule', 'cc_appendingAccount', 'cc_appendingContact', 'cc_appendingMeet',
                    'cc_appendingVote', 'cc_listVote', 'cc_recentChat', 'cc_searchChat', 'cc_sharedChat', 'cc_settingGroup', 'cc_favoriteConversation',
                    'cc_unfavoriteConversation', 'cc_searchMention', 'cc_checkUserProfile', 'cc_setAsMaster', 'cc_createChat', 'cc_leaveChat'])
        for fun in funlist :
            serviceRun(browser, wehagotest.Communication(), fun)

    def dev_mail(self, browser) :
        print('mail s')
        browser.get(getUrl('mail', 0))
        time.sleep(5)
        funlist = ['ma_deleteMail', 'ma_sendMailWedrive', 'ma_replyMail']
        for fun in funlist :
            serviceRun(browser, wehagotest.Mail(), fun)

    def mail(self, browser) :
        print('mail s')
        browser.get(getUrl('mail', 1))
        time.sleep(5)
        # 'ma_addExternalMail', 'ma_externalMailLinkEtc' 제외
        funlist = (['ma_deleteMail', 'ma_emptyTrash', 'ma_sendReservedMail', 'ma_sendSecureMail', 'ma_sendMail', 'ma_sendMailWedrive', 'ma_sendMailLocalWedrive',
                    'ma_temporarySave', 'ma_replyMail', 'ma_replyMail', 'ma_deliveryMail', 'ma_automaticClassification', 'ma_deleteAutomatic'])
        for fun in funlist :
            serviceRun(browser, wehagotest.Mail(), fun)

    def dev_todo(self, browser) :
        print('todo s')
        browser.get(getUrl('todo', 0, False))
        time.sleep(5)
        funlist = ['td_deleteProject', 'td_createProject', 'td_createTodo', 'td_addComment', 'td_completeTodo']
        for fun in funlist :
            serviceRun(browser, wehagotest.Todo(), fun)

    def todo(self, browser) :
        print('todo s')
        browser.get(getUrl('todo', 1, False))
        time.sleep(5)
        funlist = ['td_deleteProject', 'td_createProject', 'td_modifyProject', 'td_createBoard', 'td_deleteBoard', 'td_createTodo', 'td_addComment', 'td_completeTodo', 'td_searchTodo', 'td_deleteTodo']
        for fun in funlist :
            serviceRun(browser, wehagotest.Todo(), fun)

    def dev_wecrm(self, browser) :
        print('wecrm s')
        browser.get(getUrl('wecrm', 0))
        time.sleep(5)
        funlist = ['crm_deleteSales', 'crm_registerGoods', 'crm_issueManagement']
        # 프로젝트 삭제 후
        for fun in funlist :
            serviceRun(browser, wehagotest.Wecrm(), fun)

    def wecrm(self, browser) :
        print('wecrm s')
        browser.get(getUrl('wecrm', 1))
        time.sleep(5)
        funlist = (['crm_settingUnuse', 'crm_settingUse', 'crm_deleteSales', 'crm_deleteAccounts', 'crm_registerAccounts', 'crm_registerOpportunity', 'crm_opportunity',
                    'crm_registerGoods', 'crm_addContactPerson', 'crm_deleteContactPerson', 'crm_issueManagement', 'crm_addGoals', 'crm_copyGoals', 'crm_delGoals'])
        # 프로젝트 삭제 후
        for fun in funlist :
            serviceRun(browser, wehagotest.Wecrm(), fun)

    def dev_wepms(self, browser) :
        print('wepms s')
        browser.get(getUrl('wepms', 0))
        time.sleep(5)
        funlist = ['pms_deleteProject', 'pms_registerCrmProject', 'pms_registerInternalProject', 'pms_budget']
        for fun in funlist :
            serviceRun(browser, wehagotest.Wepms(), fun)

    def wepms(self, browser) :
        print('wepms s')
        browser.get(getUrl('wepms', 1))
        time.sleep(5)
        funlist = (['pms_delBudgetExecution', 'pms_delUse','pms_deleteProjectType','pms_settingUnuse', 'pms_deleteProject', 'pms_settingUse', 'pms_addUse', 'pms_addProjectType',
                    'pms_registerCrmProject_new', 'pms_registerExternalProject_new', 'pms_registerInternalProject_new', 'pms_registerCrmProject', 'pms_registerExternalProject',
                    'pms_registerInternalProject', 'pms_manpower', 'pms_schedulePlan', 'pms_budget', 'pms_budgetExecution', 'pms_createIssue', 'pms_usercreateIssue', 'pms_userProjectManamger'])
        for fun in funlist :
            serviceRun(browser, wehagotest.Wepms(), fun)

    def dev_note(self, browser) :
        print('note s')
        browser.get(getUrl('note', 0, False))
        time.sleep(5)
        funlist = ['nt_createSharedSpace', 'nt_deleteSharedSpace', 'nt_createNote', 'nt_deleteNote', 'nt_emptyTrash']
        for fun in funlist :
            serviceRun(browser, wehagotest.Note(), fun)

    def note(self, browser) :
        print('note s')
        browser.get(getUrl('note', 1, False))
        time.sleep(5)
        funlist = ['nt_createSharedSpace', 'nt_deleteSharedSpace', 'nt_createNote', 'nt_deleteNote', 'nt_emptyTrash']
        for fun in funlist :
            serviceRun(browser, wehagotest.Note(), fun)

    def dev_approval(self, browser) :
        print('approval s')
        browser.get(getUrl('eapprovals', 0))
        time.sleep(5)
        funlist = ['ap_approval', 'ap_reApproval', 'ap_modifyApproval', 'ap_approve', 'ap_reject', 'ap_enforcement']
        # 전자결재 세팅 보류
        for fun in funlist :
            serviceRun(browser, wehagotest.Approval(), fun)

    def approval(self, browser) :
        print('approval s')
        browser.get(getUrl('eapprovals', 1))
        time.sleep(5)
        funlist = (['ap_basicset', 'ap_settingType', 'ap_settingUse', 'ap_settingUnuse', 'ap_deleteApprove', 'ap_approval', 'ap_reApproval', 'ap_modifyApproval', 'ap_createArchive',
                    'ap_approveDocumentArchive', 'ap_moveDocumentArchive', 'ap_deleteArchive', 'ap_approve', 'ap_reject', 'ap_enforcement', 'ap_postApproval', 'ap_preApproval',
                    'ap_addDocumentForm','ap_approvebyUser', 'ap_rejectbyUser', 'ap_deleteDocumentForm'])
        # 전자결재 세팅 보류
        del funlist[2:4]
        for fun in funlist :
            serviceRun(browser, wehagotest.Approval(), fun)

    def dev_corporateCard(self, browser) :
        print('corporateCard s')
        browser.get(getUrl('expense', 0))
        time.sleep(5)
        funlist = ['cca_scraping', 'cca_expenseClaim', 'cca_requestApproval', 'cca_returnCard']
        for fun in funlist :
            serviceRun(browser, wehagotest.CorporateCard(), fun)

    def corporateCard(self, browser) :
        print('corporateCard s')
        browser.get(getUrl('expense', 1))
        time.sleep(5)
        funlist = (['cca_setAdminstor', 'cca_unsetAdminstor','cca_settingUse', 'cca_scraping', 'cca_expenseClaim', 'cca_requestApproval',
                    'cca_settingUnuse', 'ex_request', 'cca_expenseClaimRequest', 'ex_approve', 'ex_approveCancel', 'ex_reject', 'ex_rejectCancel', 'cca_returnCard'])
        for fun in funlist :
            if fun == 'ex_request' or fun == 'cca_expenseClaimRequest' :
                if wehagotest.wehagoBrand != 3 :
                    serviceRun(browser, wehagotest.CorporateCard(), fun)
            else :
                serviceRun(browser, wehagotest.CorporateCard(), fun)

    def dev_personalCard(self, browser) :
        print('personalCard s')
        browser.get(getUrl('expensepersonalcard', 0))
        time.sleep(5)
        funlist = ['pca_scraping', 'pca_directInput', 'pca_expenseClaim', 'pca_requestApproval', 'ex_approve', 'ex_approveCancel', 'ex_reject', 'ex_rejectCancel']
        for fun in funlist :
            serviceRun(browser, wehagotest.PersonalCard(), fun)

    def personalCard(self, browser) :
        print('personalCard s')
        browser.get(getUrl('expensepersonalcard', 1))
        time.sleep(5)
        funlist = (['pca_settingUse', 'pca_scraping', 'pca_transmitExpenseClaim', 'pca_excludeDetails', 'pca_directInput','pca_expenseClaim',
                    'pca_requestApproval', 'ex_request', 'pca_settingUnuse', 'pca_expenseClaimRequest', 'ex_approve', 'ex_approveCancel', 'ex_reject', 'ex_rejectCancel'])
        for fun in funlist :
            serviceRun(browser, wehagotest.PersonalCard(), fun)

    def dev_companyboard(self, browser):
        print('companyboard s')
        browser.get(getUrl('companyboard', 0, False))
        time.sleep(5)
        funlist = ['cb_createBoard', 'cb_createPost_blog', 'cb_comment_blog', 'cb_removeBoard']
        for fun in funlist:
            serviceRun(browser, wehagotest.Companyboard(), fun)

    def companyboard(self, browser) :
        print('companyboard s')
        browser.get(getUrl('companyboard', 1, False))
        time.sleep(5)
        funlist = (['cb_createBoard', 'cb_createPost_basic', 'cb_comment_basic', 'cb_modifyPost', 'cb_deletePost', 'cb_createPost_blog', 'cb_comment_blog',
                    'cb_createPost_gall', 'cb_comment_gall', 'cb_createPost_feed', 'cb_comment_feed', 'cb_removeBoard'])
        for fun in funlist :
            serviceRun(browser, wehagotest.Companyboard(), fun)

    def dev_meet(self, browser) :
        print('meet s')
        browser.get(getUrl('wehagomeet', 0, False))
        time.sleep(5)
        funlist = ['meet_createMeeting', 'meet_createReservedMeeting', 'meet_reservationcancel']
        for fun in funlist :
            serviceRun(browser, wehagotest.Meet(), fun)

    def meet(self, browser) :
        print('meet s')
        browser.get(getUrl('wehagomeet', 1, False))
        time.sleep(5)
        funlist = (['meet_createMeeting', 'meet_inviteMail', 'meet_chatting', 'meet_exportUser', 'meet_documentShare', 'meet_externalSharing',
                    'meet_createReservedMeeting', 'meet_reservedList', 'meet_modifyReservationMeeting', 'meet_reservationcancel'])
        for fun in funlist :
            serviceRun(browser, wehagotest.Meet(), fun)

    def dev_attendance(self, browser) :
        print('attendance s')
        browser.get(getUrl('attendance', 0))
        time.sleep(5)
        funlist = ['at_settingWorkingGroup', 'at_assignmentWorkingGroup', 'at_vacationApplication', 'at_vacationApplicationCancel', 'at_deleteWorkingGroup']
        for fun in funlist :
            serviceRun(browser, wehagotest.Attendance(), fun)

    def attendance(self, browser) :
        print('attendance s')
        browser.get(getUrl('attendance', 1))
        time.sleep(5)
        funlist = (['at_settingWorkingGroup', 'at_assignmentWorkingGroup', 'at_settingWorkingPlace', 'at_assignmentWorkingPlace', 'at_addAttendanceItem',
                    'at_deleteAttendanceItem', 'at_vacationApplication', 'at_vacationApplicationCancel', 'at_deleteWorkingGroup', 'at_deleteWorkingPlace', 'at_registerholiday',
                    'at_deleteHoliday', 'at_authorization', 'at_deauthorization'])
        for fun in funlist :
            serviceRun(browser, wehagotest.Attendance(), fun)

    def dev_invoice(self, browser) :
        print('invoice s')
        browser.get(getUrl('invoice', 0))
        time.sleep(5)
        funlist = ['tax_formTaxation', 'tr_simpleTaxation', 'de_listPublish', 're_detailPublish']
        for fun in funlist :
            serviceRun(browser, wehagotest.InvoicePublish(), fun)

    def invoice(self, browser) :
        print('invoice s')
        browser.get(getUrl('invoice', 1))
        time.sleep(5)
        # 전자세금 계산서
        funlist = (['tax_todayDeleteBtn', 'tax_savedDeleteBtn', 'tax_formTaxation', 'tax_formTaxationReverse', 'tax_formListTaxSmall', 'tax_formListTaxSmallReverse', 'tax_formDetailTaxFree', 'tax_formDetailTaxFreeReverse',
                    'tax_simpleTaxation', 'tax_simpleTaxationReverse', 'tax_simpleListTaxSmall', 'tax_simpleListTaxSmallReverse', 'tax_simpleDetailTaxFree', 'tax_simpleDetailTaxFreeReverse',
                    'tax_modifyInvoice_detail', 'tax_modifyInvoice_list', 'tax_modifyInvoice_approval'])
        for fun in funlist :
            serviceRun(browser, wehagotest.InvoicePublish(), fun)

        # 거래명세서
        funlist = (['tr_formTaxation', 'tr_formTaxationReverse', 'tr_formListTaxSmall', 'tr_formListTaxSmallReverse', 'tr_formDetailTaxFree', 'tr_formDetailTaxFreeReverse',
                    'tr_attachmentTaxation', 'tr_attachmentTaxationReverse', 'tr_attachmentListTaxSmall', 'tr_attachmentListTaxSmallReverse', 'tr_attachmentDetailTaxFree',
                    'tr_attachmentDetailTaxFreeReverse', 'tr_simpleTaxation', 'tr_simpleTaxationReverse'])
        for fun in funlist :
            serviceRun(browser, wehagotest.InvoicePublish(), fun)

        # 입금표
        funlist = (['de_formPublish', 'de_listPublish', 'de_detailPublish', 'de_simplePublish'])
        for fun in funlist :
            serviceRun(browser, wehagotest.InvoicePublish(), fun)
        # 영수증
        funlist = (['re_formPublish', 're_listPublish', 're_detailPublish', 're_simplePublish'])
        for fun in funlist :
            serviceRun(browser, wehagotest.InvoicePublish(), fun)

    def invoiceUpdate(self, browser) :
        print('invoice s')
        browser.get(getUrl('invoice', 1))
        time.sleep(5)
        funlist = ['tax_formTaxation', 'tax_formListTaxSmallReverse', 'tax_formDetailTaxFree', 'tax_simpleTaxationReverse', 'tax_simpleListTaxSmall', 'tax_simpleDetailTaxFreeReverse', 'tax_modifyInvoice_detail',
                   'tr_formTaxation', 'tr_formListTaxSmallReverse', 'tr_formDetailTaxFree', 'tr_attachmentTaxationReverse', 'tr_attachmentListTaxSmall', 'tr_attachmentDetailTaxFreeReverse', 'tr_simpleTaxation',
                   'de_listPublish', 'de_detailPublish', 're_listPublish', 're_detailPublish']
        for fun in funlist :
            serviceRun(browser, wehagotest.InvoicePublish(), fun)

    def fax(self, browser) :
        print('fax s')
        funlist = ['fax_quickSendFax', 'fax_generalSendFax', 'fax_deleteFax']
        browser.get(getUrl('fax', wehagotest.dev))
        time.sleep(5)
        for fun in funlist :
            serviceRun(browser, wehagotest.Fax(), fun)

    def sms(self, browser) :
        print('sms s')
        browser.get(getUrl('sms', wehagotest.dev))
        time.sleep(5)
        funlist = ['sms_sendText', 'sms_sendExcel', 'sms_sendIndividualText']
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
        browser.get(getUrl('webot', wehagotest.dev, False))
        time.sleep(5)
        funlist = (['wb_user', 'wb_userSendMessage', 'wb_counselorConnection', 'wb_counselorHolding', 'wb_counselorClose', 'wb_counselorSendMessage',
                    'wb_counselorSearch', 'wb_addBrand', 'wb_deleteBrand', 'wb_addTemplate', 'wb_deleteTemplate'])
        guestbrowser = chromeBrowser()
        for fun in funlist :
            if fun == 'wb_user' or fun == 'wb_userSendMessage' :
                serviceRun(guestbrowser, wehagotest.Webot(), fun)
            else :
                serviceRun(browser, wehagotest.Webot(), fun)
        guestbrowser.quit()

    def userCheck(self, browser, version) :
        print('user B')
        funlist = (['ot_deleteNote', 'ot_deleteMail', 'ot_deleteMessage', 'ot_checkUserCreateIssue', 'ot_checkUserProjectManager', 'ot_checkPostApproval',
                   'ot_checkTodoAddBoard', 'ot_checkTodoDeleteBoard', 'ot_participationChat', 'ot_addUserChat'])
        wehagotest.Other().ot_login(browser, version)
        for fun in funlist :
            serviceRun(browser, wehagotest.Other(), fun)

    def dev_wehagoRun(self, browser, id, version, brand) :
        # 개발기
        wehagotest.Common().set_wehagoBrand(version, brand, 0)
        #로그인 테스트
        wehagotest.Login().login(browser, id)
        # 메시지 테스트
        if serviceTest['message'] : self.dev_message(browser)
        #거래처 테스트
        if serviceTest['accounts'] : self.dev_accounts(browser)
        #연락처 테스트
        if serviceTest['contacts'] : self.dev_contacts(browser)
        #일정 테스트
        if serviceTest['schedule'] : self.dev_schedule(browser)
        #메신저 테스트
        if serviceTest['communication'] : self.dev_communication(browser)
        #메일 테스트
        if serviceTest['mail'] : self.dev_mail(browser)
        #할일 테스트
        if serviceTest['todo'] : self.dev_todo(browser)
        #CRM 테스트
        if serviceTest['wecrm'] : self.dev_wecrm(browser)
        #PMS 테스트
        if serviceTest['wepms'] : self.dev_wepms(browser)
        #노트 테스트
        if serviceTest['note'] : self.dev_note(browser)
        #전자결재 테스트
        if serviceTest['approval'] : self.dev_approval(browser)
        #법인카드 테스트
        if serviceTest['corporateCard'] : self.dev_corporateCard(browser)
        #개인카드 테스트
        if serviceTest['personalCard'] : self.dev_personalCard(browser)
        #근태관리 테스트
        if serviceTest['attendance'] : self.dev_attendance(browser)
        #회사게시판 테스트
        if serviceTest['companyboard'] : self.dev_companyboard(browser)
        # 화상회의 테스트
        if serviceTest['meet'] : self.dev_meet(browser)
        # 전자세금계산서 테스트
        if serviceTest['invoice']: self.dev_invoice(browser)
        self.result.savexl(version)

    def wehagoRun(self, browser, id, version, brand) :
        # 운영기
        wehagotest.Common().set_wehagoBrand(version, brand, 1)
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
        # 다른 사용자 테스트
        if serviceTest['other'] : self.userCheck(browser, version)
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
        wehagotest.Company().cs_addEmpolyee(browser)
        # # qatest123으로 가입
        # wehagotest.Join().employeeJoin(wehago)

    def companySetting(self, browser) :
        print('company s')
        browser.get(getUrl('company/management/info', wehagotest.dev))
        time.sleep(5)
        wehagotest.Company().cs_distribution(browser)
        wehagotest.Company().cs_setAdministor(browser)

    def wepmsSetting(self, browser) :
        print('wepms s')
        browser.get(getUrl('wepms', wehagotest.dev))
        time.sleep(5)
        wehagotest.Wepms().pms_basicset(browser)

    def wecrmSetting(self, browser) :
        print('wecrm s')
        browser.get(getUrl('wecrm', wehagotest.dev))
        time.sleep(5)
        wehagotest.Wecrm().crm_basicset(browser)

    def approvalSetting(self, browser) :
        print('approval s')
        browser.get(getUrl('eapprovals', wehagotest.dev))
        time.sleep(5)
        wehagotest.Approval().ap_basicset(browser)
        wehagotest.Approval().ap_settingType(browser)

    def corporateCardSetting(self, browser) :
        print('corporateCard s')
        browser.get(getUrl('expense', wehagotest.dev))
        time.sleep(5)
        wehagotest.CorporateCard().cca_clause(browser)
        wehagotest.CorporateCard().cca_cardRegist(browser)

    def personalCardSetting(self, browser) :
        print('personalCard s')
        browser.get(getUrl('expensepersonalcard', wehagotest.dev))
        time.sleep(5)
        wehagotest.PersonalCard().pca_clause(browser)
        wehagotest.PersonalCard().pca_addManager(browser)
        wehagotest.PersonalCard().pca_cardRegist(browser)

    def attendanceSetting(self, browser) :
        print('attendance s')
        browser.get(getUrl('attendance', wehagotest.dev))
        time.sleep(5)
        wehagotest.Attendance().at_settingVacation(browser)

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
            self.companySetting(browser)
        except: pass
        try:
            #PMS 테스트 (초기설정 팝업창 입력)
            self.wepmsSetting(browser)
        except: pass
        try:
            #CRM 테스트 (초기설정 팝업창 입력)
            self.wecrmSetting(browser)
        except: pass
        try:
            #전자결재 자주쓰는 결재 등록
            self.approvalSetting(browser)
        except: pass
        try:
            #법인카드 등록
            self.corporateCardSetting(browser)
        except: pass
        try:
            #개인카드 카드등록
            self.personalCardSetting(browser)
        except: pass
        try:
            #근태관리 직원휴가일설정
            self.attendanceSetting(browser)
        except : pass
        wehagotest.Login().logout(browser)
        print('logout s')
        time.sleep(3)
""" 
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
        funlist = ['ac_registAccount', 'ac_modifyAccount', 'ac_deleteAccount', 'ac_createGroup', 'ac_deleteGroup', 'ac_createSharedGroup', 'ac_deleteSharedGroup']
        for fun in funlist :
            serviceRun(browser, Android.Accounts(), fun)

    def contacts(self, browser) :
        print('contacts s')
        funlist = (['ct_registerContacts', 'ct_addpeople', 'ct_createGroup', 'ct_modifyGroup', 'ct_deleteGroup ', 'ct_createSharedGroup', 'ct_modifySharedGroup',
                   'ct_deleteSharedGroup', 'ct_contactExport', 'ct_contactImport', 'ct_organizeContact', 'ct_LinkSetting', 'ct_autosaveOnOff'])
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
        funlist = (['ma_sendMail', 'ma_sendReservedMail', 'ma_sendSecureMail', 'ma_temporarySave', 'ma_individualTransfer', 'ma_sendMailWedrive', 'ma_replyMail',
                    'ma_replyMailAll', 'ma_deliveryMail', 'ma_readProcessing', 'ma_deleteMail', 'ma_emptyTrash'])
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
        self.result.savexl(1)

class WehagoRun_Nahago :
    result = wehagoReport.WehagoResult()
    def communication(self, browser) :
        print('communication s')
        funlist = serviceFunction('ms_')
        # pms, sms 같이 조회되서 제거,
        funlist = ['cc_createGroupChat', 'cc_leaveGroupChat', 'cc_sendChat', 'cc_bookmarkChat', 'cc_createChat', 'cc_leaveChat']
        browser_click(browser, '//android.widget.TextView[@text = "채팅"]')
        time.sleep(3)
        # for fun in funlist :
        #     serviceRun(browser, nahago.Communication(), fun)
        serviceRun(browser, nahago.Communication(), 'cc_bookmarkChat')

    def nahagoRun(self, browser) :
        #로그인 테스트
        # nahago.Login().login_nahago(browser)
        #메시지 테스트
        self.communication(browser) """