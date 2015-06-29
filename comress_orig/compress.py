#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
import os
import datetime
import time
import jsonpickle
import Constants
import re
import Utils
import sys


THIS_COMPRESSED_COUNT = 0
THIS_COMPRESSED_SIZE = 0

SUCCESS = 1
CONTINUE = 2


def compressPng(parent, filename):
    # 获取文件的绝对路径
    path = os.path.join(parent, filename)

    # 过滤文件夹
    if os.path.isdir(path):
        return CONTINUE

    # 过滤文件类型
    if not os.path.splitext(filename)[1] in CONST_IMAGE_FORMAT:
        return CONTINUE

    # 略过上次压缩到现在都没有修改过的文件
    timestamp = os.path.getmtime(path)
    if timestamp <= LAST_UPDATE_TIME:
        print filename, "HAS NOT UPDATE SINCE LAST_UPDATE_TIME"
        return CONTINUE

    # 过滤关键字
    skip = False
    for ignore in COMPRESS_IGNORE_PATTERN:
        if ignore in filename:
            print "IGNORE:" + ignore + " in " + filename + " NO NEED TO COMPRESS"
            skip = True
    if skip:
        return CONTINUE

    # 执行压缩命令
    if filename:
        try:
            print 'IMAGE:', filename
            command = PNGOUT_COMMAND + " " + path
            result = os.popen(command).read()
            if Constants.HAS_COMPRESSED in result:
                # In:开头,有几个空格后跟着数字,到结尾前有任意字符，bytes结尾
                inSizeState = re.search(
                    r'\bIn\b\:\s{1,8}\d+(.*?)bytes', result).group()
                print inSizeState
                # Chg:开头，后跟有任意字符，original)结尾
                chgSizeState = re.search(
                    r'\bChg\b\:(.*?)original\)', result).group()
                print chgSizeState
                # chgSizeState中，"-"开头的数字，去除"-"到结尾(整个数字段)
                chgSize = re.search(r'\-\d+', chgSizeState).group()[1:]
                # 压缩计数器+1
                THIS_COMPRESSED_COUNT += 1
                # 压缩值累加
                THIS_COMPRESSED_SIZE += int(chgSize)
            else:
                print "NO COMPRESSION"
        except Exception, e:
            print e
            return CONTINUE

# 遍历要扫描的文件夹
@Utils.performance()
def compressAllPng(dirs):
    for BASE_DIR in dirs:
        # 三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
        for parent, dirnames, filenames in os.walk(BASE_DIR):
            for filename in filenames:
                if compressPng(parent, filename) == CONTINUE:
                    continue


# 从配置文件中读取设置
compressConfig = Utils.initCompressConfig()
if not compressConfig:
    print "LOAD CompressConfig FAILED"
    exit()
PNGOUT_COMMAND = compressConfig.command
BASE_DIR_S = compressConfig.compressDir
CONST_IMAGE_FORMAT = compressConfig.compressFormat
COMPRESS_IGNORE_PATTERN = compressConfig.compressIgnorePattern
print "PNGOUT_COMMAND:", PNGOUT_COMMAND
print "BASE_DIR_S:", BASE_DIR_S
print "CONST_IMAGE_FORMAT:", CONST_IMAGE_FORMAT
print "COMPRESS_IGNORE_PATTERN:", COMPRESS_IGNORE_PATTERN

# 从配置文件中读取状态
compressState = Utils.initCompressState()
if not compressState:
    print "LOAD CompressState FAILED"
    exit()
LAST_UPDATE_TIME = compressState.lastUpdateTime
print "LAST_UPDATE_TIME:", LAST_UPDATE_TIME
print ""

# 根据配置压缩所有图片
compressAllPng(BASE_DIR_S)

# 将设置写入文件
compressState.lastUpdateTime = time.time()
compressState.lastCompressedCount = THIS_COMPRESSED_COUNT
compressState.lastCompressedSize = THIS_COMPRESSED_SIZE
compressState.totalCompressedCount += THIS_COMPRESSED_COUNT
compressState.totalCompressedSize += THIS_COMPRESSED_SIZE
Utils.writeCompressState(Constants.COMPRESS_STATE_FILE, compressState)
