#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import StatisticsFiles
# cmd='/usr/java/jdk1.8.0_121/bin/javac -d '+'/home/wanghexin/AndroidStudioProjects/AndroidHotFixDemo/app/src/main/java/com/example/wanghexin/androidhotfixdemo/MainActivity.java'
# proc=subprocess.Popen(cmd,shell=True,check=True)
# command=raw_input('ex java\n')
# os.system(command)

cur_path=raw_input('请输入目录\n')
classPath=cur_path+'/classess/'
if not os.path.exists(classPath):
    os.mkdir(classPath)

java_list=StatisticsFiles.get_all_suffix(cur_path, 'java')
StatisticsFiles.result=[]
jar_list=StatisticsFiles.get_all_suffix(cur_path, 'jar')
print ('jar_list:'+jar_list.__str__())

# print(StatisticsFiles.result)
# print ('list_java:' + java_list.__str__())
#
filePath=''
for file in java_list:
    filePath=filePath+" "+file
    # print (filePath)
filePath=filePath+' -cp '
print ('filePath:'+filePath)
for file in jar_list:
    filePath=filePath+":"+file
    # print (filePath)

# print ('java_path:'+filePath)
command='javac -Xlint:unchecked -d '+cur_path+'/classess '+filePath+":/home/wanghexin/Android/Sdk/platforms/android-21/android.jar"
print ('command:'+command)
os.system(command)
command_jar='jar cvf '+cur_path+'/MyTestApp.jar ' +cur_path+'/classess/'
print (command_jar)
os.system(command_jar)


# os.system(command)