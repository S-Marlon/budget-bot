import json
import copy
import math

apenasPerfuração = bool
valoPergurado = 200

modelo_json = {
    "cliente": {
        "nome": "",
        "cidade": "",
        "local": ""
    },
    "prospeccao": [],
    "perfuracao": [],
    "revestimento": [],
    "equipamentos": [],
    "documentacao": []
}

selected_itens = copy.deepcopy(modelo_json)

modelo_item = {
    "descricao": "a definier",
    "quantidade": 0,
    "valor": 0.0
}

modelo_nomes_equipamentos = [
    "Bomba",
    "Tampa de poço",
    "Painel",
    "Cabos elétricos submersos",
    "Válvula de retenção",
    "Corda Submersa",
    "Hidrômetro",
    "Cimentação"
]
modelo_itens_equipamentos = {}


prospeccao = [
    {"descricao": "Prospecção geofísica", "quantidade": 1, "valor": 1500.00},
    {"descricao": "Prospecção geológica", "quantidade": 1, "valor": 2000.00},
    {"descricao": "Prospecção hidrogeológica", "quantidade": 1, "valor": 2500.00},
    {"descricao": "Prospecção geofísica e geológica", "quantidade": 1, "valor": 3000.00}
]

revestimento = [
    {"descricao": "T1ubo de 10 1/4", "quantidade": 10, "valor": 1450.00},
    {"descricao": "T2ubo galvanizado á fogo de 6", "quantidade": 10, "valor": 490.00},
    {"descricao": "T3ubo DIN 2440 de 6", "quantidade": 10, "valor": 370.00},
    {"descricao": "T4ubo geomecanico 5", "quantidade": 5, "valor": 350.00},
    {"descricao": "T5ubo geomecanico 4", "quantidade": 5, "valor": 310.00}
]


documentacao = [
    {"descricao": "Requerimento de dispensa de Outorga ", "quantidade": 1, "valor": 3500.00},
    {"descricao": "Requerimento de Outorga", "quantidade": 1, "valor": 4500.00},
    
    {"descricao": "Relatorio de Avaliação Hidrogeologica e Projeto construtivo", "quantidade": 1, "valor": 2000.00},
    {"descricao": "ART de Perfuração", "quantidade": 1, "valor": 1000.00}
]

