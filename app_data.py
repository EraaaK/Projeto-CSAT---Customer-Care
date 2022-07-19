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
