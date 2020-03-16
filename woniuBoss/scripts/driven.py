import unittest

from exec.agileone.tools.utility import Utility
from HTMLTestRunner import HTMLTestRunner


class Driven:
    def __init__(self):
        self.test_case_data = Utility.get_json('../conf/test_case.json')
        # print(self.test_case_data)

    def start_test(self):
        test_suite = unittest.TestSuite()
        loader = unittest.TestLoader()
        for value in self.test_case_data.values():
            tests_case = loader.loadTestsFromName(value)
            test_suite.addTests(tests_case)
        file_path = Utility.create_path_by_time()
        with open(file_path, 'w') as file:
            runner = HTMLTestRunner(stream=file, verbosity=2)
            runner.run(test_suite)


if __name__ == '__main__':
    Driven().start_test()
