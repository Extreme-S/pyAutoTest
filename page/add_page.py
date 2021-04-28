from poium import Page, Element


class AddPage(Page):
    usr_input = Element(xpath='//*[@id="wrapc"]/div/form/table/tbody/tr[1]/td/div/input', describe="账号输入框")
    pwd_input = Element(xpath='//*[@id="wrapc"]/div/form/table/tbody/tr[2]/td/div/input', describe="密码输入框")
    login_button = Element(xpath='//*[@id="wrapc"]/div/form/table/tbody/tr[3]/td/input', describe="登录按钮")
    forum_option = Element(id_='setforum', describe="设置板块选项")
