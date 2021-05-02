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

sys.path.insert(0, dirname(dirname(abspath(__file__))))


@ddt.ddt
class TestAdd(unittest.TestCase):
    """
       以管理员身份登录，进入后台页面，实现添加一批新分类和新板块的功能。
       需要添加的一批新分类的数据﹑新板块数据都放在json文件中.
       生成html格式的report并发送到指定邮箱
    """

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get("http://localhost/phpwind/admin.php")
        page = AddPage(cls.driver)
        page.usr_input = "admin"
        page.pwd_input = "123456"
        page.login_button.click()
        page.forum_option.click()
        cls.driver.switch_to.frame('main')
        cls.page = page

    @ddt.file_data("F:/PyProjects/pyAutoTest/test_dir/data/data_class.json")
    @ddt.unpack  # 每次运行都会从 data 中取出一组数据，动态生成一个独立的测试用例方法
    def test1_add_class(self, classname):
        u"""添加分类"""
        self.page.class_input = classname
        self.page.class_submit_button.click()
        self.page.submit_button2.click()
        self.page.confirm_button.click()
        self.assertIn(classname, self.driver.page_source)

    @ddt.file_data("F:/PyProjects/pyAutoTest/test_dir/data/data_forum.json")
    @ddt.unpack  # 每次运行都会从 data 中取出一组数据，动态生成一个独立的测试用例方法
    def test2_add_forum(self, forum_name, parent_class):
        u"""添加板块"""
        self.page.forum_input = forum_name
        s = self.driver.find_element_by_xpath('//*[@id="forum_form"]/select')
        Select(s).select_by_visible_text(">> " + parent_class)
        self.page.forum_submit_button.click()  # 提交按钮
        self.page.forum_submit_button2.click()  # 第二个提交按钮
        self.page.forum_confirm_submit.click()  # 确认提交
        self.page.forum_index.click()  # 返回板块管理主页
        self.assertIn(forum_name, self.driver.page_source)


def send_mail(report):
    yag = yagmail.SMTP(user="1716224950@qq.com", password="tydqvqptzqobbjji", host="smtp.qq.com")
    subject = "自动化测试报告"
    contents = "测试报告请查看附件"
    yag.send("1716224950@qq.com", subject, contents, report)
    print("email has send out!")


if __name__ == '__main__':
    report_html = "F:\\PyProjects\\pyAutoTest\\test_report\\" + time.strftime("%Y_%m_%d_%H_%M_%S_result.html")
    fp = open(report_html, "wb")
    suit = unittest.defaultTestLoader.discover(start_dir="F:\\PyProjects\\pyAutoTest\\test_dir", pattern="test_add.py")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"软件测试报告", description=u"用例执行过程")
    runner.run(suit)
    fp.close()
    send_mail(report_html)
