# 该模块封装与登陆有关的测试
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from woniuBoss.lib.login import Login
from woniuBoss.lib.student import Student
from woniuBoss.tools.service import Service
from woniuBoss.tools.utility import Utility

conf_path = '../conf/base.json'
login_data = {
    "userName": "wncd000",
    "userPass": "woniu123",
}
driver = Service.get_driver(conf_path)
Service().open_page(driver,conf_path)
Login().do_login(driver, data_dic=login_data)
time.sleep(1)
Service().open_page(driver, conf_path, page='student')
time.sleep(1)
Student().do_decode(driver,'woniu123')
# studentlist = Student().student_table(driver)
# for student in studentlist:
#     print(student)
# print(len(studentlist))
# for i in range(len(studentlist)):
#     print(driver.find_element_by_css_selector(f'#stuInfo_table >tbody>tr:nth-child({i+1})>td:nth-child(4)').text)
Student().select_class(driver,'WNCDC034')
print(Student().get_student_info(driver,'class'))
print(len(Student().get_student_info(driver,'class')))