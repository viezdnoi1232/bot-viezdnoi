from aiogram import Bot, Dispatcher, executor, types

from config import TOKEN_API
from main import part_definition
from designer import designer_phone, designer_Iphone


bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start_handler(message: types.Message):
    await message.answer(text='Hello my fr')

@dp.message_handler()
async def all_requests(message: types.Message):
    z = ()
    s = part_definition(message.text)
    for a in s:
        if 'Iphone' in a[1]:
            await message.answer(text=designer_Iphone(a))

        else:
            await message.answer(text=designer_phone(a))




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)