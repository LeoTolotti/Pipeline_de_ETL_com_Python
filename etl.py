import random
import pandas as pd
niveis = {'nivel_1': [], 'nivel_2': [], 'nivel_3': []}
vinhos = {'vinhos_nivel_1': [], 'vinhos_nivel_2': [], 'vinhos_nivel_3': []}


def df_user():
    df = pd.read_csv('SDW23.csv')
    for index, linha in df.iterrows():
        nivel_atual = int(linha['Nível'])
        nome = linha['Nome']
        if nivel_atual == 1:
            niveis['nivel_1'].append(nome)
        elif nivel_atual == 2:
            niveis['nivel_2'].append(nome)
        elif nivel_atual == 3:
            niveis['nivel_3'].append(nome)


def df_mensagens():
    df = pd.read_csv('Vinhos.csv')
    for index, linha in df.iterrows():
        nivel_atual = int(linha['Nível'])
        nome = linha['Nome do Vinho']
        tipo = linha['Tipo de Vinho']
        pais = linha['País de Origem']
        if nivel_atual == 1:
            vinhos['vinhos_nivel_1'].append(
                {'Nome do Vinho': nome, 'Tipo de Vinho': tipo, 'País de Origem': pais})
        elif nivel_atual == 2:
            vinhos['vinhos_nivel_2'].append(
                {'Nome do Vinho': nome, 'Tipo de Vinho': tipo, 'País de Origem': pais})
        elif nivel_atual == 3:
            vinhos['vinhos_nivel_3'].append(
                {'Nome do Vinho': nome, 'Tipo de Vinho': tipo, 'País de Origem': pais})


def escolher_vinhos_aleatoriamente(nivel_desejado):
    vinhos_selecionados = []
    if f'vinhos_nivel_{nivel_desejado}' in vinhos:

        vinhos_do_nivel = vinhos[f'vinhos_nivel_{nivel_desejado}']

        vinhos_selecionados = random.sample(
            vinhos_do_nivel, min(2, len(vinhos_do_nivel)))

    return vinhos_selecionados


df_user()
df_mensagens()

for nivel, nomes in niveis.items():
    if nivel == 'nivel_1':
        for nome in nomes:
            msg = f"Como você está começando no mundo dos vinhos, {nome}, selecionamos esses dois rótulos para você:"
            vinhos_selecionados = escolher_vinhos_aleatoriamente(1)
            print(msg)
            for vinho in vinhos_selecionados:
                msg_vinho = f"Nome do Vinho: {vinho['Nome do Vinho']}, Tipo de Vinho: {vinho['Tipo de Vinho']}, País de Origem: {vinho['País de Origem']}"
                print(msg_vinho)
    elif nivel == 'nivel_2':
        for nome in nomes:
            msg = f"Como você está se aventurando mais no mundo dos vinhos, {nome}, selecionamos esses dois rótulos para você:"
            vinhos_selecionados = escolher_vinhos_aleatoriamente(2)
            print(msg)
            for vinho in vinhos_selecionados:
                msg_vinho = f"Nome do Vinho: {vinho['Nome do Vinho']}, Tipo de Vinho: {vinho['Tipo de Vinho']}, País de Origem: {vinho['País de Origem']}"
                print(msg_vinho)
    elif nivel == 'nivel_3':
        for nome in nomes:
            msg = f"Como você é experiente no mundo dos vinhos, {nome}, selecionamos esses dois rótulos para você:"
            vinhos_selecionados = escolher_vinhos_aleatoriamente(3)
            print(msg)
            for vinho in vinhos_selecionados:
                msg_vinho = f"Nome do Vinho: {vinho['Nome do Vinho']}, Tipo de Vinho: {vinho['Tipo de Vinho']}, País de Origem: {vinho['País de Origem']}"
                print(msg_vinho)
