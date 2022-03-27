import os,requests
def download(url):
    get_response = requests.get(url,stream=True)
    file_name  = "_TEMP.py"
    with open(file_name, 'wb') as f:
        for chunk in get_response.iter_content(chunk_size=1024):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)


download("https://raw.githubusercontent.com/AnxinCanada/ArchieBot/main/Bot/Bot.py")


import os
import discord
import requests

def update():
    get_response = requests.get("https://raw.githubusercontent.com/AnxinCanada/ArchieBot/main/Bot/Bot.py", stream=True)
    file_name  = "_TEMP.py"
    with open(file_name, 'wb') as f:
        for chunk in get_response.iter_content(chunk_size=1024):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)