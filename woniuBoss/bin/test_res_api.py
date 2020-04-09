import unittest
from parameterized import parameterized
from lib.res import ResApi
from tools.utility import Utility

#后台管理
test_data_conf_path = '../conf/testdata.json'
base_conf = '../conf/base_jiang.json'
test_data = Utility.get_json(test_data_conf_path)
res_test_data = Utility.get_excel_dict_tup_list(test_data["res_api"])
print(res_test_data)


class ResTest(unittest.TestCase):
    def setUp(self) -> None:
        self.Res = ResApi(base_conf)

    def tearDown(self) -> None:
        pass

    @parameterized.expand(res_test_data)
    def test_res(self,res_data):
        res_resp = self.Res.do_res(res_data)
        res_resp_code = res_resp.status_code
        res_resp_content = res_resp.text
        print(res_resp_code)

        actual = res_resp_content
        expect = res_data['expect']
        # print(actual)
        # print(expect)

        self.assertEqual(actual,expect)






if __name__ == '__main__':
   unittest.main()
