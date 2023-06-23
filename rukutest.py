import datetime
import re

from shujuku import Database

mysb = 'diyiban'


class conf():
    def con(config):
        if mysb == 'diyiban':
            config = {"host": "47.242.62.208", "port": 3309, "database": "tgxe",
                      "charset": "utf8", "user": "tgxe", "passwd": "55GBLMkwfNBdaRRm"}
        else:
            config = {"host": "127.0.0.1", "port": 3309, "database": "tgxe",
                      "charset": "utf8", "user": "tgxe", "passwd": "55GBLMkwfNBdaRRm"}

        return config


class sql2():

    def Bill_Into(message):  # 账单入库
        try:
            # txt = message.json['text']
            txt1 = message.json['text'].split('\n')
            amount = txt1[3].split('：')[1]
            agent = txt1[4].split('：')[1]
            paytype = txt1[2].split('：')[1]
            customer = txt1[1].split('：')[1]
            print(f"txt1 是,{txt1}")
            # Bill_Inf_dict = {}
            # Bill_other = ''
            # for i in txt1:
            #     if i.find("订单已确认") >= 0:
            #         pass
            #     elif any(key in i for key in ["金额"]):
            #         amount = re.findall(r"\d+\.?\d*", i)[0]
            #     elif any(key in i for key in ["客户"]):
            #         customer = txt1[1].split('：')[1]
            #     elif any(key in i for key in ["支付方式"]):
            #         paytype = txt1[2].split('：')[1]
            #     elif any(key in i for key in ["代理"]):
            #         agent = txt1[4].split('：')[1]
            #     elif i.find("支付方式") >= 0:
            #         Bill_Inf_dict['客户'] = i
            #     elif i.find("支付方式") >= 0:
            #         Bill_Inf_dict['支付方式'] = i
            #     elif i.find("代理") >= 0:
            #         Bill_Inf_dict['代理'] = i
            #     else:
            #         Bill_other += i + '\n'
            # print('1111')
            # if all(k in Bill_Inf_dict.keys() for k in ['客户', '支付方式', '代理']) == True:
            #     operation_ID = message.from_user.id
            #     Bill_Inf = f"{Bill_Inf_dict['客户']}\n{Bill_Inf_dict['支付方式']}\n{Bill_Inf_dict['代理']}\n{Bill_other}入单时间:{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
            #     print(Bill_Inf)
            operation_ID = message.from_user.id
            chat_date = message.json['date']
            # print(type(chat_date), chat_date)
            data = (operation_ID, chat_date, "", message.json['text'] , amount, customer, paytype, agent)
            print('data', data)
            config = conf().con()
            db = Database(**config)
            db.insert(mysb, 'id,chat_date,chat_id,Bill_Info, amount,customer,paytype,agent',
                      data)
                # Bill_In = sql2.Bill_Info(chat_date)
                # if Bill_In != None:
                #     return Bill_In
        except IndexError:
            print("Error: 没有找到文件或读取文件失败")
