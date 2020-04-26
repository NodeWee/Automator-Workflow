# -*- coding: utf-8 -*-

def getFiles_inDir(dir_path,
                   includeSubfolder=True,
                   path_type=0,
                   ext_names="*"):
    '''获得指定目录下的所有文件，
        :param dir_path: 指定的目录路径
        :param includeSubfolder: 是否包含子文件夹里的文件，默认 True
        :param path_type: 返回的文件路径形式
            0 绝对路径，默认值
            1 相对路径
            2 文件名
        :param ext_names: "*" | string | list
            可以指定文件扩展名类型，支持以列表形式指定多个扩展名。默认为 "*"，即所有扩展名。
            举例：".txt" 或 [".jpg",".png"]

        :return: 以 yield 方式返回结果

    Updated:
        2020-04-21
    Author:
        nodewee (https://nodewee.github.io)
    '''

    # ext_names
    if type(ext_names) is str:
        if ext_names != "*":
            ext_names = [ext_names]
    # lower ext name letters
    if type(ext_names) is list:
        for i in range(len(ext_names)):
            ext_names[i] = ext_names[i].lower()

    def willKeep_thisFile_by_ExtName(file_name):
        if type(ext_names) is list:
            if file_name[0] == '.':
                file_ext = file_name
            else:
                file_ext = os.path.splitext(file_name)[1]
            #
            if file_ext.lower() not in ext_names:
                return False
        else:
            return True
        return True

    if includeSubfolder:
        len_of_inpath = len(dir_path)
        for root, dirs, files in os.walk(dir_path):
            for file_name in files:
                #
                if not willKeep_thisFile_by_ExtName(file_name):
                    continue
                #
                if path_type == 0:  # absolute path
                    yield os.path.join(root, file_name)
                elif path_type == 1:  # relative path
                    yield os.path.join(
                        root[len_of_inpath:].lstrip(os.path.sep), file_name)
                else:  # filen ame
                    yield file_name
    else:
        for file_name in os.listdir(dir_path):
            filepath = os.path.join(dir_path, file_name)
            if os.path.isfile(filepath):
                #
                if not willKeep_thisFile_by_ExtName(file_name):
                    continue
                #
                if path_type == 0:
                    yield filepath
                else:
                    yield file_name

