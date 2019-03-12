from __future__ import print_function
import gspread
import httplib2
import os
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/sheets.googleapis.com-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/spreadsheets'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Sheets API Python Quickstart'
'''
Name of File:-FileUtil
File Description:- This File is used for GoogleSheet related operation
Date :- 11-Sep-2018
Author :-Pankaj Kumar
'''
class GoogleSheet:
    """Gets valid user credentials from storage.

           If nothing has been stored, or if the stored credentials are invalid,
           the OAuth2 flow is completed to obtain the new credentials.

           Returns:
               Credentials, the obtained credential.
    """
    def get_credentials(self):
        """Gets valid user credentials from storage.

        If nothing has been stored, or if the stored credentials are invalid,
        the OAuth2 flow is completed to obtain the new credentials.

        Returns:
            Credentials, the obtained credential.
        """
        home_dir = os.path.expanduser('~')
        credential_dir = os.path.join(home_dir, '.credentials')
        if not os.path.exists(credential_dir):
            os.makedirs(credential_dir)
        credential_path = os.path.join(credential_dir,
                                       'sheets.googleapis.com-python-quickstart.json')

        # credential_path ="/Users/admin/Documents/SeleniumPython/Automation_Accelarator/Google/client_secret.json"
        store = Storage(credential_path)
        credentials = store.get()
        if not credentials or credentials.invalid:
            flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
            flow.user_agent = APPLICATION_NAME
            if flags:
                credentials = tools.run_flow(flow, store, flags)
            else:  # Needed only for compatibility with Python 2.6
                credentials = tools.run(flow, store)
            print('Storing credentials to ' + credential_path)

        return credentials

    def fnGetColumnCount(self,strSheetID,strSheetName):
        credentials = self.get_credentials()
        client = gspread.authorize(credentials)
        sht1 = client.open_by_key(strSheetID)
        worksheet = sht1.worksheet(strSheetName)
        return worksheet.col_count;

    def fnGetRowCount(self,strSheetID,strSheetName):
        credentials = self.get_credentials()
        client = gspread.authorize(credentials)
        sht1 = client.open_by_key(strSheetID)
        worksheet = sht1.worksheet(strSheetName)
        return worksheet.row_count;

    def fnGetCellValue(self,strSheetID,strSheetName,range):
        credentials = self.get_credentials()
        client = gspread.authorize(credentials)
        sht1 = client.open_by_key(strSheetID)
        worksheet = sht1.worksheet(strSheetName)
        return worksheet.acell(range).value;

    def fnUpdateCellValue(self,strSheetID,strSheetName,range,strData):
        credentials = self.get_credentials()
        client = gspread.authorize(credentials)
        sht1 = client.open_by_key(strSheetID)
        worksheet = sht1.worksheet(strSheetName)
        worksheet.update_acell(range,strData)

    def fnFindCellValue(self, strSheetID, strSheetName, range, strData):
        credentials = self.get_credentials()
        client = gspread.authorize(credentials)
        sht1 = client.open_by_key(strSheetID)
        worksheet = sht1.worksheet(strSheetName)
        worksheet.findall(strData)


