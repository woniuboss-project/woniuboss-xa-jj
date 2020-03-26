import unittest

from parameterized import parameterized

from woniuBoss.lib.login import LoginApi
from woniuBoss.tools.utility import Utility

test_data_conf = '../conf/testdata.json'
base_conf = '../conf/base.json'
test_data_conf = Utility.get_json(test_data_conf)
login_test_data = Utility.get_excel_dict_tup_list(test_data_conf['login_api'])
# print(login_test_data)


class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        pass

    def setUp(self) -> None:
        self.logIn = LoginApi()

    def tearDown(self) -> None:
        self.logIn.session.close()

    @parameterized.expand(login_test_data)
    def test_login(self, login_data):
        print(login_data)

        login_resp = self.logIn.do_login(login_data)
        login_resp_code = login_resp.status_code
        login_resp_content = login_resp.text
        print(login_resp_content)

        actual = login_resp_content
        expect = login_data['expect']

        self.assertEqual(expect, actual)


if __name__ == '__main__':
    unittest.main()
