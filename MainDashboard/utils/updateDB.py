import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from google.oauth2 import service_account
from MainDashboard.models import *

def updateFdDB(request):
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    SERVICE_ACCOUNT_FILE = 'D:\project_works\Django projects\MyWealthTracker_Project\MyWealthTracker\static\config\keys.json'
    creds= None
    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)    
    SAMPLE_SPREADSHEET_ID = '1C2QfUv9uWBZGzycUIthYQXdS36q-sURqdVPbdShtmQ8'
    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()
   
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range="FD!B8:F19",valueRenderOption='FORMATTED_VALUE').execute()
    values = result.get('values', [])
    FixedDepositDasboardArray = FixedDepositDasboard.objects.all().filter(userId=request.user.username).order_by('remainingDays')
    DBrow=0
    count=0
   
    for row in values:
        if DBrow<len(FixedDepositDasboardArray):
            FixedDepositDasboardArray[DBrow].startDate=row[0]
            FixedDepositDasboardArray[DBrow].endDate=row[2]
            FixedDepositDasboardArray[DBrow].deposit=row[1]
            FixedDepositDasboardArray[DBrow].interest=row[4]
            FixedDepositDasboardArray[DBrow].remainingDays=row[3]
            FixedDepositDasboardArray[DBrow].save()
            DBrow=DBrow+1
            count=count+1
            if count==len(values):
                while(count<len(FixedDepositDasboardArray)):
                    FixedDepositDasboardArray[count].delete()
                    count=count+1
        else:
            fixedDepositDasboardObj = FixedDepositDasboard.objects.create(userId=request.user.username)
            fixedDepositDasboardObj.startDate=row[0]
            fixedDepositDasboardObj.endDate=row[2]
            fixedDepositDasboardObj.deposit=row[1]
            fixedDepositDasboardObj.interest=row[4]
            fixedDepositDasboardObj.remainingDays=row[3]
            fixedDepositDasboardObj.save()

def updateDashboardDB(request):
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    SERVICE_ACCOUNT_FILE = 'D:\project_works\Django projects\MyWealthTracker_Project\MyWealthTracker\static\config\keys.json'
    creds= None
    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)    
    SAMPLE_SPREADSHEET_ID = '1POVew4KJ-WWyylIc_d1OukHbfZN8hSfMF1mQsXyIy3c'
    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()
   
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range="Portfolio!G3:G8",valueRenderOption='FORMATTED_VALUE').execute()
    values = result.get('values', [])
    if MainDashboard.objects.filter(userId=request.user.username).exists():
      mainDashboardValues = MainDashboard.objects.get(userId=request.user.username)
      mainDashboardValues.savings=values[5][0]
      mainDashboardValues.fixedDeposit = values[2][0]
      mainDashboardValues.mutualFund = values[3][0]
      mainDashboardValues.stock = values[4][0]
      mainDashboardValues.total =values[0][0]
      mainDashboardValues.save()      
    else:
      mainDashboardValues=MainDashboard.objects.create(userId=request.user.username)
      mainDashboardValues.savings=values[5][0]
      mainDashboardValues.fixedDeposit = values[2][0]
      mainDashboardValues.mutualFund = values[3][0]
      mainDashboardValues.stock = values[4][0]
      mainDashboardValues.total =values[0][0]
      mainDashboardValues.save()    

