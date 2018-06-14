# -*- coding: utf-8 -*-   
import urllib.request  
import time  
import os  
import re  
from PIL import Image  
import win32api  
import win32gui  
import win32con  
  
  
class BingPic:  
    def __init__(self):  
        self.bgImageUrl = ''  
        self.localFileName = ''  
        self.localBMPFileName = ''    
    def createLocalFileName(self):  
        path = 'F:/Bing/'  
        if not os.path.exists(path):  
            os.mkdir(path)  
        randomStr = time.strftime("%Y%m%d", time.localtime())  
        self.localFileName = path + randomStr + '.jpg'  
        self.localBMPFileName = path + randomStr + '.bmp'  
  
    def downloadImage(self):  
        if self.localFileName == '':  
            self.createLocalFileName()  

        req = urllib.request.Request("http://cn.bing.com/HPImageArchive.aspx?idx=0&n=1")
        webpage = urllib.request.urlopen(req)  
        content = str(webpage.read())  
        url_tail = re.search(r'<url>[^\s]*</url>', content) 
        path = 'http://cn.bing.com' + str(url_tail.group())[5:-6]   
        urllib.request.urlretrieve(path, self.localFileName)  
  
    def updateBGImage(self):  
        img = Image.open(self.localFileName)  
        img.save(self.localBMPFileName)  
        os.remove(self.localFileName)   
        win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, self.localBMPFileName, 1+2)  
  
if __name__ == '__main__':  
    stealBing = BingPic()  
    stealBing.downloadImage()  
    stealBing.updateBGImage()  