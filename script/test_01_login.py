from page.page_login import PageLogin
from script import log
from tools import DriverTools


class TestLogin:

    def setup_method(self):

        driver = DriverTools.get_driver()
        self.page_login = PageLogin(driver)
        self.page_login.open_url()

    def teardown_method(self):
        DriverTools.quit_driver()

    def test_01_login_success(self):

        # 调用方法
        self.page_login.login("13800001001", "Aa123456")

        # 打印日志
        result = self.page_login.get_success_result()
        # print(f"登录结果:{result}")
        log.info(f"登录结果:{result}")

        # 断言
        assert "13800001001" == result

    def test_02_login_fail_pwd_error(self):

        self.page_login.login("13800001001", "Aa123457")

        result = self.page_login.get_fail_result()
        # print(f"登录结果:{result}")
        log.info(f"登录结果:{result}")
        assert "密码错误" in result