#
    # def Bill_edit(message, chat_date):  # 修改订单
    #     config = conf().con()
    #     db = Database(**config)
    #     Bill_In = db.select_one(mysb, f"chat_date='{chat_date}'",
    #                             "chat_date,Bill_Info,edit_info,Payment_Types,exchange_rate,amount")
    #     txt1 =Bill_In[1].split('\n')
    #     Bill_Inf_dict = {}
    #     Bill_other = ''
    #     Bill_Inf_dict['金额']=Bill_In[5]
    #     Bill_Inf_dict['汇率']=Bill_In[4]
    #
    #     for i in txt1:
    #         if i.find("账号") >= 0:
    #             Bill_Inf_dict['账号'] = i
    #         elif i.find("姓名") >= 0:
    #             Bill_Inf_dict['姓名'] = i
    #         elif i.find("银行") >= 0:
    #             Bill_Inf_dict['银行'] = i
    #
    #     newtxt = message.json['text']
    #     for i in newtxt:
    #         if any(key in i for key in ["金额"]):
    #             Bill_Inf_dict['金额'] = re.findall(r"\d+\.?\d*", i)[0]
    #         elif i.find("汇率") >= 0:
    #             Bill_Inf_dict['汇率'] = re.findall(r"\d+\.?\d*", i)[0]
    #         elif i.find("姓名") >= 0:
    #             Bill_Inf_dict['姓名'] = i
    #         elif i.find("账号") >= 0:
    #             Bill_Inf_dict['账号'] = i
    #         elif i.find("银行") >= 0:
    #             Bill_Inf_dict['银行'] = i
    #         else:
    #             Bill_other += i + '\n'
    #
    #
    #     timetxt = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    #
    #     config = conf().con()
    #     db = Database(**config)
    #     db.update(mysb, edit_info, f"chat_date={chat_id}")
    #
    # def Bill_Info(chat_date):  # 查询订单信息
    #     config = conf().con()
    #     db = Database(**config)
    #     Bill_In = db.select_one(mysb, f"chat_date={chat_date}",
    #                             "chat_date,Bill_Info,edit_info,paytype,amount")
    #     Bill_Inf = "\n".join(Bill_In[1].split('\n')[0:-1])
    #     Bill_time = Bill_In[1].split('\n')[-1]
        # rtext = f"单号:{Bill_In[0]}\n\n渠道:{Bill_In[3]}\n{Bill_Inf}\n汇率:{Bill_In[4]}\n金额:{Bill_In[5]}\n\n{Bill_time}"
        # return rtext
    #
    # def chat_id_upda(msg_date, chat_id):  # 发送信息后更新ID
    #     config = conf().con()
    #     db = Database(**config)
    #     db.update(mysb, {"chat_id": f"'{chat_id}'"}, f"chat_date='{msg_date}'")
    #
    # def chat_id(chat_id):  # 查询群聊ID和个人ID
    #     config = conf().con()
    #     db = Database(**config)
    #     chat_date = db.select_one(mysb, f"chat_date={chat_id}", 'chat_id')
    #     return chat_date[0]
    #
    # def bill_Order_Status(date_id):  # 查询订单状态
    #     config = conf().con()
    #     db = Database(**config)
    #     Order_Status = db.select_one(mysb, f"chat_date={date_id}", 'Order_Status')
    #     return Order_Status
    #
    # def bill_tol_info():  # 查询生成账单
    #     config = conf().con()
    #     db = Database(**config)
    #     sql = "select supplier,Payment_Types,sum(amount) as 'samount' ,count(amount) as 'camount' from {mysb} where Order_Status = 1 group by supplier,Payment_Types,supplier order by supplier"
    #     totel = db.sql_all(sql)
    #     ztxt = ''
    #     tsamount = 0
    #     tcamount = 0
    #     for data in totel:
    #         supplier = data[0]
    #         Payment_Types = data[1]
    #         samount = data[2]
    #         camount = data[3]
    #         tsamount += samount
    #         tcamount += camount
    #         ztxt += f"{Payment_Types}:{tcamount}笔  总金额:{tsamount}\n"
    #     txt = ''
    #     Order_Status = db.select_all(mysb, 'Order_Status=1', 'chat_id,Bill_Info,amount')
    #     for data in Order_Status:
    #         txt += "\n单号:%s\n%s\n金额:%s\n" % (data[0], data[1][:-26], int(data[2]))
    #     btxt = f"总金额:{tsamount}\n总笔数:{tcamount}\n{ztxt}\n{txt}"
    #     return btxt

    # 0入单  1排单  2上游打款  3等待水单  4完成  5退款重打
    #
    # # 账单修改
    #
    # def bill_del(chat_id):  # 删除订单
    #     config = conf().con()
    #     db = Database(**config)
    #     delbill = db.update(mysb, {"bill_del": "1"}, f"chat_id='{chat_id}' and bill_del=0")
    #     return delbill
    #
    # def Bill_pd(supplier, chat_id):  # 排单模块
    #     config = conf().con()
    #     db = Database(**config)
    #     db.update(mysb, {"supplier": f"'{supplier}'", "Order_Status": 1}, f"chat_date={chat_id}")
    #
    # def Bill_qd(Payment_Types, chat_id):  # 渠道模块
    #     config = conf().con()
    #     db = Database(**config)
    #     db.update(mysb, {"Payment_Types": f"'{Payment_Types}'"}, f"chat_date={chat_id}")
    #     Order_Status = db.select_one(mysb, f"chat_date={chat_id}",
    #                                  'chat_date,Bill_Info,Payment_Types,exchange_rate,amount')
    #     print(Order_Status)
    #
    # def Bill_photo(amount, photo_file):
    #     amount = re.findall(r"\d+\.?\d*", amount)[0]
    #     config = conf().con()
    #     db = Database(**config)
    #     sql = f"select chat_id,msg_id from  {mysb}  where Order_Status=2 and amount = {amount}"
    #     Bill_photo = db.sql_all(sql)
    #     if len(Bill_photo) == 1:
    #         db.insert('photo_file_id', 'chat_id,msg_id,file_id', (Bill_photo[0][0], Bill_photo[0][1], photo_file))
    #         db.update(mysb, {"Order_Status": 3}, f"chat_id={Bill_photo[0][1]}")
    #     else:
    #         for data in Bill_photo:
    #             Bill_photo = data[0]
    #             print(Bill_photo)
    #     print(Bill_photo[0][0], len(Bill_photo), Bill_photo)

# # 稍等
