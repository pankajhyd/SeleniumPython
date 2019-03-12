'''
Name of File:-FileUtil
File Description:- This File is used for File and Folder related operation
Date :- 11-Sep-2018
Author :-Pankaj Kumar
'''
import os
import shutil
'''
Function Name           : fnCreateFolder
Function Creation Date  : 15-Feb-2019
Function Created By     : Pankaj Kumar - Cigniti Technology
Function Description    : To Create a Folder at Given Location
'''
def fnCreateFolder(folderPath,folderName):
    blnStatus=True
    file_path = folderPath + "/" + folderName
    print(file_path)
    if os.path.exists(file_path):
        print("Folder Already Exist " +file_path)
        blnStatus=False
    else:
        print("Folder Not Exist New Folder is Being Craeted")
        os.makedirs(file_path)
    return blnStatus;

'''
Function Name           : fnDeleteFolder
Function Creation Date  : 15-Feb-2019
Function Created By     : Pankaj Kumar - Cigniti Technology
Function Description    : To Delete a Folder at Given Location
'''
def fnDeleteFolder(folderPath,folderName):
    blnStatus=True
    file_path = folderPath + "/" + folderName
    print(file_path)
    if not os.path.exists(file_path):
        print("Folder Not Exist" +file_path)
    else:
        print("Folder Exist Folder is Being to Delete")
        shutil.rmtree(file_path)
    return blnStatus;

'''
Function Name           : fnRenameFolder
Function Creation Date  : 15-Feb-2019
Function Created By     : Pankaj Kumar - Cigniti Technology
Function Description    : To Rename a Folder at Given Location
'''
def fnRenameFolder(folderPath,OldfolderName,NewFolderName):
    blnStatus=True
    Oldfile_path = folderPath + "/" + OldfolderName
    Newfile_path = folderPath + "/" + NewFolderName
    print(Oldfile_path)
    print(Newfile_path)
    if not os.path.exists(Oldfile_path):
        print("Folder Not Exist" +Oldfile_path)
        blnStatus = False
    else:
        print("Folder Exist Folder is Being to Rename")
        os.rename(Oldfile_path,Newfile_path)
    return blnStatus;

'''
Function Name           : fnSearchFolder
Function Creation Date  : 15-Feb-2019
Function Created By     : Pankaj Kumar - Cigniti Technology
Function Description    : To Search a Folder at Given Location
'''
def fnSearchFolder(folderPath,folderName):
    blnStatus=True
    file_path = folderPath + "/" + folderName
    print(file_path)
    if os.path.exists(file_path):
        print("Folder Exist" +file_path)
        blnStatus = True
    else:
        print("Folder Exist" + file_path)
        blnStatus = False
    return blnStatus;

'''
Function Name           : fnCreateTextFile
Function Creation Date  : 15-Feb-2019
Function Created By     : Pankaj Kumar - Cigniti Technology
Function Description    : To Create a Text File at Given Location
'''
def fnCreateTextFile(folderPath,FileName):
    blnStatus=True
    file_path = folderPath + "/" + FileName+".txt"
    print(file_path)
    open(file_path,"w+")
    return blnStatus;

'''
Function Name           : fnDeleteTextFile
Function Creation Date  : 15-Feb-2019
Function Created By     : Pankaj Kumar - Cigniti Technology
Function Description    : To Delete a Text File at Given Location
'''
def fnDeleteTextFile(folderPath,FileName):
    blnStatus=True
    file_path = folderPath + "/" + FileName+".txt"
    print(file_path)
    os.remove(file_path)
    return blnStatus;

'''
Function Name           : fnRenameTextFile
Function Creation Date  : 15-Feb-2019
Function Created By     : Pankaj Kumar - Cigniti Technology
Function Description    : To Delete a Text File at Given Location
'''
def fnRenameTextFile(folderPath,OldFileName,NewFileName):
    blnStatus=True
    Oldfile_path = folderPath + "/" + OldFileName+".txt"
    Newfile_path = folderPath + "/" + NewFileName + ".txt"
    print(Oldfile_path)
    print(Newfile_path)
    if not os.path.exists(Oldfile_path):
        print("Folder Not Exist" + Oldfile_path)
        blnStatus = False
    else:
        print("Folder Exist Folder is Being to Rename")
        os.rename(Oldfile_path, Newfile_path)
    return blnStatus;

'''
Function Name           : fnCopyFile
Function Creation Date  : 15-Feb-2019
Function Created By     : Pankaj Kumar - Cigniti Technology
Function Description    : To Copy File From Given Location to Another Location
'''
def fnCopyFile(folderPath,NewFolderPath,FileName):
    blnStatus=True
    Oldfile_path = folderPath + "/" + FileName
    Newfile_path = NewFolderPath + "/" + FileName
    print(Oldfile_path)
    print(Newfile_path)
    if not os.path.exists(Oldfile_path):
        print("File Not Exist" + Oldfile_path)
        blnStatus = False
    else:
        print("File Exist File is Being to Rename")
        shutil.copy(Oldfile_path,Newfile_path)
    return blnStatus;

'''
Function Name           : fnCopyFolder
Function Creation Date  : 15-Feb-2019
Function Created By     : Pankaj Kumar - Cigniti Technology
Function Description    : To Copy Folder From Given Location to Another Location
'''
def fnCopyFolder(folderPath,NewFolderPath):
    blnStatus=True
    if not os.path.exists(folderPath):
        print("Folder Not Exist" + folderPath)
        blnStatus = False
    else:
        print("Folder Exist Folder is Being to Copy")
        shutil.copytree(folderPath,NewFolderPath)
    return blnStatus;

'''
Function Name           : fnWriteIntoFile
Function Creation Date  : 15-Feb-2019
Function Created By     : Pankaj Kumar - Cigniti Technology
Function Description    : To Write into File
'''
def fnWriteIntoFile(folderPath,FileName,Data):
    blnStatus=True
    file_path = folderPath + "/" + FileName + ".txt"
    print(file_path)
    f=open(file_path, "w+")
    f.write(Data)
    return blnStatus;

'''
Function Name           : fnAppendIntoFile
Function Creation Date  : 15-Feb-2019
Function Created By     : Pankaj Kumar - Cigniti Technology
Function Description    : To Append into File
'''
def fnAppendIntoFile(folderPath,FileName,Data):
    blnStatus=True
    file_path = folderPath + "/" + FileName + ".txt"
    print(file_path)
    f=open(file_path, "a+")
    f.write(Data)
    return blnStatus;

'''
Function Name           : fnReadFile
Function Creation Date  : 15-Feb-2019
Function Created By     : Pankaj Kumar - Cigniti Technology
Function Description    : To Read a File
'''
def fnReadFile(folderPath,FileName):
    file_path = folderPath + "/" + FileName + ".txt"
    print(file_path)
    f=open(file_path, "r")
    str=f.read()
    return str;

