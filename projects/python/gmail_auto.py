from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import time

driver = webdriver.Chrome()
url = 'http://google.com'
driver.get(url)
driver.maximize_window()
action = ActionChains(driver)
