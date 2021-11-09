from aiogram import types
from states.allStates import Game
from loader import dp
from loader import bot
import aiogram.dispatcher.filters as filters
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove,ReplyKeyboardMarkup, KeyboardButton
import random

@dp.message_handler(commands=["stop"], state="*")
async def stop_game(message: types.Message, state:FSMContext):
	await message.answer(f"end")
	await state.finish()
@dp.message_handler(state = Game.answers, content_types=types.ContentTypes.TEXT)
async def game_answers(message: types.Message, state:FSMContext):
	data = await state.get_data()
	correct_answer = data['correct_answer']
	print(correct_answer)
	if correct_answer != 0:
		if correct_answer == message.text:
			score = data["score"]
			score+=1
			await state.update_data(score=score)
	data_c = data['data_C']
	print(data_c)
	city = data["city"]
	try:
		question = list(data_c.popitem())
	except KeyError:
		await message.answer(f"Score: {score}", reply_markup=ReplyKeyboardRemove())
		await state.finish()
		return
	answers_kb = ReplyKeyboardMarkup(resize_keyboard=True)
	num_of_ans=4
	ch = random.randint(0,num_of_ans-1)
	print(ch)
	for ans_num in range(num_of_ans):
		print(ans_num)
		if ans_num == ch:
			answers_kb.row(KeyboardButton(question[1]))

		else:
			answers_kb.row(KeyboardButton(random.choice(city)))
	await message.answer(f"Какая столица {question[0]}",reply_markup=answers_kb)
	print(data_c)
	await state.update_data(correct_answer=question[1])
	await state.update_data(data_C=data_c)


