import sys
from time import sleep
import pytest
from os.path import dirname, abspath

from page.login_page import LoginPage

sys.path.insert(0, dirname(dirname(abspath(__file__))))


class TestLogin:
    """登录测试"""

    def test_success_login(self, browser, base_url):
        """
        用户名正确，密码也正确
        """
        page = LoginPage(browser)
        page.get(base_url)
        page.clear_cookie.click()

        page.login_option.click()
        page.usr_input = "admin"
        page.pwd_input = "123456"
        page.login_button.click()

        assert page.username_ele.text == "admin"

    def test_false_username(self, browser, base_url):
        """
        用户名不正确
        """
        page = LoginPage(browser)
        page.get(base_url)
        page.clear_cookie.click()

        page.login_option.click()
        page.usr_input = "admin2"
        page.pwd_input = "123456"
        page.login_button.click()

        assert page.fail_info.text == "用户" + "admin2" + " 不存在"

    def test_false_pwd(self, browser, base_url):
        """
        用户名正确，密码不正确
        """
        page = LoginPage(browser)
        page.get(base_url)
        page.clear_cookie.click()

        page.login_option.click()
        page.usr_input = "admin"
        page.pwd_input = "111111"
        page.login_button.click()

        assert "密码错误或安全问题错误" in page.fail_info.text

    def test_without_username(self, browser, base_url):
        """
        用户名为空
        """
        page = LoginPage(browser)
        page.get(base_url)
        page.clear_cookie.click()

        page.login_option.click()
        page.usr_input = ""
        page.pwd_input = "123456"
        page.login_button.click()

        assert "用户名或密码为空" in page.fail_info.text

    def test_without_pwd(self, browser, base_url):
        """
        密码为空
        """
        page = LoginPage(browser)
        page.get(base_url)
        page.clear_cookie.click()

        page.login_option.click()
        page.usr_input = "admin"
        page.pwd_input = ""
        page.login_button.click()

        assert "用户名或密码为空" in page.fail_info.text
