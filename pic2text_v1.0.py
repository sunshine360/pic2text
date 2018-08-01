# -*- coding: UTF-8 -*-
#识别引擎
from PIL import Image
import pytesseract
import time
import sys


def load_dict_from_file(filepath):
    _dict = {}
    try:
        with open(filepath, 'r') as dict_file:
            for line in dict_file.readlines():
                line_list = line.strip().split(',')
                v_key = line_list.pop(0)
                for item in line_list:
                    _dict[item]=v_key
    except IOError as ioerr:
        print("文件 %s 不存在" % (filepath))
    return _dict


#清理识别出的乱码以及识别错误的修改
def clean_mistake(text):
    text=text.replace("。","")
    text=text.replace("\"","",-1)
    #text=text.replace("一 ","-1.",-1)
    text=text.replace("\n\n","\n")
    text=text.replace("一 ","-1.")
    quote_text=text.replace("ˇ","")
    no_quote_text= ','.join(quote_text.split(' '))#字符串分割
    text_result=no_quote_text.replace(",,",",")
    text_end=text_result.split(',')#用逗号替换空格来分割字符串
    
    return text_end

def clean_unit(text_end):
    x=0
    while x<=len(text_end)-1:
        temp=text_end[x]
        temp1=text_end[x-1]
        if(temp=='仁'):
            text_end[x]=text_end[x]
            text_end.pop(x)
            #text_end[x]='亿'
        #temp2=text_end[x]
        if(temp == '亿'):
            #print(temp1)
            #text_end[x-1]=temp1+temp
            text_end.pop(x)
        if(temp=='万'):
            text_end[x-1]=str(float(text_end[x-1])/10000)
            text_end.pop(x)
        if(chinese.get(text_end[x])!= None):
            text_end[x]=chinese.get(text_end[x])
        #清除前面的无用符号

        x+=1
    return text_end

def chinese_combine(self):
    y=0
    while y<=len(self)-1:
        if(self[y-1].isdigit()==False and self[y].isdigit()==False 
           and self[y-1].find('-')==-1 and self[y].find('-')==-1
           and self[y-1].find('.')==-1 and self[y].find('.')==-1
           and self[y-1].find('\n')==-1 and self[y].find('\n')==-1):
            self[y-1]=self[y-1]+self[y]
            self.pop(y)
        y+=1    
    z=0
    while z<=len(self)-1:
        if(self[z-1].isdigit()==False and self[z].isdigit()==False 
           and self[z-1].find('-')==-1 and self[z].find('-')==-1
           and self[z-1].find('.')==-1 and self[z].find('.')==-1
           and self[z-1].find('\n')==-1 and self[z].find('\n')==-1):
            self[z-1]=self[z-1]+self[z]
            self.pop(z)
        z+=1
    return self

def data(list):
    if(input_file.find('sz')):
        Data={0: ['序号', '合约', '最新', '涨跌', 
                  '成交量', '成交额', '资金流向',
                  '沉淀资金', '总市值', '量比'] }
    else:
        Data={0: ['序号', '合约', '最新', '涨跌',
                  '持仓量','成交量', '成交额', '沉淀资金', 
                  '资金流向', '投机度', '昨结算'] }
    i=0
    top=1
    Width=30
    buffer=[]
    while i<=len(list)-1:
        if (list[i].find('\n')!=-1):
            num=1
            while num<=Width:
                if((i+num) == len(list)-1):
                    #buffer.append(list[i+num])
                    Data[top]=buffer
                    i=i+num-1
                    break
                if (list[i+num].find('\n')!=-1):
                    #print(buffer)
                    #buffer.append(list[i+num])
                    Data[top]=buffer.copy()
                    buffer.clear()
                    top+=1
                    i=i+num-1
                    break
                buffer.append(list[i+num])
                num+=1
        i+=1    
    return Data

def write_data(text_result):
    f = open(output_file,'w')
    for lines in text_result:
        Date=','.join(text_result[lines])
        f.write(Date)
        f.write('\n')
        #print(Date)
    f.close()

if(len(sys.argv)==1):
    #格式化成20180720形式
    date_time=time.strftime("%Y%m%d", time.localtime())
    input_file=date_time+'sz.png'
    output_file=date_time+'sz.csv'
    print('请稍后......')
if(len(sys.argv)==2):
    input_file='D:/pic/'+sys.argv[1]
    s=sys.argv[1].find('.')
    adress=sys.argv[1][:s]
    output_file='D:/text/'+adress +'.csv'

if(len(sys.argv)==4):
    input_file=sys.argv[2]+'/'+sys.argv[1]
    output_file=sys.argv[3]+'/'+adress+'.csv'

#字典，替换错别字
chinese=load_dict_from_file('D:/projects/pic2text/errortext.txt')
#print(chinese)

#图片识别
result=pytesseract.image_to_string(Image.open(input_file),lang='chi_sim')
#ret_table=result.splitlines()
#print(ret_table)
#i = 0
#for item in ret_table:
    #print(item)
    #print("No %i\n", i )
    #i=i+1
result=clean_mistake(result)
text_result=clean_unit(result)
text_result=chinese_combine(text_result)
text_result=data(text_result)
#print(len(text_result))
#print(text_result)
write_data(text_result)
#print(text_result)


        
    

