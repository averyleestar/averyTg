import telebot
from button import mkey
from button import daili
from PC import ox
from rukutest import sql2

# from avery.billtest_py import sql2

bot = telebot.TeleBot('6030350843:AAHeqsmEbTbaqNBZOKlqCejwuS1FR7KLQyg')  # ,1500
# bot = AsyncTeleBot('6085539958:AAFmcobXOYV3AuRJlzlnT51-kkAIrm1UWuE')
qun_id2 = '-1001967327440'


# qun_id = '-989436172' #第二
# 6030350843:AAHeqsmEbTbaqNBZOKlqCejwuS1FR7KLQyg   我是美女
# 6255308716:AAErPqI7m2-X_5zKvnvZ46VjXbSbGoNcsaI   第一版本


# geren_id = '1106127298


@bot.message_handler(regexp="开始")
def handle_message(message):
    # print('dfsd', message)
    if str(message.text[:2]) in ['开始']:
        # rtext = sql.Bill_Into(message)
        # print(rtext)
        chat_date = message.date
        bot.send_message(chat_id=message.chat.id,
                         text="你好有什么可以帮到您",
                         reply_markup=mkey.keyboard_inline(1),
                         parse_mode='HTML')

@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    # print(call.data)
    if call.data == "菜单":
        bot.send_message(chat_id=call.message.chat.id,
                         text="你好有什么可以帮到您",
                         reply_markup=mkey.keyboard_inline(1),
                         parse_mode='HTML')

    if call.data == 'hl':
        bot.send_message(call.message.chat.id, ox(),
                         parse_mode='markdown')


    if call.data == 'fs':
        bot.send_message(chat_id=call.message.chat.id,
                         text="请选择您的支付方式",
                         reply_markup=mkey.keyboard_inline_2(1),
                         parse_mode='HTML')

    if call.data == '银行卡':
        bot.send_message(chat_id=call.message.chat.id,
                         text=f"您已选择银行卡支付方式,请选择交易代理",
                         reply_markup=mkey.keyboard_inline_3(1),
                         parse_mode='markdown')
        # bot.register_next_step_handler(call.message, next_step_edit_auth, '银行卡', call.message.json['text'] , call.message.chat.username)

    if call.data == '支付宝':
        bot.send_message(chat_id=call.message.chat.id,
                         text=f"您已选择支付宝支付方式,请选择交易代理",
                         reply_markup=mkey.keyboard_inline_3(1),
                         parse_mode='markdown')
        # bot.register_next_step_handler(call.message, next_step_edit_auth, '支付宝', call.message.json['text'] ,call.message.chat.username)

    if call.data == '现金':
        # button0 = types.InlineKeyboardButton(text="菜单", callback_data="菜单")
        # button8 = types.InlineKeyboardButton(text="白富美", callback_data="白富美")
        # button9 = types.InlineKeyboardButton(text="老阿姨", callback_data="老阿姨")
        # button10 = types.InlineKeyboardButton(text="怪叔叔", callback_data="怪叔叔")
        # button11 = types.InlineKeyboardButton(text="高富帅", callback_data="高富帅")
        # keyboard_inline_3 = types.InlineKeyboardMarkup().add(button8, button9, button10, button11,button0)
        bot.send_message(chat_id=call.message.chat.id,
                         text=f"您已选择现金支付方式,请选择交易代理",
                         reply_markup=mkey.keyboard_inline_3(1),
                         parse_mode='markdown')
        # bot.register_next_step_handler(call.message, next_step_edit_auth, '现金' )

    if call.data == '高富帅':
        key = call.message.json['text']
        idx1 = key.index('您已选择')
        idx2 = key.index('支付方式,请选择交易代理')
        output = key[idx1 + 4: idx2]
        agent_id = '-989436172'
        bot.send_message(call.message.chat.id, f"您已选择高富帅代理交易,请输入交易金额和币种", parse_mode='markdown')
        bot.register_next_step_handler(call.message, next_step_edit_auth, '高富帅', output, agent_id)

    if call.data == '白富美':
        key = call.message.json['text']
        idx1 = key.index('您已选择')
        idx2 = key.index('支付方式,请选择交易代理')
        output = key[idx1 + 4: idx2]
        agent_id = '-4478516458968'
        bot.send_message(call.message.chat.id, f"您已选择白富美代理交易,请输入交易金额和币种", parse_mode='markdown')
        bot.register_next_step_handler(call.message, next_step_edit_auth, '白富美', output, agent_id)

    if call.data == '老阿姨':
        key = call.message.json['text']
        idx1 = key.index('您已选择')
        idx2 = key.index('支付方式,请选择交易代理')
        output = key[idx1 + 4: idx2]
        agent_id = '-41247458968'
        bot.send_message(call.message.chat.id, f"您已选择老阿姨代理交易,请输入交易金额和币种", parse_mode='markdown')
        bot.register_next_step_handler(call.message, next_step_edit_auth, '老阿姨', output, agent_id)

    if call.data == '怪叔叔':
        key = call.message.json['text']
        idx1 = key.index('您已选择')
        idx2 = key.index('支付方式,请选择交易代理')
        output = key[idx1 + 4: idx2]
        agent_id = '-4124568'
        bot.send_message(call.message.chat.id, f"您已选择怪叔叔代理交易,请输入交易金额和币种", parse_mode='markdown')
        bot.register_next_step_handler(call.message, next_step_edit_auth, '怪叔叔', output, agent_id)

    if call.data[:2] == '确认':
        key = call.message.json['text']
        chat_id = call.message.chat.id
        message_id = call.message.message_id
        # print(type(key))
        messages = key.split('\n')
        if len(messages) >= 3:
            agent_name = messages[3].split('：')[1]
            # print(messages)
            # print(key)
            agent_id = daili.agency(1)[agent_name]
            # print(agent_id)
            forwardmess = f"确认\n{key}"
            bot.edit_message_text(f"已确认\n{key}", chat_id, message_id)
            bot.edit_message_reply_markup(chat_id, message_id,  reply_markup=mkey.keyboard_inline_5(chat_id))
            yy = bot.send_message(agent_id, f"订单已确认：\n{key}", parse_mode='markdown')

            if yy.json['text'][:5] == '订单已确认':
                rtext = sql2.Bill_Into(yy)
                print(f"总的来说是这样的：,{rtext}")

    if call.data[:2] == '修改':
        key = call.message.json['text']
        chat_id = call.message.chat.id
        message_id = call.message.message_id
        # bot.send_message(chat_id, f"您想修改交易信息，请按照以下模板输入新信息:\n修改\n客户:(您的telegram账号)\n支付方式:(请输入银行卡/支付宝/现金)\n交易金额:(请输入交易金额)\n代理:(请输入交易代理)", parse_mode='markdown')
        bot.edit_message_text(f"您想修改交易信息\n{key}\n请点击[菜单]按钮重新选择交易信息", chat_id, message_id)
        bot.edit_message_reply_markup(chat_id, message_id, reply_markup=mkey.keyboard_inline_5(chat_id))

    if call.data[:2] == '取消':
        key = call.message.json['text']
        chat_id = call.message.chat.id
        message_id = call.message.message_id
        # bot.send_message(chat_id, f"您想修改交易信息，请按照以下模板输入新信息:\n修改\n客户:(您的telegram账号)\n支付方式:(请输入银行卡/支付宝/现金)\n交易金额:(请输入交易金额)\n代理:(请输入交易代理)", parse_mode='markdown')
        bot.edit_message_text(f"您想取消以下交易\n{key}\n若想继续交易,请点击[菜单]按钮重新选择交易信息", chat_id, message_id)
        bot.edit_message_reply_markup(chat_id, message_id, reply_markup=mkey.keyboard_inline_5(chat_id))


