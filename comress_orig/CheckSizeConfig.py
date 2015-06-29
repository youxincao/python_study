#! /usr/bin/env python
# -*- coding: utf-8 -*-
#


class CheckSizeConfig(object):

    def __init__(self, dict):
        # 检查目录的绝对路径
        if 'checkSizeDir' in dict:
            CheckSizeConfig.checkSizeDir = dict['checkSizeDir']
        # ignore的对象
        if 'checkSizeIgnoreList' in dict:
            CheckSizeConfig.checkSizeIgnoreList = dict['checkSizeIgnoreList']
        # 普通文件大小的限制 50k
        if 'sizeScaleNormal' in dict:
            CheckSizeConfig.sizeScaleNormal = dict['sizeScaleNormal']
        # 针对特殊文件大小的限制，可拓展添加
        # zip文件 -> 100k
        if 'sizeScale1' in dict:
            CheckSizeConfig.sizeScale1 = dict['sizeScale1']
        if 'fileType1' in dict:
            CheckSizeConfig.fileType1 = dict['fileType1']

    @property
    def checkSizeDir(self):
        return CheckSizeConfig.checkSizeDir

    @property
    def checkSizeIgnoreList(self):
        return CheckSizeConfig.checkSizeIgnoreList

    @property
    def sizeScaleNormal(self):
        return CheckSizeConfig.sizeScaleNormal

    @property
    def sizeScale1(self):
        return CheckSizeConfig.sizeScale1

    @property
    def fileType1(self):
        return CheckSizeConfig.fileType1

    def __repr__(self):
        return 'CheckSizeConfig'
