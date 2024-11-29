import os
from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)
import asyncio
from dotenv import load_dotenv
from crud_functions import *

load_dotenv()
api = os.getenv('TELEGRAM_API')
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())
products_list = get_all_products()
connection.close()

kb_reply = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Рассчитать'),
            KeyboardButton(text='Информация'),
            KeyboardButton(text='Купить'),
        ]
    ], resize_keyboard=True
)
kb_calc = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Рассчитать норму каллорий', callback_data='calories')],
        [InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')]
    ]
)
kb_products = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Product1', callback_data='product_buying')],
        [InlineKeyboardButton(text='Product2', callback_data='product_buying')],
        [InlineKeyboardButton(text='Product3', callback_data='product_buying')],
        [InlineKeyboardButton(text='Product4', callback_data='product_buying')]
    ]
)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=kb_reply)


@dp.message_handler(text='Информация')
async def info(message):
    await message.answer('Данный бот помощет вам рассчитать Вашу дневную каллорийность.')


@dp.message_handler(text='Рассчитать')
async def start(message):
    await message.answer('Выберите опцию:', reply_markup=kb_calc)


@dp.message_handler(text='Купить')
async def get_buying_list(message):
    for product in products_list:
        with open(f'{product[0]}img.jpg', 'rb') as img:
            await message.answer_photo(img, f'Название: {product[1]} | Описание: {product[2]} | Цена: {product[3]}')

    await message.answer('Что хотите приобрести?', reply_markup=kb_products)


@dp.callback_query_handler(text='product_buying')
async def back(call):
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('(10 х вес в кг) + (6,25 х рост в см) – (5 х возраст в г) – 161')
    await call.answer()


@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()
    await call.answer()


@dp.message_handler(state=UserState.age)
async def set_age(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    result = round((10 * float(data['weight']) + 6.25 * float(data['growth']) - 5 * float(data['age']) - 161), 2)
    await message.answer(f'Ваша норма калорий по формуле Миффлина-Сан Жеора: {result}')
    await state.finish()


@dp.message_handler()
async def all_massages(message):
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
