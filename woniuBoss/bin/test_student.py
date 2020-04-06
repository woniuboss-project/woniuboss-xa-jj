import unittest

from parameterized import parameterized

from woniuBoss.lib.student import StudentApi
from woniuBoss.tools.utility import Utility

test_data_conf_path = '../conf/testdata.json'
base_conf_path = '../conf/base.json'
# base_conf_data = Utility.get_json(base_conf_path)
test_data_json = Utility.get_json(test_data_conf_path)
basic_test_data = Utility.get_excel_dict_tup_list(test_data_json['student_basic_api'])
decode_test_data = Utility.get_excel_dict_tup_list(test_data_json['student_decode_api'])
often_test_data = Utility.get_excel_dict_tup_list(test_data_json['student_often_api'])
morningtest_test_data = Utility.get_excel_dict_tup_list(test_data_json['student_morningtest_api'])
query_leave_test_data = Utility.get_excel_dict_tup_list(test_data_json['student_query_leave_api'])
save_leave_test_data = Utility.get_excel_dict_tup_list(test_data_json['student_save_leave_api'])


# print(login_test_data)


class StudentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.student = StudentApi(base_conf_path)

    def setUp(self) -> None:
        pass
        # self.student = StudentApi(base_conf_path)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.student.session.close()

    @parameterized.expand(decode_test_data)
    def test_01_decode_student(self, test_data):
        if test_data['method'] == 'GET':
            test_resp = self.student.get_request(test_data)
            test_resp_code = test_resp.status_code
            if str(test_resp_code) == '200':
                actual_status = ''
            else:
                actual_status = 'fail'
            actual = [actual_status, test_resp_code]
            expect = [test_data['expect'], test_data['code']]
        if test_data['method'] == 'POST':
            test_resp = self.student.post_request(test_data)
            test_resp_code = test_resp.status_code
            test_resp_content = test_resp.text
            print(test_resp_content)
            actual = test_resp_content
            expect = test_data['expect']

        self.assertEqual(expect, actual)

    @parameterized.expand(basic_test_data)
    def test_02_basic_student(self, test_data):
        print(test_data['data'])
        if test_data['method'] == 'GET':
            test_resp = self.student.get_request(test_data)
            test_resp_code = test_resp.status_code
            if str(test_resp_code) == '200':
                actual_status = ''
            else:
                actual_status = 'fail'
            actual = [actual_status, test_resp_code]
            expect = [test_data['expect'], test_data['code']]
        if test_data['method'] == 'POST':
            test_resp = self.student.post_request(test_data)
            test_resp_code = test_resp.status_code
            test_resp_content = test_resp.text
            # print(test_resp_content)
            actual = test_resp_content
            expect = test_data['expect']

        self.assertEqual(expect, actual)

    @parameterized.expand(often_test_data)
    def test_03_often_test_student(self, test_data):
        print(test_data['data'])
        if test_data['method'] == 'GET':
            test_resp = self.student.get_request(test_data)
            test_resp_code = test_resp.status_code
            if str(test_resp_code) == '200':
                actual_status = ''
            else:
                actual_status = 'fail'
            actual = [actual_status, test_resp_code]
            expect = [test_data['expect'], test_data['code']]
        if test_data['method'] == 'POST':
            test_resp = self.student.post_request(test_data)
            test_resp_code = test_resp.status_code
            test_resp_content = test_resp.text
            # print(test_resp_content)
            actual = test_resp_content
            expect = test_data['expect']

        self.assertEqual(expect, actual)

    @parameterized.expand(morningtest_test_data)
    def test_04_morningtest(self, test_data):
        print(test_data['data'])
        if test_data['method'] == 'GET':
            test_resp = self.student.get_request(test_data)
            test_resp_code = test_resp.status_code
            if str(test_resp_code) == '200':
                actual_status = ''
            else:
                actual_status = 'fail'
            actual = [actual_status, test_resp_code]
            expect = [test_data['expect'], test_data['code']]
        if test_data['method'] == 'POST':
            test_resp = self.student.post_request(test_data)
            test_resp_code = test_resp.status_code
            test_resp_content = test_resp.text
            # print(test_resp_content)
            actual = test_resp_content
            expect = test_data['expect']

        self.assertEqual(expect, actual)

    @parameterized.expand(query_leave_test_data)
    def test_05_query_leave(self, test_data):
        print(test_data['data'])
        if test_data['method'] == 'GET':
            test_resp = self.student.get_request(test_data)
            test_resp_code = test_resp.status_code
            if str(test_resp_code) == '200':
                actual_status = ''
            else:
                actual_status = 'fail'
            actual = [actual_status, test_resp_code]
            expect = [test_data['expect'], test_data['code']]
        if test_data['method'] == 'POST':
            test_resp = self.student.post_request(test_data)
            test_resp_code = test_resp.status_code
            test_resp_content = test_resp.text
            # print(test_resp_content)
            actual = test_resp_content
            expect = test_data['expect']
    @parameterized.expand(save_leave_test_data)
    def test_06_save_leave(self, test_data):
        print(test_data['data'])
        if test_data['method'] == 'GET':
            test_resp = self.student.get_request(test_data)
            test_resp_code = test_resp.status_code
            if str(test_resp_code) == '200':
                actual_status = ''
            else:
                actual_status = 'fail'
            actual = [actual_status, test_resp_code]
            expect = [test_data['expect'], test_data['code']]
        if test_data['method'] == 'POST':
            test_resp = self.student.post_request(test_data)
            test_resp_code = test_resp.status_code
            test_resp_content = test_resp.text
            # print(test_resp_content)
            actual = test_resp_content
            expect = test_data['expect']

        self.assertEqual(expect, actual)


if __name__ == '__main__':
    unittest.main()
