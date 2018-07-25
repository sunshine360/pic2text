# -*- coding: UTF-8 -*-
from PIL import Image
import pytesseract

text=pytesseract.image_to_string(Image.open('D:/pic/20180725sp.png'),lang='chi_sim')
print(text)

#写源数据
f = open('D:/text/20180725sp_raw.csv','w')
f.write(text)
f.close()

#table=maketrans('"ˇ')
text=text.replace("。","")
text1=text.replace("\"","",-1)
text11=text1.replace("一 ","-1.",-1)
text2=text11.replace("\n\n","\n")
quote_text=text2.replace("ˇ","")
no_quote_text= ','.join(quote_text.split(' '))
text_result=no_quote_text.replace(",,",",")
#print(len(text))
#text.split(' ')
#num =len(quote_text)
#i=0
#text.replace('"',',')
#while i <= num-1:
    #temp = no_quote_text[i]
    #temp1 = no_quote_text[i-1]
    #if(temp.isdigit()== False and temp is not ',' and temp1 is ','):
        #if(temp is not '-' and temp is not '.' and temp is not ',' and temp is not '。'):
            #no_quote_text[i-1]=temp1.replace(","," ")
    #i+=1

text_end=text_result.split(',')
#print(text_end)
#数据清理
#k=0
#while k<=60:
    #text_end.pop(0)
    #k+=1
#text_end[0]=' |'
#text_fina_result=text_result
#print(text_end[9])
chinese={'钥':'铜','磐':'器','酶':'酿','锦':'镍',
         '淀':'油','橙':'橡','肽':'胶','粗':'粕',
         '自':'白','椿':'糖','榜':'棉','锯':'铝',
         '煜':'煤','柳':'粕','挺':'指','沿':'油',
         '棘':'榈','敬':'数','镇':'镍','锋':'锌',
         '樵':'橡','褥':'棉','燧':'煤','棍':'榈',
         '煌':'煤','楹':'榈','锏':'铜','锆':'锌',
         '炼':'炭'}
Date_sp={
      '螺纹指数':[],'原油指数':[],'沪镍指数':[],
      '沪锌指数':[],'焦炭指数':[],'苹果指数':[],
      '白糖指数':[],'郑棉指数':[],'豆粕指数':[],
      '郑油指数':[],'橡胶指数':[],'铁矿指数':[],
      '郑醇指数':[],'热卷指数':[],'焦煤指数':[],
      '沪银指数':[],'沥青指数':[],'PTA指数':[],
      '沪铅指数':[],'豆二指数':[],'豆油指数':[],
      '豆一指数':[],'棕榈指数':[],'菜粕指数':[],
      '塑料指数':[],'沪铝指数':[],'沪金指数':[],
      'PP指数':[]
}
Date_sz={   
    '螺纹指数':[],'原油指数':[],'沪镍指数':[],
      '沪锌指数':[],'焦炭指数':[],'苹果指数':[],
      '白糖指数':[],'郑棉指数':[],'豆粕指数':[],
      '郑油指数':[],'橡胶指数':[],'铁矿指数':[],
      '郑醇指数':[],'热卷指数':[],'焦煤指数':[],
      '沪银指数':[],'沥青指数':[],'PTA指数':[],
      '沪铅指数':[],'豆二指数':[],'豆油指数':[],
      '豆一指数':[],'棕榈指数':[],'菜粕指数':[],
      'PVC指数':[],'沪铝指数':[],'沪金指数':[],
}
x=0
while x<=len(text_end)-1:
    temp=text_end[x]
    temp1=text_end[x-1]
    if(temp=='仁'):
        text_end[x]=text_end[x]
        text_end.pop(x)
        #text_end[x]='亿'
    #temp2=text_end[x]
    if(temp == '亿'  or temp=='一'):
        #print(temp1)
        #text_end[x-1]=temp1+temp
        text_end.pop(x)
    if(temp=='万'):
        text_end[x-1]=str(float(text_end[x-1])/10000)
        text_end.pop(x)
    #if (temp=='一'):
    #    text_end[x]=str(-1.0 + float(text_end[x+1])/100)
    #    text_end.pop(x+1)
    if(chinese.get(text_end[x])!= None):
        text_end[x]=chinese.get(text_end[x])

    x+=1
#print(text_end)
y=0
while y<=len(text_end)-1:
    if(text_end[y-1].isdigit()==False and text_end[y].isdigit()==False 
       and text_end[y-1].find('-')==-1 and text_end[y].find('-')==-1
       and text_end[y-1].find('.')==-1 and text_end[y].find('.')==-1
       and text_end[y-1].find('\n')==-1 and text_end[y].find('\n')==-1):
        text_end[y-1]=text_end[y-1]+text_end[y]
        text_end.pop(y)
    y+=1
z=0
while z<=len(text_end)-1:
    if(text_end[z-1].isdigit()==False and text_end[z].isdigit()==False 
       and text_end[z-1].find('-')==-1 and text_end[z].find('-')==-1
       and text_end[z-1].find('.')==-1 and text_end[z].find('.')==-1
       and text_end[z-1].find('\n')==-1 and text_end[z].find('\n')==-1):
        text_end[z-1]=text_end[z-1]+text_end[z]
        text_end.pop(z)
    z+=1
print(text_end)
#写入文件

f = open('D:/text/20180725sp.csv','w')
i=0
while i<=len(text_end)-1:
    f.write(text_end[i])
    f.write(',')
    i+=1
f.close()
#print(text)