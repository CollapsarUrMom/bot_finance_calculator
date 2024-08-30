import json
from aiogram import types
from sqlalchemy.ext.asyncio import AsyncSession
from aiogram import Bot

from database.models import Product


async def download_files(message: types.File):
    file_id = message.file_id
    file = await message.bot.get_file(file_id)
    file_path = file.file_path 
    destination = r'C:\Users\Alex_job\Documents\Git\bot_finance_calculator\download'
    destination_file = message.bot.download_file(file_path, destination)



# async def download_file(message: types.Document):
#     print('Функция запустилась!')
#     file_id = message.file_id
#     print(message)
#     file = await message.bot.get_file(file_id)
#     file_path = file.file_path
#     print(file_path)
#     my_json = await message.bot.download(file= file_id)
#     print(type(my_json))
#     a = await message.bot.download_file(file_path, my_json)
#     print(a)
#     print(type(a))
#     with open(a, 'r', 'UTF-8') as jsn:
#         py_json = json.load(jsn)
#         new_jsn = json.dumps(py_json, ensure_ascii= False, indent= 4)
#         fl = json.loads(new_jsn)
#         print(type(fl))








# 'C:\\Users\\Alex_job\\Documents\\Git\\bot_finance_calculator\\extract.json'
# async def parse_json(session: AsyncSession, check):
#     with open(check, mode= 'r', encoding= 'UTF-8') as file:
#             my_file = json.load(file)
#             new_json = json.dumps(my_file, ensure_ascii= False, indent= 4)
#             my_json = json.loads(new_json)
#             for i in range(len(my_json)):
#                 for j in range(len(my_json[i]['ticket']['document']['receipt']['items'])):
#                     obj = Product(
#                         name = my_json[i]['ticket']['document']['receipt']['items'][j]['name'],
#                        price = my_json[i]['ticket']['document']['receipt']['items'][j]['price'],
#                        quantity = my_json[i]['ticket']['document']['receipt']['items'][j]['quantity'],
#                        suma = my_json[i]['ticket']['document']['receipt']['items'][j]['sum'],
#                        time = int(my_json[i]['ticket']['document']['receipt']['dateTime'][:4]) + "-" +
#                        int(my_json[i]['ticket']['document']['receipt']['dateTime'][5:7]) + "-" +
#                        int(my_json[i]['ticket']['document']['receipt']['dateTime'][8:10])
#                     )
#                     session.add(obj)
#             session.commit()