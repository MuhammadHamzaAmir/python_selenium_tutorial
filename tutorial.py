from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.chrome.options import Options
options = Options()
options.page_load_strategy = 'normal'

driver = webdriver.Chrome(executable_path="../chromedriver_win32/chromedriver.exe",options=options)
driver.maximize_window()
driver.get('https://gelukzaaiers.learnforce.cloud/')

xpath_login_b_mainp = "//*[@id='_next']/div/div/div/div/div/div[2]/div/div[3]/div[1]/div[1]/button"
login_b = driver.find_element_by_xpath(xpath_login_b_mainp)
login_b.click()

time.sleep(3)
xpath_login_b_happen = "//*[@id='_next']/div/div/form/div[4]/button"; #xpath of login button on sign up page
login_b_happen = driver.find_element_by_xpath(xpath_login_b_happen)
#print(login_b_happen.rect) #{'height': 65, 'width': 270, 'x': 629, 'y': 838}

time.sleep(5)


driver.quit()
