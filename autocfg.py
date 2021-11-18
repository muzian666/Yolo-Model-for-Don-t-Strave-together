#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 09:34:58 2021

@author: muzian
"""

import glob
import os,shutil
import wget
from time import sleep
import random


def emptydir(dirname):  #清空文件夹
    if os.path.isdir(dirname):   #如果文件夹存在，则删除文件夹
        shutil.retree(dirname)
        sleep(2)   #强制延迟，避免出现错误
    os.mkdir(dirname)   #建立文件夹

batch = 64   #设定每批次处理的资料数量
subdivisions = 4   #设定每批次资料分几次处理
classname = ['1','2','3']   #设定训练文件标签
train = 'cfg/train.txt'   #建立训练文件路径
valid = 'cfg/valid.txt'   #建立验证文件路径
names = 'cfg/obj.names'   #建立标记名称文件路径
backup = 'cfg/weights'    #建立储存训练模型文件路径
validratio = 0.1          #设定验证资料占全部资料数量的比例

print('===Start to build setting data (It will take some time for the first running)===')

#下载预训练档案
if not os.path.exists("darknet53.conv.74"):
    wget.download('https://pjreddie.com/media/files/darknet53.conv.74')

emptydir('cfg')     #建立cfg文件夹，用于存放训练组态资料结构
emptydir(backup)    #在cfg文件夹中，建立weights资料夹用于存放训练后的权重文件

#建立obj.data文件，重要文件！！！！，darknet系统需要使用此文件内容读取训练组态资料结构进行训练
classes = len(classname)   #分类标签数量
f = open('cfg/obj.data','w')
out = 'classes = ' + str(classes) + '\n'
out += 'train = ' + train + '\n'
out += 'valid = ' + valid + '\n'
out += 'names = ' + names + '\n'
out += 'backup = ' + backup + '\n'
f.write(out)

#建立标签文件
f = open(names, 'w')   #根据names变量的数值建立档案
out = ''
for cla in classname:  #依序将标签名称串列元素值写入档案
    out += cla +'\n'
f.write(out)


#建立训练&验证文件
imgfiles = glob.glob('yolodata/*.png')   #获取图片文件路径
for i in range (len(imgfiles)):
    imgfiles[i] = imgfiles[i].replace('\\','/')
valinum = int(len(imgfiles) * validratio)   #根据验证文件比例变量值计算验证资料数量
validlist = random.sample(imgfiles, valinum)    #验证文件串列：以random.sample方法在imgfiles图片串列中以随机数方式取得validum个元素值

#将验证的文件写入文件
f = open(valid, 'w')
out = ''
for val  in validlist:
    out += val + '\n'
f.write(out)

#建立训练文件档案
f = open(train,'w')
out = ''

#imgfile图片串列元素中不属于验证资料的就是训练资料
for tra in imgfiles:
    if tra not in validlist:
        out += tra + '\n'

f.write(out)

#建立组态档
cfglist = ['yolov3-tiny-obj.cfg','yolov3.obj.cfg']   #将两个组态档案名称建立串列以便能够使用循环处理
for cfgfile in cfglist:
    shutil.copyfile(cfgfile, 'cfg\\' + cfgfile)      #复制档案
    f = open('cgf\\' + cfgfile, 'r')                 #复制档案内容
    content = f.read()
    
    #替换资料
    content = content.replace('[[batch]]', str(batch))
    content = content.replace('[[subdivisions]]', str(subdivisions))
    content = content.replace('[[classes]]', str(classes))
    content = content.replace('[[filters]]', str((classes+5)*3))
    f = open('cfg\\' + cfgfile, 'w')
    f.write(content)
    
f.close()
print('===Success in building setting data!===')
    



