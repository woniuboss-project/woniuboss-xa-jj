import time
import unittest

from parameterized import parameterized
from selenium.webdriver.common.service import Service
from exec.agileone.lib.login import Login
from exec.agileone.lib.notice import Notice

from exec.agileone.tools.utility import Utility

test_conf = Utility.get_json('../conf/testdata.json')
notice_info = Utility.get_excel_tup_list(test_conf["login"])
print(notice_info)
login_data = {"username": "admin", "password": "admin"}


class NoticeTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        conf_path = 'conf/base.json'
        cls.driver = Service.get_driver(conf_path)
        cls.driver.get("http://192.168.114.220/agileone")
        Login().do_login(cls.driver, login_data)
        cls.driver.find_element_by_link_text('※ 公告管理 ※').click()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        # self.driver.delete_all_cookies()
        self.driver.refresh()

    @parameterized.expand(notice_info)
    def test_add_notice(self, headline, content, scope, expireddate, expect):

        notice_data = {
            "headline": headline,
            "content": content,
            "scope": scope,
            "expireddate": expireddate,
            "expect": expect
        }
        Notice().add_notice(self.driver, notice_data)
        time.sleep(0.3)
        if '成功啦' in Service.element_text(self.driver, By.ID, 'msg'):
            result = 'success'

        elif '公告标题' in Service.element_text(self.driver, By.ID, 'msg'):
            result = 'title_invalid'
        elif '公告范围' in Service.element_text(self.driver, By.ID, 'msg'):
            result = 'scope_invalid'
        elif '日期/时间' in Service.element_text(self.driver, By.ID, 'msg'):
            result = 'time_invalid'
        else:
            result = 'fail'
        self.assertEqual(result, expect)

    @parameterized.expand(notice_info)
    def test_modify_notice(self, headline, content, scope, expireddate, expect):

        notice_data = {
            "headline": headline,
            "content": content,
            "scope": scope,
            "expireddate": expireddate,
            "expect": expect
        }
        Notice().modify_notice(self.driver, notice_data)
        time.sleep(0.5)
        if '成功啦' in Service.element_text(self.driver, By.ID, 'msg'):
            result = 'success'

        elif '公告标题' in Service.element_text(self.driver, By.ID, 'msg'):
            result = 'title_invalid'
        elif '公告范围' in Service.element_text(self.driver, By.ID, 'msg'):
            result = 'scope_invalid'
        elif '日期/时间' in Service.element_text(self.driver, By.ID, 'msg'):
            result = 'time_invalid'
        else:
            result = 'fail'
        self.assertEqual(result, expect)


if __name__ == '__main__':
    unittest.main(verbosity=2)
    # driver = Service.get_driver(conf_path)
    #   Service.open_page(driver, conf_path)
    #   Login().do_login(driver, login_data)
    #
    # print(assertEqualdd_notice_data_tup_list)
