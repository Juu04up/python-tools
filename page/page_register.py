# 类三要素
# 1.定义页面类
# 2.设置实例属性
# 3.定义实例方法
import time

from selenium.webdriver.common.by import By
from base.base import BasePage
from config import BASE_URL
from tools import DriverTools

class PageRegister(BasePage):

    def __init__(self,driver):
        # driver = DriverTools.get_driver()
        super().__init__(driver)
        self.phone = (By.ID, "phone")
        self.password = (By.ID, "password")
        self.img_code = (By.ID, "verifycode")
        self.phone_click = (By.ID, "get_phone_code")
        self.phone_code = (By.ID, "phone_code")
        self.reg = (By.CLASS_NAME, "lg-btn")
        # 成功结果
        self.success_result = (By.CSS_SELECTOR, "div.reg-step-last > h1")
        # 失败结果
        self.fail_result = (By.CSS_SELECTOR, ".reg-title")
    def open_url(self):
        self.driver.get(BASE_URL+"/common/member/reg")

    def register(self,phone,pwd,img_code,phone_code):
        # 输入手机号
        self.base_input(self.phone,phone)
        # 输入密码
        self.base_input(self.password,pwd)
        # 输入验证码
        self.base_input(self.img_code,img_code)
        # 点击获取手机验证码
        self.base_click(self.phone_click)
        time.sleep(2)
        # 输入手机验证码
        self.base_input(self.phone_code,phone_code)
        # 点击注册
        self.base_click(self.reg)
        time.sleep(2)

    def get_success_result(self):
        return self.fd_element(self.success_result).text
    def get_fail_result(self):
        return self.fd_element(self.fail_result).text