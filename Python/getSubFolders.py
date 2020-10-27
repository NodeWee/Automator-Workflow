# -*- coding: utf-8 -*-

def getSubFolders(dir_path, folder_name='*'):
    '''Get Sub Folders' path
    Parameter
    ---
        dir_path : str
        folder_name : str
            过滤文件夹名称
                '*'  默认，所有子文件夹
                '=a_name'   子文件夹名是“a_name”的文件夹
                '~some_text'   子文件夹名包含“some_text”的文件夹
                '!some_text'   子文件夹不包含“some_text”的文件夹
    Return
    ---
        以 yield 方式逐一返回匹配的子文件夹路径
    Program
    ---
        Updated: 2020-06-03
        GitHub: https://github.com/NodeWee/OpenSnippets/tree/master/Python
    '''
    for root, dirs, files in os.walk(dir_path):
        filter_type = folder_name[0]
        filter_text = folder_name[1:]

        for d in dirs:
            cur_folder_path = os.path.join(root, d)
            cur_folder_name = os.path.basename(d)

            if filter_type == '*':
                yield cur_folder_path
            else:
                if filter_type == '=':
                    if cur_folder_name == filter_text:
                        yield cur_folder_path
                elif filter_type == '~':
                    if filter_text in cur_folder_name:
                        yield cur_folder_path
                elif filter_type == '!':
                    if filter_text not in cur_folder_name:
                        yield cur_folder_path