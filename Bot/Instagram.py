from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def account_info():
    with open('account_info.txt','r') as f:
        info = f.read().split()
        email = info[0]
        password = info[1]
    return email, password

email, password = account_info()

options = Options()
options.add_argument("start-maximized")
driver = webdriver.Chrome(executable_path='C:\\Users\\amar singh\\Desktop\\python\\Bot\\chromedriver.exe', options=options)

driver.get("https://www.instagram.com/accounts/login/")

email_xpath = '//*[@id="loginForm"]/div/div[1]/div/label/input'
password_xpath = '//*[@id="loginForm"]/div/div[2]/div/label/input'
login_xpath = '//*[@id="loginForm"]/div/div[3]'

time.sleep(2)

driver.find_element_by_xpath(email_xpath).send_keys(email)
time.sleep(0.5)
driver.find_element_by_xpath(password_xpath).send_keys(password)
time.sleep(0.5)
driver.find_element_by_xpath(login_xpath).click()
