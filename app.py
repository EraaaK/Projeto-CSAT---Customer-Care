import requests
import json
import app_data


class HiPlatformAPI:
    def __init__(self):
        pass

    def GetProtocolsByDate():
        auth = app_data.GenericActions.BasicAuthenticator()

        # params
        channel = 'HiChat'
        startDate = '1654044972'
        endDate = '1656377772'

        data = requests.get(
            f'https://api.directtalk.com.br/1.10/info/contacts/?startDate=' +
            startDate + '&endDate=' + endDate + '&channel=' + channel,
            headers=auth)

        fullData = json.loads(data.content)
        protocolNumberList = []
        for row in fullData:
            protocolNumberList.append(row['protocolNumber'])

        return protocolNumberList

    def GetDialogsByProtocol():
        protocolNumber = HiPlatformAPI.GetProtocolsByDate()
        auth = app_data.GenericActions.BasicAuthenticator()

        dataList = []
        for i in range(len(protocolNumber)):
            data = requests.get(
                f'https://api.directtalk.com.br/1.10/info/contacts/' + protocolNumber[i] + '/detail', headers=auth)

            fulldataViewContent = json.loads(data.content)
            dataList.append(fulldataViewContent)
            print("Protocolo: " +
                  str(protocolNumber[i]) + " Status: " + str(dataList[i]['state']))


HiPlatformAPI.GetDialogsByProtocol()
