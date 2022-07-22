import subprocess
# file='C:/Users/topdeep/Desktop/promotion-web-day.log'
# str1='inputList'
print("注：如文件与脚本不在同一目录，还需要加上文件路径")
file = input("请输入文件名：")
str1 = input("请输入关键字：")
resultFileData = ''
resultFileName = 'result.txt'
with open(file, 'r', encoding='utf-8') as f:
    for index, line in enumerate(f.readlines()):
        if str1 in line:
            pass
        else:
            resultFileData += str(index + 1) + '|' + line
with open('result.txt', 'w+', encoding='utf-8') as f:
    f.write(resultFileData)
subprocess.Popen('pause', shell=True)