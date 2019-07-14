from page.page_login import PageLogin
from tool.get_driver import GetDriver

class PageIn:
    driver = GetDriver().get_driver()

    # 获取PageLogin对象
    def page_get_PageLogin(self):
        return PageLogin(self.driver)
