from aiogram import types
from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder
from asgiref.sync import sync_to_async
from app import bot, dp

import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bot.settings')
django.setup()

from main.models import Menu

class MenuAction(CallbackData, prefix='menu'):
    menu_id: int
    parent_id: int

@dp.message()
async def echo_handler2(message: types.Message) -> None:
    # запрос к базе данных длительностью 500 мс
    # response = await message.answer(
    #     f'Hello! Your name is {message.from_user.full_name} and id is {message.from_user.id}',
    #     reply_markup=InlineKeyboardMarkup(inline_keyboard=
    #                                       [[InlineKeyboardButton(text='Youtube', callback_data='1')],
    #                                        [InlineKeyboardButton(text='Youtube', callback_data='1')],
    #                                       [[InlineKeyboardButton(text='Youtube', callback_data='1')]]
    #                                        ]),
    #
    # )
    # await bot.send_message(
    #     chat_id=message.chat.id,
    #     text='some text',
    # )
    # inline_keyboard = [
    #     [InlineKeyboardButton(text='Кнопка 1', callback_data='button1'), InlineKeyboardButton(text='Кнопка 2', callback_data='button1')],
    #     [InlineKeyboardButton(text='Кнопка 3', callback_data='button1')],
    # ]
    # keyboard1 = InlineKeyboardMarkup(inline_keyboard=inline_keyboard)
    buttons = await sync_to_async(list)(Menu.objects.filter(menu_id=1))
    builder = InlineKeyboardBuilder()
    for btn in buttons:
        data = MenuAction(menu_id=btn.menu_id, parent_id=btn.parent_id)
        builder.button(text=btn.title, callback_data=data.pack())
    builder.adjust(1, 1)
    await message.answer(text='some text', reply_markup=builder.as_markup())


@dp.callback_query()
async def answer(callback_query: CallbackQuery):
    message = callback_query.message
    data = callback_query.data.split(':')
    await bot.edit_message_text(chat_id=message.chat.id,
                                message_id=message.message_id,
                                text=data[1],
                                reply_markup=message.reply_markup,
                                )