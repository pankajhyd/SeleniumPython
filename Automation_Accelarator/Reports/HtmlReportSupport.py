from Automation_Accelarator.Reports import Reporter
from Automation_Accelarator.Utilities.FileUtil import FileUtil
from Automation_Accelarator.Config.GlobalConfig import GlobalConfig
class HtmlReportSupport:
        iStartTime = 0;
        iEndTime = 0;
        iExecutionTime = 0;
        iSuiteStartTime = 0;
        iSuiteEndTime = 0;
        iSuiteExecutionTime = 0;
        #ArrayList < Double > list = new ArrayList < Double > ();
        startStepTime = 0;
        endStepTime = 0;
        stepExecutionTime = 0;
        strTestName = "";
        startedAt = "";
        tc_name = "";
        packageName = "";
        #Map < String, String > map = new LinkedHashMap < String, String > ();
        #Map < String, String > testdescrption = new LinkedHashMap < String, String > ();
        #Map < String, String > executionTime = new LinkedHashMap < String, String > ();
        #static ConfiguratorSupport config = new ConfiguratorSupport(
        #"config.properties");
        currentSuit = "";
        pCount = 0;
        fCount = 0;
        #public static String[] key;
        #public static String value[];
        #static String workingDir = System.getProperty("user.dir").replace(File.separator, "/");;
        BFunctionNo = 0;
        #public static ConfiguratorSupport configProps = new ConfiguratorSupport(
        #"config.properties");


    def createHtmlSummaryReport(strReportPath):
        FilePath = strReportPath + "/"+ "SummaryResults_"+ Reporter.fnGetTimeStampString()+ ".html"
        FileUtil.fnDeleteTextFile(FilePath)
        writer = f=open(FilePath, "w+")
        try:
            writer.write("<!DOCTYPE html>");
            writer.write("<html> ");
            writer.write("<head> ");
            writer.write("<meta charset='UTF-8'> ");
            writer.write("<title>"+ GlobalConfig.ReportTitle+"</title>");
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
            writer.write("background:-o-linear-gradient(bottom, #999999 5%, #000000 100%);	background:-webkit-gradient( linear, left top, left bottom, color-stop(0.05, #999999), color-stop(1, #000000) );");
            writer.write("background:-moz-linear-gradient( center top, #999999 5%, #000000 100% );");
            writer.write("filter:progid:DXImageTransform.Microsoft.gradient(startColorstr=#999999, endColorstr=#000000);	background: -o-linear-gradient(top,#999999,000000);");
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
            writer.write("<img align ='left' src= .//Screenshots//" + GlobalConfig.Client_logo
            + ".png></img>");
            writer.write("</th>");
            writer.write("<th class = 'Logos' colspan='2' > ");
            writer.write("<img align ='right' src= .//Screenshots//cigniti.png></img>");
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
            writer.write("<th>&nbsp;Date&nbsp;&&nbsp;Time&nbsp;:&nbsp;" + ""
            + "</th> ");
            writer.write("<th> &nbsp;"+Reporter.fnGetTimeStamp()+"&nbsp;</th> ");
            writer.write("<th>&nbsp;OnError&nbsp;:&nbsp;</th> ");
            writer.write("<th>NextTestCase</th> ");
            writer.write("</tr> ");
            writer.write("<tr class='subheading'> ");
            writer.write("<th>&nbsp;Suite Executed&nbsp;:&nbsp;</th> ");
            writer.write("<th>Regression</th> ");
            writer.write("<th>&nbsp;Browser&nbsp;:</th> ");
            writer.write("<th>"
            + GlobalConfig.browserType+ "</th> ");
            writer.write("</tr> ");
            writer.write("<tr class='subheading'> ");
            writer.write("<th>&nbsp;Host Name&nbsp;:</th> ");
            writer.write("<th>" +
            GlobalConfig.DeviceName+ "</th> ");
            writer.write("<th>&nbsp;No.&nbsp;Of&nbsp;Threads&nbsp;:&nbsp;</th> ");
            writer.write("<th>"
            + "NA" + "</th> ");
            writer.write("</tr> ");
            writer.write("<tr class='subheading'> ");
            writer.write("<th colspan='4'> ");
            writer.write("&nbsp;Environment -  " + GlobalConfig.URL + "");
            writer.write("</th> ");
            writer.write("</tr> ");
            writer.write("</thead> ");
            writer.write("</table> ");
            writer.write("<table id='main'> ");
            writer.write("<colgroup> ");
            writer.write("<col style='width: 5%' /> ");
            writer.write("<col style='width: 35%' /> ");
            writer.write("<col style='width: 42%' /> ");
            writer.write("<col style='width: 10%' /> ");
            writer.write("<col style='width: 8%' /> ");
            writer.write("</colgroup> ");
            writer.write("<thead> ");
            writer.write("<tr class='heading'> ");
            writer.write("<th>S.NO</th> ");
            writer.write("<th>Test Case</th> ");
            writer.write("<th>Description</th> ");
            writer.write("<th>Time</th> ");
            writer.write("<th>Status</th> ");
            writer.write("</tr> ");
            writer.write("</thead> ");
            Iterator < Entry < String, String >> iterator1 = map.entrySet()
            .iterator();
            int serialNo = 1;
            while (iterator1.hasNext()) {
                Map.Entry mapEntry1 = (Map.Entry) iterator1.next();
                key = mapEntry1.getKey().toString().split(":");
                String value = (String) mapEntry1.getValue();
                writer.write("<tbody> ");
                writer.write("<tr class='content2' > ");
                writer.write("<td class='justified'>" + serialNo + "</td>");
                if (value.equals("PASS")) {
                    writer.write("<td class='justified'><a href='"+key[1]+"_Results_"
                    + TestEngine.timeStamp + ".html#'"
                    + "' target='about_blank'>" + key[1]
                    + "</a></td>");
                }
                else {
                    writer.write("<td class='justified'><a href='"+key[1]+"_Results_"
                    + TestEngine.timeStamp + ".html'"
                    + " target='about_blank'>" + key[1] + "</a></td>");
                }
            writer.write("<td class='justified'>" +testdescrption.get(key[1])
            + "</td>");
            writer.write("<td>" + executionTime.get(key[1])+ " Seconds</td>");
            if (TestEngine.testResults.get(key[1]).equals("PASS"))
                writer.write("<td class='pass'>Passed</td> ");
            else
                writer.write("<td class='fail'>Failed</td> ");
            writer.write("</tr>");
            writer.write("</tbody> ");
            serialNo = serialNo + 1;
            }
        writer.flush();
        writer.close();

    catch(Exception e):

        writer.flush();
    writer.close();
}


