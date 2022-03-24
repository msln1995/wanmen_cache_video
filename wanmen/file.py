import os.path
from pathlib import Path
import sys
import shutil

def currDirPath(filePath):
    cur_path = os.path.abspath(os.path.dirname(sys.argv[0]))
    return cur_path + "\Download\\" + filePath + "\\"

def truncateDir():
    cur_path = os.path.abspath(os.path.dirname(sys.argv[0]))
    filePath = cur_path + "\Download\\tmp"
    my_file = Path(filePath)
    if my_file.is_dir():
        shutil.rmtree(filePath)

def createDir(filePath):
    cur_path = os.path.abspath(os.path.dirname(sys.argv[0]))
    filePath = cur_path + "\Download\\" + filePath
    my_file = Path(filePath)
    if my_file.is_dir() == False:
        os.makedirs(filePath) 

def file_walker(path):
    file_list = []
    for root, dirs, files in os.walk(path): # 生成器
        for fn in files:
            p = str(root+'/'+fn)
            file_list.append(p)

    # print(file_list)
    return file_list.sort();

def combine(ts_path, combine_path, file_name):
    file_list = file_walker(ts_path)
    file_path = combine_path + file_name + '.ts'
    with open(file_path, 'wb+') as fw:
        for i in range(len(file_list)):

            fw.write(open(file_list[i], 'rb').read())
    print("已合并：" + file_name)

