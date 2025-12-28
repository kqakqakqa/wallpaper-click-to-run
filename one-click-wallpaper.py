import ctypes
import json
import os
import time
import urllib.request
import sys

# import windows_toasts


def wallpaper():
    print("getting url")
    archive = urllib.request.urlopen("https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=zh-CN").read()
    archiveJson = json.loads(archive)
    imageUrl = "https://www.bing.com" + archiveJson["images"][0]["url"].replace("1920x1080", "UHD")
    print(imageUrl)

    print("getting path")
    imagePath = os.path.dirname(os.path.realpath(sys.argv[0])) + "\\wallpaper.jpg"
    if os.path.exists(imagePath):
        os.remove(imagePath)
    print(imagePath)

    print("downloading")
    urllib.request.urlretrieve(imageUrl, imagePath)

    print("setting")
    SPI_SETDESKWALLPAPER = 0x0014
    SPIF_UPDATEINIFILE = 0x0001
    SPIF_SENDWININICHANGE = 0x0002
    ctypes.windll.user32.SystemParametersInfoW(
        SPI_SETDESKWALLPAPER, 0, imagePath, SPIF_UPDATEINIFILE | SPIF_SENDWININICHANGE
    )


# def toast(s):
#     toaster = windows_toasts.WindowsToaster("Wallpaper Only Once")
#     newToast = windows_toasts.Toast()
#     newToast.text_fields = [s]
#     toaster.show_toast(newToast)


for i in range(0, 12):
    print(f"\ntrial {i + 1}/12")
    try:
        wallpaper()
        break
    except Exception as e:
        e = "exception: " + str(e)
        print(e)
        # if i == 11:
        #     toast(e)
        #     break
        time.sleep(5)
