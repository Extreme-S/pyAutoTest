import json
import sys
from os.path import dirname, abspath
from time import sleep

from page.publish_page import PublishPage
import pytest

base_path = dirname(dirname(abspath(__file__)))  # 获取项目根路径
sys.path.insert(0, dirname(dirname(abspath(__file__))))

"""
如不使用插件，则pytest加载的所有用例都是乱序的
pip install pytest-order 用于控制用例执行顺序
@pytest.mark.run(order=[number])
"""


def get_data(file_path):
    """
    读取参数化文件
    :param file_path:
    :return:
    """
    data = []
    with(open(file_path, "r")) as f:
        dict_data = json.loads(f.read())
        for i in dict_data:
            data.append(tuple(i.values()))
    return data


class TestPublish:
    """论坛发帖功能的测试"""

    @pytest.mark.run(order=1)
    def test_login_case(self, browser, base_url):
        page = PublishPage(browser)
        page.get(base_url)
        page.clear_cookie.click()
        page.login_option.click()
        page.usr_input = "admin"
        page.pwd_input = "123456"
        page.login_button.click()
        page.forum3.click()
        self.page = page

    @pytest.mark.run(order=2)
    @pytest.mark.parametrize(
        "title, content",
        get_data(base_path + "/test_dir/data/data_publish.json")
    )
    def test_publish_case(self, browser, base_url, title, content):
        page = self.page
        page.publish_option.click()
        page.title_input = title  # 输入标题
        page.content_input = content  # 输入内容
        page.commit_button.click()  # 提交按钮
        sleep(2)
        assert 1 == 1
