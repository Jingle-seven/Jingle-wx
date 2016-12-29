# conding=utf-8

import os

# os.system("ls")

# import shutil
# shutil.copyfile('LibTest.py', 'LibTest2.py')
# shutil.move('LibTest2.py', '../demo/LibTest2.py')

import glob

resList = glob.glob('*.py')
print(resList)

import zipfile

zf = zipfile.ZipFile("test.zip", "x", zipfile.ZIP_DEFLATED)
for pyFile in resList:
    zf.write(pyFile)
zf.close()

zipfiles = zipfile.ZipFile("test.zip", 'r')
zipedFiles = zipfiles.namelist()
print(zipedFiles)
zipfiles.extractall("./ha", zipedFiles[1:3])
zipfiles.close()
