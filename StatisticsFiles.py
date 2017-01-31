import os
#coding:utf-8
result=[]
def get_all(cwd):
    get_dir=os.listdir(cwd)
    for i in get_dir:
        sub_dir=os.path.join(cwd,i)
        if os.path.isdir(sub_dir):
            get_all(sub_dir)
        else:
            ax=os.path.basename(sub_dir)#如果当前路径不是文件夹则把文件名加入列表中
            result.append(ax)
            print ("Length:",len(result))#对列表计
    print (result)

cur_path=os.getcwd()
print (cur_path)
get_all(cur_path)