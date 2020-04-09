
class Interview:
    pass


class InterViewApi:
    def __init__(self,conf_data):
        import requests
        from tools.service import Service
        self.session = Service.get_session(conf_data)
        # self.session = requests.session()

    def do_interview(self, inter_data):
        return self.session.post(inter_data['url'], inter_data['data'])
