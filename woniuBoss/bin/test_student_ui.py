# 该模块封装与登陆有关的测试
import time
import unittest

from parameterized import parameterized
from selenium import webdriver
from selenium.webdriver.common.by import By

from woniuBoss.lib.login import Login
from woniuBoss.lib.student import Student
from woniuBoss.tools.service import Service
from woniuBoss.tools.utility import Utility

test_conf = Utility.get_json('../conf/testdata.json')

student_basic_decode_data = Utility.get_excel_dict_tup_list(test_conf["student_basic_decode_ui"])
student_basic_search_name_data = Utility.get_excel_dict_tup_list(test_conf["student_basic_search_name_ui"])

conf_path = '../conf/base.json'
login_data = {
    "userName": "wncd000",
    "userPass": "woniu123",
}


# driver = Service.get_driver(conf_path)
# Service().open_page(driver,conf_path)
# Login().do_login(driver, data_dic=login_data)
# time.sleep(1)
# Service().open_page(driver, conf_path, page='student')
# time.sleep(1)
# Student().do_decode(driver,'woniu123')
# studentlist = Student().student_table(driver)
# for student in studentlist:
#     print(student)
# print(len(studentlist))
# for i in range(len(studentlist)):
#     print(driver.find_element_by_css_selector(f'#stuInfo_table >tbody>tr:nth-child({i+1})>td:nth-child(4)').text)
# Student().select_class(driver,'WNCDC034')
# print(Student().get_student_info(driver,'class'))
# print(len(Student().get_student_info(driver,'class')))

class StudentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        conf_path = '../conf/base.json'
        cls.driver = Service.get_driver(conf_path)
        cls.driver.implicitly_wait(2)
        Service.open_page(cls.driver, conf_path)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def setUp(self) -> None:
        Login().do_login(self.driver, data_dic=login_data)
        time.sleep(0.5)
        Service().open_page(self.driver, conf_path, page='student')

    def tearDown(self) -> None:
        self.driver.delete_all_cookies()
        self.driver.refresh()

    @parameterized.expand(student_basic_decode_data)
    def test_decode(self, student_test_data):
        message = Student().do_decode(self.driver, student_test_data)
        time.sleep(0.5)

        student_name_list = Student().get_student_info(self.driver, 'name')

        if student_test_data['expect'] == 'success':
            code_is_encrypt = False
            if message is not None:
                result = 'fail'
            else:
                result = 'success'
        else:
            code_is_encrypt = True
            # 判断提示消息
            if message == student_test_data['expect']:
                result = 'fail'
            else:
                result = 'success'
        if result == 'success':
            for student_name in student_name_list:
                if code_is_encrypt:
                    if not "***" in student_name:
                        result = 'fail'
                        break
                else:
                    if "***" in student_name:
                        result = 'fail'
                        break
            else:
                result = 'success'

        self.assertEqual(result, 'success')

    @parameterized.expand(student_basic_search_name_data)
    def test_search_class(self, student_test_data):
        # 解密
        student_test_data["subcode"]='woniu123'
        message = Student().do_decode(self.driver, student_test_data)
        time.sleep(0.5)
        Student().select_class(self.driver,student_test_data)
        student_class_list = Student().get_student_info(self.driver, 'class')

        for student_class in student_class_list:
            if student_test_data['class'] != student_class:
                result = 'fail'
                break
        else:
            result = 'success'

        self.assertEqual(result, student_test_data["expect"])


if __name__ == '__main__':
    unittest.main(verbosity=2)
