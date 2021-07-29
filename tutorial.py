from selenium import webdriver

browser = webdriver.Chrome(executable_path="../chromedriver_win32/chromedriver.exe")

browser.get('https://duckduckgo.com')
