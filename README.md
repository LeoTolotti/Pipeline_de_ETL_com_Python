# Projeto: Explorando IA Generativa em um Pipeline de ETL com Python

**Bootcamp Santander 2023 - Ciência de Dados com Python - DIO**

Neste projeto, reimaginamos um pipeline de ETL (Extração, Transformação e Carga) sem necessariamente utilizar a API da OpenAI ou qualquer API específica. O objetivo foi criar um fluxo de trabalho de ETL personalizado para lidar com dados de dois arquivos CSV: `SDW23.csv` e `Vinhos.csv`. O objetivo final é associar nomes a seus respectivos níveis de vinho e gerar mensagens personalizadas oferecendo vinhos com base no nível de cada pessoa.

## Descrição do Projeto

### Etapa 1: Extração

A primeira etapa consiste na extração de dados dos seguintes arquivos CSV:

- `SDW23.csv`: Contém informações sobre os usuários, incluindo IDs, nomes e níveis.
- `Vinhos.csv`: Contém informações sobre vinhos, incluindo níveis, nomes, tipos e países.

### Etapa 2: Transformação

A etapa de transformação envolve processar e associar os dados extraídos. As principais tarefas de transformação incluem:

- Carregar os dados dos arquivos CSV em estruturas de dados Python.
- Associar cada nome do arquivo `SDW23.csv` ao nível de vinho correspondente a partir do arquivo `Vinhos.csv`.
- Criar mensagens personalizadas para cada usuário com base em seu nível de vinho.
- Selecionar aleatoriamente dois vinhos do nível correspondente para oferecer.

### Etapa 3: Carga

Neste projeto, a carga refere-se à exibição das mensagens personalizadas geradas durante a etapa de transformação. As mensagens são exibidas no console, informando o nome do usuário e oferecendo vinhos com base no nível.

## Como Executar o Projeto

1.  Certifique-se de ter os seguintes arquivos no mesmo diretório do seu código Python:

    - `SDW23.csv`
    - `Vinhos.csv`

2.  Execute o código Python para realizar o processo de ETL.
3.  As mensagens personalizadas serão exibidas no console, oferecendo vinhos com base nos níveis dos usuários.

## Exemplo de Mensagem Personalizada

Aqui está um exemplo de como as mensagens personalizadas podem ser formatadas:

```
Como você é experiente no mundo dos vinhos,  João, selecionamos esses dois rótulos para você:
Nome do Vinho: Châteauneuf-du-Pape, Tipo de Vinho:  Grenache Blend, País de Origem:  França
Nome do Vinho: Barolo Riserva, Tipo de Vinho:  DOCG, País de Origem:  Itália
```

Este projeto demonstra uma aplicação prática de ETL em um contexto criativo, utilizando Python para manipular e associar dados de diferentes fontes. É uma abordagem interessante para explorar IA generativa em um pipeline de ETL personalizado.
