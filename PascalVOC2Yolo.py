#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 09:21:47 2021

@author: muzian
"""

import glob
import os,shutil
from time import sleep
from bs4 import BeautifulSoup as bs

#清空文件夹
def emptydir(dirname):
    if os.path.isdir(dirname):  #如果文件夹存在，则删除资料夹
        shutil.retree(dirname)
        sleep(2)  #必要延迟，避免出错
    os.mkdir(dirname)  #建立文件夹
    
#分类标签标记处
classes = ['1','2','3']
    
print('Start Building Training Data')
emptydir('yolodata')  #建立训练资料夹
imgfiles = glob.glob('xxxxxxx\\yyyyyyy\\*.png')  #读取图形文件

#复制图形文件
for fimg in imgfiles:
    fname = fimg.split('\\')[-1]  #获取文件名称
    shutil.copyfile(fimg,'yolodata\\' + fname)  #复制文件

#转换PascalVOC格式至Yolo格式
lbfiles = glob.glob('xxxx\\yyyyyy\\*.xml')  #获取已标记的文件
for flb in lbfiles:
    fxml = open(flb)
    content = fxml.read()
    sp = bs(content,'html.parser')  #转换为BeautifulSoup格式
    imgW = float(sp.find('width').text)  #图形宽度
    imgH = float(sp.find('height').text) #图形高度
    objs = sp.find_all('object')
    out = ''
    
    for obj in objs:
        name = obj.find('name').text  #标记
        xmin = float(obj.find('xmin').text)  #左上角x坐标
        ymin = float(obj.find('ymin').text)  #左上角y坐标
        xmax = float(obj.find('xmax').text)  #右下角x坐标
        ymax = float(obj.find('ymax').text)  #右下角y坐标
        x = (xmin + (xmax - xmin)/2)/imgW  #中心点x坐标比例
        y = (ymin + (ymax - ymin)/2)/imgH  #中心点y坐标比例
        w = (xmax - xmin)/imgW  #图形宽度比例
        h = (ymax - ymin)/imgH  #图形高度比例
        out += str(classes.index(name)) + '' + str(x) + '' + str(y) + '' + str(w) + '' + str(h) + '\n'
    fname = flb.replace('vocdata\\annotations', 'yolodata').replace('.xml','.txt')  #存档路径
    ftxt = open(fname,'w')
    ftxt.write(out)  #写入存档
    
fxml.close()
ftxt.close()
print('===Building Training Data Success===')
    



