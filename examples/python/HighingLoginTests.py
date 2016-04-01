import os
import unittest

from appium import webdriver

from time import sleep

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
            '../../../sample-code/apps/Highing.apk'
        )

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    # def tearDown(self):
    #     self.driver.quit()

    def test_swipe(self):
        sleep(5)
        self.driver.swipe(700, 640, 20, 640)
        sleep(1)
        self.driver.swipe(700, 640, 20, 640)
        sleep(1)
        self.driver.swipe(700, 640, 20, 640)
        sleep(1)
        self.driver.find_element_by_id('cn.highing.hichat:id/iv_guide_enter').click()

    # def test_login(self):
    #     sleep(3)
        textfields = self.driver.find_elements_by_class_name("android.widget.EditText")
        textfields[0].send_keys("11122223333")
        textfields[1].send_keys("123456")
        self.driver.deactivate_ime_engine()
        sleep(2)
        # self.assertEqual('18116137476', textfields[0].text)
        # self.assertEqual('123456', textfields[1].text)
        self.driver.find_element_by_id('cn.highing.hichat:id/btn_login').click()

    # # def test_find_elements(self):
    # #     # pause a moment, so xml generation can occur
    # #     sleep(2)
    # #
    # #     els = self.driver.find_elements_by_xpath('//android.widget.TextView')
    # #     self.assertEqual('API Demos', els[0].text)
    # #
    # #     el = self.driver.find_element_by_xpath('//android.widget.TextView[contains(@text, "Animat")]')
    # #     self.assertEqual('Animation', el.text)
    # #
    # #     el = self.driver.find_element_by_accessibility_id("App")
    # #     el.click()
    # #
    # #     els = self.driver.find_elements_by_android_uiautomator('new UiSelector().clickable(true)')
    # #     # there are more, but at least 10 visible
    # #     self.assertLess(10, len(els))
    # #     # the list includes 2 before the main visible elements
    # #     self.assertEqual('Action Bar', els[2].text)
    # #
    # #     els = self.driver.find_elements_by_xpath('//android.widget.TextView')
    # #     self.assertLess(10, len(els))
    # #     self.assertEqual('Action Bar', els[1].text)
    #
    # # def test_scroll(self):
    # #     sleep(2)
    # #     els = self.driver.find_elements_by_xpath('//android.widget.TextView')
    # #     self.driver.scroll(els[7], els[3])
    # #
    # #     el = self.driver.find_element_by_accessibility_id('Views')



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(HighingAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
