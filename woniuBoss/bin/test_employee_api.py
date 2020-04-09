import unittest
from parameterized import parameterized

from lib.employee import EmployeeApi
from tools.utility import Utility


test_data_conf_path = '../conf/testdata.json'
base_conf = '../conf/base_jiang.json'
test_data = Utility.get_json(test_data_conf_path)
Emp_test_data = Utility.get_excel_dict_tup_list(test_data["employee_api"])
print(Emp_test_data)


class InterViewTest(unittest.TestCase):
    def setUp(self) -> None:
        self.Emp = EmployeeApi(base_conf)

    def tearDown(self) -> None:
        pass

    @parameterized.expand(Emp_test_data)
    def test_inter(self,emp_data):
        emp_resp = self.Emp.do_employee(emp_data)
        emp_resp_code = emp_resp.status_code
        emp_resp_content = emp_resp.text
        print(emp_resp_code)

        actual = emp_resp_content
        expect = emp_data['expect']
        # print(actual)
        # print(expect)

        self.assertEqual(actual,expect)






if __name__ == '__main__':
   unittest.main()
