import unittest
from parameterized import parameterized

from guitest.weektest.common.report import Report
from guitest.weektest.util.service import Service
from guitest.weektest.util.utility import Utility, VerifyInSQL

# 获取测试信息
test_conf = Utility.get_json('../conf/testdata.json')
all_sale_num_test_data = Utility.get_excel_tup_list(test_conf["all_sale_num"])
vip_num_test_data = Utility.get_excel_tup_list(test_conf["vip_num"])
# print(vip_num_test_data)
# print(all_sale_num_test_data)


class ReportTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        conf_path = '../conf/base.json'
        cls.conf_path = conf_path
        cls.driver = Service.get_driver(conf_path)
        Service.login_by_cookie(cls.driver, conf_path)
        Service.open_page(cls.driver, conf_path, 'logs')

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        self.driver.refresh()

    @parameterized.expand(all_sale_num_test_data)
    def test_all_sale_num(self, total_sale, expect, test_id):
        data = {"total_sale": total_sale, "id": test_id}
        fact_sale_num = Report().get_all_sell_num(self.driver)
        # print(fact_sale_num)
        sql = 'select sum(totalprice) from sellsum'
        # 判读数据库添加内容是否与页面填写一致
        sql_data = VerifyInSQL(self.conf_path).query_one(sql)
        if sql_data is None:
            result = 'logs-fail'
        else:
            if sql_data[0] == int(fact_sale_num):
                result = 'logs-success'
            else:
                result = 'logs-fail'
        self.assertEqual(expect, result)

    @parameterized.expand(vip_num_test_data)
    def test_vip_num(self, vip_num, expect, test_id):
        data = {"total_sale": vip_num, "id": test_id}
        fact_vip_num = Report().get_vip_num(self.driver)
        # print(vip_num)
        sql = 'select count(*) from customer'
        # 判读数据库添加内容是否与页面填写一致
        sql_data = VerifyInSQL(self.conf_path).query_one(sql)
        if sql_data is None:
            result = 'logs-fail'
        else:
            if sql_data[0] == int(fact_vip_num):
                result = 'logs-success'
            else:
                result = 'logs-fail'
        self.assertEqual(expect, result)
