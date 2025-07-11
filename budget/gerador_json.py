import json
import copy
import math

modelo_item = {
    "descricao": "",
    "quantidade": None,
    "valor": 0
}

tubos = [
    {"descricao": "Tubo 6\" de PVC", "quantidade": 10, "valor": 150},
    {"descricao": "Tubo 6\" de Aço", "quantidade": 10, "valor": 150},
    {"descricao": "Tubo 1\" de PVC", "quantidade": 10, "valor": 150},
    {"descricao": "Tubo 1' de Aço", "quantidade": 5, "valor": 370}
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

modelo_estrutura = [
    {
      "descricao": "Revestimento em Tubo de aço 6'",
      "quantidade": 32,
      "valor": 250
    },
    {
      "descricao": "Revestimento em Tubo de PVC 6'",
      "quantidade": 32,
      "valor": 250
    },
    {
      "descricao": "Tubo Interno de Aço 1'",
      "quantidade": 32,
      "valor": 250
    },
    {
      "descricao": "Tubo Interno de PVC 1'",
      "quantidade": 32,
      "valor": 250
    }
]

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

def gerarPDF(trabalho, tipo):
    if tipo == "Simples":
        json.prospeccao.quantidade = 0
        json.perfuracao = []
        json.estrutura = []
        json.equipamentos = []
        json.documentacao = []
        
    return f"Salve"

orcamento = copy.deepcopy(modelo_json)

orcamento["cliente"]["nome"] = "João da Silva"
orcamento["cliente"]["cidade"] = "Atibaia"
orcamento["cliente"]["local"] = "Sítio Boa Vista"

estrutura = 'padrao'
valoPergurado = 129
# contra metragem, numero maximo dividido por 5 +2
item_perf = (math.ceil(valoPergurado/50) +2) 
# assim pega a quantidade de itens e adciona do modelo
print(f'itens a ser adcionado: {item_perf}')
for item in modelo_perfuracao[:item_perf]:
    orcamento["perfuracao"].append(copy.deepcopy(item))


if estrutura == 'simples':

    # adiciona item de Estrutura
    item_estr = copy.deepcopy(modelo_item)
    item_estr["descricao"] = "Tubo pvc 6'"
    item_estr["quantidade"] = math.ceil(valoPergurado/6)
    item_estr["valor"] = 80
    orcamento["estrutura"].append(item_estr)

    # adiciona item de Estrutura
    item_estr = copy.deepcopy(modelo_item)
    item_estr["descricao"] = "Tubo pvc 1'"
    item_estr["quantidade"] = math.ceil(valoPergurado/6)
    item_estr["valor"] = 30
    orcamento["estrutura"].append(item_estr)
    
elif estrutura == 'padrao':
     # adiciona item de Estrutura
    item_estr = copy.deepcopy(modelo_item)
    item_estr["descricao"] = "Tubo aço 6'"
    item_estr["quantidade"] = 6
    item_estr["valor"] = 300
    orcamento["estrutura"].append(item_estr)

    # adiciona item de Estrutura
    item_estr = copy.deepcopy(modelo_item)
    item_estr["descricao"] = "Tubo pvc 1'"
    item_estr["quantidade"] = math.ceil(valoPergurado/6)
    item_estr["valor"] = 30
    orcamento["estrutura"].append(item_estr)
elif estrutura == 'padrao':
     # adiciona item de Estrutura
    item_estr = copy.deepcopy(modelo_item)
    item_estr["descricao"] = "Tubo aço 6'"
    item_estr["quantidade"] = 6
    item_estr["valor"] = 300
    orcamento["estrutura"].append(item_estr)

    # adiciona item de Estrutura
    item_estr = copy.deepcopy(modelo_item)
    item_estr["descricao"] = "Tubo aço 1'"
    item_estr["quantidade"] = math.ceil(valoPergurado/6)
    item_estr["valor"] = 90
    orcamento["estrutura"].append(item_estr)


print(orcamento)


# Escrevendo os dados no arquivo JSON
with open("dados.json", "w") as file:
    json.dump(orcamento, file)
