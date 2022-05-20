"""
Main script running for SIC-R robot's server.
"""

from __future__ import print_function

import os.path
from threading import TIMEOUT_MAX
import requests
import json

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json, read more about scope at
# https://www.bing.com/search?q=scope+google+sheet+api&cvid=63be730e9d5f4c18b4581a6b11892537&aqs=edge..69i57j69i60j69i64j69i60l2.9033j0j1&pglt=129&FORM=ANNTA1&PC=ASTS
SCOPES                  = ['https://www.googleapis.com/auth/spreadsheets','https://www.googleapis.com/auth/drive.file','https://www.googleapis.com/auth/drive']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID   = '1aOQRmc_mDPXV7kXcOEDsUV9mowN7tM6UTR0n8eIlZAI'
SAMPLE_RANGE_NAME       = 'Sheet1!A2:B'

HEADER                  = {"X-API-KEY": "aea77273-6080-4d20-b90c-d48fbe5095e0"}


def main():
    """
    DONE:
    - Request Authentication from Google Sheet API
    - Access UserData Sheet, take data from the sheet
    - Request SEON API
    - Save data to server in JSON format.
    TO_DO:
    - User recognision?
    - Delete UserData when finish
    - Libary for ChatBot, conversation?
    - Acess to User Facebook account and take data.
    """

    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow  = InstalledAppFlow.from_client_secrets_file(
                'credential.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    print('exit: 200')

    try:
        service = build('sheets', 'v4', credentials=creds)

        # Call the Sheets API
        sheet  = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range=SAMPLE_RANGE_NAME).execute()
        values = result.get('values', [])

        if not values:
            print('No data found.')
            return
        print('retrieve data: completed')
    except HttpError as err:
        print(err)

    for row in values:
    # Print columns A and B, which correspond to indices 0 and 1.
        user_name  = row[0]
        user_email = row[1]
    
        # Call SEON API and get account detail branch
        request    = requests.get("https://api.seon.io/SeonRestService/email-api/v2.1/" + user_email, headers=HEADER)
        userData   = request.json()
        userData   = userData['data']['account_details']

        # save the data into SERVER
        with open(user_name + ".json", "w") as file:
            json.dump(userData, file, indent=4, separators=(".","="))
    print('exit: 0')

# Delete unregistered account
def filter():
    return 0

if __name__ == '__main__':
    main()