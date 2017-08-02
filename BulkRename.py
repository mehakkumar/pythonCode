import sys, os
path='D:/dir1'
os.chdir(path)
filenames = os.listdir(path)
newname=''
for filename in filenames:
    os.rename(filename, newname)
