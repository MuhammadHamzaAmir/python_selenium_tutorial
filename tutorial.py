from logging import log
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

options = Options()
options.page_load_strategy = 'normal'

driver = webdriver.Chrome(executable_path="../chromedriver_win32/chromedriver.exe",options=options)
driver.maximize_window()
driver.get('https://gelukzaaiers.learnforce.cloud/')
time.sleep(3)

xpath_login_b_mainp = "//*[@id='_next']/div/div/div/div/div/div[2]/div/div[3]/div[1]/div[1]/button"
login_b = driver.find_element_by_xpath(xpath_login_b_mainp)
login_b.click()

time.sleep(3)
xpath_login_b_happen = "//*[@id='_next']/div/div/form/div[4]/button"; #xpath of login button on sign up page
login_b_happen = driver.find_element_by_xpath(xpath_login_b_happen)
#print(login_b_happen.rect) #{'height': 65, 'width': 270, 'x': 629, 'y': 838}
driver.execute_script("arguments[0].scrollIntoView();", login_b_happen)
time.sleep(2)

xpath_email_if = "//*[@id='email']"; #xpath of email input field on login page
xpath_password_if = "//*[@id='password']"; #xpath of password input field on login page

email_ip = "homam57854@dedatre.com"; #email used for signup and login
password_ip = "17againpc"; #default password for all the accounts

email = driver.find_element_by_id("email")
password = driver.find_element_by_id("password")

email.send_keys(email_ip)
password.send_keys(password_ip)
time.sleep(1)

print(password.get_attribute('value'), " || ", email.get_property("value"), " ", login_b_happen.text)

login_b_happen.click()

time.sleep(8)


driver.quit()