def createHtmlSummaryReport(browser, Url):
    Filefile = new File(TestEngine.filePath() + File.separator + "SummaryResults_"
+ TestEngine.timeStamp + ".html"); // "SummaryReport.html"
Writer
writer = null;

if (file.exists())
{
file.delete();
}
writer = new
FileWriter(file, true);
try {
writer.write("<!DOCTYPE html>");
writer.write("<html> ");
writer.write("<head> ");
writer.write("<meta charset='UTF-8'> ");
writer.write("<title>HOOQ - Automation Execution Results Summary</title>");

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
writer.write("background:-o-linear-gradient(bottom, #999999 5%, #000000 100%);	background:-webkit-gradient( linear, left top, left bottom, color-stop(0.05, #999999), color-stop(1, #000000) );");
writer.write("background:-moz-linear-gradient( center top, #999999 5%, #000000 100% );");
writer.write("filter:progid:DXImageTransform.Microsoft.gradient(startColorstr=#999999, endColorstr=#000000);	background: -o-linear-gradient(top,#999999,000000);");
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
writer.write("<img align ='left' src= ./Screenshots//" + config.getProperty("Client_logo")
+ ".png></img>");
writer.write("</th>");
writer.write("<th class = 'Logos' colspan='2' > ");
writer.write("<img align ='right' src= .//Screenshots//cigniti.png></img>");
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
writer.write("HOOQ -  Automation Execution Result Summary ");
writer.write("</th> ");
writer.write("</tr> ");
writer.write("<tr class='subheading'> ");
writer.write("<th>&nbsp;Date&nbsp;&&nbsp;Time&nbsp;:&nbsp;" + ""
+ "</th> ");
// writer.write("<th>&nbsp;:&nbsp;08-Apr-2013&nbsp;06:24:21&nbsp;PM</th> ");
writer.write("<th> &nbsp;"+ReportStampSupport.dateTime()+"&nbsp;</th> ");
writer.write("<th>&nbsp;OnError&nbsp;:&nbsp;</th> ");
writer.write("<th>NextTestCase</th> ");
writer.write("</tr> ");


writer.write("<tr class='subheading'> ");
writer.write("<th>&nbsp;Suite Executed&nbsp;:&nbsp;</th> ");
writer.write("<th>Regression</th> ");
writer.write("<th>&nbsp;Browser&nbsp;:</th> ");
writer.write("<th>"
+ browser+ "</th> ");
writer.write("</tr> ");


writer.write("<tr class='subheading'> ");
writer.write("<th>&nbsp;Host Name&nbsp;:</th> ");
writer.write("<th>" +
TestEngine.DeviceName+ "</th> ");
writer.write("<th>&nbsp;No.&nbsp;Of&nbsp;Threads&nbsp;:&nbsp;</th> ");
writer.write("<th>"
+ "NA" + "</th> ");
writer.write("</tr> ");

writer.write("<tr class='subheading'> ");
writer.write("<th colspan='4'> ");
writer.write("&nbsp;Environment -  " + Url + "");
writer.write("</th> ");
writer.write("</tr> ");
writer.write("</thead> ");
writer.write("</table> ");
writer.write("<table id='main'> ");
writer.write("<colgroup> ");
writer.write("<col style='width: 5%' /> ");
writer.write("<col style='width: 35%' /> ");
writer.write("<col style='width: 42%' /> ");
writer.write("<col style='width: 10%' /> ");
writer.write("<col style='width: 8%' /> ");
writer.write("</colgroup> ");
writer.write("<thead> ");
writer.write("<tr class='heading'> ");
writer.write("<th>S.NO</th> ");
writer.write("<th>Test Case</th> ");
writer.write("<th>Description</th> ");
writer.write("<th>Time</th> ");
writer.write("<th>Status</th> ");
writer.write("</tr> ");
writer.write("</thead> ");
Iterator < Entry < String, String >> iterator1 = map.entrySet()
.iterator();
int serialNo = 1;
while (iterator1.hasNext()) {
Map.Entry mapEntry1 = (Map.Entry) iterator1.next();
key = mapEntry1.getKey().toString().split(":");
String value = (String) mapEntry1.getValue();
writer.write("<tbody> ");
writer.write("<tr class='content2' > ");
writer.write("<td class='justified'>" + serialNo + "</td>");
if (value.equals("PASS")) {
writer.write("<td class='justified'><a href='"+key[1]+"_Results_"
+ TestEngine.timeStamp + ".html#'"
+ "' target='about_blank'>" + key[1].substring(0, key[1].indexOf("-"))
+ "</a></td>");
} else {
writer.write("<td class='justified'><a href='"+key[1]+"_Results_"
+ TestEngine.timeStamp + ".html'"
+ " target='about_blank'>" + key[1].substring(0, key[1].indexOf("-"))
+ "</a></td>");
}
writer.write("<td class='justified'>" + TestEngine.testDescription.get(key[1])
+ "</td>");

writer.write("<td>" + executionTime.get(key[1])+ " Seconds</td>");
if (TestEngine.testResults.get(key[1]).equals("PASS"))
writer.write("<td class='pass'>Passed</td> ");
else
writer.write("<td class='fail'>Failed</td> ");
writer.write("</tr>");
writer.write("</tbody> ");
serialNo = serialNo + 1;
}
writer.flush();
writer.close();

} catch(Exception
e) {
writer.flush();
writer.close();
}

}

