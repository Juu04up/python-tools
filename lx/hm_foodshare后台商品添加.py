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
driver.get("http://localhost:8080/Group7/login.jsp")
driver.maximize_window()
# 页面操作
# 获取账号并输入
driver.find_element(By.ID, "username").send_keys("Juu04up")
# 密码
driver.find_element(By.ID, "password").send_keys("123456")
# 点击登录操作
driver.find_element(By.CSS_SELECTOR, ".btn.btn-danger.btn-block.btn-lg").click()
# 点击发布美食
# 隐式等待,显式等待,固定等待
ele = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT,"发布美食")))
ele.click()
# result = ele.text
# print(result)
# assert "OK" in result
# time.sleep(2)
# driver.find_element(By.LINK_TEXT,value="发布美食").click()
# 输入美食信息
driver.find_element(By.NAME,"foodName").send_keys("香蕉冻")
# 下拉框（文本、索引、value值）
select = Select(driver.find_element(By.NAME,"categoryId"))
# select.select_by_index("6")
# select.select_by_value(6)
select.select_by_visible_text("甜品")
driver.find_element(By.NAME,"avgPrice").send_keys("15")
driver.find_element(By.NAME,"address").send_keys("翻斗大街翻斗花园二号楼1001室")
driver.find_element(By.NAME,"description").send_keys("夯爆了")
driver.find_element(By.NAME,"steps").send_keys("先这样再那样")
driver.find_element(By.NAME,"reason").send_keys("好吃")
driver.find_element(By.CSS_SELECTOR,".btn.btn-danger.btn-lg.px-5").click()
# 固定等待
time.sleep(4)
driver.quit()
