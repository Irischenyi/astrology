from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from bs4 import BeautifulSoup
import re
import os

class getFile:
    def __init__(self, url):
        self.url = url

    def getHtml(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option("detach", True)
        self.driver = driver = webdriver.Chrome(options = option)
        driver.get(self.url)
        driver.maximize_window()
        source = self.driver.page_source
        self.getContent(source)
        self.driver.quit()
    

    def getContent(self, content):
        outContent = str(content)
        content = re.findall(r'"text": "(.*[^"]*)"',outContent)[0]
        name =  re.findall(r'"name": "(.*[^"]*)",',outContent)[0]

        replays = re.findall(r'<p class="reply-content">(.*[^\<]*)</p>', outContent)
        time = re.findall(r'<span class="create-time color-green">(.*)</span>', outContent)[0]

        files = '<a href="'+self.url+'">link</a> '+name+'<br/><br/>'+time+'<br/><br/><br/>'
        files = files+ '<div style="border: 1px dashed grey;padding: 20px;">'+content+'</div><br><br/><br/>'
        for item in replays:
            files = files + '—— <div>'+item+'</div><br/>'

        os.mkdir('./file/'+time[0:10]+'-'+time[17:19])
        f = open('./file/'+time[0:10]+'-'+time[17:19]+'/index.html', mode='wb')
        f.write(files.encode('utf-8'))
        f.close()


getFile('url').getHtml()

# getHtml().getContent()