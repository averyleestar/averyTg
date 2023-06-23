import MySQLdb

class Database():
    # **config是指连接数据库时需要的参数,这样只要参数传入正确，连哪个数据库都可以
    # 初始化时就连接数据库
    def __init__(self, **config):
        try:
            # 连接数据库的参数我不希望别人可以动，所以设置私有
            self.__conn = MySQLdb.connect(**config)
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





#
#
# class sqldb():
#     # 初始化方法
#     def __init__(self):
#         # 初始化方法中调用连接数据库的方法
#         print('g')
#         self.conn = self.get_conn()
#         # 调用获取游标的方法
#         self.cursor = self.get_cursor()
#
#     # 连接数据库的方法
#     def get_conn(self, **config):
#         print('g')
#         # **config代表不定长参数
#         conn = MySQLdb.connect(**config)
#         return conn
#
#     # 获取游标
#     def get_cursor(self):
#         cursor = self.conn.cursor()
#         return cursor
#
#     # 查询sql语句返回的所有数据
#     def select_all(self, sql):
#         self.cursor.execute(sql)
#         return self.cursor.fetchall()
#
#     # 查询sql语句返回的一条数据
#     def select_one(self, sql):
#         self.cursor.execute(sql)
#         return self.cursor.fetchone()
#
#     # 查询sql语句返回的几条数据
#     def select_many(self, sql, num):
#         self.cursor.execute(sql)
#         return self.cursor.fetchmany(num)
#
#     # 增删改除了SQL语句不一样其他都是一样的，都需要提交
#     def commit_data(self, sql):
#         try:
#             # 执行语句
#             self.cursor.execute(sql)
#             # 提交
#             self.conn.commit()
#             print("提交成功")
#         except Exception as e:
#             print("提交出错\n:", e)
#             # 如果出错要回滚
#             self.conn.rollback()
#
#     # 当对象被销毁时，游标要关闭,连接也要关闭
#     # 创建时是先创建连接后创建游标，关闭时是先关闭游标后关闭连接
#     def __del__(self):
#         self.cursor.close()
#         self.conn.close()
