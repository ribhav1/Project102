import os
import time
import shutil

path = 'C:/Users/risha/AppData/Local/Temp/'

if os.path.exists(path):
    directory_list = os.listdir(path)

for file in directory_list:
    name, ext = os.path.splitext(file)
    age = time.time() - os.stat(path + file).st_ctime

    days = age / 86400

    if days >= 30:
        if os.path.isdir(path + file):
            shutil.rmtree(path + file)
        else:
            os.remove(path + file)
