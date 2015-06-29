#! /usr/bin/env python
# -*- coding: utf-8 -*-
#


class CompressState(object):
    lastUpdateTime = 0
    lastCompressedCount = 0
    lastCompressedSize = 0
    totalCompressedCount = 0
    totalCompressedSize = 0

    def __init__(self, dict):
        if 'lastUpdateTime' in dict:
            self.lastUpdateTime = dict['lastUpdateTime']
        if 'lastCompressedCount' in dict:
            self.lastCompressedCount = dict['lastCompressedCount']
        if 'lastCompressedSize' in dict:
            self.lastCompressedSize = dict['lastCompressedSize']
        if 'totalCompressedCount' in dict:
            self.totalCompressedCount = dict['totalCompressedCount']
        if 'totalCompressedSize' in dict:
            self.totalCompressedSize = dict['totalCompressedSize']

    def __repr__(self):
        return 'CompressState'
