from tools import DriverTools

class TestCreditApplication(object):

    def setup_method(self):
        dr = DriverTools.get_driver()
        # 登录
        login_page = Login(dr)  # 创建登录页面类对象
        login_page.open_url()   # 打开登录页面
        login_page.login("18800002008", "Aa123456")  # 登录
        self.credit_page = CreditApplication(dr)

    def test_01_credit_application_success(self):
        # 调用方法
        self.credit_page.credit_application("100000", "额度申请详情信息", "8888")
        # 记录结果日志
        # 断言
        # 截图