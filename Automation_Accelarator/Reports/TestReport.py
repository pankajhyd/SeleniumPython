from Automation_Accelarator.Reports.Report import Report
from Automation_Accelarator.Reports.Report import DetailReportSummary
from Automation_Accelarator.Reports.Report import SummaryReport
from Automation_Accelarator.Reports import Reporter
from Automation_Accelarator.Utilities.FileUtil import FileUtil
import time
import collections
print("Test Report")
objSuite=SummaryReport()
path=objSuite.strReportPath
print("Path ==> " + path)
objTest1=DetailReportSummary()
objTest1.strBrowser="Chrome"
objTest1.strDevice="Android"
objTest1.strIPAddress="10.10.99.19"
objTest1.strTestName="Verify HOOQ Login"
#objTest1.strReportName="Verify_HOOQ_Login"
objTest1.strCountry="India"
objTest1.strEnvironment="Prod"
objTest1.strReportPath=path
objTest1.strDateTime=Reporter.fnGetTimeStampString()
objTest1.fnAddTestDetails(Report("Info", "Verify User Name"))
objTest1.fnAddTestDetails(Report("Step", "Login", "Verify Usr Name", "PASS", "S1"))
time.sleep(3)
objTest1.fnAddTestDetails(Report("Step", "Login", "Verify Password Name", "PASS", "S2"))
time.sleep(3)
objTest1.fnAddTestDetails(Report("Step", "Login", "Verify Password Name", "PASS", "S3"))
time.sleep(3)
objTest1.fnAddTestDetails(Report("Info", "Verify Password"))
objTest1.fnAddTestDetails(Report("Step", "Reg", "Verify Usr Name1", "PASS", "S1"))
time.sleep(3)
objTest1.fnAddTestDetails(Report("Step", "Reg", "Verify Password Name1", "Warning", "S2"))
time.sleep(3)
objTest1.fnAddTestDetails(Report("Step", "Reg", "Verify Password Name1", "PASS", "S3"))
time.sleep(3)
objTest1.fnAddTestDetails(Report("Info", "Verify Signup"))
objTest1.fnAddTestDetails(Report("Step", "SignUp", "Verify Usr Name1", "PASS", "S1"))
time.sleep(3)
objTest1.fnAddTestDetails(Report("Step", "SignUp", "Verify Password Name1", "Warning", "S2"))
time.sleep(3)
objTest1.fnAddTestDetails(Report("Step", "SignUp", "Verify Password Name1", "PASS", "S3"))
print("Report Name ==> " ,objTest1.strReportName)
print("Browser ==> " ,objTest1.strBrowser)
print("Device ==> " ,objTest1.strDevice)
print("IP Address ==> " ,objTest1.strIPAddress)
print("Date & Time ==> ",objTest1.strDateTime)
print("Test Name ==> " ,objTest1.strTestName)
print("Report Path ==> ",objTest1.strReportPath)
print(objTest1.DetailReportDetails[0].strStepName)
print(objTest1.DetailReportDetails[1].strStepDetail)
print(objTest1.DetailReportDetails[2].strStepDetail)
#objTest1.fnDetails()
print("PASS Count ",objTest1.strPassCount)
print("FAIL COUNT ",objTest1.strFailCount)
print("Waring COUNT ",objTest1.strWarning)
print("Step COUNT ",objTest1.strStepCount)
print("Record Count ==> ",objTest1.intRecordCount)
time.sleep(3)
objTest1.fnCreateDetailHTMLReport()
objSuite.fnAddTestDetails(objTest1)
#Test 2
objTest2=DetailReportSummary()
objTest2.strBrowser="Firefox"
objTest2.strDevice="Windows"
objTest2.strIPAddress="10.10.99.20"
objTest2.strTestName="Verify HOOQ Registration"
#objTest1.strReportName="Verify_HOOQ_Login"
objTest2.strCountry="India"
objTest2.strEnvironment="Prod"
objTest2.strReportPath=path
objTest2.strDateTime=Reporter.fnGetTimeStampString()
objTest2.fnAddTestDetails(Report("Info", "Verify User Name"))
objTest2.fnAddTestDetails(Report("Step", "Login", "Verify Usr Name", "PASS", "S1"))
time.sleep(3)
objTest2.fnAddTestDetails(Report("Step", "Login", "Verify Password Name", "PASS", "S2"))
time.sleep(3)
objTest2.fnAddTestDetails(Report("Step", "Login", "Verify Password Name", "PASS", "S3"))
time.sleep(3)
objTest2.fnAddTestDetails(Report("Info", "Verify Password"))
objTest2.fnAddTestDetails(Report("Step", "Reg", "Verify Usr Name1", "PASS", "S1"))
time.sleep(3)
objTest2.fnAddTestDetails(Report("Step", "Reg", "Verify Password Name1", "PASS", "S2"))
time.sleep(3)
objTest2.fnAddTestDetails(Report("Step", "Reg", "Verify Password Name1", "PASS", "S3"))
time.sleep(3)
objTest2.fnAddTestDetails(Report("Info", "Verify Signup"))
objTest2.fnAddTestDetails(Report("Step", "SignUp", "Verify Usr Name1", "PASS", "S1"))
time.sleep(3)
objTest2.fnAddTestDetails(Report("Step", "SignUp", "Verify Password Name1", "PASS", "S2"))
time.sleep(3)
objTest2.fnAddTestDetails(Report("Step", "SignUp", "Verify Password Name1", "PASS", "S3"))
objTest2.fnCreateDetailHTMLReport()
objSuite.fnAddTestDetails(objTest2)

