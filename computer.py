from typing import Pattern

from bs4 import BeautifulSoup
import re
import urllib.request,urllib.error
import xlwt
import sqlite3



def main():
    baseurl = "https://search.jd.com/Search?keyword=%E7%94%B5%E8%84%91&wq=%E7%94%B5%E8%84%91&pvid=11af15b3bc994fe99fcedfdf9695cb5a&page="
    savepath=".\\computer.xls"
    #爬取网页 并提取信息
    datalist=getData(baseurl)

    #保存数据
    saveData(datalist,savepath)
url1="&s=1&click=0"#补充baseurl形成网页列表形式
# 电脑信息查找规则
findName = re.compile(r'<em>(.*?)<font class="skcolor_ljg">')    #生成正则表达式的对象，表示规则
price = re.compile(r'<i data-price="(.*?)</i>')
shop = re.compile(r'<a class="curr-shop hd-shopname"(.*?)</a>')
web = re.compile(r'<a href="(.*?)" onclick="')
def getData(baseurl):
    datalist=[]
    for i in range(0,60):
        url = baseurl+str(i*2+1)+url1
        html=askURL(url)
        #逐一进行解析
        soup =BeautifulSoup(html,"html.parser")
        for item in soup.select("div.gl-i-wrap"):
            data = []#保存一部电脑的全部信息
            item = str(item)

            name = re.findall(findName,item)#re库通过正则表达式查找指定的字符串
            namearray1 = ("联想")
            namearray2 = ("华为")
            namearray3 = ("惠普")
            namearray4 = ("戴尔")
            namearray5 = ("华硕")
            if name.__len__()!=0: #不抓取带有 京东电脑 标签的电脑
                print(name)
                data.append(name)#在data中加入name

                Price=re.findall(price,item)#抓取价格标签内数据
                index=Price[0].find('>')#只提取价格标签数字部分
                print(Price[0][index+1:])
                data.append(Price[0][index+1:])

                Web = re.findall(web,item)#抓取网页部分信息
                print("https:"+Web[0])
                data.append("https:"+Web[0])

                #确定电脑品牌
                if namearray1 in name[0]:
                    brand="联想"
                elif namearray2 in name[0]:
                    brand="华为"
                elif namearray3 in name[0]:
                    brand="惠普"
                elif namearray4 in name[0]:
                    brand="戴尔"
                elif namearray5 in name[0]:
                    brand="华硕"
                else:
                    brand="其他品牌"
                print(brand)
                data.append(brand)

                datalist.append(data)
    return datalist

#得到指定一个url的网页信息
def askURL(url):
    #用户代理表示不是爬虫，模拟头部信息
    head={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"}
    request=urllib.request.Request(url,headers=head)
    html=""
    try:
        response=urllib.request.urlopen(request)
        html=response.read().decode("utf-8")
        #print(html)
    #异常处理机制
    except urllib.error.URLError as e:
        if(hasattr(e,"code")):
            print(e,"code")
        if(hasattr(e,"reason")):
            print(e,"reason")
    return html

def saveData(datalist,savepath):
    book = xlwt.Workbook(encoding="utf-8")#utf-8编码方式
    sheet = book.add_sheet('information')#命名Excel文件sheet名字为information
    col = ("电脑标签","电脑价格","网址","品牌")
    for i in range(0,4):
        sheet.write(0,i,col[i])#列名的写入
    for i in range(0,1000):#
        print("第%d条"%i)#将抓取的前1000条数据存入Excel中
        data = datalist[i]#按行提取数据
        for j in range(0,4):
            sheet.write(i+1,j,data[j])#写入数据
    book.save(savepath)#保存Excel路径

if __name__=="__main__":
    main()