from poium import Page, Element


class LoginPage(Page):
    clear_cookie = Element(xpath='//*[@id="mode-footer"]/div/div[4]/ul/li[1]/a', describe="清除cookie")
    login_option = Element(xpath='//*[@id="nav-user"]/table/tbody/tr/td/a[1]', describe="登录选项")
    usr_input = Element(xpath='//*[@id="main"]/form/div/table/tbody/tr[2]/td/div/dl[1]/dd/input', describe="用户名输入框")
    pwd_input = Element(xpath='//*[@id="main"]/form/div/table/tbody/tr[2]/td/div/dl[2]/dd/input', describe="密码输入框")
    login_button = Element(xpath='//*[@id="main"]/form/div/table/tbody/tr[2]/td/div/dl[5]/dd/input', describe="登录按钮")
    username_ele = Element(xpath='//*[@id="td_userinfo_more"]/span', describe="用户名称元素")
    fail_info = Element(xpath='//*[@id="main"]/div[2]/table/tbody/tr[2]/td/center', describe="登陆失败提示")
