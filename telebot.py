import requests
from telegraph import Telegraph
import json
from PPA import main_1



'''result=telegraph.create_account(short_name='1337')
with open('graph_bot.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=4)'''


'''telegraph = Telegraph("01ef55c10d55736e6904f6bee19e8699c2696a5d1b0a08bd4b5244c76722") # передаём токен доступ к страницам аккаунта
response = telegraph.create_page(
    'Hey', # заголовок страницы
    html_content='<p>Hello, world!</p>' # ставим параметр html_content, добавляем текст страницы
)

print('https://telegra.ph/{}'.format(response['path']))'''

'''data={
    'path':'Hey-03-23-46', #путь к странице он содержится в url после https://telegra.ph/
    'access_token':'01ef55c10d55736e6904f6bee19e8699c2696a5d1b0a08bd4b5244c76722',  # токен
    'title':'Hey', #заголовок, обязательный параметр, если не меняется, всё равно надо прописывать
    'author_name':None,
    'content': main_1(),  #содержание страницы должен быть  Array of Node
    'return_content':'false'
}'''
#редактирование страницы


telegraph = Telegraph('01ef55c10d55736e6904f6bee19e8699c2696a5d1b0a08bd4b5244c76722') # чтобы получить доступ к вашим страницам

telegraph.edit_page(
    path="Hey-03-23-46", # обязательный параметр
    title="Hey", # обязательный параметр
    html_content=str(main_1()),  #измененное содержание страницы, тут можно передать хоть строку с тегами, хоть руками написать что надо
    author_name="", # можно пропустить
    author_url="", # можно пропустить
    return_content=False
)