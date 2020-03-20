import json


# 工具类方法都在此存放
# 对类方法增加装饰器,该方法可以直接被访问
# 应该不依赖于具体的应用，也不应依赖于具体的库


class Utility:
    @classmethod
    def get_json(cls, path):
        # print(path)
        with open(path) as file:
            content = json.load(file)
        return content

    @classmethod
    def send_input(cls, ele, keys):
        ele.click()
        ele.clear()
        ele.send_keys(keys)

    @classmethod
    def assert_equals(cls, expect, actual):
        if expect == actual:
            return True
        else:
            return False

    # 根据conf里面定义的测试数据列，返回一个包含测试数据key和value的字典的列表
    # 具体格式请运行本脚本进行查看
    @classmethod
    def get_excel(cls, conf_data):
        import xlrd
        path = conf_data["data_path"]
        sheetname = conf_data["sheetname"]
        start_row = conf_data["start_row"]
        end_row = conf_data["end_row"]
        test_data_col = conf_data["test_data_col"]
        expect_col = conf_data["except_col"]
        id_col = conf_data["id_col"]
        workbook = xlrd.open_workbook(path)
        # print(workbook)
        contents = workbook.sheet_by_name(sheetname)
        # contents = workbook.sheet_by_index(0)
        # print(contents)
        # 定义列表用于存储当前sheet页中的测试信息
        test_info = []
        # 按行读取
        for i in range(start_row, end_row + 1):
            # 读取单元格中的内容
            data = contents.cell(i, test_data_col).value
            # 获取期望结果
            expect = contents.cell(i, expect_col).value
            # h获取测试用例编号
            data_id = contents.cell(i, id_col).value
            # 单一单元格内容按换行切割
            tmp = data.split('\n')
            d = {}
            for t in tmp:
                t_tmp = t.split("=")
                d[t_tmp[0]] = t_tmp[1]
            d["expect"] = expect
            d["id"] = data_id
            test_info.append(d)
        return test_info

    # 根据conf里面定义的测试数据列，返回一个只包含测试数据value的列表
    @classmethod
    def get_excel_tup_list(cls, conf_data):
        test_info = cls.get_excel(conf_data)
        li = []
        for test in test_info:
            tup = tuple(test.values())
            li.append(tup)
        return li

    @classmethod
    def create_path_by_time(cls):
        import time
        ctime = time.strftime("%Y-%m-%d_%H-%M-%S-%ms", time.localtime())
        path = '../logs/%s.html' % ctime
        return path


# 数据库类的操作
class VerifyInSQL:
    def __init__(self, conf_path):
        coon_data = Utility.get_json(conf_path)
        import pymysql
        self.conn = pymysql.connect(coon_data["host"], coon_data["dbuser"], coon_data["dbpassword"],
                                    coon_data["dbname"], charset='utf8')
        self.cursor = self.conn.cursor()

    def close_sql(self):
        self.conn.close()
        self.cursor.close()

    def query_one(self, sql):
        self.cursor.execute(sql)
        result = self.cursor.fetchone()
        return result

    def query_all(self, sql):
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result

    def verify_batch_manage(self, batch_code):
        sql = f"select * from goods where batchname ='{batch_code}'"
        # print(self.query_all(sql))
        if self.query_all(sql):
            print(f'批次{batch_code}在数据库中查询成功')
        else:
            print(f'批次{batch_code}在数据库中未查找到')
        self.close_sql()


if __name__ == '__main__':
    confdata={
        "data_path": "../data/woniuBoss_test_cases.xlsx",
        "sheetname": "login",
        "start_row": 1,
        "end_row": 5,
        "test_data_col": 3,
        "except_col": 4,
        "id_col": 0
    }
    print(Utility().get_excel(confdata))
