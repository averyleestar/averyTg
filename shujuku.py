import MySQLdb
def mysql_db():
    # 连接数据库的参数
    conn = pymysql.connect(
            host="47.242.62.208", port='3309', database = "tgxe",
                      charset= "utf8", user = "tgxe",  passwd= "55GBLMkwfNBdaRRm")
# if __name__ == "__main__":
#     mysql_db()

# class conf():
#     def con(config):
#         if mysb == 'diyiban':
#             config = {"host": "47.242.62.208", "port": 3309, "database": "tgxe",
#                       "charset": "utf8", "user": "tgxe", "passwd": "55GBLMkwfNBdaRRm"}
#         else:
#             config = {"host": "127.0.0.1", "port": 3309, "database": "tgxe",
#                       "charset": "utf8", "user": "tgxe", "passwd": "55GBLMkwfNBdaRRm"}
#         return config


class Database():
    # **config是指连接数据库时需要的参数,这样只要参数传入正确，连哪个数据库都可以
    # 初始化时就连接数据库
    def __init__(self, **config):
        try:
            # 连接数据库的参数我不希望别人可以动，所以设置私有
            self.__conn = pymysql.connect(**config)
            self.__cursor = self.__conn.cursor()
        except Exception as e:
            print("数据库连接失败：\n", e)
    # 查询一条数据
    # 参数：表名table_name,条件factor_str,要查询的字段field 默认是查询所有字段*
    def select_one(self, table_name, factor_str='', field="*"):
        if factor_str == '':
            sql = f"select {field} from {table_name}"
        else:
            sql = f"select {field} from {table_name} where {factor_str}"
        self.__cursor.execute(sql)
        return self.__cursor.fetchone()

    # 查询多条数据
    # 参数：要查询数据的条数num,表名table_name,条件factor_str,要查询的字段field 默认是查询所有字段*
    def select_many(self, num, table_name, factor_str='', field="*"):
        if factor_str == '':
            sql = f"select {field} from {table_name}"
        else:
            sql = f"select {field} from {table_name} where {factor_str}"
        self.__cursor.execute(sql)
        return self.__cursor.fetchmany(num)

    # 查询全部数据
    # 参数：表名table_name,条件factor_str,要查询的字段field 默认是查询所有字段*
    def select_all(self, table_name, factor_str='', field="*"):
        if factor_str == '':
            sql = f"select {field} from {table_name}"
        else:
            sql = f"select {field} from {table_name} where {factor_str}"
        self.__cursor.execute(sql)
        return self.__cursor.fetchall()


    def sql_all(self, sql):
        self.__cursor.execute(sql)
        return self.__cursor.fetchall()

    # 新增数据
    def insert(self,table_name, key, value):
        sql = f"insert into {table_name} ( {key} ) values {value}"
        try:
            self.__cursor.execute(sql)
            self.__conn.commit()
            print("插入成功")
        except Exception as e:
            print("插入失败\n", e)
            self.__conn.rollback()

    # 修改数据
    # 参数：表名，set值(可能是一个，也可能是多个，所以用字典)，条件
    def update(self, table_name, val_obl,change_str):
        sql = f"update {table_name} set"
        # set后面应该是要修改的字段，但是可能会修改多个字段的值，所以遍历一下
        # key对应字段的名，val对应字段的值
        for key, val in val_obl.items():
            sql += f" {key} = {val},"
        # 遍历完的最后面会有一个逗号，所以给它切掉，然后再拼接条件
        # !!!空格很重要
        sql = sql[:-1]+" where "+change_str
        try:
            sqlup=self.__cursor.execute(sql)
            self.__conn.commit()
            if sqlup>0:
                return 1
            else:
                return 0
            print("修改成功")
        except Exception as e:
            print("修改失败\n", e)
            self.__conn.rollback()

    def sqlupdate(self,sql):
        try:
            self.__cursor.execute(sql)
            self.__conn.commit()
            print("修改成功")
        except Exception as e:
            print("修改失败\n", e)
            self.__conn.rollback()

    # 删除数据
    def delete(self,table_name, item):
        sql = f"delete from {table_name} where {item}"
        try:
            sqldel=self.__cursor.execute(sql)
            self.__conn.commit()
            if sqldel>0:
                return 1
            else:
                return 0

        except Exception as e:
            print("删除失败\n", e)
            self.__conn.rollback()