// Create
a
report
file
public
static
void
htmlCreateReport()
throws
Exception
{

// map.clear();
File
file = new
File(TestEngine.filePath() + "/" + strTestName + "_Results_"
+ TestEngine.timeStamp + ".html"); // "Results.html"
if (file.exists())
{
file.delete();
}

}


public
static
void
onSuccess(String
strStepName, String
strStepDes) {

    File
file = new
File(TestEngine.filePath() + "/" + strTestName + "_Results_"
+ TestEngine.timeStamp + ".html"); // "SummaryReport.html"
Writer
writer = null;
TestEngine.stepNum = TestEngine.stepNum + 1;

try {
// testdescrption.put(TestTitleDetails.x.toString(), TestEngine.testDescription.get(TestTitleDetails.x));
if (!map.get(packageName + ":" + tc_name).equals("FAIL")) {
map.put(packageName + ":" + tc_name, "PASS");
// map.put(TestTitleDetails.x.toString(), TestEngine.testDescription.get(TestTitleDetails.x.toString()));
}
writer = new FileWriter(file, true);
writer.write("<tr class='content2' >");
writer.write("<td>" + TestEngine.stepNum + "</td> ");
writer.write("<td class='justified'>" + strStepName + "</td>");
writer.write("<td class='justified'>" + strStepDes + "</td> ");
writer.write("<td class='Pass' align='center'><img  src='./Screenshots/passed.ico' width='18' height='18'/></td> ");
TestEngine.PassNum = TestEngine.PassNum + 1;
String strPassTime = ReportStampSupport.getTime();
writer.write("<td><small>" + strPassTime + "</small></td> ");
writer.write("</tr> ");
writer.close();

}catch (Exception e) {
e.printStackTrace();
}

}
public
static
void
onWarning(String
strStepName, String
strStepDes) {
Writer
writer = null;
try {
File file = new File(TestEngine.filePath() + "/" + strTestName+"_Results_"
+ TestEngine.timeStamp + ".html"); // "SummaryReport.html"

writer = new FileWriter(file, true);
TestEngine.stepNum = TestEngine.stepNum + 1;

writer.write("<tr class='content2' >");
writer.write("<td>" + TestEngine.stepNum + "</td> ");
writer.write("<td class='justified'>" + strStepName + "</td>");
writer.write("<td class='justified'>" + strStepDes + "</td> ");
// TestEngine.FailNum = TestEngine.FailNum + 1;


writer.write("<td class='Fail'  align='center'><a  href='"+"./Screenshots"+"/"
+ strStepName.replace(" ", "_") + "_" + TestEngine.timeStamp
+ ".jpeg'"+" alt= Screenshot  width= 15 height=15 style='text-decoration:none;'><img src='./Screenshots/warning.ico' width='18' height='18'/></a></td>");

String strFailTime = ReportStampSupport.getTime();
writer.write("<td><small>" + strFailTime + "</small></td> ");
writer.write("</tr> ");
writer.close();

} catch (Exception e) {

}

}

