import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from films import fancam

TOKEN = '6480871502:AAHne6UPzL5w39zu0PrpLHzAACImDktFU-Y'
logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
ADMINS = [1247578333]


@dp.message_handler(commands='start')
async def start(message: types.Message):
    fancam_choice = InlineKeyboardMarkup()
    for fanc in fancam:
        button = InlineKeyboardButton(text=fanc, callback_data=fanc)
        fancam_choice.add(button)
    await message.answer(text='Привіт! Я - бот-фанкам, який ти хочеш знайти?',reply_markup=fancam_choice)
                         
@dp.callback_query_handler()
async def get_fancam_info(callback_query: types.CallbackQuery):
    fancam_choice = InlineKeyboardMarkup()
    for fanc in fancam['Aespa']:
        button = InlineKeyboardButton(callback_data=fanc)
        fancam_choice.add(button)
    await callback_query.message.answer(reply_markup=fancam_choice)
    for fanc in fancam['(G)I-dle']:
        button = InlineKeyboardButton(callback_data=fanc)
        fancam_choice.add(button)
    await callback_query.message.answer(reply_markup=fancam_choice)
    for fanc in fancam['Stray Kids']:
        button = InlineKeyboardButton(callback_data=fanc)
        fancam_choice.add(button)
    await callback_query.message.answer(reply_markup=fancam_choice)
    for fanc in fancam['Itzy']:
        button = InlineKeyboardButton(callback_data=fanc)
        fancam_choice.add(button)
    await callback_query.message.answer(reply_markup=fancam_choice)
    for fanc in fancam['Blackpink']:
        button = InlineKeyboardButton(callback_data=fanc)
        fancam_choice.add(button)
    await callback_query.message.answer(reply_markup=fancam_choice)
    for fanc in fancam['Le Sserafim']:
        button = InlineKeyboardButton(callback_data=fanc)
        fancam_choice.add(button)
    await callback_query.message.answer(reply_markup=fancam_choice)
    for fanc in fancam['Nmixx']:
        button = InlineKeyboardButton(callback_data=fanc)
        fancam_choice.add(button)
    await callback_query.message.answer(reply_markup=fancam_choice)
    for fanc in fancam['Ive']:
        button = InlineKeyboardButton(callback_data=fanc)
        fancam_choice.add(button)
    await callback_query.message.answer(reply_markup=fancam_choice)
    for fanc in fancam['New Jeans']:
        button = InlineKeyboardButton(callback_data=fanc)
        fancam_choice.add(button)
    await callback_query.message.answer(reply_markup=fancam_choice)
    for fanc in fancam['Twice']:
        button = InlineKeyboardButton(callback_data=fanc)
        fancam_choice.add(button)
    await callback_query.message.answer(reply_markup=fancam_choice)
    
if __name__ == '__main__':
    executor.start_polling(dp)