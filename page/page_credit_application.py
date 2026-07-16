from selenium.webdriver.common.by import By
from base.base import BasePage


class PageCreditApplication(BasePage):
    """额度申请页面"""

    def __init__(self, driver):
        super().__init__(driver)
        # 页面元素定位信息
        self.switch_role = (By.XPATH, "//em[text()='借款账户']")
        self.application = (By.LINK_TEXT, "申请额度")
        self.money = (By.ID, "amount_account")
        self.detail = (By.NAME, "remark")
        self.code = (By.ID, "verifycode")
        self.submit = (By.CSS_SELECTOR, ".btn-submit.btn-md")

    def switch_role(self):
        """点击切换账户"""
        self.base_click(self.role)

    def click_application(self):
        """点击额度申请"""
        self.base_click(self.application)

    def credit_application(self):
        # 输入信息
        self.base_input(self.money, "10000")
        self.base_input(self.detail, "测试额度申请")
        # 点击提交
        self.base_click(self.submit)