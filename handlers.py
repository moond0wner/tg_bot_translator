
from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

import googletrans

import keyboards as kb

router = Router()

class Translate(StatesGroup):
    user_input = State()
    language_before = State()
    language_after = State()


@router.message(CommandStart())
async def start(message: Message):
    await message.answer("Привет, я бот переводчик.\nНажмите кнопку чтобы начать", reply_markup=kb.main)


@router.message(F.text == 'Начать перевод')
async def start_translate(message: Message, state: FSMContext):
    await message.answer("Выберите исходный язык", reply_markup=kb.languages)
    await state.set_state(Translate.language_before)


@router.callback_query(Translate.language_before)
async def lang_after(callback_query: CallbackQuery, state: FSMContext):
    await state.update_data(language_before=callback_query.data)
    await callback_query.answer()
    await callback_query.message.answer("Выберите язык на который нужно перевести", reply_markup=kb.languages)
    await state.set_state(Translate.language_after)


@router.callback_query(Translate.language_after)
async def get_text(callback_query: CallbackQuery, state: FSMContext):
    await state.update_data(language_after=callback_query.data)
    await callback_query.answer()
    await callback_query.message.answer("Введите текст который хотите перевести")
    await state.set_state(Translate.user_input)


@router.message(Translate.user_input, F.text)
async def translate_text(message: Message, state: FSMContext):
    await state.update_data(user_text=message.text)
    data = await state.get_data()
    async with googletrans.Translator() as ts:
        result = await ts.translate(text=data['user_text'], src=data['language_before'], dest=data['language_after'])
        await message.answer(f'Перевод: {result.text}', reply_markup=kb.to_main)
    await state.clear()


