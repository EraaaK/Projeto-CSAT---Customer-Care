import requests
import json
import app_data

import datetime


class HiPlatformAPI:
    def __init__(self):
        self.auth = app_data.GenericActions.BasicAuthenticator()

    def GetChatProtocolsByDate(self, **kwargs):

        # params
        channel = 'HiChat'
        dateValue1 = datetime.datetime(2022, 7, 18, 00, 00, 00)
        dateValue2 = datetime.datetime(2022, 7, 18, 23, 59, 59)
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

        return protocolNumberList

    def GetDialogsByProtocol(self, **kwargs):
        protocolNumber = HiPlatformAPI().GetBotProtocolByDate()
        dataList = []
        for i in range(len(protocolNumber)):
            data = requests.get(
                f'https://api.directtalk.com.br/1.10/info/contacts/' + protocolNumber[i] + '/detail', headers=self.auth)

            loadData = json.loads(data.content)
            dataList.append(loadData)
            # print("Protocolo: " +
            #      str(protocolNumber[i]) + " Status: " + str(dataList[i]['state']))
        fullDataView = []
        for i in range(len(protocolNumber)):
            tupleValues = (protocolNumber[i], dataList[i])
            fullDataView.append(tupleValues)

        consumerName = fullDataView[82][1]['properties'][4]['value']
        consumerReview = fullDataView[82][1]['properties'][9]['value']
        print("PING")
        return fullDataView

    def GoogleSheetsExport(self, **kwargs):
        # realizar integração com o Sheets
        pass


start = HiPlatformAPI()
start.GoogleSheetsExport()
