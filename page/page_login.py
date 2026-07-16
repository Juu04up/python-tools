# 类三要素
# 1.定义页面类
# 2.设置实例属性
# 3.定义实例方法
import time

from selenium.webdriver.common.by import By
from base.base import BasePage
from config import BASE_URL
from tools import DriverTools

class PageLogin(BasePage):

    def __init__(self,driver):
        # driver = DriverTools.get_driver()
        super().__init__(driver)
        self.username = (By.ID, "keywords")
        self.password = (By.ID, "password")
        self.login_button = (By.ID, "login-btn")
        # 成功结果
        self.success_result = (By.CLASS_NAME, "a-link1")
        # 失败结果
        # 1.密码错误
        self.fail_result = (By.CSS_SELECTOR, "#err > span")
    def open_url(self):
        self.driver.get(BASE_URL+"/common/member/login")

    def login(self,username,password):
        # 输入账号
        self.base_input(self.username,username)
        # WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.username)).send_keys("Juu04up")
        # self.driver.find_element(*self.username).send_keys("Juu04up")
        # 输入密码
        self.base_input(self.password,password)
        # WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.password)).send_keys("123456")
        # self.driver.find_element(*self.password).send_keys("123456")
        # 点击登录
        self.base_click(self.login_button)
        time.sleep(2)
        # WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.login_button)).click()
        # self.driver.find_element(*self.login_button).click()

    def get_success_result(self):
        return self.fd_element(self.success_result).text
    def get_fail_result(self):
        return self.fd_element(self.fail_result).text
if __name__ == '__main__':
    lg = PageLogin(DriverTools.get_driver())
    lg.open_url()
    lg.login("13800001001","Aa123456")