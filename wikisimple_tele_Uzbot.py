# This Bot from @geekcoder17 you can check her codes in instagram

import logging
import wikipedia

from googletrans import Translator
translator = Translator()
wikipedia.set_lang('En')

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = ''  # You need write your api key


# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
   This handler will be called when user sends `/start` or `/help` command    """
    await message.reply(f"Sizni Bu Yerda Ko`rishdan Xursandman :) "
                        f"Nima haqida ma`lumot izlayabsiz ? "
                        f"-Iltimos Botdan foydalanish uchun izlayotgan "
                        f"Ma`lumotingizning Nomini Ingliz tilida kiriting ")
@dp.message_handler()
# bu yer bosh bolsa demak value habarlar boladi.
async def sendWiki(message: types.Message):
    try:
        # translate message from Uz to En by Google API
        # request = translator.translate(message.text, dest='en').text
        # Then search the result by English
        respond = wikipedia.summary(message.text)
        translations = translator.translate(respond, dest='uz').text
        # for respond in translations:
        await message.answer(translations)
    except:
        await message.answer("Siz so`ragan ma`lumot Topilmadi. Tashrifingiz uchun Rahmat !")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
