# 导包
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 打开浏览器（创建浏览器驱动对象）
path = r"D:\Python\msedgedriver.exe"
ser = Service(executable_path=path)
driver = webdriver.Edge(service=ser)

# 输入网址
driver.get("http://localhost:8080/Group7/login.jsp")

# 页面操作
# 获取账号并输入
driver.find_element(By.ID, "username").send_keys("Juu04up")
# 密码
driver.find_element(By.ID, "password").send_keys("123456")
# 点击登录操作
driver.find_element(By.CSS_SELECTOR, ".btn.btn-danger.btn-block.btn-lg").click()
# 进入账号设置
# //span[text()="账户设置"]
ele2 = (WebDriverWait(driver, 5).
 until(EC.visibility_of_element_located((By.XPATH, "//span[text()='账户设置']"))))
# driver.find_element(by=By.XPATH, value="//span[text()='账户设置']").click()
action = ActionChains(driver)
action.move_to_element(ele2)
action.perform()
# 点击收货地址 //a[2][text()="收货地址"]
driver.find_element(by=By.XPATH, value='//a[2][text()="收货地址"]').click()
# 固定等待
time.sleep(4)
driver.quit()
