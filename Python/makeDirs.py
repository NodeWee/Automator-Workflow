# -*- coding: utf-8 -*-

def makeDirs(dirpath):
    '''
    创建目录
        支持多级目录，若目录已存在自动忽略
        Updated: 2020-02-27
        Author: nodewee (https://nodewee.github.io)
    '''

    # 去除首尾空白符和右侧的路径分隔符
    dirpath = dirpath.strip().rstrip(os.path.sep)

    if dirpath:
        if not os.path.exists(dirpath):  # 如果目录已存在, 则忽略，否则才创建
            os.makedirs(dirpath)
