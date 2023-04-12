from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import Dispatcher
from aiogram import types


class FSMword(StatesGroup):
    word = State()
    translation = State()


# @dp.message_handler(commands='add new word', state=None)
async def add_start(message: types.Message):
    await FSMword.word.set()
    await message.reply('write new word')


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
        await message.reply(str(data))

    await state.finish()


def register_add_word(dp: Dispatcher):
    dp.register_message_handler(add_start, commands=['add'], state=None)
    dp.register_message_handler(add_word, state=FSMword.word)
    dp.register_message_handler(add_translation, state=FSMword.translation)
