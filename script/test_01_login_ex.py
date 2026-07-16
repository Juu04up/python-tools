import pytest

from page.page_login import PageLogin
from script import log
from tools import DriverTools, read_json


class TestLogin:

    def setup_method(self):

        driver = DriverTools.get_driver()
        self.page_login = PageLogin(driver)
        self.page_login.open_url()

    def teardown_method(self):
        DriverTools.quit_driver()

    @pytest.mark.parametrize("phone,password,expect",read_json("login_data.json"))
    def test_01_login(self,phone,password,expect):

        # 调用方法
        self.page_login.login(phone, password)

        # 打印日志
        if phone == expect:
            result = self.page_login.get_success_result()
        else:
            result = self.page_login.get_fail_result()
        log.info(f"登录结果:{result}")

        # 断言
        assert expect in result


