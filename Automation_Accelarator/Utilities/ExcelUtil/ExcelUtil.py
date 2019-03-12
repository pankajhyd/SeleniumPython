'''
Name of File:-FileUtil
File Description:- This File is used for Excel related operation
Date :- 11-Sep-2018
Author :-Pankaj Kumar
'''
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
from pandas import read_excel
'''
Function Name           : fnGetColumnCounter
Function Creation Date  : 18-Feb-2019
Function Created By     : Pankaj Kumar - Cigniti Technology
Function Description    : To Get Column Name Position from Excel Sheet
'''
def fnGetColumnCounter(filePath,SheetName,columnName):
    col_counter=-99
    df = read_excel(filePath, sheet_name=SheetName)
    for i in range(len(df.columns)):
        #print(i, df.columns[i])
        if(df.columns[i]==columnName):
            col_counter=i
            break;
    return col_counter

'''
Function Name           : fnGetDataFromPosition
Function Creation Date  : 18-Feb-2019
Function Created By     : Pankaj Kumar - Cigniti Technology
Function Description    : To Get Data from Excel Sheet Based on Row and Column Position
'''
def fnGetDataFromPosition(filePath,SheetName,row,col):
    data=-99
    df = read_excel(filePath, sheet_name=SheetName)
    data=df.iloc[row, col]
    return data

'''
Function Name           : fnGetDataFromSheet
Function Creation Date  : 18-Feb-2019
Function Created By     : Pankaj Kumar - Cigniti Technology
Function Description    : To Get Data from Excel Sheet Based on Row and Column Name
'''
def fnGetDataFromSheet(filePath,SheetName,ColumnNamne,row):
    data=-99
    st = fnGetColumnCounter(filePath, SheetName, ColumnNamne)
    if(st==-99):
        data=-99
    else:
        data = fnGetDataFromPosition(filePath, SheetName, row-2, st)
    return data
