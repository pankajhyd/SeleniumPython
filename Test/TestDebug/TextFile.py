from Automation_Accelarator.Utilities.ExcelUtil import ExcelUtil
print("Text Text File Operation")
testDataPath="/Users/admin/Documents/SeleniumPython/Test/TestData/TestData.xls"
#print(testDataPath)
my_sheet = 'HOOQ_IOS_MOBILE'
#data=ExcelUtil.fnGetDataFromSheet(testDataPath,my_sheet,"ActiveUser",3)
#print(data)
from Automation_Accelarator.Reports import Reporter
Path=Reporter.fnGetReportPath()
print(Path)
