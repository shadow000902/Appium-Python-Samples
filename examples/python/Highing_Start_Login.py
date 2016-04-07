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
            'C:/Highing/app/build/outputs/apk/app-Test-debug.apk'
        )

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        # end the session
        self.driver.quit()

    def test_Swipe_Login(self):
        sleep(5)
        self.driver.swipe(1000, 960, 80, 960, 500)
        sleep(2)
        self.driver.swipe(1000, 960, 80, 960, 500)
        sleep(2)
        self.driver.swipe(1000, 960, 80, 960, 500)
        sleep(2)
        el = self.driver.find_element_by_id('cn.highing.hichat:id/iv_guide_enter')
        el.click()
        sleep(3)
        textfields = self.driver.find_elements_by_class_name("android.widget.EditText")
        textfields[0].send_keys("11122223333")
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

        # el = self.driver.find_element_by_accessibility_id('Arcs')
        # self.assertIsNotNone(el)
        #
        # self.driver.back()
        #
        # el = self.driver.find_element_by_accessibility_id("App")
        # self.assertIsNotNone(el)
        #
        # els = self.driver.find_elements_by_android_uiautomator("new UiSelector().clickable(true)")
        # self.assertGreaterEqual(12, len(els))
        #
        # self.driver.find_element_by_android_uiautomator('text("API Demos")')


    # def test_simple_actions(self):
    #     el = self.driver.find_element_by_accessibility_id('Graphics')
    #     el.click()
    #
    #     el = self.driver.find_element_by_accessibility_id('Arcs')
    #     el.click()
    #
    #     self.driver.find_element_by_android_uiautomator('new UiSelector().text("Graphics/Arcs")')


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(HighingAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