/ *
*
*
* /
public
static
void
onFailure(String
strStepName, String
strStepDes, String
randomValueForScreeShot) {
Writer
writer = null;
try {
File file = new File(TestEngine.filePath() + "/" + strTestName+"_Results_"
+ TestEngine.timeStamp + ".html"); // "SummaryReport.html"

writer = new FileWriter(file, true);
TestEngine.stepNum = TestEngine.stepNum + 1;

writer.write("<tr class='content2' >");
writer.write("<td>" + TestEngine.stepNum + "</td> ");
writer.write("<td class='justified'>" + strStepName + "</td>");
writer.write("<td class='justified'>" + strStepDes
/ * +" <a href= '"+TestEngine.driver.getCurrentUrl()
+ "'>" +TestEngine.driver.getCurrentUrl()+ "</a> " * / + "</td> ");
TestEngine.FailNum = TestEngine.FailNum + 1;


writer.write("<td class='Fail' align='center'><a  href='"+"./Screenshots"+"/"
+ strStepName.replace(" ", "_") + "_" + TestEngine.timeStamp + randomValueForScreeShot
+ ".jpeg'"+" alt= Screenshot  width= 15 height=15 style='text-decoration:none;'><img  src='./Screenshots/failed.ico' width='18' height='18'/></a></td>");

String strFailTime = ReportStampSupport.getTime();
writer.write("<td><small>" + strFailTime + "</small></td> ");
writer.write("</tr> ");
writer.close();
if (!map.get(packageName + ":" + tc_name).equals("PASS")) {
map.put(packageName + ":" + tc_name, "FAIL");
// map.put(TestTitleDetails.x.toString(), TestEngine.testDescription.get(TestTitleDetails.x.toString()));
}
} catch (Exception e) {

}finally{
Assert.assertTrue(false,
"Step "+strStepName+" Failed with description "+  strStepDes);
}

}

