import requests
import json

# variaveis dicionairios
parametros = dict()
dataJson = dict()
urlData = dict()
tokenDataApp = dict()
dadosGetUrl = dict()
tokenAccess = dict()
endpoint = dict()

#  Variavel dict para armazenar o link da api e dados de acesso do token
tokenDataApp['access_token'] = 'EAALxQPbRkCoBAJMYvqP48wMb91f7w7wCRdQbhZBYJGzTavrN5IVpERmXMoQUfGRyftGxAgQNMtOCjHXyFN1U0gZB1JOM9j1Q3vBTZBJoBr5sU7dw3cNi0i1PellJFxbPRwvUVQx0siscn7JprdYAZBdmZA3OgQuoFcuHJYzAt16AFui8Xxhbh1yZCN9oGCMAkUMkP4RTTB2fTFH06WtndTHhYPeeaHol7qnbYai0hBnPptuLki39kFImGbNC5Y2YEZD'
tokenDataApp['client_secret'] = '5d1f8782732476667c42d5e811c62a92'
tokenDataApp['client_id'] = '828211274551338'
tokenDataApp['debug'] = 'no'
tokenDataApp['graph_version'] = 'v11.0'
tokenDataApp['url_graph'] = 'https://graph.facebook.com/'
tokenDataApp['endpoint_base'] = tokenDataApp['url_graph'] + tokenDataApp['graph_version'] + '/'


# function que permite acesso a graph api, validando o token
def ChamandoApi(url, endpoint, debug='no'):
    getLinkApi = requests.get(url, endpoint)
    dadosGetUrl['url'] = getLinkApi
    dadosGetUrl['endpoint_params'] = endpoint
    dadosGetUrl['endpoint_params_pretty'] = json.dumps(endpoint, indent=4)
    dadosGetUrl['parser'] = json.loads(dadosGetUrl['url'].content)
    dadosGetUrl['json_data_pretty'] = json.dumps(dadosGetUrl['parser'], indent=4)
    if debug == 'yes':
        print(f"url: {dadosGetUrl['url']}\nEndpoint: {dadosGetUrl['endpoint_params_pretty']}\nApi: {dadosGetUrl['json_data_pretty']}")
    return dadosGetUrl


#  Get do link de acesso a api e retorno em json da resposta parseada
url = f"{tokenDataApp['endpoint_base']}oauth/access_token?client_id={tokenDataApp['client_id']}&client_secret={tokenDataApp['client_secret']}&grant_type=client_credentials "
tokenAccess['get_page'] = requests.get(url)
tokenAccess['parser'] = json.loads(tokenAccess['get_page'].content)


# Requisitando token de longa vida
def GetAccessToken():
    endpoint['grant_type'] = 'fb_exchange_token'
    endpoint['client_id'] = tokenDataApp['client_id']
    endpoint['client_secret'] = tokenDataApp['client_secret']
    endpoint['fb_exchange_token'] = tokenDataApp['access_token']
    url = tokenDataApp['endpoint_base'] + 'oauth/access_token'  # Url da autenticaçao
    return ChamandoApi(url, endpoint, debug='yes')

GetAccessToken()