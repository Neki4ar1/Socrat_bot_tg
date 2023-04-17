from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import Dispatcher
from aiogram import types
from database.sqlite_database import SQliteRepository
from models.words import Word


DB_NAME = 'users_info.db'
words_db = SQliteRepository[Word](DB_NAME, Word)


class FSMword(StatesGroup):
    word = State()
    translation = State()


# @dp.message_handler(commands='add new word', state=None)
async def add_start(message: types.Message):
    await FSMword.word.set()
    await message.reply('write new word')


async def cancel_add(message: types.Message, state: FSMword):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('adding was canceled')


# @dp.message_handler(content_types=['word'], state=FSMword.word)
async def add_word(message: types.Message, state: FSMword):
    async with state.proxy() as data:
        data['word'] = message.text
    await FSMword.next()
    await message.reply('write translation of this word')


# @dp.message_handler(state=FSMword.translation)
async def add_translation(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['translation'] = message.text

    async with state.proxy() as data:
        await words_db.add(Word(word=str(data['word']), translation=str(data['translation'])))

    await state.finish()


def register_add_word(dp: Dispatcher):
    dp.register_message_handler(add_start, commands=['add'], state=None)
    dp.register_message_handler(cancel_add, state='*', commands='cancel')
    dp.register_message_handler(cancel_add, Text(equals='cancel', ignore_case=True), state="*")
    dp.register_message_handler(add_word, state=FSMword.word)
    dp.register_message_handler(add_translation, state=FSMword.translation)
