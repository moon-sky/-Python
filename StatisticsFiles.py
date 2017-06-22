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
            if sub_dir.endswith('.java'):
                ax = os.path.abspath(sub_dir)  # 如果当前路径不是文件夹则把文件名加入列表中
                result.append(ax)
                # print sub_dir
    return result
def get_all_suffix(targetDir,suffix):
    # print ('targetDir:'+targetDir+'|suffix:'+suffix)
    get_dir=os.listdir(targetDir)
    for i in get_dir:
        sub_dir=os.path.join(targetDir,i)
        if os.path.isdir(sub_dir):
            get_all_suffix(sub_dir,suffix)
        else:
            if sub_dir.endswith('.'+suffix):
                ax = os.path.abspath(sub_dir)  # 如果当前路径不是文件夹则把文件名加入列表中
                result.append(ax)
    return result
# targetDir=raw_input('请输入目录\n')
# print (get_all_suffix(targetDir,'java'))
# finalResult=get_all(targetDir)



# print (finalResult)
# print (test_sum(1,3))
# cur_path=os.getcwd()
# print (cur_path)
