from telebot import types


class mkey():
    def keyboard_inline(chat_username):
        button1 = types.InlineKeyboardButton(text="今日汇率", callback_data="hl")
        button2 = types.InlineKeyboardButton(text="支持方式", callback_data="fs")
        button0 = types.InlineKeyboardButton(text="交易记录", callback_data=f"jyjl,{chat_username}")
        # button3 = types.InlineKeyboardButton(text="代理", callback_data="dl")
        keyboard_inline = types.InlineKeyboardMarkup().add(button1, button2, button0)
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

    def keyboard_inline_4(chat_id):
        button0 = types.InlineKeyboardButton(text="菜单", callback_data="菜单")
        button12 = types.InlineKeyboardButton(text="确认", callback_data=f"确认,{chat_id}")
        button13 = types.InlineKeyboardButton(text="修改", callback_data=f"修改,{chat_id}")
        button14 = types.InlineKeyboardButton(text="取消", callback_data=f"取消,{chat_id}")
        keyboard_inline_4 = types.InlineKeyboardMarkup().add(button12, button13, button14, button0)
        return keyboard_inline_4

    def keyboard_inline_5(chat_id):
        button0 = types.InlineKeyboardButton(text="菜单", callback_data="菜单")
        keyboard_inline_5 = types.InlineKeyboardMarkup().add(button0)
        return keyboard_inline_5


class daili():
    def agency(self):
        agent_id = {"高富帅": "-989436172", "白富美": "-4478516458968", "老阿姨": "-41247458968", "怪叔叔": "-4124568"}
        return agent_id

#
# {'content_type': 'text', 'id': 1259, 'message_id': 1259,
#  'from_user': {'id': 6030350843, 'is_bot': True, 'first_name': '我是美女', 'username': 'testmeinv_bot',
#                'last_name': None, 'language_code': None, 'can_join_groups': None, 'can_read_all_group_messages': None,
#                'supports_inline_queries': None, 'is_premium': None, 'added_to_attachment_menu': None},
#  'date': 1687576573,
#  'chat': {'id': 1106127298, 'type': 'private', 'title': None, 'username': 'lolodada', 'first_name': 'Miso',
#           'last_name': None, 'is_forum': None, 'photo': None, 'bio': None, 'join_to_send_messages': None,
#           'join_by_request': None, 'has_private_forwards': None, 'has_restricted_voice_and_video_messages': None,
#           'description': None, 'invite_link': None, 'pinned_message': None, 'permissions': None,
#           'slow_mode_delay': None, 'message_auto_delete_time': None, 'has_protected_content': None,
#           'sticker_set_name': None, 'can_set_sticker_set': None, 'linked_chat_id': None, 'location': None,
#           'active_usernames': None, 'emoji_status_custom_emoji_id': None, 'has_hidden_members': None,
#           'has_aggressive_anti_spam_enabled': None}, 'sender_chat': None, 'forward_from': None,
#  'forward_from_chat': None, 'forward_from_message_id': None, 'forward_signature': None, 'forward_sender_name': None,
#  'forward_date': None, 'is_automatic_forward': None, 'reply_to_message': None, 'via_bot': None, 'edit_date': None,
#  'has_protected_content': None, 'media_group_id': None, 'author_signature': None, 'text': '你好有什么可以帮到您',
#  'entities': None, 'caption_entities': None, 'audio': None, 'document': None, 'photo': None, 'sticker': None,
#  'video': None, 'video_note': None, 'voice': None, 'caption': None, 'contact': None, 'location': None, 'venue': None,
#  'animation': None, 'dice': None, 'new_chat_member': None, 'new_chat_members': None, 'left_chat_member': None,
#  'new_chat_title': None, 'new_chat_photo': None, 'delete_chat_photo': None, 'group_chat_created': None,
#  'supergroup_chat_created': None, 'channel_chat_created': None, 'migrate_to_chat_id': None,
#  'migrate_from_chat_id': None, 'pinned_message': None, 'invoice': None, 'successful_payment': None,
#  'connected_website': None, 'reply_markup': {'row_width': 3,
#                                              'keyboard': [[ < telebot.types.InlineKeyboardButton object at
#                                                           0x0000026359D17690 >, < telebot.types.InlineKeyboardButton
#                                              object at 0x0000026359D17610 >, < telebot.types.InlineKeyboardButton
# object
# at
# 0x0000026359D17650 >]]}, 'message_thread_id': None, 'is_topic_message': None, 'forum_topic_created': None, 'forum_topic_closed': None, 'forum_topic_reopened': None, 'has_media_spoiler': None, 'forum_topic_edited': None, 'general_forum_topic_hidden': None, 'general_forum_topic_unhidden': None, 'write_access_allowed': None, 'user_shared': None, 'chat_shared': None, 'json': {
#     'message_id': 1259,
#     'from': {'id': 6030350843, 'is_bot': True, 'first_name': '我是美女', 'username': 'testmeinv_bot'},
#     'chat': {'id': 1106127298, 'first_name': 'Miso', 'username': 'lolodada', 'type': 'private'}, 'date': 1687576573,
#     'text': '你好有什么可以帮到您', 'reply_markup': {'inline_keyboard': [
#         [{'text': '今日汇率', 'callback_data': 'hl'}, {'text': '支持方式', 'callback_data': 'fs'},
#          {'text': '交易记录', 'callback_data': 'jyjl,1'}]]}}}
