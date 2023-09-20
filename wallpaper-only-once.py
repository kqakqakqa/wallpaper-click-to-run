import ctypes
import json
import os
import time
import urllib.request


def wallpaper():
    # get url
    archive = urllib.request.urlopen("https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=zh-CN").read()
    archiveJson = json.loads(archive)
    imageUrl = "https://www.bing.com" + archiveJson["images"][0]["url"]
    imageUrl = imageUrl.replace("1920x1080", "UHD")

    # get path
    imagePath = os.path.dirname(os.path.abspath(__file__)) + "/bg.jpg"
    if os.path.exists(imagePath):
        os.remove(imagePath)

    # download
    urllib.request.urlretrieve(imageUrl, imagePath)

    # set
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
        break
    except:
        trialLeft -= 1
        time.sleep(5)
