from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

kb = InlineKeyboardMarkup(rou_width=2)
b1 = InlineKeyboardButton(text='Спросить', callback_data='btnKeywords')
b2 = InlineKeyboardButton(text='Сообщить', callback_data='btnReport')

kb.add(b1,b2)