forma_pagamento = [
    {"descricao": "30% de entrada mais 3x boleto", "quantidade": 1, "valor": 3500.00},
    {"descricao": "50% de ebtrada e mais 10x cartão sem juros", "quantidade": 1, "valor": 4500.00},
    {"descricao": "50% de entrada mais 4x no boleto", "quantidade": 1, "valor": 370.00}
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


modelo_orcamento = [
    {'valorPerfurado': 76}
]

def gerarJson_geral():

    orcamento = copy.deepcopy(modelo_json)
    # ---------nome----------
    orcamento["cliente"]["nome"] = "João da Silva"
    orcamento["cliente"]["cidade"] = "Atibaia"
    orcamento["cliente"]["local"] = "Sítio Boa Vista"
    # ---------nome----------

    estrutura = 'padrao'
    

    # ----------prospeccao-----------
    prospecaescolhida = "Prospecção geofísica e geológica"

    for item in prospeccao:
        orcamento["prospeccao"].append(copy.deepcopy(item))
        
        if item["descricao"] == prospecaescolhida:
            selected_itens["prospeccao"] = copy.deepcopy(item)

    
    
    # ----------prospeccao-----------


    # ----------perfuração-----------

    item_perf = (math.ceil(valoPergurado/50) +2) 

    # print(f'itens a ser adcionado: {item_perf}')
    for item in modelo_perfuracao[:item_perf]:
        orcamento["perfuracao"].append(copy.deepcopy(item))
        selected_itens["perfuracao"].append(copy.deepcopy(item))

    # ----------perfuração-----------


    # ---------revestimento----------

    revestimentoescolhido = "T5ubo geomecanico 4"

    for item in revestimento:
        orcamento["revestimento"].append(copy.deepcopy(item))
        
        if item["descricao"] == revestimentoescolhido:
            selected_itens["revestimento"] = copy.deepcopy(item)

    
    # ---------revestimento----------
    for item_nome in modelo_nomes_equipamentos:
    # Agora sim, você pode usar item_nome (string) como CHAVE de um dicionário
        modelo_itens_equipamentos[item_nome] = copy.deepcopy(modelo_item)

    apenasPerfuração = False

    # ---------materiais----------
    if apenasPerfuração == True:
        print(f'Orçamento de perfuração apenas.')
    else:

        
        # Atribua o dicionário completo de equipamentos ao orçamento
        orcamento["equipamentos"] = [copy.deepcopy(modelo_itens_equipamentos)]
        

       # Para acessar e modificar os itens, agora você precisa especificar o índice da lista (nesse caso, 0).
        orcamento["equipamentos"][0]["Bomba"]["descricao"] = "Bomba Submersa 2cv"
        orcamento["equipamentos"][0]["Bomba"]["quantidade"] = 1
        orcamento["equipamentos"][0]["Bomba"]["valor"] = 1500.00

        orcamento["equipamentos"][0]["Tampa de poço"]["descricao"] = "Tampa de PVC"
        orcamento["equipamentos"][0]["Tampa de poço"]["quantidade"] = 1
        orcamento["equipamentos"][0]["Tampa de poço"]["valor"] = 200.00

        orcamento["equipamentos"][0]["Painel"]["descricao"] = "Painel Multesio"
        orcamento["equipamentos"][0]["Painel"]["quantidade"] = 1
        orcamento["equipamentos"][0]["Painel"]["valor"] = 600.00
        

        print(f'Orçamento de perfuração e materiais.')
    # ---------materiais----------


    # ---------documentacao----------
    for item in documentacao:
        orcamento["documentacao"].append(copy.deepcopy(item))
        
        if item["descricao"] == revestimentoescolhido:
            selected_itens["documentacao"] = copy.deepcopy(item)

    # ---------documentacao----------
    # ---------forma_pagamento----------
    
    

    with open("dados.json", "w") as file:
        json.dump(orcamento, file)

    itens_selecionados()
    print("lala")

def itens_selecionados():

    with open("selecionados.json", "w") as file:
        json.dump(selected_itens, file)
    print("lala")
 

# # def dadosPerf():

#     # 1# verificar se o orçamento será apenas perfuração ou perfuração e materiais



#     # 2# coletar quantidade perfurada e fzer a divisão de acordo com regras próprias

#         valoPergurado = 130
#     if valoPergurado >= 50:

#         # ----------perfuração-----------

        # item_perf = (math.ceil(valoPergurado/50) +2) 

        # # print(f'itens a ser adcionado: {item_perf}')
        # for item in modelo_perfuracao[:item_perf]:
        #     orcamento["perfuracao"].append(copy.deepcopy(item))

# ----------perfuração-----------
#     else:
#         return f'valor minimo de orçamento é 50 metros'

#     # 3# verificar revestimento utilizado e calcular valor, e se for apenas perfuração já gerar PDF´

#    revestimentoescolhido = "T5ubo geomecanico 4"



#     # #4.1 se materias não estiver incluso, calcular valor individual de materiais

#     if apenasPerfuração == True:
#         print(f'orçamento de perfuração')

#         return gerarPDF()

#     # #4.2 se materiais incluso incrementar valor do metro perfurado

#     # #5 se houver demanda de alteração de valor em especifico, realiza-la

#     # #6 Verificar itens auxiliares e adcionar ao Orçamento

#     # #7 gerar PDF de orçamento e retornar ao Telegram

#     gerarPDF()

def gerarPDF( ):
        # disparar um gatilho para gerador_pdf.py gerar PDF
    return f"gerando PDF com os dados do orçamento..."


gerarJson_geral()