import os
import sys
sys.path.append(os.getcwd())
from tool.get_driver import GetDriver


import pytest

from page.page_in import PageIn
def get_data():
    return [("18301247398","xiaobei","xiaobei8529",None)]


class TestLogin():
    # 初始化
    def setup_class(self):
        # 获取PageLogin对象
        self.login = PageIn().page_get_PageLogin()
        # 点击我
        self.login.page_click_me()
        # 点击已有账号去登录
        self.login.page_click_account_link()

    # 结束
    def teardown_class(self):
        # 关闭driver
        GetDriver().quit_driver()

    # 登录测试方法
    @pytest.mark.parametrize("username,pwd,nickname,expect_toast", get_data())
    def test_login(self, username, pwd, nickname,expect_toast):
        # 调用登录业务方法
        self.login.page_login(username, pwd)
        # 如果是正向
        if nickname:
            # 断言 昵称
            assert nickname == self.login.page_get_nickname()
        # 否则逆向
        else:
            print("toast消息：", self.login.page_get_err_info(expect_toast))
            # 断言 toast
            assert expect_toast in self.login.page_get_err_info(expect_toast)


# pytest.main('-s test_login.py')
