#	coding=gbk
'''
ͨ��������ȡ��Ʒ��Ϣ
'''
import json
from .utils import create_chrome_driver, add_cookies

browser = create_chrome_driver()  # �����ȸ����������ͨ�����������������url
browser.get('https://www.taobao.com')
add_cookies(browser, 'taobao2.json')
browser.get('https://s.taobao.com/search?q=�ֻ�&s=0')  # �Ա��ϵ��������ܱ���Ҫ��¼������������Ҫ��cookie���������
with open('taobao2.json', 'r') as file:
    cookie_list = json.load(file)
    print(cookie_list)