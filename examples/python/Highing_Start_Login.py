#!/usr/bin/python
# coding=utf-8

import os
from time import sleep

import unittest

# from Scripts.HTMLTestRunner import HTMLTestRunner
from appium import webdriver

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class HighingAndroidTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'Nexus 5'
        desired_caps['appPackage'] = 'cn.highing.hichat'  # 被测App的包名
        desired_caps['appActivity'] = 'cn.highing.hichat.ui.SplashActivity'  # 启动时的Activity
        # desired_caps['app'] = PATH('D:/highing.apk')

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        # end the session
        self.driver.quit()

    def test_Swipe_Login(self):
        sleep(10)
        if self.driver.current_activity == ".ui.GuideActivity":
            try:
                # 划过引导页
                self.driver.swipe(1000, 960, 80, 960, 500)
                self.driver.implicitly_wait(10)
                self.driver.swipe(1000, 960, 80, 960, 500)
                self.driver.implicitly_wait(10)
                self.driver.swipe(1000, 960, 80, 960, 500)
                self.driver.implicitly_wait(10)
                el = self.driver.find_element_by_id('cn.highing.hichat:id/iv_guide_enter')
                el.click()
                self.driver.implicitly_wait(10)
            except:
                return

        # 登录
        textfields = self.driver.find_elements_by_class_name("android.widget.EditText")
        textfields[0].send_keys("18116137476")
        textfields[1].send_keys("123456")

        self.driver.hide_keyboard()
        el = self.driver.find_element_by_id('cn.highing.hichat:id/btn_login')
        el.click()

        # 隐性等待/如果一个无素没有出现都会默认等待你所设定的时间，直到超时或者元素出现
        self.driver.implicitly_wait(15)
        el = self.driver.find_element_by_xpath('//android.widget.TextView[contains(@text, "每日频道")]')
        el.click()
        self.driver.implicitly_wait(10)
        try:
            # 过教学页
            el = self.driver.find_element_by_xpath('//android.widget.ImageView[contains(@text, "")]')
            el.click()
        except:
            return

        try:
            # 发文字帖
            el_1 = self.driver.find_element_by_id('cn.highing.hichat:id/topic_text_send')
            el_1.click()
            self.driver.implicitly_wait(10)

            try:
                # 过教学页
                el = self.driver.find_element_by_xpath('//android.widget.ImageView[contains(@text, "")]')
                el.click()
                sleep(1)
                el = self.driver.find_element_by_xpath('//android.widget.ImageView[contains(@text, "")]')
                el.click()
                sleep(1)
                el = self.driver.find_element_by_xpath('//android.widget.ImageView[contains(@text, "")]')
                el.click()
            except:
                return

            # 发文字帖
            el = self.driver.find_element_by_id('cn.highing.hichat:id/content_text')
            el.click()

            textfield = self.driver.find_element_by_class_name("android.widget.EditText")
            textfield.send_keys("text_test_0001")

            el = self.driver.find_element_by_id('cn.highing.hichat:id/header_btn_right')
            el.click()
            self.driver.implicitly_wait(10)

        except:
            try:
                # 发图片帖
                el_2 = self.driver.find_element_by_id('cn.highing.hichat:id/topic_img_send')
                el_2.click()
                self.driver.implicitly_wait(10)


                # 这里还没调通，图片复用的选择有问题
                imagefields = self.driver.find_elements_by_class_name("android.widget.EditText")
                imagefields[5].click()
                imagefields[6].click()
                imagefields[7].click()

                el = self.driver.find_element_by_id('cn.highing.hichat:id/header_layout_rightview_container')
                el.click()
                self.driver.implicitly_wait(10)

                textfield = self.driver.find_element_by_class_name("android.widget.EditText")
                textfield.send_keys("image_test_0001")

                el = self.driver.find_element_by_id('cn.highing.hichat:id/header_btn_right')
                el.click()
                self.driver.implicitly_wait(10)

            except:
                # 发语音帖
                el_3 = self.driver.find_element_by_id('cn.highing.hichat:id/topic_voice_send')
                el_3.click()
                self.driver.implicitly_wait(10)

                textfield = self.driver.find_element_by_class_name("android.widget.EditText")
                textfield.send_keys("voice_test_0001")

                el = self.driver.find_element_by_id('cn.highing.hichat:id/header_btn_right')
                el.click()
                self.driver.implicitly_wait(10)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(HighingAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)

    # filename="./myAppiumLog.html"        # 定义个报告存放路径，支持相对路径。
    # fp=file(filename, 'wb')
    # runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Report_title', description='Report_description')  # 使用HTMLTestRunner配置参数，输出报告路径、报告标题、描述
    # runner.run(testunit)                 # 自动进行测试
