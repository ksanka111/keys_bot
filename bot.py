import config
import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from aiogram.types.message import ContentType
from aiogram.types.message import ContentTypes
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.utils import executor
from aiogram.utils.callback_data import CallbackData

from markups import kb



import sys
import re

import pandas as pd


logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.TOKEN)
db = Dispatcher(bot)

# remove new joined messages
@db.message_handler(content_types=["new_chat_members"])
async def on_user_joined(message: types.Message):
    await message.delete()

 # Скачивание в каталог с ботом с созданием подкаталогов по типу файла
# @db.message_handler(content_types=[types.ContentType.DOCUMENT])
# async def download_doc(message: types.Message):
#     await message.document.download()

# кнопки выводим
# @db.message_handler(commands='start')
# async def start(message: types.Message):
#     await message.answer("Выберите:", reply_markup=kb)
#
# # вариант 3
# @db.callback_query_handler(text='btnKeywords')
# async def btn_call(call: types.CallbackQuery) -> None:
#     await call.message.answer('Введите ключ:')
#     await call.answer()
#     @db.message_handler()
#     async def send_up(message: types.Message):
#         df = pd.read_csv('./documents/file_7.csv', names=['key', 'volume', 'link'], delimiter=';')
#         # a = df.loc[df['volume'] < 5][:10]  # новая бд со строками у которых volume < 5
#         for i in df.key:
#             if message.text in i:
#                 await message.answer(i)
#         print(df)
#
# @db.callback_query_handler(text='btnReport')
# async def btn_call(call: types.CallbackQuery) -> None:
#     await call.message.answer('Что удалить?')
#     print(call.message.answer)
#     await call.answer()
#     @db.message_handler()
#     async def send_up(message: types.Message):
#         df = pd.read_csv('./documents/file_7.csv', names=['key', 'volume', 'link'], delimiter=';')
#         a = [message.text]
#         print(a)
#         df = df[~df['key'].isin(a)]
#         print(df)

# Вариант 3
cb = CallbackData ('ikb', 'action')
cb_2 = CallbackData ('ikb_2', 'action')

ikb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton('Спросить' , callback_data=cb.new('push'))],
    [InlineKeyboardButton('Сообщить' , callback_data=cb_2.new('pus_2'))]

])

@db.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer("Выберите:", reply_markup=ikb)

@db.callback_query_handler(cb.filter())
async def btn_call(call: types.CallbackQuery, callback_data: dict) -> None:
    if callback_data['action'] == 'push':
        await call.message.answer('Введите ключ:')
        await call.answer()
        @db.message_handler()
        async def send_up(message: types.Message):
            df = pd.read_csv('./documents/file_7.csv', names=['key', 'volume', 'link'], delimiter=';')
            # a = df.loc[df['volume'] < 5][:10]  # новая бд со строками у которых volume < 5
            for i in df.key:
                if message.text in i:
                    await message.answer(i)
            print(df)

@db.callback_query_handler(cb_2.filter())
async def btn_call(call: types.CallbackQuery, callback_data: dict) -> None:
    if callback_data['action'] == 'push_2':
        await call.message.answer('Что удалить?')
        print(call.message.answer)
        await call.answer()
        @db.message_handler()
        async def send_up(message: types.Message):
            df = pd.read_csv('./documents/file_7.csv', names=['key', 'volume', 'link'], delimiter=';')
            a = [message.text]
            print(a)
            df = df[~df['key'].isin(a)]
            print(df)


if __name__ == "__main__":
    executor.start_polling(db, skip_updates=True)
