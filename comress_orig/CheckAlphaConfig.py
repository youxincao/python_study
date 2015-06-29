#! /usr/bin/env python
# -*- coding: utf-8 -*-
#


class CheckAlphaConfig(object):

    def __init__(self, dict):
        # 检查目录的绝对路径
        if 'checkAlphaDir' in dict:
            CheckAlphaConfig.checkAlphaDir = dict['checkAlphaDir']
        # ignore的对象
        if 'checkAlphaIgnoreList' in dict:
            CheckAlphaConfig.checkAlphaIgnoreList = dict[
                'checkAlphaIgnoreList']
        # 检查的文件类型
        if 'checkAlphaFormat' in dict:
            CheckAlphaConfig.checkAlphaFormat = dict['checkAlphaFormat']
        # 文件大小的阈值
        if 'sizeScale' in dict:
            CheckAlphaConfig.sizeScale = dict['sizeScale']

    @property
    def checkAlphaDir(self):
        return CheckAlphaConfig.checkAlphaDir

    @property
    def checkAlphaIgnoreList(self):
        return CheckAlphaConfig.checksAlphaIgnoreList

    @property
    def checkAlphaFormat(self):
        return CheckAlphaConfig.checkAlphaFormat

    @property
    def sizeScale(self):
        return CheckAlphaConfig.sizeScale

    def __repr__(self):
        return 'CheckAlphaConfig'
