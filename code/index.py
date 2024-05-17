import requests
import re
import os
# get month asttologyzone


# https://www.astrologyzone.com/forecasts/aries-horoscope-for-june-2023/2/

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin":"https://www.astrologyzone.com"
}

url = "https://www.astrologyzone.com/forecasts/"
urlEnd = "-horoscope-for-"

params = {}
year = '2024'

moths = [
    #3
    'march',
    #4
    'april',
    # 5
    'may',
    # 6
    'june',
    # 7
    'july',
    # 8
    'august',
    #9
    'september',
    #10
    'october',
    #11
    'november',
    #12
    'december'
]

day = 'may-'+year

typeList = [
    'aries',
    # 白羊
    'taurus',
    # 金牛
    'gemini',
    # 双子
    'cancer',
    # 巨蟹
    'leo',
    # 狮子
    'virgo',
    # 处女
    'libra',
    # 天秤
    'scorpio',
    # 天蝎座
    'sagittarius',
    # 射手座
    'capricorn',
    # 摩羯座
    'aquarius',
    # 水瓶座
    'pisces'
    # 双鱼座
]

content = ''

def getHtml(item, n):
    global content
    href = ''
    if(n == 0):
        href = url+item+urlEnd+day
       
    else:
        href = url+item+urlEnd+day+'/'+str(n+1)

    print('==='+str(n+1))
    response = requests.get(href, headers=headers, params=params)
    result = re.findall('article---horoscope-content\">(.*?)<div---class=\"page-links', response.text.replace(' ','---').replace('&quot;','+++').replace('\n','==='))
    content = content + (result[0].replace('===','\n').replace('---',' '))+'\n\n\n'
    

    # 
    # print(item)
    # 
    # 
    # f.close()

for item in typeList:
    href = url+item+urlEnd+day
    content = ''
    response = requests.get(href, headers=headers, params=params)
    patt = r'<span>([0-9]|[0-9][0-9])</span>'
    pattern = re.compile(patt)
    result = pattern.findall(response.text)

    print(item +':' +str(len(result)))

    
    for n in range(len(result)):
        getHtml(item, n)
    
    
    os.makedirs('D:/astrology/files/'+year+'/'+day+'/'+item)
    f = open('D:/astrology/files/'+year+'/'+day+'/'+item+'/index.html', mode='w',encoding='utf-8')
    f.write(content)
    f.close()




   



# f = open('./a.html', mode='w',encoding='utf-8')
# patt = r'<span>[0-9]</span>'
# pattern = re.compile(patt)
# result = pattern.findall(response.text)
# print(len(result))
# f.write(response.text)
# f.close()