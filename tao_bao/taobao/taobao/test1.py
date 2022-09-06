#	coding=gbk
import json
import time
from selenium.webdriver.common.by import By
from .utils import create_chrome_driver
browser = create_chrome_driver()
browser.get('https://login.taobao.com')

# ��ʽ�ȴ�
browser.implicitly_wait(10)

# ��ȡҳ��Ԫ��ģ���û�����͵����Ϊ
username_input = browser.find_element(By.CSS_SELECTOR, '#fm-login-id')
username_input.send_keys('����ӻ�')  # ��д�û���

password_input = browser.find_element(By.CSS_SELECTOR, '#fm-login-password')
password_input.send_keys('xx')  # ��д��Ӧ������

# ��¼��ť
login_button = browser.find_element(By.CSS_SELECTOR, '#login-form > div.fm-btn > button')
login_button.click()

# ��ʾ�ȴ�
# wait_obj = WebDriverWait(browser, 10)
# wait_obj.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, 'div.m-userinfo')))
time.sleep(30)

# ��ȡ��¼��cookie���ݣ�����д���ļ�
with open('taobao2.json', 'w') as file:
    json.dump(browser.get_cookies(), file)

