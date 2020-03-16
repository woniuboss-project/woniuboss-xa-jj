from selenium import webdriver
from selenium.webdriver.support.select import Select

from woniuBoss.tools.utility import Utility


class Service:
    @classmethod
    def get_driver(cls, conf_path):
        browser = Utility.get_json(conf_path)["browser"]
        # 通过反射机制可以直接获取相应的结果
        driver = getattr(webdriver, browser, webdriver.Chrome)()
        driver.implicitly_wait(0.5)
        driver.maximize_window()
        return driver

    @classmethod
    def is_element_exist(cls, driver, how, what):
        from selenium.common.exceptions import NoSuchElementException
        result = False
        try:
            driver.find_element(how, what)
            result = True
        except NoSuchElementException:
            pass
        finally:
            return result

    # 获取下拉菜单选项
    @classmethod
    def get_select_values(cls, driver, how, what):
        ele = driver.find_element(how, what)
        all_options = ele.find_elements_by_tag_name("option")
        all_options_li = []
        for option in all_options:
            all_options_li.append(option.text)
        print(all_options_li)

    @classmethod
    def element_text(cls, driver, how, what):
        from selenium.common.exceptions import NoSuchElementException
        result = ''
        try:
            ele = driver.find_element(how, what)
            result = ele.text
        except NoSuchElementException:
            pass
        finally:
            return result

    @classmethod
    def select_random(cls, selector):
        import random
        Select(selector).select_by_index(random.randint(0, len(Select(selector).options) - 1))
    # 依照显示的选项名进行选择
    @classmethod
    def select_by_name(cls, selector, name):
        Select(selector).select_by_visible_text(name)

    # 去掉只读属性
    @classmethod
    def remove_readonly(cls, driver, element_id=None, element_class=None):
        if element_id is not None:
            driver.execute_script(f'document.getElementById("{element_id}").readOnly=false')
        if element_class is not None:
            driver.execute_script(f'document.getElementsByClassName("{element_class}").readOnly=false')

    # 打开页面
    @classmethod
    def open_page(cls, driver, conf_path, page=None):
        aurl = Utility.get_json(conf_path)["aurl"]
        host = Utility.get_json(conf_path)["host"]
        port = Utility.get_json(conf_path)["port"]
        # 构造url打开网页
        if page is not None:
            driver.get(f"http://{host}:{port}/{aurl}/{page}")
        else:
            driver.get(f"http://{host}:{port}/{aurl}")

    # 绕过登陆使用cookies
    @classmethod
    def login_by_cookie(cls, driver, conf_path, page=None):

        cls.open_page(driver, conf_path)
        data = Utility.get_json(conf_path)
        driver.add_cookie({'name': 'username', 'value': data['username']})
        driver.add_cookie({'name': 'password', 'value': data['password']})
        driver.refresh()
        # # 判断是否登陆成功
        # if ExistElement(self.driver).by_link('注销'):
        #     print('登陆成功')
        # else:
        #     print('登陆失败')
        # import time
        # time.sleep(0.5)
        cls.open_page(driver, conf_path, page)
        # cls.open_page(driver, conf_path, page)

    # def open_page(self):
    #     aurl = Utility.get_json(self.path)["aurl"]
    #     host = Utility.get_json(self.path)["host"]
    #     port = Utility.get_json(self.path)["port"]
    #     # 构造url打开网页
    #     self.driver.get(f"http://{host}:{port}/{aurl}")

    # 截图，仅进行截图
    @classmethod
    def get_png(cls, driver, png_path):
        # 截图
        driver.save_screenshot(png_path)

    @classmethod
    def get_error_png(cls, driver):
        # 格式化时间
        import time
        ctime = time.strftime("%Y-%m-%d_%H-%M-%S-%ms", time.localtime())
        png_path = '../bugPng/error_%s.png' % ctime
        # 截图
        cls.get_png(driver, png_path)


if __name__ == '__main__':
    Service.get_driver()
