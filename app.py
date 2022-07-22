from concurrent.futures import thread
import requests
from dotenv import load_dotenv, find_dotenv
import json
import app_data
import datetime
import gspread
import os
import threading


class HiPlatformAPI:
    def __init__(self):
        self.auth = app_data.GenericActions.BasicAuthenticator()

    def GetChatProtocolsByDate(self, **kwargs):

        # params
        channel = 'HiChat'
        dateValue1 = datetime.datetime(2022, 7, 21, 14, 00, 00)
        dateValue2 = datetime.datetime(2022, 7, 21, 15, 40, 00)
        startDate = str(datetime.datetime.timestamp(
            dateValue1))
        endDate = str(datetime.datetime.timestamp(
            dateValue2))

        data = requests.get(
            f'https://api.directtalk.com.br/1.10/info/contacts/?startDate=' +
            startDate + '&endDate=' + endDate + '&channel=' + channel,
            headers=self.auth)

        fullData = json.loads(data.content)
        protocolNumberList = []
        for row in fullData:
            protocolNumberList.append(row['protocolNumber'])

        return protocolNumberList

    def GetBotProtocolByDate(self, **kwargs):
        # params
        channel = 'HiBot'
        dateValue1 = datetime.datetime(2022, 7, 20, 14, 00, 00)
        dateValue2 = datetime.datetime(2022, 7, 20, 15, 59, 59)
        startDate = str(datetime.datetime.timestamp(
            dateValue1))
        endDate = str(datetime.datetime.timestamp(
            dateValue2))

        data = requests.get(
            f'https://api.directtalk.com.br/1.10/info/contacts/?startDate=' +
            startDate + '&endDate=' + endDate + '&channel=' + channel,
            headers=self.auth)

        fullData = json.loads(data.content)
        protocolNumberList = []
        for row in fullData:
            protocolNumberList.append(row['protocolNumber'])
            print("Protocolo " + row['protocolNumber'] + " retornado")

        return protocolNumberList

    def GetDialogsByProtocol(self, **kwargs):
        protocolNumber = HiPlatformAPI().GetBotProtocolByDate()
        dataList = []
        for i in range(len(protocolNumber)):
            data = requests.get(
                f'https://api.directtalk.com.br/1.10/info/contacts/' + protocolNumber[i] + '/detail', headers=self.auth)

            loadData = json.loads(data.content)
            dataList.append(loadData)
        fullDataView = []
        for i in range(len(protocolNumber)):
            tupleValues = (protocolNumber[i], dataList[i])
            fullDataView.append(tupleValues)
            print(str(i) + "dado inserido")
        return fullDataView

    def GoogleSheetsExport(self, **kwargs):
        load_dotenv(find_dotenv("keys.env"))
        code = os.environ.get('CODE')

        data = HiPlatformAPI().GetDialogsByProtocol()

        gc = gspread.service_account(filename='key.json')
        sh = gc.open_by_key(code)
        ws = sh.worksheet('CSAT')

        rowIndex = 2
        for i in range(len(data)):
            consumerName = data[i][1]['properties'][4]['value']
            consumerReview = data[i][1]['properties'][9]['value']
            ws.update_acell('A1', "Identificação")
            ws.update_acell('B1', "Nota")
            ws.format('A1:B1', {'textFormat': {'bold': True}})

            ws.update_cell(rowIndex, 1, consumerName)
            ws.update_cell(rowIndex, 2, consumerReview)
            rowIndex += 1


start = HiPlatformAPI()

threading.Thread(target=start.GetBotProtocolByDate)
threading.Thread(target=start.GetDialogsByProtocol)
threading.Thread(target=start.GoogleSheetsExport)

print("PING")
start.GoogleSheetsExport()
