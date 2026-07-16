# 1. 导包
import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service

# 2. 打开浏览器（创建Edge浏览器驱动对象）
path = r"D:\Python\msedgedriver.exe"
ser = Service(executable_path=path)
driver = webdriver.Edge(service=ser)  # 打开Edge浏览器
# 3. 输入网址
driver.get("https://www.itheima.com/")
# 4. 页面操作
# 5. 等待5秒
time.sleep(5)
# 6. 退出浏览器
driver.quit()