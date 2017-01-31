#coding=utf-8
import random
from Tkinter import *
import tkMessageBox

root=Tk()
def _maopao_sort_(list):
    for i in range(len(list)):
        j=i+1
        print (i,j)
        for j in range(i+1,len(list)):
            if list[i] > list[j]:
                print(i,list[i],j,list[j])
                temp=list[j]
                list[j]=list[i]
                list[i]=temp
                print (list)
    result='排序结果'+','.join(map(str,list))
    tkMessageBox.showinfo('Title',result)
    text.insert(INSERT,'\n'+result)

def click():
    tkMessageBox.showinfo('Hello', 'hello python')
if __name__ == '__main__':
    items=[1,2,3,4,5,11,12,15,10]
    random.shuffle(items)
    text=Text(root)
    text.insert(INSERT,'待排序数组'+''.join(map(str,items)))
    text.pack()
    button=Button(root,text='冒泡排序',command=lambda:_maopao_sort_(items))
    # button=Button(root,text='冒泡',command=click)
    button.pack()
    root.mainloop()
    print (items)
    # print (range(len(items)))
    # _maopao_sort_(items)


