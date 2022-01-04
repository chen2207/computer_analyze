import xlrd
import matplotlib.pyplot as plt

data = xlrd.open_workbook('computer.xls')#读取Excel文件
table = data.sheets()[0]#打开information名字的sheet
num1=0;num2=0;num3=0;num4=0;num5=0;num6=0
price1=0;price2=0;price3=0;price4=0;price5=0;price6=0
cols_value = table.col_values(3)#提取品牌(第3列)  列表形式  包括所有品牌
cols_value_price = table.col_values(1)#提取价格(第1列)

for i in range(1,1001):#读取这1000个数据
    #检测到对应品牌--对应数量加1 并且 对应总价钱加上搜索到的价钱
    if(cols_value[i]=="联想"):
        num1=num1+1
        price1=price1+float(cols_value_price[i])
    elif(cols_value[i]=="华为"):
        num2=num2+1
        price2 = price2 + float(cols_value_price[i])
    elif (cols_value[i] == "惠普"):
        num3 = num3 + 1
        price3 = price3 + float(cols_value_price[i])
    elif (cols_value[i] == "戴尔"):
        num4 = num4 + 1
        price4 = price4 + float(cols_value_price[i])
    elif(cols_value[i]=="华硕"):
        num5=num5+1
        price5 = price5 + float(cols_value_price[i])
    else:
        num6=num6+1
        price6 = price6 + float(cols_value_price[i])
print(num1,num2,num3,num4,num5,num6,num1+num2+num3+num4+num5+num6)
avg_price1=price1/num1
avg_price2=price2/num2
avg_price3=price3/num3
avg_price4=price4/num4
avg_price5=price5/num5
avg_price6=price6/num6
labels=['lenovo','Huawei','hp','Dell','ASUS','other brand']
#关于市场份额的扇形图
X=[num1,num2,num3,num4,num5,num6]#数据成员
fig = plt.figure()
plt.pie(X, labels=labels, autopct='%1.2f%%')  # 画饼图（数据，数据对应的标签，百分数保留两位小数点）
plt.title("Market share of various computer brands") #设置图片标题
plt.show()

#画关于平均价格的条形图
avg_ = [avg_price1,avg_price2,avg_price3,avg_price4,avg_price5,avg_price6]
plt.bar(labels, avg_)
plt.title('Average price of computer brands in the market')
plt.show()

#将title导入到文本中
text = table.col_values(0)
print(text)
doc = open('computer.txt','w',encoding='UTF-8')
#for i in range(1,1001):
print(text,file=doc)
doc.close()