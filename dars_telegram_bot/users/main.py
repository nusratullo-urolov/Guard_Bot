import asyncio
import io
import re
from datetime import datetime

import aiogram.utils.exceptions
from aiogram import Bot, Dispatcher, executor, types

import logging

from aiogram.dispatcher.filters import AdminFilter, Command, BoundFilter
from aiogram.dispatcher.filters.builtin import CommandStart
from dars_telegram_bot.filter.group_filter import IsGroup
from dars_telegram_bot.filter.private_chat import IsPrivate


API_TOKEN = '5741103352:AAGOUVgjw4xLwjBfFGkFP4YdG5jUF24g6TA'

bot = Bot(API_TOKEN)
logging.basicConfig(level=logging.INFO)
dp = Dispatcher(bot)


@dp.message_handler(AdminFilter(), CommandStart())
async def bot_s(message: types.Message):
    await message.answer(f"Salom Admin {message.from_user.first_name}")


@dp.message_handler(IsPrivate(), CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.first_name} !")


@dp.message_handler(IsGroup(), CommandStart())
async def bot_start1(message: types.Message):
    await message.answer(f"Salom,{message.from_user.first_name} guruhga hush kelibsiz !")


# @dp.message_handler(IsGroup(), content_types=types.ContentTypes.LEFT_CHAT_MEMBER)
# async def ban_member(message: types.Message):
#     if message.left_chat_member.id == message.from_user.id:
#         await message.answer(f"{message.left_chat_member.get_mention(as_html=True)} guruhni tark etdi")
#     elif message.from_user.id == (await bot.me).id:
#         return
#     else:
#         await message.answer(f"{message.left_chat_member.full_name} guruhdan haydaldi"
#                              f"Admin : {message.from_user.get_mention(as_html=True)}.")


# @dp.message_handler(IsGroup(),Command("set_photo",prefixes = "!/"),AdminFilter())
# async def set_new_photo(message : types.Message):
#     source_message = message.reply_to_message
#     photo = source_message.photo[-1]
#     photo = await photo.download(destination=io.BytesIO())
#     input_file = types.InputFile(photo)
#     #1-usul
#     await message.chat.set_photo(photo=input_file)
#
#
# @dp.message_handler(IsGroup(),Command("set_title",prefixes = "!/"),AdminFilter())
# async def set_new_title(message : types.Message):
#     source_message = message.reply_to_message
#     title = source_message.text
#     #2-usul
#     await bot.set_chat_title(message.chat.id,title=title)
#
#
# @dp.message_handler(IsGroup(),Command("set_description",prefixes = "!/"),AdminFilter())
# async def set_new_description(message : types.Message):
#     source_message = message.reply_to_message
#     description = source_message.text
#     #1-usul
#     # await bot.set_chat_description(message.chat.id,description=description)
#     #2-usul
#     await message.chat.set_description(description=description)
#
#
# #faqat o'qiydigan qilamiz
# @dp.message_handler(IsGroup(),Command("ro",prefixes="!/"),AdminFilter())
# async def read_only_mode(message : types.Message):
#     member = message.reply_to_message.from_user
#     member_id = member.id
#     chat_id = message.chat.id
#     command_parse = re.compile(r"(!ro|ro) ?(\d+)? ?([\w+\D]+)?")
#     parsed = command_parse.match(message.text)
#     time = parsed.group(2)
#     comment = parsed.group(3)
#     if not time:
#         time = 5
#     #5 minutga izohsiz cheklash
#
#     time = int(time)
#
#     #Ban vaqtini Hisoblaymiz
#     until_date = datetime.now() + datetime.timedelta(minutes = time)
#
#     try:
#         await message.chat.restrict(user_id=member_id,can_send_messages=False,until_date = until_date)
#         await message.reply_to_message.delete()
#     except aiogram.utils.exceptions.BadRequest as err:
#         await message.answer(f"Xatolik {err.args}")
#         return
#
#     #pishem v chat
#     await message.answer(f"foydalanuvchi {message.reply_to_message.from_user.full_name} {time} minut"
#                          f"Sabab:\n<b>{comment}<b>")
#
#     service_message = await message.reply("Xabar 5 sekundan keyin o'chadi")
#     #5 sekund kutib xabarmi o'chiramiz
#     await asyncio.sleep(5)
#     await message.delete()
#     await service_message.delete()
#
#     #read only_holatidan qayta tiklaymiz


# @dp.message_handler(IsGroup(),Command("undo",prefixes="!/"),AdminFilter())
# async def undo_read_only(message : types.Message):
#     member = message.reply_to_message.from_user
#     member_id = member.id
#     chat_id = message.chat.id
#
#     user_allowed = types.ChatPermissions(
#         can_send_messages=True,
#         can_send_media_messages=True,
#         can_send_polls=True,
#         can_send_other_messages=True,
#         can_add_web_page_previews=True,
#         can_invite_users=True,
#         can_change_info=True,
#         can_pin_messages=True
#     )
#     service_message = await message.reply("Xabar 5 sekundan keyin o'chib ketadi")
#
#     await asyncio.sleep(5)
#     await message.chat.restrict(user_id=member_id,permissions=user_allowed,until_date=0)
#     await message.reply(f"Foydalanuvchi {message.from_user.full_name} tiklandi")
#
#     #Xabarlarni O'chiramiz
#     await message.delete()
#     await service_message.delete()
#
#
#
# class Filter(BoundFilter):
#     key = 'content_types'
#     required = True
#     default = types.ContentTypes.TEXT
#
#     def __init__(self, content_types):
#         if isinstance(content_types, str):
#             content_types = (content_types,)
#         self.content_types = content_types
#
#     async def check(self, message):
#         return types.ContentType.ANY in self.content_types or \
#                message.content_type in self.content_types


@dp.message_handler(IsGroup(),content_types=['photo','video','document','sticer','audio','animation','game','contact','location'])
async def photo_handler(message: types.Message):
    await message.answer("Iltimos Reklama Tarqatmang !!!")
    await message.delete()

@dp.message_handler(IsGroup(),content_types='text')
async def bot_data(message : types.Message):
    if message.text.startswith('https'):
        await message.answer('Iltimos Reklama Tarqatmang !!!')
        await message.delete()
executor.start_polling(dp, skip_updates=True)
