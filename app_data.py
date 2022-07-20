from dotenv import load_dotenv, find_dotenv
import os
import json
import base64
import webbrowser


class GenericActions:

    def BasicAuthenticator():
        load_dotenv(find_dotenv("keys.env"))
        apiUserKey = os.environ.get('HI_USER')
        apiPasswordKey = os.environ.get('HI_PWD')
        concatKey = (apiUserKey + ':' + apiPasswordKey)
        hiApiKey = base64.b64encode(str.encode(concatKey)).decode("ascii")
        headers = {'Content-Type': "application/json",
                   'Authorization': "Basic %s" % hiApiKey, 'Accept': "application/json"}
        return headers

    #def GetTimeLineConsumerName(self, **kwargs):
        #dialogsData = HiPlatformAPI().GetDialogsByProtocol()
        #eventTypeName = 'Hi.Bot'

        # for i in range(len(dialogsData)):
        #originData = dialogsData[i][0]
        #originDataOnlyNumbers = re.sub("\-", "", originData)

        #originId = 'fc6834c3-d0d4-4edf-9389-89938d5551a1'
        # timelineApiGetInfo = 'https://history-api.hiplatform.com/1.0/api/event?eventTypeName=' + \
        #eventTypeName + '&originID=' + originId
        #timelineApiGetInfo = 'https://history-api.hiplatform.com/1.0/api/event?eventTypeName=' + \
            #eventTypeName + '&originID=' + originId
        #response = requests.get(timelineApiGetInfo, headers=self.auth)
        #fullTimeLineData = json.loads(response.content)
        #timeLineData = fullTimeLineData['data']