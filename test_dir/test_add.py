import sys
from time import sleep

import ddt
import pytest
from os.path import dirname, abspath

from page.add_page import AddPage

sys.path.insert(0, dirname(dirname(abspath(__file__))))


@ddt.ddt
class TestAdd:
    """添加分类测试"""

    @ddt.file_data("F:/program/PythonWorkSpace/selenium/exp/exp_unittest/data/test_add_type.json")
    def test_add_class(self, browser, base_url):
        """
       以管理员身份登录，进入后台页面，实现添加一批新分类和新板块的功能。
       需要添加的一批新分类的数据﹑新板块数据都放在json文件中.
       生成html格式的report并发送到指定邮箱
        """
        page = AddPage(browser)
        page.get(base_url)
        page.usr_input = "admin"
        page.pwd_input = "123456"
        page.login_button.click()
        page.forum_option.click()
        browser.switch_to.frame('main')
