from Automation_Accelarator.Google.GoogleSheet.GoogleSheet import GoogleSheet
print(GoogleSheet().fnGetColumnCount("10hAWZku6sbNVflg5ihZdrTkTTrV4HTYvQsByDwjdvF8","Sheet1"))
print(GoogleSheet().fnGetRowCount("10hAWZku6sbNVflg5ihZdrTkTTrV4HTYvQsByDwjdvF8","Sheet1"))
print(GoogleSheet().fnGetCellValue("10hAWZku6sbNVflg5ihZdrTkTTrV4HTYvQsByDwjdvF8","Sheet1","B1"))
print(GoogleSheet().fnUpdateCellValue("10hAWZku6sbNVflg5ihZdrTkTTrV4HTYvQsByDwjdvF8","Sheet1","B1","RajaRani"))
print(GoogleSheet().fnGetCellValue("10hAWZku6sbNVflg5ihZdrTkTTrV4HTYvQsByDwjdvF8","Sheet1","B1"))