def next_step_edit_auth(message, agent, output, agent_id):
    chat_id = message.message_id
    xx = bot.send_message(chat_id=message.chat.id,
                     text= f"客户：{message.chat.username}\n支付方式： {output}\n交易金额：{message.json['text']}\n代理：{agent} ",
                     reply_markup=mkey.keyboard_inline_4(chat_id),
                     parse_mode='markdown')





bot.infinity_polling()
# message.json['text']
#
#         qchat_id = bot_message.chat.id
#         qmsg_id = bot_message.message_id
#
#         geren_message = bot.send_message(chat_id=message.chat.id,
#                                          text=rtext,
#                                          reply_markup=mkey.makeKeyboard(chat_date, 1),
#                                          parse_mode='HTML')
#
#         msg_id = geren_message.message_id
#         chat_id = geren_message.chat.id
#         chat_id = f"{qchat_id},{qmsg_id},{chat_id},{msg_id}"
#
#         sql.chat_id_upda(message.date, chat_id)
#
#         # bot.edit_message_reply_markup(qun_id, qmsg_id, reply_markup=mkey.makeKeyboard(1))
#         # bot.edit_message_reply_markup(chat_id, msg_id, reply_markup=mkey.makeKeyboard(0))
#
#     # msg_date = message.date
#     # bot_date = bot_message.date
#     # bot_msid = bot_message.message_id
#     # sql.chat_id_upda(msg_date, bot_date, bot_msid)
#     # bot.delete_message(message.chat.id, message.message_id)
#
#
# @bot.callback_query_handler(func=lambda call: True)
# def handle_query(call):
#     key = call.data
#     key = key.replace(f"]'", '').replace(f"'[", '')
#     key = ast.literal_eval(key)
#     print(key[3])
#     if key[2] == 'edit':
#         Order_Status = sql.bill_Order_Status(key[3])
#         if Order_Status[0] <= 1:
#             bot.send_message(call.message.chat.id, "改单只可以改银行信息\n无法改金额,请发送最新银行信息",
#                              parse_mode='markdown')
#             bot.register_next_step_handler(call.message, next_step_edit_auth, call.message)
#         else:
#             bot.send_message(call.message.chat.id, "已经排单，无法修改，请联系上游", parse_mode='markdown')
#
#     elif key[2] == 'Journal':
#         txt = sql.bill_tol_info()
#         bot.send_message(call.message.chat.id, txt)
#
#     elif key[2] == 'del':
#         bill_del = sql.bill_del(key[3])
#         if bill_del > 0:
#             bot.delete_message(call.message.chat.id, call.message.message_id)
#             bot.delete_message(qun_id, key[4])
#
#     elif key[2] == 'pd':
#         print(call.data)
#         bill_del = sql.Bill_pd(key[1], key[3])
#         txt = f"{call.message.text}\n排单:{key[1]}"
#         bot.edit_message_text(txt, qun_id, key[4])
#         bot.edit_message_reply_markup(qun_id, key[4], reply_markup=mkey.makeKeyboard(key[3], key[4], 1))
#
#
# def next_step_edit_auth(message, call_message, chat_date, tmsg_id):
#     chat_id = call_message.chat.id
#     msg_id = call_message.message_id
#     sql.Bill_edit(message, chat_date)
#     txttime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#
#     editxt = f"{call_message.json['text'][:13]}\n最新信息:\n{message.json['text']}\n修改时间：{txttime}\n{'- -' * 10}\n修改前信息:\n{call_message.json['text'][13:]}"
#     print(chat_id, msg_id)
#     bot.edit_message_text(editxt, chat_id, msg_id)
#     bot.edit_message_reply_markup(message.chat.id, msg_id, reply_markup=mkey.makeKeyboard(chat_date, tmsg_id))
#
#     bot.edit_message_text(editxt, qun_id, tmsg_id)
#     bot.edit_message_reply_markup(qun_id, tmsg_id, reply_markup=mkey.makeKeyboard(chat_date, tmsg_id))
#
#
# @bot.message_handler(regexp="sd")
# def handle_message(message):
#     if message.reply_to_message.content_type == 'photo':
#         photo_file = message.reply_to_message.photo[0].file_id
#         sql.Bill_photo(message.json['text'], photo_file)
#
#
# # @bot.message_handler(content_types=['photo', 'audio'])
# # def handle_docs_audio(message):
# #     bot.send_message(message, message)
# #     pass
#
#
# # @bot.message_handler()
# # def echo(message):
# #     print(message)
#


