from appium import webdriver

class GetDriver:
    driver=None

    #获取driver
    @classmethod
    def get_driver(cls):
        if not cls.driver:
            desired_caps = {}
            desired_caps['platformName'] = 'Android'
            desired_caps['platformVersion'] = '5.1'
            desired_caps['deviceName'] = '192.168.56.101:5555'
            #app的信息
            desired_caps['appPackage'] = 'com.yunmall.lc'
            desired_caps['appActivity'] = 'com.yunmall.ymctoc.ui.activity.MainActivity'
            #中文
            desired_caps['unicodeKeyboard']=True
            desired_caps['resetKeyboard']=True
            #指定模拟器（多个模拟器使用）
            # desired_caps['udid']='emulator-5554'
            # 获取toast消息
            desired_caps['automationName'] = 'Uiautomator2'
            #不重置应用
            # desired_caps['noRest']=True
            # 获取driver
            cls.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        return cls.driver

    #关闭driver
    @classmethod
    def quit_driver(cls):
        if cls.driver:
            cls.driver.quit()
            cls.driver=None
