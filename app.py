import requests
import json
import app_data


class HiPlatformAPI:
    def __init__(self):
        self.auth = app_data.GenericActions.BasicAuthenticator()

    def GetProtocolsByDate(self, **kwargs):

        # params
        channel = 'HiChat'
        startDate = '1654044972'
        endDate = '1656377772'

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

            fulldataViewContent = json.loads(data.content)
            dataList.append(fulldataViewContent)
            print("Protocolo: " +
                  str(protocolNumber[i]) + " Status: " + str(dataList[i]['state']))

    def GetTimeLineConsumerName(self, **kwargs):
        pass


start = HiPlatformAPI()
start.GetDialogsByProtocol()
