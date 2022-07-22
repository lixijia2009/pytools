import os
import sys
filename = input("请输入文件名(不带后缀)：")
print(filename)
os.system('pyinstaller -F  D:/pythonPro/'+filename+'.py')
