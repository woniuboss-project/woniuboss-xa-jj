import unittest
from parameterized import parameterized
from lib.interview import InterViewApi
from tools.utility import Utility


test_data_conf_path = '../conf/testdata.json'
base_conf = '../conf/base_jiang.json'
test_data = Utility.get_json(test_data_conf_path)
Inter_test_data = Utility.get_excel_dict_tup_list(test_data["interview_api"])
print(Inter_test_data)


class InterViewTest(unittest.TestCase):
    def setUp(self) -> None:
        self.Inter = InterViewApi(base_conf)

    def tearDown(self) -> None:
        pass

    @parameterized.expand(Inter_test_data)
    def test_inter(self,inter_data):
        inter_resp = self.Inter.do_interview(inter_data)
        inter_resp_code = inter_resp.status_code
        inter_resp_content = inter_resp.text
        print(inter_resp_code)

        actual = inter_resp_content
        expect = inter_data['expect']
        # print(actual)
        # print(expect)

        self.assertEqual(inter_resp_code,int('200'))






if __name__ == '__main__':
   unittest.main()
