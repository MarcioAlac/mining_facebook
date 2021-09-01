import requests
import json

# variaveis dicionairios

parametros = dict()
dataJson = dict()
urlData = dict()
tokenDataApp = dict()
tokenAccess = dict()


#  Variavel dict para armazenar o link da api e dados de acesso do token
tokenDataApp['access_token'] = 'EAALxQPbRkCoBADQeDtaqZCZBapedEQIwX3x4ZBigaiZC5IZC8hTAPZATQyMM26wH6qsRDRx15BUopCduc3ZAno2xs7ZCe7jYDZCGLMub0Bv8SAwEeZA9DwJwlJIxcOXHutvZCaHFMmZCYF8Wowfnq0debtIBR46RqNLtkZAbIHU2IqFIYjWvxIs06QiMSzO6egOHvf9CephAWIUaTL1U2G5uqYCyvYEP3uZCtZBlqlZCsJtxRXURfMICqUeH7BSv0EYd9MGV0YIZD'
tokenDataApp['client_secret'] = '5d1f8782732476667c42d5e811c62a92'
tokenDataApp['client_id'] = '828211274551338'
tokenDataApp['debug'] = 'no'
tokenDataApp['graph_version'] = 'v11.0'
tokenDataApp['url_graph'] = 'https://graph.facebook.com/'
tokenDataApp['endpoint_base'] = tokenDataApp['url_graph'] + tokenDataApp['graph_version'] + '/'


# function que permite acesso a graph api, validando o token
def ChamandoApi(url, endpoint, debug='no'):
    dadosGetUrl = dict()
    getLinkApi = requests.get(url, endpoint)
    dadosGetUrl['url'] = getLinkApi
    dadosGetUrl['endpoint_params'] = endpoint
    dadosGetUrl['endpoint_params_pretty'] = json.dumps(endpoint, indent=4)
    dadosGetUrl['parser'] = json.loads(dadosGetUrl['url'].content)
    dadosGetUrl['json_data_pretty'] = json.dumps(dadosGetUrl['parser'], indent=4)
    if debug == 'yes':
        expira = int(dadosGetUrl['parser']['expires_in'])
        expira = (expira / 86400)
        print(int(expira))
        print(f"url: {dadosGetUrl['url']}\nEndpoint: {dadosGetUrl['endpoint_params_pretty']}\nDias ate o token Api expirar: {int(expira)}")
    return dadosGetUrl


#  Get do link de acesso a api e retorno em json da resposta parseada
url = f"{tokenDataApp['endpoint_base']}oauth/access_token?client_id={tokenDataApp['client_id']}&client_secret={tokenDataApp['client_secret']}&grant_type=client_credentials "
tokenAccess['get_page'] = requests.get(url)
tokenAccess['parser'] = json.loads(tokenAccess['get_page'].content)


# Requisitando token de longa vida
def GetAccessToken():
    endpoint = dict()
    endpoint['grant_type'] = 'fb_exchange_token'
    endpoint['client_id'] = tokenDataApp['client_id']
    endpoint['client_secret'] = tokenDataApp['client_secret']
    endpoint['fb_exchange_token'] = tokenDataApp['access_token']
    url = tokenDataApp['endpoint_base'] + 'oauth/access_token'  # Url da autenticaçao
    ChamandoApi(url, endpoint, debug='yes')
    return endpoint

# retorna funcao
def Search():
    search = dict()
    endpoint = GetAccessToken()  # instanciando a def para torna usavel a variavel enpoint
    search['fields'] = 'me?fields=email,first_name,last_name,languages,friends,likes{engagement,fan_count},birthday,posts{link,is_popular,message},feed{comments}&' + 'access_token='
    search['url'] = tokenDataApp['endpoint_base'] + search['fields'] +tokenDataApp['access_token']
    search['request'] = requests.get(search['url'], params=endpoint)
    search['parser'] = json.loads(search['request'].content)
    search['json_data_pretty'] = json.dumps(search['parser'], indent=4)
    print(search['json_data_pretty'])
    return search

if __name__ == '__main__':
    print('-'*5, ' Dados da conta abaixo ', '-'*5)
Search()
