import page
from base.base import Base


class PageLogin(Base):

    # 点击 我
    def page_click_me(self):
        self.base_click(page.login_me)

    # 点击已有账号，去登录
    def page_click_account_link(self):
        self.base_click(page.login_account_exists)

    # 输入用户名
    def page_input_username(self, username):
        self.base_input(page.login_username, username)

    # 输入密码
    def page_input_pwd(self, pwd):
        self.base_input(page.login_pwd, pwd)

    # 点击登录
    def page_click_login_btn(self):
        self.base_click(page.login_btn)

    # 获取登录后的昵称
    def page_get_nickname(self):
        return self.base_get_text(page.login_nickname)

    # 获取异常提示消息 toast
    def page_get_err_info(self, msg):
        return self.base_get_toast(msg)

    # 组合业务方法
    def page_login(self, username, pwd):
        self.page_input_username(username)
        self.page_input_pwd(pwd)
        self.page_click_login_btn()
