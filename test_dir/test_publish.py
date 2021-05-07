import sys
import time
import unittest
import ddt
import HTMLTestRunner
from os.path import dirname, abspath

import yagmail
from selenium import webdriver
from selenium.webdriver.support.select import Select
from page.add_page import AddPage
from page.publish_page import PublishPage

sys.path.insert(0, dirname(dirname(abspath(__file__))))


class TestPublish:
    """论坛发帖功能的测试"""

    @classmethod
    def setup_class(cls, browser, base_url):
        page = PublishPage(browser)
        cls.page = page
        page.get(base_url)
        page.clear_cookie.click()
        page.login_option.click()
        page.usr_input = "admin"
        page.pwd_input = "123456"
        page.login_button.click()

    def test_publish(self, browser):
        page = self.page
        page.forum3.click()
        page.publish_option.click()
        page.title_input = "my-test"
