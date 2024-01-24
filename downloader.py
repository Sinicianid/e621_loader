from e621 import E621
import requests as req
import os
import time
from colorama import init, Fore

init()

name = 0

os.chdir('oral')

api = E621(("", "")) # it's should be (("name", "API_key")) // go to https://e621.net/users/home/api_key/view
posts = api.posts.search("") #tags here like a "tag tag -tag" or you can ["tag", "tag", "-tag"] OwO

for post in posts: #Проверяет формат и присваивает название с соответствующим форматом
    print("Загружаю..." + Fore.BLUE)
    get_post = post.file_obj.url
    resource = req.get(get_post)
    if post.file_obj.ext == 'jpg':
        out = open(f"image{str(name)}.jpg", 'wb')
    elif post.file_obj.ext == 'png':
        out = open(f"image{str(name)}.png", 'wb')
    elif post.file_obj.ext == 'webm':
        out = open(f"image{str(name)}.webm", 'wb')
    elif post.file_obj.ext == 'gif':
        out = open(f"image{str(name)}.gif", 'wb')
    out.write(resource.content)
    out.close
    print(f">Файл {get_post} загружен, расширение {post.file_obj.ext}." + Fore.GREEN)
    print(f">Загруженно за {time.gmtime().tm_sec} секунд." + Fore.GREEN)
    print(">Качаю следующий..." + Fore.BLUE)
    name = name + 1
