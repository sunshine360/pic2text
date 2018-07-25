# -*- coding: UTF-8 -*-
import json
f = open('D:/pic/20180716sz.txt','r')
js = f.read()
dic = json.loads(js)   
#print(dic) 
f.close() 
#print(dic['words_result'])
tag = dic['words_result']
#print(tag[10:21])
#d = tag[0]
#print (len(tag))
number = len(tag) -1
x=0
y=0
z=0
buffer = []
while x <= number:
    d=tag[x]
    buffer.append(d['words'])
    #b = buffer
    d.clear()
    x+=1
print(buffer)
#while y <=4:
    #buffer.pop(0)
    #y+=1

#print(buffer[-1])
#buffer.pop(-1)
#buffer.pop(-2)
numbers = len(buffer)-1
#print(buffer)
file = open('D:/pic/20180716sz.csv','w')
while z <= numbers:
    item=list(buffer[z])
    item2="".join(item[0])
    #if(not item.isalnum() and item.find('亿')==-1 and item.find('.')==-1):
    if(item2.isdigit()== False and item2.find('亿')== -1):
        file.write('\n')
        #print(item2)
    file.write(buffer[z])
    file.write(',')
    z+=1

#jd = json.dumps(buffer)
#file.write(jd)
file.close()
