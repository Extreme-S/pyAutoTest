import sys
import json
from time import sleep

import pytest
from os.path import dirname, abspath
from page.publish_page import PublishPage

base_path = dirname(dirname(abspath(__file__)))
sys.path.insert(0, base_path)


def get_data(file_path):
    u"""
    读取参数化文件
    :param file_path:
    :return:
    """
    data = []
    with(open(file_path, "r")) as f:
        dict_data = json.loads(f.read())
        print("=========\n")
        print(dict_data)
        for i in dict_data:
            data.append(tuple(i.values()))
    return data


@pytest.mark.run(order=1)
def test_login_case(browser, base_url):
    page = PublishPage(browser)
    page.get(base_url)
    page.clear_cookie.click()
    page.login_option.click()
    page.usr_input = "admin"
    page.pwd_input = "123456"
    page.login_button.click()
    page.forum3.click()  # 进入板块分类3


@pytest.mark.run(order=2)
@pytest.mark.parametrize(
    "name, title, content",
    [
        ("1", "标题1", "这是内容1"),
        ("2", "标题2", "这是内容2"),
        ("3", "标题3", "这是内容3"),
    ],
    ids=["case1", "case2", "case3"]
)
def test_publish_case(name, title, content, browser, base_url):
    page = PublishPage(browser)
    page.publish_option.click()
    # page.title_input = "标题"  # 输入标题
    # page.content_input = "内容"  # 输入内容
    page.title_input = title  # 输入标题
    page.content_input = content  # 输入内容
    page.commit_button.click()  # 提交按钮
    sleep(2)
    assert 1 == 1
