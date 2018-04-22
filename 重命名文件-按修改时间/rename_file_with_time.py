#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2018-04-22

@author: https://github.com/NodeWee/Automator-Workflow
"""


import os, sys, time


def rename_cur_path(path_list):
    global count,conflict_count
    for inpath in path_list:
        in_path = inpath.strip()
        if os.path.isfile(in_path):
            extname = os.path.splitext(in_path)[1]
            time_name = time.strftime('%Y%m%d-%H%M%S',time.localtime(os.path.getmtime(in_path))) #创建时间
            file_new_name = time_name + extname
            new_file_path = os.path.join(os.path.dirname(in_path),file_new_name)
            
            if not os.path.exists(new_file_path):
                os.rename(in_path, new_file_path)
                count+=1
            else:
                conflict_count+=1
        elif os.path.isdir(in_path):
            def join_filepath(filename):
                return os.path.join(in_path, filename)
            rename_cur_path(list(map(join_filepath, os.listdir(in_path))))

#========================
            
            
path_argv = sys.argv[1:]

count=0
conflict_count = 0

rename_cur_path(path_argv)

print('重命名：%d 个' % count)
if conflict_count>0:
    print('\n名称有冲突：%d 个' % conflict_count)

