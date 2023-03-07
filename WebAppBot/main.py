from aiogram import Bot, Dispatcher

token = '6216753871:AAGNEMOcJvxCR7sAn2s4QnsqxZM36jaXGHk'
bot = Bot(token)

dp = Dispatcher(bot)

@dp.message_handler()

