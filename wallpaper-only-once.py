import ctypes
import json
import os
import time
import urllib.request
import sys


def wallpaper():
    print("getting url:")
    archive = urllib.request.urlopen("https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=zh-CN").read()
    archiveJson = json.loads(archive)
    imageUrl = "https://www.bing.com" + archiveJson["images"][0]["url"]
    imageUrl = imageUrl.replace("1920x1080", "UHD")
    print(imageUrl + "\n")

    print("getting path:")
    imagePath = os.path.dirname(os.path.realpath(sys.argv[0])) + "\\wallpaper.jpg"
    if os.path.exists(imagePath):
        os.remove(imagePath)
    print(imagePath + "\n")

    print("downloading")
    urllib.request.urlretrieve(imageUrl, imagePath)

    print("setting")
    SPI_SETDESKWALLPAPER = 0x0014
    SPIF_UPDATEINIFILE = 0x0001
    SPIF_SENDWININICHANGE = 0x0002
    ctypes.windll.user32.SystemParametersInfoW(
        SPI_SETDESKWALLPAPER, 0, imagePath, SPIF_UPDATEINIFILE | SPIF_SENDWININICHANGE
    )


trialLeft = 12
while trialLeft > 0:
    try:
        wallpaper()
        print("done")
        break
    except:
        print("retrying")
        trialLeft -= 1
        time.sleep(5)
