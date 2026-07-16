import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

path = r"D:\Python\msedgedriver.exe"
ser = Service(executable_path=path)
driver = webdriver.Edge(service=ser)

driver.get("https://hmshop-test.itheima.net/Home/user/login.html")

driver.find_element(By.ID, "username").send_keys("13800000001")
driver.find_element(By.NAME, "password").send_keys("123456")
driver.find_element(By.ID, "verify_code").send_keys("8888")
time.sleep(3)
driver.find_element(By.CLASS_NAME, "J-login-submit").click()
time.sleep(6)
driver.quit()

