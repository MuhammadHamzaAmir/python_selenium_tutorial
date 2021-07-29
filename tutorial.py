from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
import time

browser = webdriver.Chrome(executable_path="../chromedriver_win32/chromedriver.exe")

browser.get('https://duckduckgo.com')
time.sleep(5)

browser.quit()
