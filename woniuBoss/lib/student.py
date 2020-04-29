import time

from selenium import webdriver

from woniuBoss.tools.service import Service
from woniuBoss.tools.utility import Utility


class Student:
    def click_decode_btton(self, driver):
        decode_button = driver.find_element_by_css_selector('button#btn-decrypt')
        decode_button.click()

    def input_subcode(self, driver, subcode):
        subcode_input_ele = driver.find_element_by_css_selector('input[name=secondPass]')
        Utility.send_input(subcode_input_ele, subcode)

    def click_subcode_confirm(self, driver):
        driver.find_element_by_css_selector('.btn-info').click()

    def get_decode_message(self, driver):
        message = driver.find_element_by_css_selector('.bootbox-body').text
        driver.find_element_by_css_selector('button[data-bb-handler="ok"]').click()
        return message

    def do_decode(self, driver, data_dic):
        self.click_decode_btton(driver)
        self.input_subcode(driver, data_dic["subcode"])
        self.click_subcode_confirm(driver)
        from selenium.webdriver.common.by import By
        if Service().is_element_exist(driver, By.CSS_SELECTOR, '.bootbox-body'):
            message = self.get_decode_message(driver)
            driver.find_element_by_css_selector('#secondPass-modal button[class="close"]').click()
            return message
        return None

    def select_class(self, driver, data_dic):
        student_class = driver.find_element_by_css_selector('.stu-class')
        Service().select_by_name(student_class, data_dic['class'])

    def select_orientation(self,driver,data_dic):
        student_orientation = driver.find_element_by_css_selector('.stu-orientation')
        Service().select_by_name(student_orientation, data_dic['orientation'])

    def select_status(self,driver,data_dic):
        student_status = driver.find_element_by_css_selector('.stuStatus')
        Service().select_by_name(student_status, data_dic['status'])


    def student_table(self, driver):
        student_table_list = driver.find_elements_by_css_selector('#stuInfo_table >tbody>tr')
        return student_table_list

    def get_table_page_list(self, driver):
        # 获取列表页码数量
        table_page_list = driver.find_elements_by_css_selector('.page-number')
        return table_page_list

    def get_student_info(self, driver, attribute):
        attribute_dict = {
            "class": 4,
            "field": 3,
            "status": 11,
            "name": 1
        }

        info_list = []
        if '无符合条件的记录' in driver.find_element_by_css_selector('#stuInfo_table >tbody>tr>td').text:
            return info_list
        table_page_list = self.get_table_page_list(driver)
        click_flag = 1
        while click_flag <= len(table_page_list):
            student_list = self.student_table(driver)
            for i in range(len(student_list)):
                info_list.append(driver.find_element_by_css_selector(
                    f'#stuInfo_table >tbody>tr:nth-child({i + 1})>td:nth-child({attribute_dict[attribute]})').text)
            click_flag += 1
            # 翻页
            driver.find_element_by_css_selector('.page-next>a').click()
        return info_list

    def input_student_name(self, driver, student_name):
        subcode_input_ele = driver.find_element_by_css_selector('input[name=stuName]')
        Utility.send_input(subcode_input_ele, student_name)

    def input_student_number(self, driver, student_No):
        subcode_input_ele = driver.find_element_by_css_selector('input[name=stuNo]')
        Utility.send_input(subcode_input_ele, student_No)

    def click_search_button(self, driver):
        driver.find_element_by_css_selector('button.btn.btn-padding:nth-child(2)').click()

    def search_by_name(self, driver, data_dic):
        self.input_student_name(driver, data_dic["student_name"])
        self.click_search_button(driver)

    def search_by_studentNo(self, driver, data_dic):
        self.input_student_number(driver, data_dic["student_No"])
        self.click_search_button(driver)

    def change_module(self, driver, data_dic):
        driver.find_element_by_link_text(f'{data_dic["module_name"]}').click()


class StudentApi:
    def __init__(self, conf_data):
        self.session = Service.get_session(conf_data)

    def get_request(self, data):
        return self.session.get(data['url'])

    def post_request(self, post_data):
        return self.session.post(post_data['url'], post_data['data'])
