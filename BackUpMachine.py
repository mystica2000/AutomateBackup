import winreg

def boom_create_this(ftype,reg_title,cmd,title=None):
    reg=winreg.OpenKey(winreg.HKEY_CURRENT_USER,"Software\\Classes",0,winreg.KEY_SET_VALUE)
    key1=winreg.CreateKey(reg,ftype)
    key2=winreg.CreateKey(key1,"shell")
    key3=winreg.CreateKey(key2,reg_title)
    key4=winreg.CreateKey(key3,"command")
    if title !=None:
        winreg.SetValueEx(key3,None,0,winreg.REG_SZ,title)
    winreg.SetValueEx(key4,None,0,winreg.REG_SZ,cmd)
    winreg.CloseKey(key3)
    winreg.CloseKey(key2)
    winreg.CloseKey(key1)
    winreg.CloseKey(reg)


boom_create_this("*","Printfile","\"C:\\Users\\User\\Python38-32\\python.exe\" \"E:\\Python\\CrazyIdea\\BackUpMachine.py\" \"%1\"",title="BackUpFile")

f= open(r'E:\Python\CrazyIdea\log.txt',"w+")

import sys, os
try:
    entries=[]
    entries=sys.argv
    print(entries)
    os.system("pause")
    i=0
    for entry in entries:
        if i==0:
            i=1
            continue
        else:
          f.write(entry)
          f.write("\t")
except Exception as e:
     print(e)


f.close()
file_from=open(r'E:\Python\CrazyIdea\log.txt',"r+")


import shutil

str=file_from.readline()#always backup
str1=[]
str1=str.split("\t")
length=len(str1)
del str1[length-1]

try:
    for i in str1:        
       path=shutil.copy(i,'F:\\BackUpStorage\\')
except Exception as e:
    print(e)



