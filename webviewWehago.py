#-*- coding: utf-8 -*-
import time, datetime, os, platform
import wehagotestrun, wehagotest, varname
import wehagoReport
from driver import wehagoID, chromeBrowser, checkSerivce, mobileBrowser
from pathos.multiprocessing import ProcessingPool
import numpy as np
from wehagotest import Login

def multi_browser(service):
    browser = mobileBrowser()
    # version, brand, dev
    wehagotest.Common().set_wehagoBrand(1, 1, 1)
    Login().login(browser,id)
    time.sleep(3)
    return serviceRun(browser, service)

def serviceRun(browser, service) :
    for i in range(len(service)) :
        getattr(wehagotestrun.WehagoRun_webview(), service[i])(browser)
        time.sleep(1)
    browser.quit()

def get_serviceList(process=2) :
    serviceList = (['message', 'accounts', 'contacts', 'schedule', 'communication', 'mail'])
    # serviceList = ['dev_meet']

    service = np.array_split(serviceList, process)
    service = [x.tolist() for x in service]
    return service

if __name__ == '__main__': # ， ，pathos
    #현재 폴더 경로 받아옴
    path = os.getcwd()
    id = 'qatest'
    # pool = ProcessingPool()
    # pool.map(multi_browser, get_serviceList(4))
    # pool.close()
    # pool.join()
    #
    version = int(input('0-개발기전체 / 1-개발기특정서비스 '))
    if version == 1 :
        # 특정 서비스만 실행
        print('0-메시지/1-거래처/2-연락처/3-일정/4-메신저/5-메일\n6-할일/7-crm/8-pms/9-노트/10-전자결재')
        print('11-법인카드/12-개인카드/13-근태관리/14-화상회의/15-회사게시판\n16-전자세금계산서/17-팩스/18-문자/19-위스튜디오/20-위봇')
        number = map(int, input('\n숫자만 입력 ').split())
        checkSerivce(num=number)
        # 개발기
        browser = chromeBrowser()
        print('개발기 시작')
        wehagotestrun.WehagoRun_webview().wehagoRun(browser, 'qatest', 1, 1)
        print('WEHAGO 테스트 끝')
        browser.quit()
    else :
        pool = ProcessingPool()
        pool.map(multi_browser, get_serviceList())
        pool.close()
        pool.join()
