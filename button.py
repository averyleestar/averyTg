from telebot import types


class mkey():
    def keyboard_inline(self):
        button1 = types.InlineKeyboardButton(text="今日汇率", callback_data="hl")
        button2 = types.InlineKeyboardButton(text="支持方式", callback_data="fs")
        # button3 = types.InlineKeyboardButton(text="代理", callback_data="dl")
        keyboard_inline = types.InlineKeyboardMarkup().add(button1, button2)
        return keyboard_inline

    def keyboard_inline_2(self):
        button0 = types.InlineKeyboardButton(text="菜单", callback_data="菜单")
        button5 = types.InlineKeyboardButton(text="银行卡", callback_data="银行卡")
        button6 = types.InlineKeyboardButton(text="支付宝", callback_data="支付宝")
        button7 = types.InlineKeyboardButton(text="现金", callback_data="现金")
        keyboard_inline_2 = types.InlineKeyboardMarkup().add(button5, button6, button7, button0)
        return keyboard_inline_2


    def keyboard_inline_3(self):
        button0 = types.InlineKeyboardButton(text="菜单", callback_data="菜单")
        button8 = types.InlineKeyboardButton(text="白富美", callback_data="白富美")
        button9 = types.InlineKeyboardButton(text="老阿姨", callback_data="老阿姨")
        button10 = types.InlineKeyboardButton(text="怪叔叔", callback_data="怪叔叔")
        button11 = types.InlineKeyboardButton(text="高富帅", callback_data="高富帅")
        keyboard_inline_3 = types.InlineKeyboardMarkup().add(button8, button9, button10, button11, button0)
        return keyboard_inline_3




