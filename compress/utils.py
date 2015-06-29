# coding=utf-8

import os

from filters import endswith
from os.path import abspath

class FileUtils:

    """
        get_all_files(str,str)-> list

        返回目录下固定后缀的文件的绝对路径
    """
    @staticmethod
    def get_all_files(dir_path, pattern):
        result = []
        # 保存当前工作目录
        cwd = os.path.abspath(os.getcwd())
         
        # 获取符合Pattern的文件名，的到其绝对路径，并保存到数组中    
        os.chdir(dir_path)
        for dir_path, _, filenames in os.walk(dir_path, topdown=False):
            os.chdir(dir_path)
            for filename in filenames:
                if endswith(filename, pattern):
                    result.append(abspath(filename))
                    
        # 恢复原工作目录
        os.chdir(cwd)
        return result

    @staticmethod
    def compress_png(src_file_path, dst_file_path):
        pass


if __name__ == "__main__":
    pics = FileUtils.get_all_files("E:\\work\\repo\\dev\\weibo_dev_res_git\\res", "png")
    for pic in pics :
        print pic 