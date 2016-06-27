#!/usr/bin/python
# coding=utf-8

import os
import time
from time import sleep

import unittest

import HTMLTestRunner
from appium import webdriver

# Returns abs path relative to this file and not cwd

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class Dasouche_Login_Test(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'Nexus 5'
        desired_caps['appPackage'] = 'com.souche.fengche'  # 被测App的包名
        desired_caps['appActivity'] = 'com.souche.fengche.ui.activity.SplashActivity'  # 启动时的Activity
        # desired_caps['app'] = PATH('/Users/taoyi/Downloads/dasouche.apk')

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        # end the session
        self.driver.quit()

    def Test_Login(self):
        sleep(10)
        if self.driver.current_activity == ".ui.GuideActivity":
            self.driver.implicitly_wait(10)
            try:
                # 划过引导页
                self.driver.swipe(1000, 960, 80, 960, 500)
                self.driver.swipe(1000, 960, 80, 960, 500)
                self.driver.implicitly_wait(10)
                self.driver.swipe(1000, 960, 80, 960, 500)
                self.driver.implicitly_wait(10)
                el = self.driver.find_element_by_id('cn.souche.fengche:id/iv_guide_enter')
                el.click()
                self.driver.implicitly_wait(10)
            except:
                return

        # 登录
        textfields = self.driver.find_elements_by_class_name("android.widget.EditText")
        textfields[0].send_keys("15558135526")
        textfields[1].send_keys("souche2015")

        self.driver.hide_keyboard()
        el = self.driver.find_element_by_id('com.souche.fengche:id/login_sign_in')
        el.click()
        sleep(5)



if __name__ == '__main__':
    # suite = unittest.TestLoader().loadTestsFromTestCase(Dasouche_Login_Test)
    # unittest.TextTestRunner(verbosity=2).run(suite)


    suite = unittest.TestSuite()
    suite.addTest(Dasouche_Login_Test("Test_Login"))

    timestr = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    filename = "./results/result_" + timestr + ".html"                          # 定义个报告存放路径，支持相对路径。

    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Test Results',
                                           description='Test Reports')          # 使用HTMLTestRunner配置参数，输出报告路径、报告标题、描述

    runner.run(suite)                                                           # 自动进行测试
    fp.close()                                                                  # 测试报告关闭
