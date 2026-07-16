from page.page_register import PageRegister
from script import log
from tools import DriverTools
from config import *

class TestRegister:

    def setup_method(self):

        driver = DriverTools.get_driver()
        self.page_register = PageRegister(driver)
        self.page_register.open_url()

    def teardown_method(self):
        DriverTools.quit_driver()

    def test_01_register_success(self):

        # 调用方法
        self.page_register.register("15800005006", "Aa123456","8888","6666666")

        # 打印日志
        result = self.page_register.get_success_result()
        log.info(f"注册结果:{result}")

        # 断言
        assert "注册成功" in result
    def test_02_register_fail_phone_exist(self):

        # 调用方法
        self.page_register.register("15800005006", "Aa123456","8888","6666666")

        # 打印日志
        result = self.page_register.get_fail_result()
        log.info(f"注册结果:{result}")

        # 断言
        assert "88" in result

