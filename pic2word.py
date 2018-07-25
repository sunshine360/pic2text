# -*- coding: UTF-8 -*-

from aip import AipOcr
import json

# 定义常量
APP_ID = '9851066'
API_KEY = 'LUGBatgyRGoerR9FZbV4SQYk'
SECRET_KEY = 'fB2MNz1c2UHLTximFlC4laXPg7CVfyjV'

# 初始化AipFace对象
aipOcr = AipOcr(APP_ID, API_KEY, SECRET_KEY)

# 读取图片
filePath = "d:/pic/20180716sz.jpg"
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

# 定义参数变量
options = {
    'detect_direction': 'true',
    'language_type': 'CHN_ENG',
}

# 调用通用文字识别接口
result = aipOcr.basicGeneral(get_file_content(filePath), options)
#print(json.dumps(result))
print(type(result))
print(result)
d = dict(result)
import json
js = json.dumps(result)
#print(len(d))
#print (d)
f = open('D:/pic/20170716sz.txt','w')
f.write(js)
#for m in d:
#        f.write(m['words_result'])

f.close()
