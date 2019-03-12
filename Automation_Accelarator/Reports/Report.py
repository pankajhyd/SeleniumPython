from Automation_Accelarator.Utilities.FileUtil import FileUtil
from Automation_Accelarator.Config.GlobalConfig import GlobalConfig
from Automation_Accelarator.Reports import Reporter
import time
import datetime
class Report:
    strType=""
    strStepNo=""
    strStepName=""
    strStepDetail="";
    strStatus=""
    strTimeStamp=""
    strFilePath=""
    def __init__(self,strType,strStepName,strStepDetail="",strStatus="",strFilePath=""):
        self.strType=strType
        self.strStepName=strStepName
        self.strStepDetail=strStepDetail
        self.strStatus=strStatus
        self.strTimeStamp=Reporter.fnGetTime()
        self.strFilePath=strFilePath

class DetailReportSummary:
    strPassCount=0
    strFailCount=0
    strWarning=0
    strStepCount=0
    strDateTime=""
    strTimeTaken=""
    strReportPath=""
    strReportName=""
    strTestName=""
    strCountry=""
    strEnvironment=""
    strBrowser = ""
    strDevice = ""
    strIPAddress = ""
    intRecordCount=0
    DetailReportDetails= list()

    def __init__(self):
        print("DetailReportSummary")
        self.DetailReportDetails = list()
        self.strStepCount=0
        self.intRecordCount=0
        self.strTimeTaken=time.time()

    def fnDetails(self):
        for x in self.DetailReportDetails:
            if(x.strStatus.upper()=="PASS"):
                self.strPassCount=self.strPassCount+1
            if(x.strStatus.upper()=="FAIL"):
                self.strFailCount=self.strFailCount+1

    def fnAddTestDetails(self,objRecord):
        self.intRecordCount=self.intRecordCount+1
        if(objRecord.strType.upper()=="INFO"):
            self.DetailReportDetails.append(objRecord)
        if(objRecord.strType.upper()=="STEP"):
            self.strStepCount=self.strStepCount+1
            objRecord.strStepNo=self.strStepCount
            if(objRecord.strStatus.upper()=="PASS"):
                self.strPassCount = self.strPassCount + 1
            if (objRecord.strStatus.upper() == "FAIL"):
                self.strFailCount = self.strFailCount + 1
            if (objRecord.strStatus.upper() == "WARNING"):
                self.strWarning = self.strWarning + 1
            self.DetailReportDetails.append(objRecord)

    def fnCreateDetailHTMLReport(self):
        self.strReportName=self.strTestName.replace(" ","_")+"_"+self.strDevice.replace(" ","_")+"_"+self.strBrowser.replace(" ","_")+"_"+Reporter.fnGetTimeStampString()
        print("Create Detail HTML Summry Report")
        self.strTimeTaken = int(time.time() - self.strTimeTaken)
        self.strTimeTaken=str(datetime.timedelta(seconds=self.strTimeTaken))
        strFileName=self.strReportPath+"/"+self.strReportName+".html"
      #  FileUtil.fnDeleteTextFile(self.strReportPath,"/",self.strReportName)
        writer = f = open(strFileName, "w+")
        try:
            writer.write("<!DOCTYPE html> ");
            writer.write("<html>");
            writer.write("<head> ");
            writer.write("<meta charset='UTF-8'> ");
            writer.write("<title>" + self.strTestName + " Execution Results</title> ");
            writer.write("<style type='text/css'> ");
            writer.write("body { ");
            writer.write("background-color: #FFFFFF; ");
            writer.write("font-family: Verdana, Geneva, sans-serif; ");
            writer.write("text-align: center; ");
            writer.write("} ");
            writer.write("small { ");
            writer.write("font-size: 0.7em; ");
            writer.write("} ");
            writer.write("table { ");
            writer.write("box-shadow: 9px 9px 10px 4px #BDBDBD;");
            writer.write("border: 0px solid #4D7C7B; ");
            writer.write("border-collapse: collapse; ");
            writer.write("border-spacing: 0px; ");
            writer.write("width: 1000px; ");
            writer.write("margin-left: auto; ");
            writer.write("margin-right: auto; ");
            writer.write("} ");
            writer.write("tr.heading { ");
            writer.write("background-color: #041944; ");
            writer.write("color: #FFFFFF; ");
            writer.write("font-size: 0.7em; ");
            writer.write("font-weight: bold; ");
            writer.write("background:-o-linear-gradient(bottom, #999999 5%, #000000 100%);	background:-webkit-gradient( linear, left top, left bottom, color-stop(0.05, #999999), color-stop(1, #000000) );");
            writer.write("background:-moz-linear-gradient( center top, #999999 5%, #000000 100% );");
            writer.write("filter:progid:DXImageTransform.Microsoft.gradient(startColorstr=#999999, endColorstr=#000000);	background: -o-linear-gradient(top,#999999,000000);");
            writer.write("} ");
            writer.write("tr.subheading { ");
            writer.write("background-color: #FFFFFF; ");
            writer.write("color: #000000; ");
            writer.write("font-weight: bold; ");
            writer.write("font-size: 0.7em; ");
            writer.write("text-align: justify; ");
            writer.write("} ");
            writer.write("tr.section { ");
            writer.write("background-color: #A4A4A4; ");
            writer.write("color: #333300; ");
            writer.write("cursor: pointer; ");
            writer.write("font-weight: bold; ");
            writer.write("font-size: 0.7em; ");
            writer.write("text-align: justify; ");
            writer.write("background:-o-linear-gradient(bottom, #56aaff 5%, #e5e5e5 100%);	background:-webkit-gradient( linear, left top, left bottom, color-stop(0.05, #56aaff), color-stop(1, #e5e5e5) );");
            writer.write("background:-moz-linear-gradient( center top, #56aaff 5%, #e5e5e5 100% );");
            writer.write("filter:progid:DXImageTransform.Microsoft.gradient(startColorstr=#56aaff, endColorstr=#e5e5e5);	background: -o-linear-gradient(top,#56aaff,e5e5e5);");
            writer.write("} ");
            writer.write("tr.subsection { ");
            writer.write("cursor: pointer; ");
            writer.write("} ");
            writer.write("tr.content { ");
            writer.write("background-color: #FFFFFF; ");
            writer.write("color: #000000; ");
            writer.write("font-size: 0.7em; ");
            writer.write("display: table-row; ");
            writer.write("} ");
            writer.write("tr.content2 { ");
            writer.write("background-color: #E1E1E1; ");
            writer.write("border: 1px solid #4D7C7B;");
            writer.write("color: #000000; ");
            writer.write("font-size: 0.75em; ");
            writer.write("display: table-row; ");
            writer.write("} ");
            writer.write("td, th { ");
            writer.write("padding: 5px; ");
            writer.write("border: 1px solid #4D7C7B; ");
            writer.write("text-align: inherit\0/; ");
            writer.write("} ");
            writer.write("th.Logos { ");
            writer.write("padding: 5px; ");
            writer.write("border: 0px solid #4D7C7B; ");
            writer.write("text-align: inherit /;");
            writer.write("} ");
            writer.write("td.justified { ");
            writer.write("text-align: justify; ");
            writer.write("} ");
            writer.write("td.pass { ");
            writer.write("font-weight: bold; ");
            writer.write("color: green; ");
            writer.write("} ");
            writer.write("td.fail { ");
            writer.write("font-weight: bold; ");
            writer.write("color: red; ");
            writer.write("} ");
            writer.write("td.done, td.screenshot { ");
            writer.write("font-weight: bold; ");
            writer.write("color: black; ");
            writer.write("} ");
            writer.write("td.debug { ");
            writer.write("font-weight: bold;");
            writer.write("color: blue; ");
            writer.write("} ");
            writer.write("td.warning { ");
            writer.write("font-weight: bold; ");
            writer.write("color: orange; ");
            writer.write("} ");
            writer.write("</style> ");
            writer.write("<script> ");
            writer.write("function toggleMenu(objID) { ");
            writer.write("if (!document.getElementById) return; ");
            writer.write("var ob = document.getElementById(objID).style; ");
            writer.write("if(ob.display === 'none') { ");
            writer.write("try { ");
            writer.write("ob.display='table-row-group'; ");
            writer.write("} catch(ex) { ");
            writer.write("ob.display='block'; ");
            writer.write("} ");
            writer.write("} ");
            writer.write("else { ");
            writer.write("ob.display='none'; ");
            writer.write("} ");
            writer.write("} ");
            writer.write("function toggleSubMenu(objId) { ");
            writer.write("for(i=1; i<10000; i++) { ");
            writer.write("var ob = document.getElementById(objId.concat(i)); ");
            writer.write("if(ob === null) { ");
            writer.write("break; ");
            writer.write("} ");
            writer.write("if(ob.style.display === 'none') { ");
            writer.write("try { ");
            writer.write("ob.style.display='table-row'; ");
            writer.write("} catch(ex) { ");
            writer.write("ob.style.display='block'; ");
            writer.write("} ");
            writer.write("} ");
            writer.write("else { ");
            writer.write("ob.style.display='none'; ");
            writer.write("} ");
            writer.write("} ");
            writer.write("} ");
            writer.write("</script> ");
            writer.write("</head> ");
            writer.write(" <body> ");
            writer.write("</br>");
            writer.write("<table id='Logos'>");
            writer.write("<colgroup>");
            writer.write("<col style='width: 25%' />");
            writer.write("<col style='width: 25%' />");
            writer.write("<col style='width: 25%' />");
            writer.write("<col style='width: 25%' />");
            writer.write("</colgroup> ");
            writer.write("<thead> ");
            writer.write("<tr class='content'>");
            writer.write("<th class ='Logos' colspan='2' >");
           # writer.write("<img align ='left' src= ./Screenshots//" + GlobalConfig.Client_logo+ ".png></img>");
            writer.write("<img align ='left' src= ./Screenshots//" + GlobalConfig.Client_logo + "></img>");
            writer.write("</th>");
            writer.write("<th class = 'Logos' colspan='2' > ");
            writer.write("<img align ='right' src= .//Screenshots//"+GlobalConfig.Company_logo+"></img>");
            writer.write("</th> ");
            writer.write("</tr> ");
            writer.write("</thead> ");
            writer.write("</table> ");
            writer.write("<table id='header'> ");
            writer.write("<colgroup> ");
            writer.write("<col style='width: 25%' /> ");
            writer.write("<col style='width: 25%' /> ");
            writer.write("<col style='width: 25%' /> ");
            writer.write("<col style='width: 25%' /> ");
            writer.write("</colgroup> ");
            writer.write(" <thead> ");
            writer.write("<tr class='heading'> ");
            writer.write("<th colspan='4' style='font-family:Copperplate Gothic Bold; font-size:1.4em;'> ");
            writer.write("**" + self.strTestName + " Execution Results **");
            writer.write("</th> ");
            writer.write("</tr> ");
            writer.write("<tr class='subheading'> ");
            writer.write("<th>&nbsp;Device&nbsp;&nbsp;:&nbsp;</th> ");
            writer.write("<th>" + self.strDevice + "</th> ");
            writer.write("<th>&nbsp;Browser&nbsp;:&nbsp;</th> ");
            writer.write("<th>"+self.strBrowser+"</th> ");
            writer.write("</tr> ");
            writer.write("<tr class='subheading'> ");
            writer.write("<th>&nbsp;Country&nbsp;Name&nbsp;:&nbsp;</th> ");
            writer.write("<th>" + self.strCountry + "</th> ");
            writer.write("<th>&nbsp;Environment&nbsp;:&nbsp;</th> ");
            writer.write("<th>" + self.strEnvironment + "</th> ");
            writer.write("</tr> ");
            writer.write("<tr class='subheading'> ");
            writer.write("<th>&nbsp;Date&nbsp;&&nbsp;Time&nbsp;:&nbsp;</th> ");
            writer.write("<th>" + Reporter.fnGetTimeStamp()+ "</th> ");
            writer.write("<th>&nbsp;IP Address&nbsp;&nbsp;:&nbsp;</th> ");
            writer.write("<th>"+self.strIPAddress+"</th> ");
            writer.write("</tr> ");
            writer.write("</thead> ");
            writer.write("</table> ");
            self.fnCloseDetailReport(writer)
            writer.write("<table id='main'> ");
            writer.write("<colgroup> ");
            writer.write("<col style='width: 5%' /> ");
            writer.write("<col style='width: 26%' /> ");
            writer.write("<col style='width: 51%' /> ");
            writer.write("<col style='width: 8%' /> ");
            writer.write("<col style='width: 10%' /> ");
            writer.write("</colgroup> ");
            writer.write("<thead> ");
            writer.write("<tr class='heading'> ");
            writer.write("<th>S.NO</th> ");
            writer.write("<th>Steps</th> ");
            writer.write("<th>Details</th> ");
            writer.write("<th>Status</th> ");
            writer.write("<th>Time</th> ");
            writer.write("</tr> ");
            writer.write("</thead> ");
            for x in self.DetailReportDetails:
                if(x.strType.upper()=="INFO"):
                    self.fnAddStepToDetailRecord(writer,x)
                else:
                    if(x.strStatus.upper()=="PASS"):
                        self.fnAddPassToDetailRecord(writer, x)
                    if(x.strStatus.upper()=="FAIL"):
                        self.fnAddFailToDetailRecord(writer,x)
                    if (x.strStatus.upper() == "WARNING"):
                        self.fnAddWarningToDetailRecord(writer, x)
            self.fnCloseDetailReport(writer)
            self.fnCopyRight(writer)
            writer.close();
        except Exception :
            print(Exception.str())
            print("Test")

    def fnCloseDetailReport(self,writer):
        writer.write("</table>");
        writer.write("<table id='footer'>");
        writer.write("<colgroup>");
        writer.write("<col style='width: 25%' />");
        writer.write("<col style='width: 25%' />");
        writer.write("<col style='width: 25%' />");
        writer.write("<col style='width: 25%' />");
        writer.write("</colgroup>");
        writer.write("<tfoot>");
        writer.write("<tr class='heading'> ");
        writer.write("<th colspan='4'>Execution Time (Includes Report Creation Time) : "
                     +str(self.strTimeTaken)+ "&nbsp;</th> ");
        writer.write("</tr> ");
        writer.write("<tr class='subheading'>");
        writer.write("<td>&nbsp;Execution Status&nbsp;:</td>");
        if(self.strFailCount==0):
            writer.write("<td class='pass'> PASS&nbsp</td>");
        else:
            writer.write("<td class='fail'>FAIL&nbsp</td>");
        writer.write("<td class='subheading'>&nbsp;Steps Passed&nbsp;:</td>");
        writer.write("<td class='pass'> " + str(self.strPassCount)
                     + "</td>");
        writer.write("</tr> ");
        writer.write("<tr class='subheading'>");
        writer.write("<td class='subheading'>&nbsp;Steps Failed&nbsp;: </td>");
        writer.write("<td class='fail'>" + str(self.strFailCount)
                     + "</td>");

        writer.write("<td class='subheading'>&nbsp;Steps Warning&nbsp;: </td>");
        writer.write("<td class='warning'>" + str(self.strWarning)
                     + "</td>");
        writer.write("</tr>");


    def fnCopyRight(self,writer):
        strFooterText = "Cigniti Technologies Limited \\xa9 Copyright 2019. All Rights Reserved."
        writer.write("</table>");
        writer.write("<table id='footer'>");
        writer.write("<colgroup>");
        writer.write("<col style='width: 25%' />");
        writer.write("<col style='width: 25%' />");
        writer.write("<col style='width: 25%' />");
        writer.write("<col style='width: 25%' />");
        writer.write("</colgroup>");
        writer.write("<tfoot>");
        writer.write("<tr class='heading'> ");
        writer.write("<th colspan='4'>Cigniti Technologies Limited @ Copyright 2019. All Rights Reserved.&nbsp;</th> ");
        writer.write("</tr> ");

    def fnAddPassToDetailRecord(self,writer,objData):
        writer.write("<tr class='content2' >");
        writer.write("<td class='justified'>" + str(objData.strStepNo) + "</td>");
        writer.write("<td class='justified'>" + objData.strStepName + "</td>");
        writer.write("<td class='justified'>" + objData.strStepDetail+ "</td> ");
        if (objData.strFilePath != ""):
            writer.write("<td class='PASS' align='center'><a  href='" + "./Screenshots" + "/" + objData.strFilePath
                         + ".jpeg'" + " alt= Screenshot  width= 15 height=15 style='text-decoration:none;'><img  src='./Screenshots/passed.ico' width='18' height='18'/></a></td>");
        else:
            writer.write(
                "<td class='Pass' align='center'><img  src='./Screenshots/passed.ico' width='18' height='18'/></td> ");
        writer.write("<td><small>" + objData.strTimeStamp + "</small></td> ");
        writer.write("</tr> ");

    def fnAddFailToDetailRecord(self,writer,objData):
        writer.write("<tr class='content2' >");
        writer.write("<td class='justified'>" + str(objData.strStepNo) + "</td>");
        writer.write("<td class='justified'>" + objData.strStepName + "</td>");
        writer.write("<td class='justified'>" + objData.strStepDetail + "</td> ");
        if(objData.strFilePath!=""):
            writer.write("<td class='FAIL' align='center'><a  href='" + "./Screenshots" + "/"+objData.strFilePath
                     + ".jpeg'" + " alt= Screenshot  width= 15 height=15 style='text-decoration:none;'><img  src='./Screenshots/failed.ico' width='18' height='18'/></a></td>");
        else:
            writer.write("<td class='FAIL' align='center'><img  src='./Screenshots/failed.ico' width='18' height='18'/></td> ");
        writer.write("<td><small>" + objData.strTimeStamp + "</small></td> ");
        writer.write("</tr> ");

    def fnAddWarningToDetailRecord(self,writer,objData):
        writer.write("<tr class='content2' >");
        writer.write("<td class='justified'>" + str(objData.strStepNo) + "</td>");
        writer.write("<td class='justified'>" + objData.strStepName + "</td>");
        writer.write("<td class='justified'>" + objData.strStepDetail + "</td> ");
        if(objData.strFilePath!=""):
            writer.write("<td class='Warning' align='center'><a  href='" + "./Screenshots" + "/"+objData.strFilePath
                     + ".jpeg'" + " alt= Screenshot  width= 15 height=15 style='text-decoration:none;'><img  src='./Screenshots/warning.ico' width='18' height='18'/></a></td>");
        else:
            writer.write("<td class='Warning' align='center'><img  src='./Screenshots/warning.ico' width='18' height='18'/></td> ");
        writer.write("<td><small>" + objData.strTimeStamp + "</small></td> ");
        writer.write("</tr> ");

    def fnAddStepToDetailRecord(self,writer,objData):
        print(objData.strStepName)
        print(objData.strStepDetail)
        writer.write("<tbody>");
        writer.write("<tr class='section'> ");
        writer.write(
            "<td colspan='5' onclick=toggleMenu('" + objData.strStepName.replace(" ", "_")+ "')>+ " + objData.strStepName.replace(" ", "_")
 + "</td>");
        writer.write("</tr> ");
        writer.write("</tbody>");
        writer.write("<tbody id='" + objData.strStepName.replace(" ", "_") + "' style='display:table-row-group'>");


