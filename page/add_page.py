from poium import Page, Element


class AddPage(Page):
    usr_input = Element(xpath='//*[@id="wrapc"]/div/form/table/tbody/tr[1]/td/div/input', describe="账号输入框")
    pwd_input = Element(xpath='//*[@id="wrapc"]/div/form/table/tbody/tr[2]/td/div/input', describe="密码输入框")
    login_button = Element(xpath='//*[@id="wrapc"]/div/form/table/tbody/tr[3]/td/input', describe="登录按钮")
    forum_option = Element(id_='setforum', describe="设置板块选项")
    class_input = Element(xpath='/html/body/div[1]/table/tbody/tr[2]/td/form/input[3]', describe="新分类输入框")
    class_submit_button = Element(xpath='/html/body/div[1]/table/tbody/tr[2]/td/form/input[4]', describe="新分类提交按钮")
    forum_input = Element(xpath='//*[@id="forum_form"]/input[4]', describe="板块输入框")
    forum_submit_button = Element(xpath='//*[@id="forum_form"]/input[6]', describe="板块提交按钮")
    parent_forum_selector = Element(xpath='//*[@id="forum_form"]/select', describe="父板块单选框")
