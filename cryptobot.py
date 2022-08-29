import requests
import json
import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text


_name = 't.me/bit_bit_bit_bit_bit_bit_bot'
_n = 'Bit_bit_bit'
_key = '5534391982:AAF8JRuyZHyaMNP979ULlBKRh3PSsTSNQCo'


bot = Bot(token=_key)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands="start")
async def start(message: types.Message):
    start_buttons = ["Bitcoin", "Ethereum", "Litecoin"]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)
    
    await message.answer("Cryptobot here! Type /help to find out a commands.", reply_markup=keyboard)

@dp.message_handler(commands="help")
async def cmd_help(message: types.Message):
	await message.reply('All commands:\n/btc - return price of bitcoin\n/eth - return price of ethereum\n/ltc - return price of litecoin\n/all - return all of them')


# Хэндлер на команду /btc
@dp.message_handler(commands="btc")
async def cmd_btc(message: types.Message):
	req = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd').text
	price = json.loads(req)['bitcoin']['usd']
	await message.reply(f'Bitcoin price: {price}$')

@dp.message_handler(Text(equals="Bitcoin"))
async def but_btc(message: types.Message):
	req = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd').text
	price = json.loads(req)['bitcoin']['usd']
	await message.reply(f'Bitcoin price: {price}$')


@dp.message_handler(commands="eth")
async def cmd_eth(message: types.Message):
	req = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd').text
	price = json.loads(req)['ethereum']['usd']
	await message.reply(f'Ethereum price: {price}$')

@dp.message_handler(Text(equals="Ethereum"))
async def but_eth(message: types.Message):
	req = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd').text
	price = json.loads(req)['ethereum']['usd']
	await message.reply(f'Ethereum price: {price}$')


@dp.message_handler(commands="ltc")
async def cmd_ltc(message: types.Message):
	req = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=litecoin&vs_currencies=usd').text
	price = json.loads(req)['litecoin']['usd']
	await message.reply(f'Litecoin pric: {price}$')

@dp.message_handler(Text(equals="Litecoin"))
async def but_ltc(message: types.Message):
	req = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=litecoin&vs_currencies=usd').text
	price = json.loads(req)['litecoin']['usd']
	await message.reply(f'Litecoin price: {price}$')


@dp.message_handler(commands="all")
async def cmd_all(message: types.Message):
	req = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd').text
	priceb = json.loads(req)['bitcoin']['usd']

	req = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd').text
	pricee = json.loads(req)['ethereum']['usd']

	req = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=litecoin&vs_currencies=usd').text
	pricel = json.loads(req)['litecoin']['usd']

	await message.reply(f'Bitcoin price: {priceb}$\nEthereum price: {pricee}$\nLitecoin price: {pricel}$')

if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)
