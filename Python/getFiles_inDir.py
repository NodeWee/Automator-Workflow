# -*- coding: utf-8 -*-

def getFiles_inDir(dir_path,
                   include_subfolder=True,
                   path_type=0,
                   ext_names="*"):
    '''获得指定目录下的所有文件
    Parameter
    ---
        dir_path : str
            指定的目录路径
        include_subfolder : bool
            是否包含子文件夹里的文件，默认 True
        path_type : int
            返回的文件路径形式
                0 绝对路径，默认值
                1 相对路径
                2 文件名
        ext_names: str | list
            可以指定文件扩展名类型，支持以列表形式指定多个扩展名。默认为 "*"，即所有扩展名。
            举例：".txt" 或 [".jpg",".png"]
    Return
    ---
        以 yield 方式逐一返回文件路径

    Program
    ---
        Updated: 2020-06-03
        GitHub: https://github.com/NodeWee/OpenSnippets/tree/master/Python
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

    if include_subfolder:
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

