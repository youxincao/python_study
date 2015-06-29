#! /usr/bin/env python
# -*- coding: utf-8 -*-


class CompressConfig(object):

    def __init__(self, dict):
        # 执行的绝对路径命令
        if 'command' in dict:
            CompressConfig.command = dict['command']
        # 压缩扫描文件夹的绝对路径
        if 'compressDir' in dict:
            CompressConfig.compressDir = dict['compressDir']
        # 压缩对象的格式
        if 'compressFormat' in dict:
            CompressConfig.compressFormat = dict['compressFormat']
        # 压缩忽略的patterner(当前只有.9)
        if 'compressIgnorePattern' in dict:
            CompressConfig.compressIgnorePattern = dict[
                'compressIgnorePattern']

    @property
    def command(self):
        return CompressConfig.command

    @property
    def compressDir(self):
        return CompressConfig.compressDir

    @property
    def compressFormat(self):
        return CompressConfig.compressFormat

    @property
    def compressIgnorePattern(self):
        return CompressConfig.compressIgnorePattern

    def __repr__(self):
        return 'CompressConfig'
