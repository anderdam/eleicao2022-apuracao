import time
import requests
import json
import pandas as pd

data = requests.get('https://resultados.tse.jus.br/oficial/ele2022/544/dados-simplificados/br/br-c0001-e000544-r.json')
json_data = json.loads(data.content)

candidato = []
partido = []
votos = []
porcentagem = []

for informacoes in json_data['cand']:
    candidato.append(informacoes['nm'])
    votos.append(informacoes['vap'])
    porcentagem.append(informacoes['pvap'])

df_eleicao = pd.DataFrame(list(zip(candidato, votos, porcentagem)), columns=['Candidato', 'Nº Votos', 'Porcentagem'])

print(df_eleicao)

while data:
    print(df_eleicao)
    time.sleep(10)
