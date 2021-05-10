from poium import Page, Element


class PublishPage(Page):
    clear_cookie = Element(xpath='//*[@id="mode-footer"]/div/div[4]/ul/li[1]/a', describe="清除cookie")
    login_option = Element(xpath='//*[@id="nav-user"]/table/tbody/tr/td/a[1]', describe="登录选项")
    usr_input = Element(xpath='//*[@id="main"]/form/div/table/tbody/tr[2]/td/div/dl[1]/dd/input',
                        describe="username输入框")
    pwd_input = Element(xpath='//*[@id="main"]/form/div/table/tbody/tr[2]/td/div/dl[2]/dd/input', describe="pwd输入框")
    login_button = Element(xpath='//*[@id="main"]/form/div/table/tbody/tr[2]/td/div/dl[5]/dd/input', describe="登录按钮")

    index_page = Element(xpath='//*[@id="nav-global"]/li[1]/a', describe="首页")
    publish_option = Element(xpath='//*[@id="td_post"]', describe="发表新帖选项")
    title_input = Element(xpath='//*[@id="atc_title"]', describe="新帖标题输入")
    content_input = Element(xpath='//*[@id="textarea"]', describe="新帖内容输入")
    commit_button = Element(xpath='//*[@id="main"]/form[1]/div/table[2]/tbody/tr[4]/td[1]/div/input[1]',
                            describe="新帖提交")
    forum3 = Element(xpath='//*[@id="fn_61"]', describe="板块3")
    back_forum3 = Element(xpath='//*[@id="breadCrumb"]/a[2]', describe="返回板块3")
