class Res:
    pass


class ResApi:
    def __init__(self, conf_data):
        from tools.service import Service
        self.session = Service.get_session(conf_data)

    def do_res(self, res_data):
        return self.session.post(res_data['url'], res_data['data'])