#Test 3
objTest3=DetailReportSummary()
objTest3.strBrowser="Safari"
objTest3.strDevice="iOS"
objTest3.strIPAddress="10.10.99.20"
objTest3.strTestName="Verify HOOQ ME"
#objTest1.strReportName="Verify_HOOQ_Login"
objTest3.strCountry="India"
objTest3.strEnvironment="Prod"
objTest3.strReportPath=path
objTest3.strDateTime=Reporter.fnGetTimeStampString()
objTest3.fnAddTestDetails(Report("Info", "Verify User Name"))
objTest3.fnAddTestDetails(Report("Step", "Login", "Verify Usr Name", "PASS", "S1"))
time.sleep(3)
objTest3.fnAddTestDetails(Report("Step", "Login", "Verify Password Name", "PASS", "S2"))
time.sleep(3)
objTest3.fnAddTestDetails(Report("Step", "Login", "Verify Password Name", "PASS", "S3"))
time.sleep(3)
objTest3.fnAddTestDetails(Report("Info", "Verify Password"))
objTest3.fnAddTestDetails(Report("Step", "Reg", "Verify Usr Name1", "PASS", "S1"))
time.sleep(3)
objTest3.fnAddTestDetails(Report("Step", "Reg", "Verify Password Name1", "PASS", "S2"))
time.sleep(3)
objTest3.fnAddTestDetails(Report("Step", "Reg", "Verify Password Name1", "PASS", "S3"))
time.sleep(3)
objTest3.fnAddTestDetails(Report("Info", "Verify Signup"))
objTest3.fnAddTestDetails(Report("Step", "SignUp", "Verify Usr Name1", "PASS", "S1"))
time.sleep(3)
objTest3.fnAddTestDetails(Report("Step", "SignUp", "Verify Password Name1", "PASS", "S2"))
time.sleep(3)
objTest3.fnAddTestDetails(Report("Step", "SignUp", "Verify Password Name1", "PASS", "S3"))
objTest3.fnCreateDetailHTMLReport()
objSuite.fnAddTestDetails(objTest3)
objSuite.fnCreateSummaryReport()



#objTest1.fnCreateDetailHTMLReport()




'''
objTest2=DetailReportSummary()
objTest2.strBrowser="Firefox"
objTest2.strDevice="Web"
objTest2.strIPAddress="10.10.99.49"
objTest2.strReportName="Verify HOOQ Reg"
objTest2.strDateTime=Reporter.fnGetTimeStampString()
objTest2.fnAddTestDetails(DetailReport("Step","Reg","Verify Usr Name22","PASS","12-Feb_2019","/Test/Pass.png"))
objTest2.fnAddTestDetails(DetailReport("Step","Reg","Verify Password Name22","FAIL","12-Feb_2019","/Test/FAIL.png"))
print(objTest2.strReportName)
print(objTest2.strBrowser)
print(objTest2.strDevice)
print(objTest2.strIPAddress)
print(objTest2.strDateTime)
print(objTest2.DetailReportDetails[0].strStepName)
print(objTest2.DetailReportDetails[0].strStepDetail)
print(objTest2.DetailReportDetails[1].strStepDetail)
#objTest2.fnDetails()
print("PASS Count ",objTest2.strPassCount)
print("FAIL Count ",objTest2.strFailCount)
print("Step COUNT ",objTest2.strStepCount)
print("========", len(objTest2.DetailReportDetails))


objSuite=SummaryReport()
objSuite.DetailReportSummary.append(objTest2)
objSuite.DetailReportSummary.append(objTest1)'''







