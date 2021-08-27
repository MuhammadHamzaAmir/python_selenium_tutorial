from logging import log
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

email = "intern.alphasquad@gmail.com"
password = "aqkhan88"
name = "ATESTER"

options = Options()
options.page_load_strategy = 'normal'
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

#for windows
# driver = webdriver.Chrome(
#     executable_path="../chromedriver_win32/chromedriver.exe", options=options)
#for linux
driver = webdriver.Chrome(executable_path="../chromedriver_win32/chromedriver", options=options)
driver.maximize_window()
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36'})
print(driver.execute_script("return navigator.userAgent;"))
driver.get('https://alquin.learnforce.cloud/')
time.sleep(3)

start_tr = driver.find_element_by_id("welcomeSignUp")
driver.execute_script(
    "arguments[0].scrollIntoView({behavior: 'smooth',block: 'center',inline: 'center'});", start_tr)
time.sleep(3)
start_tr.click()

time.sleep(3)

driver.find_element_by_css_selector(
    "#_next > div > div > div > div.flex.items-start.justify-center.px-4.md\\:px-0.py-16.xl\\:py-6.\\32 xl\\:py-12.mx-auto.container > div > div > div:nth-child(2) > div > div:nth-child(1) > button").click()
time.sleep(3)

driver.find_element_by_id("identifierId").send_keys(email)
time.sleep(3)
driver.find_element_by_css_selector(
    "#identifierNext > div > button").click()
time.sleep(3)
driver.find_element_by_css_selector(
    "#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input").send_keys(email)
time.sleep(3)
driver.find_element_by_css_selector(
    "#passwordNext > div > button > div.VfPpkd-Jh9lGc").click()
time.sleep(5)

driver.quit()
