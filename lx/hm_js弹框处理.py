# 导包
import time
from selenium import webdriver
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
driver.get("http://121.43.169.97:8848/pageA.html")
driver.maximize_window()
# 页面操作

js = "window.scrollTo(0,400)"
driver.execute_script(js)

driver.find_element(By.ID, "confirma").click()
# 固定等待
time.sleep(2)
alert = driver.switch_to.alert
print(alert.text)
time.sleep(2)
alert.accept()  # 点击【确定】
time.sleep(2)
driver.quit()
