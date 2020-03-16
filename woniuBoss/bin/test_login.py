# 该模块封装与登陆有关的测试
from selenium.webdriver.common.by import By
from woniuBoss.lib.login import Login
from woniuBoss.tools.service import Service
from woniuBoss.tools.utility import Utility

import unittest
from parameterized import parameterized

# 获取登陆用的测试信息
test_conf = Utility.get_json('../conf/testdata.json')
login_info = Utility.get_excel_tup_list(test_conf["login"])
print(login_info)


# # 1.获取测试数据 2。 对每条数据执行
# # 3.实际结果actual与与其结果进行对比，如果一致则测试通过

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        conf_path = '../conf/base.json'
        cls.driver = Service.get_driver(conf_path)
        Service.open_page(cls.driver, conf_path)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        self.driver.delete_all_cookies()
        self.driver.refresh()

    @parameterized.expand(login_info)
    def test_longin(self, uname, upass, expect, tes_id):

        login_data = {
            "username": uname,
            "password": upass,

        }
        Login().do_login(self.driver, login_data)
        if Service.is_element_exist(self.driver, By.LINK_TEXT, '注销'):
            result = 'successful'
        elif '用户名不能为空' in Service.element_text(self.driver, By.ID, 'userNameMsg'):
            result = 'user_invalid'
        elif '密码不能为空' in Service.element_text(self.driver, By.ID, 'pwMsg'):
            result = 'password_invalid'
        elif '用户名或密码错误' in Service.element_text(self.driver, By.ID, 'pwMsg'):
            result = 'login-fail'
        else:
            result = 'login-fai_withNoMessage'
        # 出现错误将截图
        if result != expect:
            Service.get_error_png(self.driver)
        self.assertEqual(result, expect)


if __name__ == '__main__':
    print(login_info)
    # unittest.main(verbosity=2)
