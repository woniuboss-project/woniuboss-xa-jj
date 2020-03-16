import time

from selenium.webdriver.support.select import Select

from exec.agileone.tools.utility import Utility


class Notice:

    def modify_expireddate(self, driver, expireddate):
        expireddate_ele = driver.find_element_by_id('expireddate')
        Utility.send_input(expireddate_ele, expireddate)

    def modify_headline(self, driver, headline):
        headline_ele = driver.find_element_by_id('headline')
        Utility.send_input(headline_ele, headline)

    def modify_scope(self, driver, scope):
        scope_ele = driver.find_element_by_id('scope')
        # Utility.send_input(scope_ele, scope)
        # Select(scope_ele).select_by_index(int(scope))
        Select(scope_ele).select_by_value(scope)

    def modify_content(self, driver, content):
        content_ele = driver.find_element_by_class_name('ke-iframe')
        driver.switch_to.frame(content_ele)
        inside_content_ele = driver.find_element_by_xpath('/html/body')
        Utility.send_input(inside_content_ele, content)
        driver.switch_to.default_content()

    def add_notice(self, driver, data_dic):
        self.modify_expireddate(driver, data_dic["expireddate"])
        self.modify_content(driver, data_dic["content"])
        self.modify_scope(driver, data_dic["scope"])
        self.modify_headline(driver, data_dic["headline"])
        driver.find_element_by_id("add").click()

    def modify_notice(self, driver, data_dic):
        time.sleep(0.2)
        total = driver.find_element_by_id('totalRecord').text
        import random
        ran_index = random.randint(1, int(total))
        driver.find_element_by_xpath('//tbody[@id="dataPanel"]/tr[%d]/td[5]/label[1]' % (ran_index)).click()
        self.modify_expireddate(driver, data_dic["expireddate"])
        self.modify_content(driver, data_dic["content"])
        self.modify_scope(driver, data_dic["scope"])
        self.modify_headline(driver, data_dic["headline"])
        driver.find_element_by_id("edit").click()
