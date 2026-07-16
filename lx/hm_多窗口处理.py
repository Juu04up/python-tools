# 导包
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

# 打开浏览器（创建浏览器驱动对象）
path = r"D:\Python\msedgedriver.exe"
ser = Service(executable_path=path)
driver = webdriver.Edge(service=ser)

# 输入网址
driver.get("http://121.43.169.97:8848/pageA.html")
driver.maximize_window()
# 页面操作

driver.find_element(By.ID, "fw").click()
handles = driver.window_handles
print(handles)
# 切换窗口
driver.switch_to.window(handles[1])
# 新窗口搜索软件测试
driver.find_element(By.ID, "chat-textarea").send_keys("软件测试")
# driver.find_element(By.ID, "chat-submit-button").click()
time.sleep(2)
# 搜索操作截图
# driver.get_screenshot_as_file("baidu.png")
driver.refresh()
driver.back()
driver.forward()
# 固定等待
time.sleep(2)
driver.quit()