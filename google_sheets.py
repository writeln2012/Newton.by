from pprint import pprint
from oauth2client.service_account import ServiceAccountCredentials

import httplib2
import googleapiclient
from googleapiclient import discovery

CREDENTIALS_FILE = 'creds.json'
spreadsheet_id = "119zT2AFXdJvJHPrd5PR1sCpnU8NMNk5S"

credentials = ServiceAccountCredentials.from_json_keyfile_name(
    CREDENTIALS_FILE,
    'https://www.googleapis.com/auth/spreadsheets')
httpAuth = credentials.authorize(httplib2.Http())
service = googleapiclient.discovery.build('sheets', 'v4', http=httpAuth)

values = service.spreadsheets().values().get(
    spreadsheetId=spreadsheet_id,
    range='B1E10',
    majorDimension='ROWS')
response = values.execute()
pprint(response)
