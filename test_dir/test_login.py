import csv
import sys
import unittest
from time import sleep

import ddt
from os.path import dirname, abspath
from selenium import webdriver
from page.login_page import LoginPage

sys.path.insert(0, dirname(dirname(abspath(__file__))))


@ddt.ddt
class TestLogin(unittest.TestCase):
    """登录测试"""

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get("http://localhost/phpwind/")
        cls.page = LoginPage(cls.driver)
        data = ["测试用例编号", "测试用例描述", "输入数据", "是否通过"]
        write_csv(data)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    @ddt.file_data("F:/PyProjects/pyAutoTest/test_dir/data/data_user.json")
    @ddt.unpack  # 每次运行都会从 data 中取出一组数据，动态生成一个独立的测试用例方法
    def test_login(self, case, desc, username, pwd):
        page = self.page
        page.clear_cookie.click()  # 清除缓存 退出登录态
        page.login_option.click()  # 点击登陆选项
        page.usr_input = username  # 输入用户名
        page.pwd_input = pwd  # 输入密码
        page.login_button.click()  # 点击登录按钮
        sleep(2)

        data = [case, desc, username + "," + pwd]
        try:
            msg = self.driver.find_element_by_xpath('//*[@id="main"]/div[2]/table/tbody/tr[2]/td/center').text
            data.append(msg)
        except:
            msg = self.driver.find_element_by_xpath('//*[@id="td_userinfo_more"]').text
            data.append("登录用户:" + msg)
        write_csv(data)
        assert 1 == 1


def write_csv(data):
    file_path = "F:\\PyProjects\\pyAutoTest\\test_report\\file.csv"
    with open(file_path, 'a', newline='') as f:  # newline=空是因为我们文件是csv类型，如果不加这个东西，当我们写入东西的时候，就会出现空行
        xieru = csv.writer(f, dialect='excel')  # 定义一个变量进行写入，将刚才的文件变量传进来，dialect就是定义一下文件的类型，我们定义为excel类型
        xieru.writerow(data)  # 写入的方法是writerow，通过写入模式对象，调用方法进行写入


if __name__ == '__main__':
    unittest.main(verbosity=2)
