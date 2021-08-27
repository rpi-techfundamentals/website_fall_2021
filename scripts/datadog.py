from __future__ import print_function
import os.path
import json
from os import fdopen, remove
from tempfile import mkstemp
from shutil import move
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from datetime import datetime
from datetime import timedelta
import dateutil.parser
import pytz

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/drive']


# helper function to replace a json key value
def replace(file_path, pattern, subst):
    # Create temp file
    fh, abs_path = mkstemp()
    with fdopen(fh, 'w') as new_file:
        with open(file_path) as old_file:
            for line in old_file:
                new_file.write(line.replace(pattern, subst))
    # Remove original file
    remove(file_path)
    # Move new file
    move(abs_path, file_path)


def main():
    # load the json file containing file ID and last edited time
    with open('../config/datadogConfig.json') as f:
        data = json.load(f)

    # standardize the timezone
    utc = pytz.UTC

    # read time from string
    time_before = data["lastModified"]
    time_before_obj = dateutil.parser.isoparse(time_before)
    time_before_obj.replace(tzinfo=pytz.UTC)
    print(time_before_obj)

    # get time now
    time_now = datetime.now(utc).isoformat()
    time_now = dateutil.parser.isoparse(time_now)
    print(time_now)

    # grab a timedelta
    timeBefore = time_now - timedelta(minutes=30)
    print(timeBefore)

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
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('drive', 'v3', credentials=creds)

    # read in the sheet ID from JSON file
    sheet_id = data["sheet_id"]

    # make secondary call to get test file last modified time
    results2 = service.files().get(
        fileId=sheet_id,
        includePermissionsForView="published",
        supportsAllDrives="false",
        fields="modifiedTime"
    ).execute()
    # if the queried time is within 30 minutes of the written time:
    last_modified_time = results2.get("modifiedTime")
    last_modified_time = dateutil.parser.isoparse(last_modified_time)
    last_modified_time.replace(tzinfo=pytz.UTC)

    if last_modified_time < timeBefore:
        # overwrite the results if the query in the Config JSON file to be used next time
        replace('../config/datadogConfig.json', data['lastModified'], time_now.isoformat())


        # download the file
        request = service.files().export_media(
            fileId=sheet_id,
            mimeType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        ).execute()

        # overwrite the data in the class file
        with open('../config/class.xlsx', 'wb') as classFile:
            classFile.write(request)
            classFile.close()

        print('File Update Complete')
    else:
        print('No Changes Detected')


if __name__ == '__main__':
    main()
