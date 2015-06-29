#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
import Constants
import Utils
import sys
import Image

reload(sys)
sys.setdefaultencoding('utf-8')


def check_imgMode(filedir):
    try:
        img = Image.open(filedir)
        return img.mode
    except:
        errInfo = encodeChinese('This is not image: ') + str(filedir) + '\n'
        print errInfo
        return errInfo

# 从配置文件中读取设置
checkAlphaConfig = Utils.initCheckAlphaConfig()
if not checkAlphaConfig:
    print "LOAD CheckAlphaConfig FAILED"
    exit()

BASE_DIR_S = checkAlphaConfig.checkAlphaDir
CONST_IMAGE_FORMAT = checkAlphaConfig.checkAlphaFormat
SIZE_SCALE = checkAlphaConfig.sizeScale

print "BASE_DIR_S:", BASE_DIR_S
print "CONST_IMAGE_FORMAT:", CONST_IMAGE_FORMAT
print "SIZE_SCALE:", SIZE_SCALE
print ""

count = 0
# 遍历要扫描的文件夹s
for BASE_DIR in BASE_DIR_S:
    # 三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
    for parent, dirnames, filenames in os.walk(BASE_DIR):
        for filename in filenames:
            # 获取文件的绝对路径
            path = os.path.join(parent, filename)

            # 过滤文件类型
            if not os.path.splitext(filename)[1] in CONST_IMAGE_FORMAT:
                continue

            # 判断文件存在
            if not filename:
                continue

            # 检查文件类型
            mode = check_imgMode(path)
            if mode != 'RGB':
                continue

            # 检查文件阈值范围
            size = os.path.getsize(path)
            if size < SIZE_SCALE:
                continue

            print 'IMAGE:', Utils.getFloderName(parent) + os.sep + filename
            count += 1

if count > 0:
    print 'These ' + str(count) + ' images may be pngs with no alpha and size larger than 20k, considering jpeg?'
