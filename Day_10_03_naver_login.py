
from selenium import webdriver

browser = webdriver.PhantomJS('phantomjs.exe')

url = 'http://www.naver.com'
browser.get(url)

username = browser.find_element_by_name('id')
username.send_keys('strawji02')

password = browser.find_element_by_name('pw')
password.send_keys('wnsgur020')

form = browser.find_element_by_id('frmNIDLogin')
form.submit()


mail = 'https?//mail.naver.com'
browser.get(mail)
print(browser.title)
print(browser.name)
print(browser.page_source)

























