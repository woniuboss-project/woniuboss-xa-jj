class Employee:
    pass


class EmployeeApi:
    def __init__(self,conf_data):
        from tools.service import Service
        self.session = Service.get_session(conf_data)


    def do_employee(self, employee_data):
        return self.session.post(employee_data['url'], employee_data['data'])