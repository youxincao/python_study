# coding=utf-8

"""
  endswith(str, str) -> Bool

  判断文件的结尾
"""
def endswith(filename, suffix):
    return filename.rfind("." + suffix) == (len(filename) - len(suffix) - 1)
