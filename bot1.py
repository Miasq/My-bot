import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from fancam import fancam

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
                         
@dp.callback_query_handler(text='aespa')
async def get_fancam_info(callback_query: types.CallbackQuery):
    fancam_choice = InlineKeyboardMarkup()
    for fanc in fancam['aespa']:
        button = InlineKeyboardButton(text=fanc, callback_data=fanc)
        fancam_choice.add(button)
    await callback_query.message.answer(text='Фанками', reply_markup=fancam_choice)

@dp.callback_query_handler(text='Ningning')
async def get_fancam_info2(callback_query: types.CallbackQuery):
    fancam_choice2 = InlineKeyboardMarkup()
    for i in fancam['aespa']['Ningning']:
        button = InlineKeyboardButton(text=i, callback_data=i)
        fancam_choice2.add(button)
    await callback_query.message.answer(text='Інформація:', reply_markup=fancam_choice2)
@dp.callback_query_handler(text='drama')
async def get_fancam_info3(callback_query: types.CallbackQuery):
    music = fancam['aespa']['Ningning']['drama']
    await callback_query.message.answer(text=f'Драма: {music}')
@dp.callback_query_handler(state='member')
async def members(callback_query: types.CallbackQuery, state: FSMContext):
    if callback_query.data in fancam['aespa']:
            video = "ningningdrama1.mp4"
            video_bot = open(video, 'rb')
            await bot.send_video(callback_query.id, video_bot)
            video_bot.close()
    # for fanc in fancam['(G)I-dle']:
    #     button = InlineKeyboardButton(text=fanc, callback_data=fanc)
    #     fancam_choice.add(button)
    # await callback_query.message.answer(reply_markup=fancam_choice)
    # for fanc in fancam['Stray Kids']:
    #     button = InlineKeyboardButton(text=fanc, callback_data=fanc)
    #     fancam_choice.add(button)
    # await callback_query.message.answer(reply_markup=fancam_choice)
    # for fanc in fancam['Itzy']:
    #     button = InlineKeyboardButton(text=fanc, callback_data=fanc)
    #     fancam_choice.add(button)
    # await callback_query.message.answer(reply_markup=fancam_choice)
    # for fanc in fancam['Blackpink']:
    #     button = InlineKeyboardButton(text=fanc, callback_data=fanc)
    #     fancam_choice.add(button)
    # await callback_query.message.answer(reply_markup=fancam_choice)
    # for fanc in fancam['Le Sserafim']:
    #     button = InlineKeyboardButton(text=fanc, callback_data=fanc)
    #     fancam_choice.add(button)
    # await callback_query.message.answer(reply_markup=fancam_choice)
    # for fanc in fancam['Nmixx']:
    #     button = InlineKeyboardButton(text=fanc, callback_data=fanc)
    #     fancam_choice.add(button)
    # await callback_query.message.answer(reply_markup=fancam_choice)
    # for fanc in fancam['Ive']:
    #     button = InlineKeyboardButton(text=fanc, callback_data=fanc)
    #     fancam_choice.add(button)
    # await callback_query.message.answer(reply_markup=fancam_choice)
    # for fanc in fancam['New Jeans']:
    #     button = InlineKeyboardButton(text=fanc, callback_data=fanc)
    #     fancam_choice.add(button)
    # await callback_query.message.answer(reply_markup=fancam_choice)

if __name__ == '__main__':
    executor.start_polling(dp)
