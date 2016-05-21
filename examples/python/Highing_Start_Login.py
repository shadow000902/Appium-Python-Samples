import os
from time import sleep

import unittest

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
        desired_caps['app'] = PATH(
            'D:/highing.apk'
        )

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        # end the session
        self.driver.quit()

    def test_Swipe_Login(self):
        sleep(5)

        # 过引导页
        self.driver.swipe(1000, 960, 80, 960, 500)
        sleep(2)
        self.driver.swipe(1000, 960, 80, 960, 500)
        sleep(2)
        self.driver.swipe(1000, 960, 80, 960, 500)
        sleep(2)
        el = self.driver.find_element_by_id('cn.highing.hichat:id/iv_guide_enter')
        el.click()
        sleep(3)

        # 登录
        textfields = self.driver.find_elements_by_class_name("android.widget.EditText")
        textfields[0].send_keys("15558135521")
        textfields[1].send_keys("123456")

        # self.assertEqual('11122223333', textfields[0].text)
        # self.assertEqual('123456', textfields[1].text)

        self.driver.deactivate_ime_engine()
        el = self.driver.find_element_by_id('cn.highing.hichat:id/btn_login')
        el.click()

        # 隐性等待/如果一个无素没有出现都会默认等待你所设定的时间，直到超时或者元素出现
        self.driver.implicitly_wait(15)
        el = self.driver.find_element_by_xpath('//android.widget.TextView[contains(@text, "每日频道")]')
        el.click()

        # 过教学页
        el = self.driver.find_element_by_xpath('//android.widget.ImageView[contains(@text, "")]')
        el.click()

        # 进入发帖页
        # el = self.driver.find_element_by_id()
        el_1 = self.driver.find_element_by_id('cn.highing.hichat:id/topic_text_send')
        # el_2 = self.driver.find_element_by_id('cn.highing.hichat:id/topic_img_send')
        # el_3 = self.driver.find_element_by_id('cn.highing.hichat:id/topic_voice_send')
        #
        # if (el == el_1) :
        #     el_1.click()
        # elif (el == el_2) :
        #     el_2.click()
        # else:
        #     el_3.long_press()

        el_1.click()


        # 过教学页
        el = self.driver.find_element_by_xpath('//android.widget.ImageView[contains(@text, "")]')
        el.click()
        sleep(1)
        el = self.driver.find_element_by_xpath('//android.widget.ImageView[contains(@text, "")]')
        el.click()
        sleep(1)
        el = self.driver.find_element_by_xpath('//android.widget.ImageView[contains(@text, "")]')
        el.click()

        # 发帖
        el = self.driver.find_element_by_id('cn.highing.hichat:id/content_text')
        el.click()

        textfield = self.driver.find_element_by_class_name("android.widget.EditText")
        textfield.send_keys("123456")

        el = self.driver.find_element_by_id('cn.highing.hichat:id/header_btn_right')
        el.click()
        sleep(3)



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(HighingAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
