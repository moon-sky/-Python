#coding:utf-8
import tkMessageBox
from Tkinter import *
root=Tk()
# top.mainloop()
li = ['c','python']
movie=['CSS','Jquery']
def click():
    tkMessageBox.showinfo('Hello','hello python')
button=Button(root,text='我只是一个按钮',command=click)
button.pack()
listb = Listbox(root)
listb2 =Listbox(root)
for item in li:
    listb.insert(0,item)

for item in movie:
    listb2.insert(0,item)

listb.pack()
listb2.pack()
root.mainloop()
