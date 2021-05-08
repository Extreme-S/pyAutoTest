import os

PRO_PATH = os.path.dirname(os.path.abspath(__file__))


class RunConfig:
    """
    运行测试配置
    """
    # 运行测试用例的目录或文件
    cases_path = os.path.join(PRO_PATH, "test_dir", "test_publish.py")

    # 配置浏览器驱动类型(chrome/firefox/chrome-headless/firefox-headless)。
    driver_type = "chrome"

    # 配置运行的 URL
    # url = "https://www.baidu.com"
    url = "http://localhost/phpwind/"  # 登录功能测试的 url
    # url = "http://localhost/phpwind/admin.php"  # 管理员添加分类板块测试的 url

    # 失败重跑次数
    rerun = "0"

    # 当达到最大失败数，停止执行
    max_fail = "5"

    # 浏览器驱动（不需要修改）
    driver = None

    # 报告路径（不需要修改）
    NEW_REPORT = None
