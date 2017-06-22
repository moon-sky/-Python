import os

import time
import random
import GetBingImg
interval = 100
def update_wallpaper(picpath):
    os.system('gsettings set org.gnome.desktop.background picture-uri "file://%s"' % (picpath))
    os.system('gsettings set org.gnome.desktop.background picture-options "centered"')
    print ("done")

def get_and_set():
    print ('check updating')
    GetBingImg.get_bing_backimg()
    print('update wallpaper')
    while True:
        os.path.isdir('photos')
        photo_list=os.listdir('photos')
        print (photo_list.__len__())
        index = random.randint(0,photo_list.__len__()-1)
        print (index)
        print (photo_list[index])
        print (os.getcwd())
        update_wallpaper('/home/wanghexin/PycharmProjects/untitled/photos/'+photo_list[index])
        # print interval
        time.sleep(interval)


if __name__ == '__main__':
    get_and_set()

# update_wallpaper('/home/wanghexin/PycharmProjects/untitled/photos/BehindTheFalls_ZH-CN6370841810_1920x1080.jpg')