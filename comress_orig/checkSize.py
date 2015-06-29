#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
import Constants
import Utils
# 检查文件夹下所有体积过大的文件


# 获取文件中的配置
checkSizeConfig = Utils.initCheckSizeConfig()
if not checkSizeConfig:
    print "LOAD checkSizeConfig FAILED"
    exit()


BASE_DIR_S = checkSizeConfig.checkSizeDir
TOTAL_IGNORE_SIZE = 0
TOTAL_TOO_BIG_SIZE = 0

# 遍历要扫描的文件夹s
for BASE_DIR in BASE_DIR_S:
    # 三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
    for parent, dirnames, filenames in os.walk(BASE_DIR):
        # 遍历所有文件
        for filename in filenames:

            path = os.path.join(parent, filename)
            size = os.path.getsize(path)
            sizeScale = checkSizeConfig.sizeScaleNormal

            if filename in checkSizeConfig.checkSizeIgnoreList:
                TOTAL_IGNORE_SIZE += size
                continue

            # 过滤设置fileType1的sizeScale
            if os.path.splitext(filename)[1] in checkSizeConfig.fileType1:
                sizeScale = checkSizeConfig.sizeScale1

            if size >= sizeScale:
                TOTAL_TOO_BIG_SIZE += size
                print "file:" + Utils.getFloderName(parent) + os.sep + filename
                print "size:" + Utils.convertBytes(size)
                print ""

# 打印忽略文件的总共大小
print "TOTAL IGNORE FILE SIZE:" + Utils.convertBytes(TOTAL_IGNORE_SIZE)
# 打印太大文件的总共大小
print "TOTAL TOO BIG FILE SIZE:" + Utils.convertBytes(TOTAL_TOO_BIG_SIZE)
