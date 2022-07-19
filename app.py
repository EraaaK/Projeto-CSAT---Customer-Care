import requests
import json

# Headers
headers = {
    'Authorization': 'Basic ZHRzMTZkOTdmZTQwLWQ5OWItNDVkOS05NGIxLTlhNmZmZDE4MTNhMTpuMjRhdndqOTk1NzBhOTM3bjd4cA=='
}
# API
Data = requests.get(
    f'https://api.directtalk.com.br/1.10/info/contacts/?startDate=1654044972&endDate=1656377772&channel=HiChat',
    headers=headers)

number_protocol = []

# Exibir resultados
# print(Data)
# print(Data.__dict__)

# Definir resultado json como dic_request
dic_request = Data.json()

# Filtrar resultados na requisição.
for row in dic_request:
    # print(row['protocolNumber'])
    #    id = (row['protocolNumber'])
    number_protocol.append(row['protocolNumber'])

# print(id)

# # Montar nova requisição com dados filtrados

dataList = []
for i in range(len(number_protocol)):
    # print(row)
    details = requests.get(
        f'https://api.directtalk.com.br/1.10/info/contacts/' + number_protocol[i] + '/detail', headers=headers)

    fulldataViewContent = json.loads(details.content)
    dataList.append(fulldataViewContent)
    print("Protocolo:" +
          str(number_protocol[i]) + "\nStatus:" + str(dataList[i]['state']))


# # Exibir resultados details

print(details.json())

# Salvar CSV
arquivo = open('Retorno API.csv', 'w')
print(details.json(), file=arquivo)
arquivo.close()
