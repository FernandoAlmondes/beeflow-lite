import requests
import json
import sys

# Desenvolvido por: Bee Solutions
# Autor: Fernando Almondes
# Data: 11/05/2025 - 16:39

try:
    senha_bd = sys.argv[1]
except:
    print()
    print("--> Desenvolvido por: Bee Solutions")
    print("--> Autor: Fernando Almondes")
    print("--> Data: 11/05/2025 - 16:39")
    print("--> Use: /opt/bee/beeflow/venv/bin/python /opt/bee/beeflow/grafana/bee_grafana.py senha_bd_beeflowconsultor")
    print()
    sys.exit(1)

url_grafana = 'http://localhost:3000/login'

headers = {
    'content-type': 'application/json',
}

data = {
    "user": "admin",
    "password": "beesolutions"
}

session = requests.Session()

# Logando no Grafana
logando = session.post(url_grafana, json=data, headers=headers)

print(logando.text)

##########

# Criar uma nova datasource
grafana_url_datasource = 'http://localhost:3000/api/datasources'

# Verificando versao do datasource
grafana_url_dt = 'http://localhost:3000/api/datasources/uid/aell2zgszaltsc?accesscontrol=true'

dt = session.get(grafana_url_dt, headers=headers)

versao = json.loads(dt.text)
versao = versao['version']

dt_id = 1
dt_uid = "aell2zgszaltsc"

print('ID:', dt_id)
print('UID:', dt_uid)
print('Versao:', versao)

data = {
    "id": dt_id,
    "uid": dt_uid,
    "orgId":1,
    "name":"mysql-beeflow",
    "type":"mysql",
    "typeLogoUrl":"public/app/plugins/datasource/mysql/img/mysql_logo.svg",
    "access":"proxy",
    "url":"localhost:3306",
    "user":"beeflowconsultor",
    "database":"",
    "basicAuth":False,
    "basicAuthUser":"",
    "withCredentials":False,
    "isDefault":False,
    "jsonData":{"maxOpenConns":100,"maxIdleConns":100,"maxIdleConnsAuto":True,"connMaxLifetime":14400,"database":"beeflow_db_01"},
    "secureJsonFields":{},
    "version": versao,
    "readOnly":False,
    "accessControl":{"alert.instances.external:read":True,"alert.instances.external:write":True,"alert.notifications.external:read":True,"alert.notifications.external:write":True,"alert.rules.external:read":True,"alert.rules.external:write":True,"datasources.id:read":True,"datasources:delete":True,"datasources:query":True,"datasources:read":True,"datasources:write":True},
    "apiVersion":"","secureJsonData":{"password":senha_bd}
}

grafana_url_datasource_uid = f'{grafana_url_datasource}/uid/{dt_uid}'

#print(grafana_url_datasource_uid)

# Editando datasource do mysql com a senha do banco de dados criada durante a instalacao
editando_datasource = session.put(grafana_url_datasource_uid, json=data, cookies=session.cookies, headers=headers)

#print(editando_datasource.text)

##########

# Fazendo logout

grafana_url_tokens = 'http://localhost:3000/api/admin/users/cell2p9tb20w0d/auth-tokens'

checa_tokens = session.get(grafana_url_tokens)

tokens_json = json.loads(checa_tokens.text)

grafana_url_revoke_token = 'http://localhost:3000/api/admin/users/cell2p9tb20w0d/revoke-auth-token'

# Desloga cada um dos usuarios logados menos a sessao atual
for i in tokens_json:
    data = {"authTokenId":i['id']}
    session.post(grafana_url_revoke_token, headers=headers, json=data)