from telebot import types


class mkey():
    def makeKeyboard(chat_id,xxx):
        valueList = ["修改", "回执单", "删单"]
        keyList = [f"['edit','{chat_id}']", f"['Journal','{chat_id}']",
                   f"['del','{chat_id}']"]

        if xxx == 1:
            valueList = ["托尼", "千万", "LL"] + valueList
            keyList = [f"['pd','{chat_id}']", f"['pd','{chat_id}']",
                       f"['pd','{chat_id}']"] + keyList

        markup = types.InlineKeyboardMarkup()

        i = 0
        while len(valueList)-i > 1:
            markup.add(types.InlineKeyboardButton(text=valueList[i],
                                                  callback_data="['value', '" + valueList[i] + "', '" + keyList[
                                                      i] + "']"),
                       types.InlineKeyboardButton(text=valueList[i + 1],
                                                  callback_data="['value', '" + valueList[i + 1] + "', '" + keyList[
                                                      i + 1] + "']"))
            i = i + 2
        else:
            if len(valueList) % 2 != 0:
                markup.add(types.InlineKeyboardButton(text=valueList[i],
                                                      callback_data="['value', '" + valueList[i ] + "', '" + keyList[
                                                          i ] + "']"))
        return markup
