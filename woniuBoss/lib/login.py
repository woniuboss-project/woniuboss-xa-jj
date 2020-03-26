from woniuBoss.tools.utility import Utility


class Login:
    # 向用用户名输入框中输入
    def input_uname(self, driver, username):
        uname = driver.find_element_by_css_selector('input[name=userName]')
        Utility.send_input(uname, username)

    def input_upass(self, driver, password):
        upass = driver.find_element_by_css_selector('input[name=userPass]')
        Utility.send_input(upass, password)

    def click_button(self, driver):
        driver.find_element_by_css_selector('button.btn-save').click()

    def do_login(self, driver, data_dic):
        self.input_uname(driver, data_dic["userName"])
        self.input_upass(driver, data_dic["userPass"])
        self.click_button(driver)


class LoginApi:
    def __init__(self):
        import requests
        self.session = requests.session()

    def do_login(self, login_data):
        return self.session.post(login_data['url'], login_data['data'])