public
static
void
onSuccessContinue(String
strStepName, String
strStepDes, String
randomValueForScreeShot) {
Writer
writer = null;
try {
File file = new File(TestEngine.filePath() + "/" + strTestName+"_Results_"
+ TestEngine.timeStamp + ".html"); // "SummaryReport.html"

writer = new FileWriter(file, true);
TestEngine.stepNum = TestEngine.stepNum + 1;

writer.write("<tr class='content2' >");
writer.write("<td>" + TestEngine.stepNum + "</td> ");
writer.write("<td class='justified'>" + strStepName + "</td>");
writer.write("<td class='justified'>" + strStepDes
/ * +" <a href= '"+TestEngine.driver.getCurrentUrl()
+ "'>" +TestEngine.driver.getCurrentUrl()+ "</a> " * / + "</td> ");
TestEngine.PassNum = TestEngine.PassNum + 1;


writer.write("<td class='Fail' align='center'><a  href='"+"./Screenshots"+"/"
+ strStepName.replace(" ", "_") + "_" + TestEngine.timeStamp + randomValueForScreeShot
+ ".jpeg'"+" alt= Screenshot  width= 15 height=15 style='text-decoration:none;'><img  src='./Screenshots/screenshot.png' width='18' height='18'/></a></td>");

String strFailTime = ReportStampSupport.getTime();
writer.write("<td><small>" + strFailTime + "</small></td> ");
writer.write("</tr> ");
writer.close();
if (!map.get(packageName + ":" + tc_name).equals("PASS")) {
map.put(packageName + ":" + tc_name, "FAIL");
// map.put(TestTitleDetails.x.toString(), TestEngine.testDescription.get(TestTitleDetails.x.toString()));
}
} catch (Exception e) {

}

}
public
static
void
onFailureContinue(String
strStepName, String
strStepDes, String
randomValueForScreeShot) {
Writer
writer = null;
try {
File file = new File(TestEngine.filePath() + "/" + strTestName+"_Results_"
+ TestEngine.timeStamp + ".html"); // "SummaryReport.html"

writer = new FileWriter(file, true);
TestEngine.stepNum = TestEngine.stepNum + 1;

writer.write("<tr class='content2' >");
writer.write("<td>" + TestEngine.stepNum + "</td> ");
writer.write("<td class='justified'>" + strStepName + "</td>");
writer.write("<td class='justified'>" + strStepDes
/ * +" <a href= '"+TestEngine.driver.getCurrentUrl()
+ "'>" +TestEngine.driver.getCurrentUrl()+ "</a> " * / + "</td> ");
TestEngine.FailNum = TestEngine.FailNum + 1;


writer.write("<td class='Fail' align='center'><a  href='"+"./Screenshots"+"/"
+ strStepName.replace(" ", "_") + "_" + TestEngine.timeStamp + randomValueForScreeShot
+ ".jpeg'"+" alt= Screenshot  width= 15 height=15 style='text-decoration:none;'><img  src='./Screenshots/failed.ico' width='18' height='18'/></a></td>");

String strFailTime = ReportStampSupport.getTime();
writer.write("<td><small>" + strFailTime + "</small></td> ");
writer.write("</tr> ");
writer.close();
if (!map.get(packageName + ":" + tc_name).equals("PASS")) {
map.put(packageName + ":" + tc_name, "FAIL");
// map.put(TestTitleDetails.x.toString(), TestEngine.testDescription.get(TestTitleDetails.x.toString()));
}
} catch (Exception e) {

}

}
public
static
void
testHeader(String
testName) {
Writer
writer = null;
try {
strTestName = testName;
File file = new File(TestEngine.filePath() +"/"+strTestName+ "_Results_"
+ TestEngine.timeStamp + ".html"); // "Results.html"
writer = new FileWriter(file, true);

writer.write("<!DOCTYPE html> ");
writer.write("<html>");
writer.write("<head> ");
writer.write("<meta charset='UTF-8'> ");
writer.write("<title>" + strTestName
+ " Execution Results</title> ");

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
writer.write("<img align ='left' src= ./Screenshots//" + config.getProperty("Client_logo")
+ ".png></img>");
writer.write("</th>");
writer.write("<th class = 'Logos' colspan='2' > ");
writer.write("<img align ='right' src= .//Screenshots//cigniti.png></img>");
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
writer.write("**" + strTestName + " Execution Results **");
writer.write("</th> ");
writer.write("</tr> ");
writer.write("<tr class='subheading'> ");
writer.write("<th>&nbsp;Date&nbsp;&&nbsp;Time&nbsp;:&nbsp;</th> ");

writer.write("<th>" + ReportStampSupport.dateTime()
+ "</th> ");
writer.write("<th>&nbsp;Iteration&nbsp;Mode&nbsp;:&nbsp;</th> ");
writer.write("<th>RunAllIterations</th> ");
writer.write("</tr> ");

writer.write("<tr class='subheading'> ");
writer.write("<th>&nbsp;Browser&nbsp;:&nbsp;</th> ");
writer.write("<th>"
+configProps.getProperty("browserType")+ "</th> ");
writer.write("<th>&nbsp;Executed&nbsp;on&nbsp;:&nbsp;</th> ");
writer.write("<th>" + TestEngine.DeviceName
+ "</th> ");
writer.write("</tr> ");
writer.write("</thead> ");
writer.write("</table> ");

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
writer.close();
map.put(packageName + ":" + tc_name, "status");
} catch (Exception e) {

} finally {
try {
writer.flush();
writer.close();
} catch (Exception e) {

}
}
}


