import time
from selenium import webdriver

driver = webdriver.Edge()

driver.get("https://www.baidu.com")

time.sleep(5)

driver.quit()