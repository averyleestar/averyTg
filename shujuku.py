import pymysql

def mysql_db():
    # 连接数据库的参数
    conn = pymysql.connect(
            host="47.242.62.208", port='3309', database = "tgxe",
                      charset= "utf8", user = "tgxe",  passwd= "55GBLMkwfNBdaRRm")
if __name__ == "__main__":
    mysql_db()

# class conf():
#     def con(config):
#         if mysb == 'diyiban':
#             config = {"host": "47.242.62.208", "port": 3309, "database": "tgxe",
#                       "charset": "utf8", "user": "tgxe", "passwd": "55GBLMkwfNBdaRRm"}
#         else:
#             config = {"host": "127.0.0.1", "port": 3309, "database": "tgxe",
#                       "charset": "utf8", "user": "tgxe", "passwd": "55GBLMkwfNBdaRRm"}
#         return config

    try:
        with conn.cursor() as cursor:
            sql = select *
            from user
