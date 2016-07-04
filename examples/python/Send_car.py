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


class Dasouche_SendCar_Test(unittest.TestCase):
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

    def Test_Send_Car(self):
        sleep(5)

        # 点击加号
        self.driver.find_element_by_id('com.souche.fengche:id/action_bar_workbench_add').click()
        # 点击发车
        self.driver.find_element_by_id('com.souche.fengche:id/popview_workbench_send_car').click()
        # 点击车辆管理
        self.driver.find_element_by_id('com.souche.fengche:id/record_car_sdv_car').click()
        # 点击照片管理中的车辆照片中的加号
        self.driver.find_element_by_id('com.souche.fengche:id/photo_manager_viewpager_item_image').click()
        # 选择"从相册中选取"
        self.driver.find_element_by_id('com.souche.fengche:id/photo_manager_pick_photo').click()
        # 点击第一个相册
        imagefields = self.driver.find_elements_by_class_name('android.widget.ImageView')
        imagefields[0].click()
        # 选择第一张图片
        imagefields = self.driver.find_elements_by_class_name('android.widget.ImageView')
        imagefields[0].click()
        # 点击确定
        self.driver.find_element_by_id('com.souche.fengche:id/carlib_tv_confirm').click()
        # 点击保存
        self.driver.find_element_by_id('com.souche.fengche:id/carlib_toolbar_save').click()
        # 点击品牌车型
        self.driver.find_element_by_id('com.souche.fengche:id/record_car_tv_brand_type').click()
        # 选择品牌
        self.driver.find_element_by_xpath('//android.widget.TextView[contains(@text, "阿斯顿・马丁")]').click()
        # 选择车系
        self.driver.find_element_by_xpath('//android.widget.TextView[contains(@text, "Rapide")]').click()
        # 选择车型
        self.driver.find_element_by_xpath('//android.widget.TextView[contains(@text, "2016款 Rapide 6.0L S")]').click()
        # 填写表显里程
        self.driver.find_element_by_id('com.souche.fengche:id/record_car_et_car_mileage').click()
        self.driver.find_element_by_id('com.souche.fengche:id/record_car_et_car_mileage').send_keys('5')
        self.driver.hide_keyboard()
        # 填写初次上牌
        self.driver.find_element_by_id('com.souche.fengche:id/record_car_tv_first_license').click()
        # 完成填写
        self.driver.find_element_by_id('com.souche.fengche:id/carlib_tv_story_dialog_time_sure').click()
        # 车身颜色
        self.driver.find_element_by_id('com.souche.fengche:id/record_car_tv_car_color').click()
        # 选择车身颜色
        el1 = self.driver.find_element_by_xpath('//android.widget.TextView[contains(@text, "银灰色")]')
        # el2 = self.driver.find_element_by_xpath('//android.widget.TextView[contains(@text, "其他")]')
        # self.driver.scroll(el1, el2)
        el1.click()
        # 输入颜色值
        # self.driver.find_element_by_id('com.souche.fengche:id/record_car_et_note').send_keys('123456')
        # 点击保存
        self.driver.find_element_by_id('com.souche.fengche:id/carlib_toolbar_save').click()
        # 点击保存
        self.driver.find_element_by_id('com.souche.fengche:id/carlib_toolbar_save').click()
        sleep(10)
        # 点击 暂不上架
        self.driver.find_element_by_id('android:id/button2').click()
        sleep(10)




if __name__ == '__main__':
    # suite = unittest.TestLoader().loadTestsFromTestCase(Dasouche_Login_Test)
    # unittest.TextTestRunner(verbosity=2).run(suite)


    suite = unittest.TestSuite()
    suite.addTest(Dasouche_SendCar_Test("Test_Send_Car"))

    timestr = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    filename = "./results/result_" + timestr + ".html"                          # 定义个报告存放路径，支持相对路径。

    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Test Results',
                                           description='Test Reports')          # 使用HTMLTestRunner配置参数，输出报告路径、报告标题、描述

    runner.run(suite)                                                           # 自动进行测试
    fp.close()                                                                  # 测试报告关闭