# asyncio.run(bot.polling())

# @bot.message_handler(regexp="Play")
# def sign_in_handler(message):
#     print(message)
#     bot.send_message(message.chat.id, "next step", parse_mode='markdown')
#     bot.register_next_step_handler(message, next_step_add_auth)
#
#
# def next_step_add_auth(message):
#     print(message)
#     print('***'*20)


# @bot.message_handler()
# def handle_message(message):
#     if str.lower(message.text) in ['ko', 'k']:
#         bot.send_message(message.chat.id, PC.ox())
#     elif str.lower(message.text) in ['kb']:
#         bot.send_message(message.chat.id, PC.bian())
#
#
#
# pass
#
#
# @bot.message_handler(content_types=['photo', 'audio'])
# def handle_docs_audio(message):
#     bot.send_message(message.chat.id, message)
#     pass
#
# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
#     print('ddd')
#     bot.reply_to(message, "Howdy, how are you doing?")

# @bot.message_handler(commands=['sign_in'])
# def sign_in_handler(message):
#     print(message)
#     bot.send_message(message.chat.id, "next step", parse_mode='markdown')
#     bot.register_next_step_handler(message, next_step_add_auth)

# def next_step_add_auth(message):
#     load_data = message.json['photo'][0]['file_id']
#     print(load_data)
#
#     bot.send_chat_action(message.chat.id, 'typing')
#     bot.send_message(message.chat.id, "this step", parse_mode='markdown')
#
#
# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
# 	bot.reply_to(message, "Howdy, how are you doing?")
#
# @bot.message_handler()
# def handle_message(message):
#     print(message)
#     if message.text in ['JJ','小弟']:
#         bot.reply_to(message, "小弟是个帅哥")
#         print(message.message_id)
#     elif message.text in ['@ccc_6868']:
#         bot.reply_to(message, "美女，今晚你几点睡觉呀~")


# @bot.message_handler(regexp="Play")
# def handle_message(message):@ccc_6868
#     if message.text in ['Play','One more try!']:
#         bot.reply_to(message, "Howdy, h111")
#
# @bot.message_handler(regexp="SOME_REGEXP")
# def handle_message(message):
# 	bot.reply_to(message, "This is a message handler")


#
# @bot.message_handler()
# def echo(message):
#     bot.reply_to(message, message)
# print()123
