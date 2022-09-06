#	coding=gbk
import json
from selenium import webdriver

def create_chrome_driver(*, headless=False):  # �����ȸ������������selenium�������������url
    options = webdriver.ChromeOptions()
    if headless:  # ���ΪTrue������ȡʱ����ʾ���������
        options.add_argument('--headless')

    # ��һЩ�����ϵ��Ż�
    options.add_experimental_option('excludeSwitches', ['enable - logging'])
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_experimental_option('useAutomationExtension', False)
    # �������������
    browser = webdriver.Chrome(options=options,executable_path=r"C:\Users\kong\AppData\Local\Google\Chrome\Application\chromedriver.exe")
    # �ƽⷴ����ʩ
    browser.execute_cdp_cmd(
        'Page.addScriptToEvaluateOnNewDocument',
        {'source': 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'}
    )

    return browser
def add_cookies(browser, cookie_file):  # �������������ӵ�¼��cookie
    print(cookie_file)
    with open(cookie_file, 'r') as file:
        cookie_list = json.load(file)
        for cookie_dict in cookie_list:
            if cookie_dict['secure']:
                browser.add_cookie(cookie_dict)