public
static
void
testHeader(String
testName, String
browser) {
    Writer
writer = null;
try {
strTestName = testName;
File file = new File(TestEngine.filePath() +"/"+strTestName+ "_Results_"
+ TestEngine.timeStamp + ".html"); // "Results.html"
writer = new FileWriter(file, true);

writer.write("<!DOCTYPE html> ");
writer.write("<html>");
writer.write("<head> ");
writer.write("<meta charset='UTF-8'> ");
writer.write("<title>" + strTestName
+ " Execution Results</title> ");

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
writer.write("<img align ='left' src= ./Screenshots//" + config.getProperty("Client_logo")
+ ".png></img>");
writer.write("</th>");
writer.write("<th class = 'Logos' colspan='2' > ");
writer.write("<img align ='right' src= .//Screenshots//cigniti.png></img>");
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
writer.write("**" + strTestName + " Execution Results **");
writer.write("</th> ");
writer.write("</tr> ");
writer.write("<tr class='subheading'> ");
writer.write("<th>&nbsp;Date&nbsp;&&nbsp;Time&nbsp;:&nbsp;</th> ");

writer.write("<th>" + ReportStampSupport.dateTime()
+ "</th> ");
writer.write("<th>&nbsp;Iteration&nbsp;Mode&nbsp;:&nbsp;</th> ");
writer.write("<th>RunAllIterations</th> ");
writer.write("</tr> ");

writer.write("<tr class='subheading'> ");
writer.write("<th>&nbsp;Browser&nbsp;:&nbsp;</th> ");
writer.write("<th>"
+browser+ "</th> ");
writer.write("<th>&nbsp;Executed&nbsp;on&nbsp;:&nbsp;</th> ");
writer.write("<th>" + TestEngine.DeviceName
+ "</th> ");
writer.write("</tr> ");
writer.write("</thead> ");
writer.write("</table> ");

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
writer.close();
map.put(packageName + ":" + tc_name, "status");
} catch (Exception e) {

} finally {
try {
writer.flush();
writer.close();
} catch (Exception e) {

}
}
}


public
static
void
reportStep(String
StepDesc) {
    StepDesc = StepDesc.replaceAll(" ", "_");
File
file = new
File(TestEngine.filePath() + "/" + strTestName + "_Results_"
+ TestEngine.timeStamp + ".html"); // "SummaryReport.html"
FileWriter
writer = null;

try {
writer = new FileWriter(file, true); / * new BufferedWriter(new FileWriter(file), 32768); * /
if (BFunctionNo > 0) {
writer.write("</tbody>");
}
writer.write("<tbody>");
writer.write("<tr class='section'> ");
writer.write("<td colspan='5' onclick=toggleMenu('" + StepDesc+TestEngine.stepNum+ "')>+ " + StepDesc + "</td>");
writer.write("</tr> ");
writer.write("</tbody>");
writer.write("<tbody id='" + StepDesc+TestEngine.stepNum + "' style='display:table-row-group'>");
writer.close();
BFunctionNo = BFunctionNo + 1;
} catch (Exception e) {

}
}

