import os,requests
def download(url):
    get_response = requests.get(url,stream=True)
    file_name  = "_TEMP.py"
    with open(file_name, 'wb') as f:
        for chunk in get_response.iter_content(chunk_size=1024):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)


download("https://raw.githubusercontent.com/AnxinCanada/ArchieBot/main/Bot/Bot.py")


from time import sleep
import os
import discord
import requests
import shutil

def update():
    try:
        os.system("mv TEMP/assets assets")
    except Exception:
        pass
    os.system("svn checkout https://github.com/AnxinCanada/ArchieBot/trunk/Bot TEMP")
    try:
        os.system("mv assets TEMP/assets")
    except Exception:
        pass
update()