class SummaryReport:
    strReportName=""
    strReportPath=""
    strTestCaseCount=0
    strTestPassCount=0
    strTestFailCount=0
    strStartDate=""
    strEndDate=""
    strTimeTaken=""
    DetailReportSummary=[]
    def __init__(self):
        print("SummaryReport")
        self.strTimeTaken = time.time()
        self.strStartDate=Reporter.fnGetTimeStamp()
        self.DetailReportSummary = list()
        strFolderName=Reporter.fnGetTimeStampString()
        print(strFolderName)
        strFolderPath=Reporter.fnGetReportPath()
        print(strFolderPath)
        FileUtil.fnCreateFolder(strFolderPath,strFolderName)
        self.strReportPath=strFolderPath+"/"+strFolderName
        FileUtil.fnCreateFolder(self.strReportPath, "Screenshots")
        Reporter.fnCopyReportLogo(self.strReportPath+"/Screenshots")
        self.strTestCaseCount = 0
        self.strTestPassCount = 0
        self.strTestFailCount = 0

    def fnCreateSummaryReport(self):
        print("Create Detail HTML Summry Report")
        self.strTimeTaken = int(time.time() - self.strTimeTaken)
        self.strEndDate = Reporter.fnGetTimeStamp()
        strFileName = self.strReportPath + "/Automation_Summary_Report.html"
        writer = f = open(strFileName, "w+")
        try:
            writer.write("<!DOCTYPE html>");
            writer.write("<html> ");
            writer.write("<head> ");
            writer.write("<meta charset='UTF-8'> ");
            writer.write("<title>"+GlobalConfig.ReportTitle+"</title>");
            writer.write("<style type='text/css'>");
            writer.write("body {");
            writer.write("background-color: #FFFFFF; ");
            writer.write("font-family: Verdana, Geneva, sans-serif; ");
            writer.write("text-align: center; ");
            writer.write("} ");
            writer.write("small { ");
            writer.write("font-size: 0.7em; ");
            writer.write("} ");
            writer.write("table { ");
            writer.write("box-shadow: 9px 9px 10px 4px #BDBDBD;");
            writer.write("border: 0px solid #4D7C7B;");
            writer.write("border-collapse: collapse; ");
            writer.write("border-spacing: 0px; ");
            writer.write("width: 1000px; ");
            writer.write("margin-left: auto; ");
            writer.write("margin-right: auto; ");
            writer.write("} ");
            writer.write("tr.heading { ");
            writer.write("background-color: #041944;");
            writer.write("color: #FFFFFF; ");
            writer.write("font-size: 0.7em; ");
            writer.write("font-weight: bold; ");
            writer.write(
                "background:-o-linear-gradient(bottom, #999999 5%, #000000 100%);	background:-webkit-gradient( linear, left top, left bottom, color-stop(0.05, #999999), color-stop(1, #000000) );");
            writer.write("background:-moz-linear-gradient( center top, #999999 5%, #000000 100% );");
            writer.write(
                "filter:progid:DXImageTransform.Microsoft.gradient(startColorstr=#999999, endColorstr=#000000);	background: -o-linear-gradient(top,#999999,000000);");
            writer.write("} ");
            writer.write("tr.subheading { ");
            writer.write("background-color: #6A90B6;");
            writer.write("color: #000000; ");
            writer.write("font-weight: bold; ");
            writer.write("font-size: 0.7em; ");
            writer.write("text-align: justify; ");
            writer.write("} ");
            writer.write("tr.section { ");
            writer.write("background-color: #A4A4A4; ");
            writer.write("color: #333300; ");
            writer.write("cursor: pointer; ");
            writer.write("font-weight: bold;");
            writer.write("font-size: 0.8em; ");
            writer.write("text-align: justify;");
            writer.write("background:-o-linear-gradient(bottom, #56aaff 5%, #e5e5e5 100%);	background:-webkit-gradient( linear, left top, left bottom, color-stop(0.05, #56aaff), color-stop(1, #e5e5e5) );");
            writer.write("background:-moz-linear-gradient( center top, #56aaff 5%, #e5e5e5 100% );");
            writer.write("filter:progid:DXImageTransform.Microsoft.gradient(startColorstr=#56aaff, endColorstr=#e5e5e5);	background: -o-linear-gradient(top,#56aaff,e5e5e5);");
            writer.write("} ");
            writer.write("tr.subsection { ");
            writer.write("cursor: pointer; ");
            writer.write("} ");
            writer.write("tr.content { ");
            writer.write("background-color: #FFFFFF; ");
            writer.write("color: #000000; ");
            writer.write("font-size: 0.7em; ");
            writer.write("display: table-row; ");
            writer.write("} ");
            writer.write("tr.content2 { ");
            writer.write("background-color:#;E1E1E1");
            writer.write("border: 1px solid #4D7C7B;");
            writer.write("color: #000000; ");
            writer.write("font-size: 0.7em; ");
            writer.write("display: table-row; ");
            writer.write("} ");
            writer.write("td, th { ");
            writer.write("padding: 5px; ");
            writer.write("border: 1px solid #4D7C7B; ");
            writer.write("text-align: inherit\0/; ");
            writer.write("} ");
            writer.write("th.Logos { ");
            writer.write("padding: 5px; ");
            writer.write("border: 0px solid #4D7C7B; ");
            writer.write("text-align: inherit /;");
            writer.write("} ");
            writer.write("td.justified { ");
            writer.write("text-align: justify; ");
            writer.write("} ");
            writer.write("td.pass {");
            writer.write("font-weight: bold; ");
            writer.write("color: green; ");
            writer.write("} ");
            writer.write("td.fail { ");
            writer.write("font-weight: bold; ");
            writer.write("color: red; ");
            writer.write("} ");
            writer.write("td.done, td.screenshot { ");
            writer.write("font-weight: bold; ");
            writer.write("color: black; ");
            writer.write("} ");
            writer.write("td.debug { ");
            writer.write("font-weight: bold; ");
            writer.write("color: blue; ");
            writer.write("} ");
            writer.write("td.warning { ");
            writer.write("font-weight: bold; ");
            writer.write("color: orange; ");
            writer.write("} ");
            writer.write("</style> ");
            writer.write("<script> ");
            writer.write("function toggleMenu(objID) { ");
            writer.write(" if (!document.getElementById) return;");
            writer.write(" var ob = document.getElementById(objID).style; ");
            writer.write("if(ob.display === 'none') { ");
            writer.write(" try { ");
            writer.write(" ob.display='table-row-group';");
            writer.write("} catch(ex) { ");
            writer.write("	 ob.display='block'; ");
            writer.write("} ");
            writer.write("} ");
            writer.write("else { ");
            writer.write(" ob.display='none'; ");
            writer.write("} ");
            writer.write("} ");
            writer.write("function toggleSubMenu(objId) { ");
            writer.write("for(i=1; i<10000; i++) { ");
            writer.write("var ob = document.getElementById(objId.concat(i)); ");
            writer.write("if(ob === null) { ");
            writer.write("break; ");
            writer.write("} ");
            writer.write("if(ob.style.display === 'none') { ");
            writer.write("try { ");
            writer.write(" ob.style.display='table-row'; ");
            writer.write("} catch(ex) { ");
            writer.write("ob.style.display='block'; ");
            writer.write("} ");
            writer.write(" } ");
            writer.write("else { ");
            writer.write("ob.style.display='none'; ");
            writer.write("} ");
            writer.write(" } ");
            writer.write("} ");
            writer.write("</script> ");
            writer.write("</head> ");
            writer.write("<body> ");
            writer.write("</br>");
            writer.write("<table id='Logos'>");
            writer.write("<colgroup>");
            writer.write("<col style='width: 25%' />");
            writer.write("<col style='width: 25%' />");
            writer.write("<col style='width: 25%' />");
            writer.write("<col style='width: 25%' />");
            writer.write("</colgroup> ");
            writer.write("<thead> ");
            writer.write("<tr class='content'>");
            writer.write("<th class ='Logos' colspan='2' >");
            writer.write("<img align ='left' src= ./Screenshots//" + GlobalConfig.Client_logo + "></img>");
            writer.write("</th>");
            writer.write("<th class = 'Logos' colspan='2' > ");
            writer.write("<img align ='right' src= .//Screenshots//" + GlobalConfig.Company_logo + "></img>");
            writer.write("</th> ");
            writer.write("</tr> ");
            writer.write("</thead> ");
            writer.write("</table> ");
            writer.write("<table id='header'> ");
            writer.write("<colgroup> ");
            writer.write("<col style='width: 25%' /> ");
            writer.write("<col style='width: 25%' /> ");
            writer.write("<col style='width: 25%' /> ");
            writer.write(" <col style='width: 25%' /> ");
            writer.write("</colgroup> ");
            writer.write("<thead> ");
            writer.write("<tr class='heading'> ");
            writer.write("<th colspan='4' style='font-family:Copperplate Gothic Bold; font-size:1.4em;'> ");
            writer.write(GlobalConfig.ReportTitle);
            writer.write("</th> ");
            writer.write("</tr> ");
            writer.write("<tr class='subheading'> ");
            writer.write("<th>&nbsp;Suite Executed&nbsp;:&nbsp;</th> ");
            writer.write("<th>Regression</th> ");
            writer.write("<th>&nbsp;Suite Execution Time&nbsp;:&nbsp;</th> ");
            writer.write("<th>" + str(datetime.timedelta(seconds=self.strTimeTaken))+ "</th> ");
            writer.write("<tr class='subheading'> ");
            writer.write("<th>&nbsp;Start&nbspDate&nbsp;Time&nbsp;:&nbsp;</th> ");
            writer.write("<th> &nbsp;" + str(self.strStartDate) + "&nbsp;</th> ");
            writer.write("<th>&nbsp;End&nbspDate&nbsp;Time&nbsp;:&nbsp;</th> ");
            writer.write("<th> &nbsp;" + str(self.strEndDate) + "&nbsp;</th> ");
            writer.write("</tr>");
            writer.write("</thead> ");
            writer.write("</table> ");
            self.fnExecutionDetails(writer)
            writer.write("<table id='main'> ");
            writer.write("<colgroup> ");
            writer.write("<col style='width: 5%' />");
            writer.write("<col style='width: 40%' />");
            writer.write("<col style='width: 10%' />");
            writer.write("<col style='width: 5%' />");
            writer.write("<col style='width: 5%' />");
            writer.write("<col style='width: 5%' />");
            writer.write("<col style='width: 10%' />");
            writer.write("<col style='width: 10%' />");
            writer.write("<col style='width: 10%' />");
            writer.write("</colgroup> ");
            writer.write("<thead> ");
            writer.write("<tr class='heading'> ");
            writer.write("<th>S.NO</th> ");
            writer.write("<th>Test Case</th> ");
            writer.write("<th>Status</th> ");
            writer.write("<th>PASS</th>");
            writer.write("<th>FAIL</th>");
            writer.write("<th>Warning</th>");
            writer.write("<th>Device</th>");
            writer.write("<th>Browser</th>");
            writer.write("<th>Time</th>");
            writer.write("</tr> ");
            writer.write("</thead> ");
            strCount=1
            for x in self.DetailReportSummary:
                self.fnAddTestDetailsReport(writer,x,strCount)
                strCount=strCount+1
            self.fnExecutionDetails(writer)
            self.fnCopyRight(writer)
        except Exception :
            print(Exception.str())
            print("Test")

    def fnAddTestDetails(self, objRecord):
        self.strTestCaseCount = self.strTestCaseCount+1
        if(objRecord.strFailCount>0):
            self.strTestFailCount=self.strTestFailCount+1
        else:
            self.strTestPassCount=self.strTestPassCount+1
        self.DetailReportSummary.append(objRecord)





    def fnExecutionDetails(self,writer):
        writer.write("</table>");
        writer.write("<table id='footer'>");
        writer.write("<colgroup>");
        writer.write("<col style='width: 25%' />");
        writer.write("<col style='width: 25%' />");
        writer.write("<col style='width: 25%' />");
        writer.write("<col style='width: 25%' />");
        writer.write("</colgroup>");
        writer.write("<tfoot>");
        writer.write("<tr class='heading'> ");
        writer.write("<th colspan='4'>Execution Details</th> ");
        writer.write("</tr> ");
        writer.write("<table id='details'> ");
        writer.write("<colgroup> ");
        writer.write("<col style='width: 25%' /> ");
        writer.write("<col style='width: 25%' /> ");
        writer.write("<col style='width: 25%' /> ");
        writer.write(" <col style='width: 25%' /> ");
        writer.write("</colgroup> ");
        writer.write("<thead> ");
        writer.write("<tr class='subheading'> ");
        writer.write("<th>Execution Status : </th> ");
        if (self.strTestFailCount == 0):
            writer.write("<td class='pass'> PASS&nbsp</td>");
        else:
            writer.write("<td class='fail'>FAIL&nbsp</td>");
        writer.write("<th>Total&nbspTest&nbspCase&nbspExecuted&nbsp:&nbsp</th> ");
        writer.write("<th>" + str(self.strTestCaseCount) + "</th>");
        writer.write("<tr class='subheading'> ");
        writer.write("<th>Test&nbspCase&nbspPASS&nbsp:&nbsp</th> ");
        writer.write("<th>"+str(self.strTestPassCount)+"</th>");
        writer.write("<th>Test&nbspCase&nbspFAIL&nbsp:&nbsp</th> ");
        writer.write("<th>" + str(self.strTestFailCount) + "</th>");
        writer.write("</tr> ");
        writer.write("</thead> ");

    def fnAddTestDetailsReport(self,writer,objData,strCount):
        writer.write("<tr class='content' >");
        writer.write("<td class='justified'><b><center>" + str(strCount) + "</center></b></td>");
        writer.write("<td class='justified'><a  href='" + "./"+objData.strReportName
                     + ".html'<b><center>" + objData.strTestName+ "</center></b></td>");
        if (objData.strFailCount == 0):
            writer.write("<td class='pass'> PASS&nbsp</td>");
        else:
            writer.write("<td class='fail'>FAIL&nbsp</td>");
        writer.write("<td class='justified'><b><center>" + str(objData.strPassCount) + "</center></b></td>");
        writer.write("<td class='justified'><b><center>" + str(objData.strFailCount) + "</center></b></td>");
        writer.write("<td class='justified'><b><center>" + str(objData.strWarning) + "</center></b></td>");
        writer.write("<td class='justified'><b><center>" + str(objData.strDevice) + "</center></b></td>");
        writer.write("<td class='justified'><b><center>" + str(objData.strBrowser) + "</center></b></td>");
        writer.write("<td class='justified'><b><center>" + str(objData.strTimeTaken) + "</center></b></td>");
        writer.write("</tr> ");

    def fnCopyRight(self,writer):
        writer.write("</table>");
        writer.write("<table id='footer'>");
        writer.write("<colgroup>");
        writer.write("<col style='width: 25%' />");
        writer.write("<col style='width: 25%' />");
        writer.write("<col style='width: 25%' />");
        writer.write("<col style='width: 25%' />");
        writer.write("</colgroup>");
        writer.write("<tfoot>");
        writer.write("<tr class='heading'> ");
        writer.write("<th colspan='4'>Cigniti Technologies Limited @ Copyright 2019. All Rights Reserved.&nbsp;</th> ");
        writer.write("</tr> ");