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
driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth',block: 'center',inline: 'center'});", login_b_happen)
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

xpath_arrow_drop_down = "//*[@id='_next']/div/div[1]/div/div[1]/div/div/div/div/div/div[1]/div"; #xpath of dropdown
xpath_menu_drop_down = "//*[@id='_next']/div/div[1]/div/div[1]/div/div/div/div/div/div[2]/ul/a"; #xpath of dropdown_menu

arrow_drop_down = driver.find_element_by_xpath(xpath_arrow_drop_down)
arrow_drop_down.click()
time.sleep(3)

menu_drop_down = driver.find_element_by_xpath(xpath_menu_drop_down)
#menu_drop_down.click()
driver.execute_script("arguments[0].click();", menu_drop_down)
time.sleep(3)

xpath_account = "//*[@id='_next']/div/div/div[2]/div/div[2]/div[1]/ul/li[2]/a"; #xpath of account section
xpath_update_b = "//*[@id='_next']/div/div/div[2]/div/div/div[2]/div[2]/div/div/form[1]/div/div[2]/button"; ##xpath of update button
xpath_voorname_first_input_field = "//*[@id='_next']/div/div/div[2]/div/div/div[2]/div[2]/div/div/form[1]/div/div[1]/div[1]/input"; #xpath of voorname first input field
xpath_voorname_second_input_field = "//*[@id='_next']/div/div/div[2]/div/div/div[2]/div[2]/div/div/form[1]/div/div[1]/div[3]/input"; #xpath of voorname second input field
xpath_Achternaam_input_field = "//*[@id='_next']/div/div/div[2]/div/div/div[2]/div[2]/div/div/form[1]/div/div[1]/div[2]/input"; #xpath of Achternaam input field

account_b = driver.find_element_by_xpath(xpath_account)
account_b.click()

time.sleep(2.5)

update_b = driver.find_element_by_xpath(xpath_update_b)
driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth',block: 'end',inline: 'nearest'})", update_b)

time.sleep(3)

voorname_first_input_field = driver.find_element_by_xpath(xpath_voorname_first_input_field)
Achternaam_input_field = driver.find_element_by_xpath(xpath_Achternaam_input_field)
voorname_second_input_field = driver.find_element_by_xpath(xpath_voorname_second_input_field)

voorname_first_input_field.clear()
time.sleep(1)
voorname_first_input_field.send_keys("SETT TESTER")

Achternaam_input_field.clear()
time.sleep(1)
Achternaam_input_field.send_keys("TEST CORE RYZEN")

voorname_second_input_field.clear()
time.sleep(1)
voorname_second_input_field.send_keys("JUST TESTING")

update_b.click()

time.sleep(5)

driver.back()
time.sleep(2)
driver.back()

time.sleep(4.5)

# xpath of dropdown
xpath_arrow_drop_down_2 = "//*[@id='_next']/div/div[1]/div/div[1]/div/div/div/div/div/div[1]/div"
# xpath of dropdown_menu
xpath_signout_down = "//*[@id='_next']/div/div[1]/div/div[1]/div/div/div/div/div/div[2]/ul/li"

arrow_drop_down_2 = driver.find_element_by_xpath(xpath_arrow_drop_down_2)
arrow_drop_down_2.click()
time.sleep(2.5)

signOUT_b = driver.find_element_by_xpath(xpath_signout_down)
signOUT_b.click()
time.sleep(5)

driver.quit()
