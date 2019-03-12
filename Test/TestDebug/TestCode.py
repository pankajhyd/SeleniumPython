import os
import time
from Automation_Accelarator.Utilities.FileUtil import FileUtil
print("Test Code")
folderPath="/Users/admin/Documents/Python_Test"
folderName="Raja"
NewfolderName="Pankaj"
file_path = folderPath+ "/"+ folderName
print("Folder Creation ",FileUtil.fnCreateFolder(folderPath,folderName))
time.sleep(5)
print("Folder Rename ",FileUtil.fnRenameFolder(folderPath,folderName,NewfolderName))
time.sleep(5)
print("Folder Search ",FileUtil.fnSearchFolder(folderPath,NewfolderName))
time.sleep(5)
print("Create a Text File ",FileUtil.fnCreateTextFile(folderPath + "/" + NewfolderName,"Sample"))
time.sleep(5)
print("Rename a Text File ",FileUtil.fnRenameTextFile(folderPath + "/" + NewfolderName,"Sample","NewSample"))
time.sleep(5)
print("Copy File a Text File ",FileUtil.fnCopyFile(folderPath + "/" + NewfolderName,folderPath + "/CopyTest","NewSample.txt"))
time.sleep(5)
print("Copy Folder  ",FileUtil.fnCopyFolder(folderPath + "/" + NewfolderName,folderPath + "/CopyTest"))
time.sleep(5)
print("Delete a Text File ",FileUtil.fnDeleteTextFile(folderPath + "/" + NewfolderName,"NewSample"))
time.sleep(5)
print("Folder Creation ",FileUtil.fnDeleteFolder(folderPath,NewfolderName))
import os
import time
from Automation_Accelarator.Utilities.FileUtil import FileUtil
folderPath="/Users/admin/Documents/Python_Test"
print("Writing into File",FileUtil.fnWriteIntoFile(folderPath,"TestData","ABCDEFGHIKLMNOPQRSTUVWXYZ"))
print("Append into File",FileUtil.fnAppendIntoFile(folderPath,"TestData","\n Pankaj Kumar"))
print("Read From File\n",FileUtil.fnReadFile(folderPath,"TestData"))

import os
import sys
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
from pandas import read_excel


print("Excel Read")
testDataPath="/Users/admin/Documents/SeleniumPython/Test/TestData/TestData1.xlsx"
print(testDataPath)
my_sheet = 'HOOQ_1'
df = read_excel(testDataPath, sheet_name = my_sheet)
print(df.head()) # shows headers with top 5 rows
#arr=print(df.columns)
for i in range(len(df.columns)):
   print(i, df.columns[i])

print("Data")

row=1
col=2
print(df.iloc[row,col])