from woniuBoss.tools.utility import Utility
from woniuBoss.tools.service import Service


class Report:
    pass


class ReportApi:
    def __init__(self, conf_path):
        self.session = Service().get_session(conf_path)

    def get_resp(self, dict_dict):
        return Service().get_resp(self.session, dict_dict)

    def get_region(self, data_dict):
        return self.session.post(data_dict['url'], data_dict['data'])

    def get_select_value(self, data_dict):
        return self.session.post(data_dict['url'], data_dict['data'])


if __name__ == '__main__':
    data_dict = {'url': 'http://192.168.114.220:8080/WoniuBoss2.5/select/getRegion',
          'data': {},
          'method': 'POST'}
    resp =ReportApi("../conf/base.json").get_resp(data_dict)
    print(resp.text)
    print(resp.status_code)
