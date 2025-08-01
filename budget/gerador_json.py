import json
import copy
import math

apenasPerfuração = bool

modelo_json = {
    "cliente": {
        "nome": "",
        "cidade": "",
        "local": ""
    },
    "prospeccao": [],
    "perfuracao": [],
    "estrutura": [],
    "equipamentos": [],
    "documentacao": []
}

modelo_item = {
    "descricao": "",
    "quantidade": 0,
    "valor": 0
}

modelo_itens_equipamentos = [
    "Bomba",
    "Tampa de poço",
    "Painel",
    "Cabos elétricos submersos",
    "Válvula de retenção",
    "Corda Submersa",
    "Hidrômetro",
    "Cimentação"
]

revestimento = [
    {"descricao": "Tubo de 10 1/4'", "quantidade": 10, "valor": 1450.00},
    {"descricao": "Tubo galvanizado á fogo de 6'", "quantidade": 10, "valor": 490.00},
    {"descricao": "Tubo DIN 2440 de 6'", "quantidade": 10, "valor": 370.00},
    {"descricao": "Tubo geomecanico 5'", "quantidade": 5, "valor": 350.00},
    {"descricao": "Tubo geomecanico 4'", "quantidade": 5, "valor": 320.00}
]

modelo_perfuracao = [
    {
      "descricao": "Perfuração 6\" em sedimento - de 00 a 32 m",
      "quantidade": 32,
      "valor": 250
    },
    {
      "descricao": "Perfuração 6\" em rocha sã - de 32 a 40 m",
      "quantidade": 8,
      "valor": 235
    },
    {
      "descricao": "Perfuração 6\" em rocha sã - de 40 a 60 m",
      "quantidade": 8,
      "valor": 235
    },
    {
      "descricao": "Perfuração 6\" em rocha sã - de 60 a 100 m",
      "quantidade": 60,
      "valor": 200
    },
    {
      "descricao": "Perfuração 4\" em rocha sã - de 100 a 150 m",
      "quantidade": 50,
      "valor": 195
    },
    {
      "descricao": "Perfuração 4\" em rocha sã - de 150 a 200 m",
      "quantidade": 50,
      "valor": 195
    },
    {
      "descricao": "Perfuração 4\" em rocha sã - de 200 a 250 m",
      "quantidade": 50,
      "valor": 195
    }
]

modelo_estrutura = {
    "simples": [
        {"descricao": "Tubo pvc 6'", "quantidade": lambda m: math.ceil(m / 6), "valor": 80},
        {"descricao": "Tubo pvc 1'", "quantidade": lambda m: math.ceil(m / 6), "valor": 30}
    ],
    "padrao": [
        {"descricao": "Tubo aço 6'", "quantidade": lambda m: 6, "valor": 300},
        {"descricao": "Tubo pvc 1'", "quantidade": lambda m: math.ceil(m / 6), "valor": 30}
    ],
    "reforcada": [
        {"descricao": "Tubo aço 6'", "quantidade": lambda m: 6, "valor": 300},
        {"descricao": "Tubo aço 1'", "quantidade": lambda m: math.ceil(m / 6), "valor": 90}
    ]
}


modelo_orcamento = [
    {'valorPerfurado': 76}
]

def dadosPerf():

    # 1# verificar se o orçamento será apenas perfuração ou perfuração e materiais

    if apenasPerfuração == True:
        print(f'orçamento de perfuração')
    else:
        print(f'orçamento de perfuração e materiais ')


    # 2# coletar quantidade perfurada e fzer a divisão de acordo com regras próprias

    if modelo_orcamento[0] >= 50:
        print("slave")

        # calcular divisoes por valor e adcionar ao orçamento, usando sempre um divisor de 10
    else:
        return f'valor minimo de orçamento é 50 metros'

    # 3# verificar revestimento utilizado e calcular valor, e se for apenas perfuração já gerar PDF´

    if apenasPerfuração == True:
        print(f'orçamento de perfuração')



        return gerarPDF()

    # #4.1 se materias não estiver incluso, calcular valor individual de materiais

    if apenasPerfuração == True:
        print(f'orçamento de perfuração')

        return gerarPDF()

    # #4.2 se materiais incluso incrementar valor do metro perfurado

    # #5 se houver demanda de alteração de valor em especifico, realiza-la

    # #6 Verificar itens auxiliares e adcionar ao Orçamento

    # #7 gerar PDF de orçamento e retornar ao Telegram

    gerarPDF()

def gerarPDF(trabalho, tipo):
    if tipo == "Simples":
        json.prospeccao.quantidade = 0
        json.perfuracao = []
        json.estrutura = []
        json.equipamentos = []
        json.documentacao = []
        
    return f"Salve"

orcamento = copy.deepcopy(modelo_json)
# ---------nome----------
orcamento["cliente"]["nome"] = "João da Silva"
orcamento["cliente"]["cidade"] = "Atibaia"
orcamento["cliente"]["local"] = "Sítio Boa Vista"
# ---------nome----------

estrutura = 'padrao'
valoPergurado = 130

item_perf = (math.ceil(valoPergurado/50) +2) 

# print(f'itens a ser adcionado: {item_perf}')
for item in modelo_perfuracao[:item_perf]:
    orcamento["perfuracao"].append(copy.deepcopy(item))

# ---------estrutura----------

if estrutura in modelo_estrutura:
    for item in modelo_estrutura[estrutura]:
        item_estr = copy.deepcopy(modelo_item)
        item_estr["descricao"] = item["descricao"]
        item_estr["quantidade"] = item["quantidade"](valoPergurado)
        item_estr["valor"] = item["valor"]
        orcamento["estrutura"].append(item_estr)
else:
    print("⚠️ Tipo de estrutura desconhecido:", estrutura)

# ---------estrutura----------


# ---------equipamento----------

# equipamentos: = modelo_equipamento e cada item recebe modelo_itens_equipamentos que recebe modelo_item

if valoPergurado <= 60:
    profundidade = 60
else:
    profundidade = math.ceil(valoPergurado / 50) * 50  

if profundidade in modelo_equipamento:
    for nome_item in modelo_itens_equipamentos:
        item = copy.deepcopy(modelo_item)
        item["descricao"] = nome_item
        item["quantidade"] = 1  # ou algum valor padrão se quiser
        
        modelo_equipamento[profundidade].append(item)
else:
     print("⚠️ Tipo de profundidade não suportada :", profundidade)

for chave in list(modelo_equipamento):
    if modelo_equipamento[chave] == []:
        modelo_equipamento.pop(chave)
        print(f"Profundidade {chave} removida")

        
orcamento["equipamentos"].append(copy.deepcopy(modelo_equipamento))

# Visualizar


print(modelo_equipamento)


with open("dados.json", "w") as file:
    json.dump(orcamento, file)
