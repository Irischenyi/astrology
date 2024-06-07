from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from bs4 import BeautifulSoup
import mysql.connector
import re
import os

class getFile:
    def __init__(self, url):
        self.url = url

    def getHtml(self):
        self.mydb = []
        self.name = self.content = self.replaysContent = self.time = ''

        option = webdriver.ChromeOptions()
        option.add_experimental_option("detach", True)
        self.driver = driver = webdriver.Chrome(options = option)
        driver.get(self.url)
        driver.maximize_window()
        source = self.driver.page_source
        self.getContent(source)
        # self.driver.quit()
        # 
        return self
    

    def getContent(self, content):
        outContent = str(content)
        content = re.findall(r'"text": "(.*[^"]*)"',outContent)[0]
        name =  re.findall(r'"name": "(.*[^"]*)",',outContent)[0]

        replays = re.findall(r'<p class="reply-content">(.*[^\<]*)</p>', outContent)
        time = re.findall(r'<span class="create-time color-green">(.*)</span>', outContent)[0]

        files = '<a href="'+self.url+'">link</a> '+name+'<br/><br/>'+time+'<br/><br/><br/>'
        files = files+ '<div style="border: 1px dashed grey;padding: 20px;">'+content+'</div><br><br/><br/>'
        
        replaysContent = ''
        for item in replays:
            replaysContent = replaysContent + '—— <div>'+item+'</div><br/>'


        self.name = name
        self.content = files
        self.replaysContent = replaysContent
        self.time = time
        
        # self.writeDB()
        # os.mkdir('./file/'+time[0:10]+'-'+time[17:19])
        # f = open('./file/'+time[0:10]+'-'+time[17:19]+'/index.html', mode='wb')
        # f.write(files.encode('utf-8'))
        # f.close()



    def connetDB(self):
        self.mydb = mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="123456",
            database="astrology"
        )
        return self

    def createDB(self):
        cursor = self.mydb.cursor()
        cursor.execute("CREATE DATABASE astrology")


    def createTable(self):
        cursor = self.mydb.cursor()
        cursor.execute("CREATE TABLE articles (name VARCHAR(255), content LONGTEXT, back lONGTEXT, time VARCHAR(255))")
        return self

    def writeDB(self):
        cursor = self.mydb.cursor()
        sql = "INSERT INTO articles (name, content, back, time) VALUES (%s, %s, %s, %s)"
        val = (self.name, self.content, self.replaysContent, self.time)
        cursor.execute(sql, val)
        self.mydb.commit()


getFile('https://www.douban.com/group/topic/305852920/?_i=7676565cYhIypq').getHtml().connetDB().writeDB()

# .getHtml().connetDB().writeDB()

# getFile('url').connetDB().createTable()

# getHtml().getContent()