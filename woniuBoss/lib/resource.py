from woniuBoss.tools.service import Service
from woniuBoss.tools.utility import Utility


class Resource:
    pass


class ResourceAPI:

    def __init__(self, conf_data):
        self.session = Service.get_session(conf_data)

    def get_request(self, data):
        return self.session.get(data['url'])

    def post_request(self, post_data):
        return self.session.post(post_data['url'], post_data['data'])
