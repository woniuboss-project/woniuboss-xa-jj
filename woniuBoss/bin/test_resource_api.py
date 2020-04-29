import unittest

from parameterized import parameterized

from woniuBoss.lib.resource import ResourceAPI
from woniuBoss.tools.utility import Utility

test_data_conf_path = '../conf/testdata.json'
base_conf_path = '../conf/base.json'
# base_conf_data = Utility.get_json(base_conf_path)
test_data_json = Utility.get_json(test_data_conf_path)
basic_test_data = Utility.get_excel_dict_tup_list(test_data_json['resource_basic_api'])


class ResourceTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.resource = ResourceAPI(base_conf_path)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.resource.session.close()

    @parameterized.expand(basic_test_data)
    def test_01_decode_resource(self, test_data):
        if test_data['method'] == 'GET':
            test_resp = self.resource.get_request(test_data)
            test_resp_code = test_resp.status_code
            if str(test_resp_code) == '200':
                actual_status = ''
            else:
                actual_status = 'fail'
            actual = [actual_status, test_resp_code]
            expect = [test_data['expect'], test_data['code']]
        if test_data['method'] == 'POST':
            test_resp = self.resource.post_request(test_data)
            test_resp_code = test_resp.status_code
            test_resp_content = test_resp.text
            # print(test_resp_content)
            actual = test_resp_content
            expect = test_data['expect']

        self.assertEqual(expect, actual)


if __name__ == '__main__':
    unittest.main()
