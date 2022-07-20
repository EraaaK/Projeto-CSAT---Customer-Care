from ssl import OP_NO_RENEGOTIATION
import requests
import json
import app_data
import asyncio
import time
import datetime
import re

class HiPlatformAPI:
    def __init__(self):
        self.auth = app_data.GenericActions.BasicAuthenticator()

    def GetProtocolsByDate(self, **kwargs):

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

    def GetDialogsByProtocol(self, **kwargs):
        protocolNumber = HiPlatformAPI().GetProtocolsByDate()

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

        return fullDataView

    def GetTimeLineConsumerName(self, **kwargs):
        dialogsData = HiPlatformAPI().GetDialogsByProtocol()
        eventTypeName = 'DT.Chat'

        for i in range(dialogsData):
            originData = dialogsData[i][0]
            originDataOnlyNumbers = re.sub("\-","", originData)
            

            #originId = '160411461'
            timelineApiGetInfo = 'https://history-api.hiplatform.com/1.0/api/event?eventTypeName=' + \
                eventTypeName + '&originID=' + originId
            response = requests.get(timelineApiGetInfo, headers=self.auth)
            fullTimeLineData = json.loads(response.content)
            timeLineData = fullTimeLineData['data']


start = HiPlatformAPI()
asyncio.run(start.GetTimeLineConsumerName())
