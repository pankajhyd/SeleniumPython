import time
import datetime
import random
import os
from Automation_Accelarator.Utilities.FileUtil import FileUtil
from Automation_Accelarator.Config.GlobalConfig import GlobalConfig
'''
Function Name           : fnGetTimeStampString
Function Creation Date  : 18-Feb-2019
Function Created By     : Pankaj Kumar - Cigniti Technology
Function Description    : To Get The Time Stamp String
'''
def fnGetTimeStampString():
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%d_%m_%Y_%H_%M_%S')
    return st;
'''
Function Name           : fnGetTimeStampString
Function Creation Date  : 18-Feb-2019
Function Created By     : Pankaj Kumar - Cigniti Technology
Function Description    : To Get The Time Stamp String
'''
def fnGetTimeStamp():
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y - %H : %M : %S')
    return st;

'''
Function Name           : fnGetTime
Function Creation Date  : 18-Feb-2019
Function Created By     : Pankaj Kumar - Cigniti Technology
Function Description    : To Get The Time Stamp String
'''
def fnGetTime():
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%H : %M : %S')
    return st;



'''
Function Name           : fnGetReportPath
Function Creation Date  : 18-Feb-2019
Function Created By     : Pankaj Kumar - Cigniti Technology
Function Description    : To Get Test Report Folder Path
'''
def fnGetReportPath():
    path = os.path.abspath(__file__)
    dir_path = os.path.dirname(path)
    dir_Path1=dir_path.replace("/Automation_Accelarator/Reports","/Test/TestReport")
    return dir_Path1;

'''
Function Name           : fnGetReportPath
Function Creation Date  : 18-Feb-2019
Function Created By     : Pankaj Kumar - Cigniti Technology
Function Description    : To Get Test Report Folder Path
'''
def fnGetReportLogoPath():
    path = os.path.abspath(__file__)
    dir_path = os.path.dirname(path)
    dir_Path1=dir_path.replace("/Automation_Accelarator/Reports","/Automation_Accelarator/Reports/Logos")
    return dir_Path1;

'''
Function Name           : fnCopyReportLogo
Function Creation Date  : 18-Feb-2019
Function Created By     : Pankaj Kumar - Cigniti Technology
Function Description    : To Get Copy Report Logo
'''
def fnCopyReportLogo(strFolderLocation):
    strReportLogo=fnGetReportLogoPath()
    print(strReportLogo)
    FileUtil.fnCopyFile(strReportLogo, strFolderLocation, GlobalConfig.Company_logo)
    FileUtil.fnCopyFile(strReportLogo,strFolderLocation,GlobalConfig.Client_logo)
    FileUtil.fnCopyFile(strReportLogo, strFolderLocation, "failed.ico")
    FileUtil.fnCopyFile(strReportLogo, strFolderLocation, "Minus.ico")
    FileUtil.fnCopyFile(strReportLogo, strFolderLocation, "passed.ico")
    FileUtil.fnCopyFile(strReportLogo, strFolderLocation, "Plus.ico")
    FileUtil.fnCopyFile(strReportLogo, strFolderLocation, "screenshot.png")
    FileUtil.fnCopyFile(strReportLogo, strFolderLocation, "warning.ico")



'''
Function Name           : fnGetrandomValue
Function Creation Date  : 18-Feb-2019
Function Created By     : Pankaj Kumar - Cigniti Technology
Function Description    : To Get Random Value String
'''
def fnGetrandomValue():
    st = random.randint(1,10000000)
    return st;

'''
Function Name           : fnGetTime
Function Creation Date  : 18-Feb-2019
Function Created By     : Pankaj Kumar - Cigniti Technology
Function Description    : To Get The Time String
'''
def fnGetTime():
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
    return st;

'''
Function Name           : fnGetDate
Function Creation Date  : 18-Feb-2019
Function Created By     : Pankaj Kumar - Cigniti Technology
Function Description    : To Get The Date String
'''
def fnGetDate():
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
    return st;
'''
Function Name           : reportCreater
Function Creation Date  : 18-Feb-2019
Function Created By     : Pankaj Kumar - Cigniti Technology
Function Description    : To Generate Report
'''
def reportCreater():
    print("reportCreater")


'''
Function Name           : SuccessReport
Function Creation Date  : 18-Feb-2019
Function Created By     : Pankaj Kumar - Cigniti Technology
Function Description    : To Generate Success Report
'''
def SuccessReport(strStepName,strStepDes):
    print("reportCreater")



'''
Function Name           : successReportWithScreenShot
Function Creation Date  : 18-Feb-2019
Function Created By     : Pankaj Kumar - Cigniti Technology
Function Description    : To Generate Success Report With ScreenShot
'''
def successReportWithScreenShot(strStepName,strStepDes):
    print("reportCreater")


'''
Function Name           : failureReport
Function Creation Date  : 18-Feb-2019
Function Created By     : Pankaj Kumar - Cigniti Technology
Function Description    : To Generate Failure Report
'''
def failureReport(strStepName,strStepDes):
    print("reportCreater")

'''
Function Name           : warningReport
Function Creation Date  : 18-Feb-2019
Function Created By     : Pankaj Kumar - Cigniti Technology
Function Description    : To Generate warning Report
'''
def warningReport(strStepName,strStepDes):
    print("reportCreater")