public
static
void
closeDetailedReport()
{

File
file = new
File(TestEngine.filePath() + File.separator + strTestName + "_Results_"
     + TestEngine.timeStamp + ".html"); // "SummaryReport.html"
Writer
writer = null;

try {
writer = new FileWriter(file, true);
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
writer.write("<th colspan='4'>Execution Time In Seconds (Includes Report Creation Time) : "
+ executionTime.get(HtmlReportSupport.tc_name)+ "&nbsp;</th> ");
writer.write("</tr> ");
writer.write("<tr class='content'>");
writer.write("<td class='pass'>&nbsp;Steps Passed&nbsp;:</td>");
writer.write("<td class='pass'> " + TestEngine.PassNum
+ "</td>");
writer.write("<td class='fail'>&nbsp;Steps Failed&nbsp;: </td>");
writer.write("<td class='fail'>" + TestEngine.FailNum
+ "</td>");
writer.write("</tr>");
writer.close();
} catch (Exception e) {

}
}

public
static
void
closeSummaryReport()
{
File
file = new
File(TestEngine.filePath() + File.separator + "SummaryResults_"
     + TestEngine.timeStamp + ".html"); // "SummaryReport.html"
Writer
writer = null;
try {
writer = new FileWriter(file, true);

writer.write("<table id='footer'>");
writer.write("<colgroup>");
writer.write("<col style='width: 25%' />");
writer.write("<col style='width: 25%' />");
writer.write("<col style='width: 25%' />");
writer.write("<col style='width: 25%' /> ");
writer.write("</colgroup> ");
writer.write("<tfoot>");
writer.write("<tr class='heading'>");
writer.write("<th colspan='4'>Total Duration  In Seconds (Including Report Creation) : "
+ ((int)HtmlReportSupport.iSuiteExecutionTime) + "</th>");
writer.write("</tr>");
writer.write("<tr class='content'>");
writer.write("<td class='pass'>&nbsp;Tests Passed&nbsp;:</td>");
writer.write("<td class='pass'> " + TestEngine.passCounter
+ "</td> ");
writer.write("<td class='fail'>&nbsp;Tests Failed&nbsp;:</td>");
writer.write("<td class='fail'> " + TestEngine.failCounter
+ "</td> ");
writer.write("</tr>");
writer.write("</tfoot>");
writer.write("</table> ");

writer.close();
} catch (Exception e) {

}
}
public
static
void
copyLogos()
{
File
srcFolder = new
File("Logos");
File
destFolder = new
File(TestEngine.filePath() + File.separator + "Screenshots");
// make
sure
source
exists
if (!srcFolder.exists()){
System.out.println("Directory does not exist.");
} else {

try{
copyFolder(srcFolder, destFolder);
}catch(IOException e){

}
}
}
public
static
void
copyFolder(File
src, File
dest)
throws
IOException
{

if (src.isDirectory())
{

// if directory not exists, create it
if (!dest.exists()){
dest.mkdir();
System.out.println("Directory copied from "
+ src + "  to " + dest);
}

// list
all
the
directory
contents
String
files[] = src.list();

for (String file: files) {
                         // construct the src and dest file structure
File srcFile = new File(src, file);
File destFile = new File(dest, file);
// recursive copy
copyFolder(srcFile, destFile);
}

} else {
// if file, then copy it
// Use
bytes
stream
to
support
all
file
types
InputStream in = new
FileInputStream(src);
OutputStream
out = new
FileOutputStream(dest);

byte[]
buffer = new
byte[1024];

int
length;
// copy
the
file
content in bytes
while ((length = in.read(buffer)) > 0){
out.write(buffer, 0, length);
}
in.close();
out.close();
System.out.println("File copied from " + src + " to " + dest);
}
}

}
