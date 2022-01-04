import xlrd
from PIL import Image
from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt
import numpy as np
import  jieba

def ToTxt():
    # 将title导入到文本中
    data = xlrd.open_workbook('computer.xls')  # 读取Excel文件
    table = data.sheets()[0]  # 打开information名字的sheet
    text = table.col_values(0)
    print(text)
    doc = open('computer.txt', 'w+', encoding='UTF-8')
    print(text, file=doc)
    doc.close()

def GetWordCloud():
   path_txt = 'computer.txt'
   path_img = "heart.png"
   f = open(path_txt, 'r', encoding='UTF-8').read()
   background_image = np.array(Image.open(path_img))
   # 结巴分词，生成字符串，如果不通过分词，无法直接生成正确的中文词云
   #Python join()方法用于将序列中的元素以指定的字符连接生成一个新的字符串。
   cut_text = " ".join(jieba.cut(f))

   wordcloud = WordCloud(
       # 设置字体，不然会出现口字乱码，文字的路径是电脑的字体一般路径，可以换成别的
       font_path="C:/Windows/Fonts/simfang.ttf",
       background_color="white",
       mask=background_image).generate(cut_text)
   # 生成颜色值
   image_colors = ImageColorGenerator(background_image)
   # 下面代码表示显示图片
   plt.imshow(wordcloud.recolor(color_func=image_colors), interpolation="bilinear")
   plt.axis("off")
   plt.show()

if __name__ == '__main__':
    ToTxt()
    GetWordCloud()