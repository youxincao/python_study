#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
import json
import CompressConfig
import CompressState
import CheckSizeConfig
import CheckAlphaConfig
import math
import functools
import Constants
import time
import functools


def openReadFile():
    def decorator(func):
        @functools.wraps(func)
        def wrapper(fileDir):
            try:
                inputFile = file(r'' + fileDir)
                f = json.load(inputFile)
                inputFile.close()
                return f
            except Exception, e:
                print e
                exit()
        return wrapper
    return decorator


@openReadFile()
def getJsonFromFile(fileDir):
    pass


# 从配置文件中读取压缩设置
def initCompressConfig():
    json = getJsonFromFile(Constants.COMPRESS_CONFIG_FILE)
    compressConfig = CompressConfig.CompressConfig(json)
    return compressConfig



# 从配置文件获取压缩状态
def initCompressState():
    json = getJsonFromFile(Constants.COMPRESS_STATE_FILE)
    compressState = CompressState.CompressState(json)
    return compressState


# 从配置文件中读取检查大小的设置
def initCheckSizeConfig():
    json = getJsonFromFile(Constants.CHECK_SIZE_CONFIG_FILE)
    checkSizeConfig = CheckSizeConfig.CheckSizeConfig(json)
    return checkSizeConfig



# 从配置文件中读取检查太大非透明png的设置
def initCheckAlphaConfig():
    json = getJsonFromFile(Constants.CHECK_ALPHA_CONFIG_FILE)
    checkAlphaConfig = CheckAlphaConfig.CheckAlphaConfig(json)
    return checkAlphaConfig


# 将compressState写入文件
def writeCompressState(fileDir, compressState):
    try:
        outputS = open(fileDir, 'w+')
        output = json.dumps(
            compressState.__dict__, ensure_ascii=False, indent=4, sort_keys=True)
        outputS.write(output)
        outputS.flush()
    except Exception, e:
        print e
        exit()



# 将bytes数据自动向上转换
def convertBytes(bytes, lst=['Bytes', 'KB', 'MB', 'GB', 'TB', 'PB']):
    # 舍弃小数点，取小
    # 求对数(对数：若 a**b = N 则 b 叫做以 a 为底 N 的对数)
    i = int(math.floor(math.log(bytes, 1024)))

    if i >= len(lst):
        i = len(lst) - 1
    return ('%.2f' + " " + lst[i]) % (bytes / math.pow(1024, i))



# 获取从weibo_dev_res到根目录的路径
def getFloderName(parent):
    floderName = os.path.split(parent)
    if floderName[1] == Constants.CHECK_SIZE_FLODER_ROOT:
        return floderName[1]
    else:
        return getFloderName(floderName[0]) + os.sep + floderName[1]



# 打印方法使用时间
def performance():
    def perf_decorator(f):
        @functools.wraps(f)
        def wrapper(*args, **kw):
            t1 = time.time()
            r = f(*args, **kw)
            t2 = time.time()
            t = (t2 - t1)
            print 'Totally used time %f s' % (t)
            return r
        return wrapper
    return perf_decorator
