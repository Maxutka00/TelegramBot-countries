from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from allStates import Game
from loader import dp
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher import FSMContext
import json,random


@dp.message_handler(CommandStart(), state=None)
async def bot_start(message: types.Message, state:FSMContext):
	kb = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton("Начать тест"))
	await message.answer(f"Привет, {message.from_user.full_name}!", reply_markup=kb)
	await Game.answers.set()
	fp = open(r'data\eu_country.json', 'r',encoding='UTF-8')
	data_c = json.load(fp)
	l = list(data_c.items())
	random.shuffle(l)
	try:
		a = int(message.text.split()[1])
		print(a)
		if a!=0:
			max_q=a
		else:
			max_q=len(l)
	except Exception as e:
		max_q=len(l)
		await message.answer(e)

	data_an = dict(l[:max_q])
	await state.update_data(data_C=data_an)
	await state.update_data(correct_answer=0)
	await state.update_data(score=0)
	await state.update_data(city=list(data_c.values()))
	print(data_an)


