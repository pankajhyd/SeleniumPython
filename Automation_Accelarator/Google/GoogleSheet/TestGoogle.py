from __future__ import print_function
import gspread
import httplib2
import os
from Automation_Accelarator.Google.GoogleSheet.GoogleSheet import GoogleSheet

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


def get_credentials():
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

    #credential_path ="/Users/admin/Documents/SeleniumPython/Automation_Accelarator/Google/client_secret.json"
    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)

    return credentials




'''
credentials = get_credentials()
client = gspread.authorize(credentials)
sht1 = client.open_by_key('10hAWZku6sbNVflg5ihZdrTkTTrV4HTYvQsByDwjdvF8')
test=sht1.get_worksheet(0)
data=test.cell(1, 1).value
print(data)
data=test.cell(1, 2).value
print(data)
data=test.cell(2, 1).value
print(data)
data=test.cell(2, 2).value
print(data)
test.update_cell(3, 1, "I just wrote to a spreadsheet using Python!")
print(test.col_count)
print(test.row_count)
worksheet = sht1.worksheet("January")
val = worksheet.acell('B1').value
print(val)
print("Column Count==> ",worksheet.col_count)'''

print("Google Sheet Test Column Count ==> ", GoogleSheet.fnGetColumnCount("10hAWZku6sbNVflg5ihZdrTkTTrV4HTYvQsByDwjdvF8","Sheet1"))



