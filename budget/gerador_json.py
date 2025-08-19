import json
import copy
import math
from dicts import *


apenasPerfuração = bool
ES_valoPerfurar = 60



def gerarJson_geral():

    orcamento = copy.deepcopy(modelo_json)


    # 1# coletar e delegar os dados do usuario
    # ---------nome----------
    orcamento["cliente"]["nome"] = "João da Silva"
    orcamento["cliente"]["cidade"] = "Atibaia"
    orcamento["cliente"]["local"] = "Sítio Boa Vista"
    # ---------nome----------

    # 2# coletar e delegar prospeccao selecionada
    # ----------prospeccao-----------
    prospecaescolhida = ["1","2"]
        
    n = -1
    for item in prospeccao:
        n + 1
        orcamento["prospeccao"].append(copy.deepcopy(item))
        
        if item["descricao"] in prospecaescolhida:
            selected_itens["prospeccao"].append(copy.deepcopy(item))
            selected_itens["prospeccao"][n]["quantidade"] = 1


    
    
    # ----------prospeccao-----------


    # 3# coletar e delegar perfuracao quantidade e valor da perfuração
    # 3# verificar revestimento utilizado e calcular valor, e se for apenas perfuração já gerar PDF´

    # ----------perfuração-----------
    apenasPerf = False

    item_perf = (math.ceil(ES_valoPerfurar/50) +1) 

    n = -1
    if apenasPerf == True:
        print(f'Orçamento de perfuração apenas.')
        valorAdcional = 100

        for item in modelo_perfuracao[:item_perf]:
            n +1
            orcamento["perfuracao"].append(copy.deepcopy(item))
            orcamento["perfuracao"][n]["valor"] += valorAdcional


    else:
        print(f'Orçamento de perfuração e materiais.')
        valorAdcional = -50

        for item in modelo_perfuracao[:item_perf]:
            n +1
            orcamento["perfuracao"].append(copy.deepcopy(item))
            orcamento["perfuracao"][n]["valor"] += valorAdcional

    # print(f'itens a ser adcionado: {item_perf}')
  
         

    # ----------perfuração-----------


    # ---------revestimento----------

    revestimentoescolhido = ["Tubo geomecanico 4"]
 
    n = -1
    for item in revestimento:
        n + 1
        orcamento["revestimento"].append(copy.deepcopy(item))
        
        if item["descricao"] in revestimentoescolhido:
            selected_itens["revestimento"].append(copy.deepcopy(item))
            selected_itens["revestimento"][n]["quantidade"] = 9

    
    # ---------revestimento----------


    for item_nome in modelo_nomes_equipamentos:
    # Agora sim, você pode usar item_nome (string) como CHAVE de um dicionário
        
        modelo_itens_equipamentos[item_nome] = copy.deepcopy(modelo_item)


    # ---------materiais----------

    if apenasPerf == True:
        print(f'Orçamento de perfuração apenas.')
        # Atribua o dicionário completo de equipamentos ao orçamento
        orcamento["equipamentos"] = [copy.deepcopy(modelo_itens_equipamentos)]
        

       # Para acessar e modificar os itens, agora você precisa especificar o índice da lista (nesse caso, 0).
        orcamento["equipamentos"][0]["Bomba"]["descricao"] = "Bomba Submersa"
        orcamento["equipamentos"][0]["Bomba"]["quantidade"] = 1
        orcamento["equipamentos"][0]["Bomba"]["valor"] = "1800.00"

        orcamento["equipamentos"][0]["Tampa de poço"]["descricao"] = "Tampa de PVC"
        orcamento["equipamentos"][0]["Tampa de poço"]["quantidade"] = 1
        orcamento["equipamentos"][0]["Tampa de poço"]["valor"] = 200.00

        orcamento["equipamentos"][0]["Painel"]["descricao"] = "Painel Multesio"
        orcamento["equipamentos"][0]["Painel"]["quantidade"] = 1
        orcamento["equipamentos"][0]["Painel"]["valor"] = 600.00

        orcamento["equipamentos"][0]["Cabos elétricos submersos"]["descricao"] = "Cabos eletricos"
        orcamento["equipamentos"][0]["Cabos elétricos submersos"]["quantidade"] = 60
        orcamento["equipamentos"][0]["Cabos elétricos submersos"]["valor"] = 6.00

        orcamento["equipamentos"][0]["Válvula de retenção"]["descricao"] = "Válvula de retenção"
        orcamento["equipamentos"][0]["Válvula de retenção"]["quantidade"] = 1
        orcamento["equipamentos"][0]["Válvula de retenção"]["valor"] = 60.00
        
        orcamento["equipamentos"][0]["Hidrômetro"]["descricao"] = "Hidrômetro"
        orcamento["equipamentos"][0]["Hidrômetro"]["quantidade"] = 1
        orcamento["equipamentos"][0]["Hidrômetro"]["valor"] = 160.00

        
        orcamento["equipamentos"][0]["Cimentação"]["descricao"] = "Cimentação espaço anular"
        orcamento["equipamentos"][0]["Cimentação"]["quantidade"] = 1
        orcamento["equipamentos"][0]["Cimentação"]["valor"] = 400.00

        orcamento["equipamentos"][0]["Corda Submersa"]["descricao"] = "Corda Submersa"
        orcamento["equipamentos"][0]["Corda Submersa"]["quantidade"] = 60
        orcamento["equipamentos"][0]["Corda Submersa"]["valor"] = 1.40
    else:

        
        # Atribua o dicionário completo de equipamentos ao orçamento
        orcamento["equipamentos"] = [copy.deepcopy(modelo_itens_equipamentos)]
        

       # Para acessar e modificar os itens, agora você precisa especificar o índice da lista (nesse caso, 0).
        orcamento["equipamentos"][0]["Bomba"]["descricao"] = "Bomba Submersa"
        orcamento["equipamentos"][0]["Bomba"]["quantidade"] = 1
        orcamento["equipamentos"][0]["Bomba"]["valor"] = 1800.00

        orcamento["equipamentos"][0]["Tampa de poço"]["descricao"] = "Tampa de PVC"
        orcamento["equipamentos"][0]["Tampa de poço"]["quantidade"] = 1
        orcamento["equipamentos"][0]["Tampa de poço"]["valor"] = 200.00

        orcamento["equipamentos"][0]["Painel"]["descricao"] = "Painel Multesio"
        orcamento["equipamentos"][0]["Painel"]["quantidade"] = 1
        orcamento["equipamentos"][0]["Painel"]["valor"] = 600.00

        orcamento["equipamentos"][0]["Cabos elétricos submersos"]["descricao"] = "Cabos eletricos"
        orcamento["equipamentos"][0]["Cabos elétricos submersos"]["quantidade"] = 60
        orcamento["equipamentos"][0]["Cabos elétricos submersos"]["valor"] = 6.00

        orcamento["equipamentos"][0]["Válvula de retenção"]["descricao"] = "Válvula de retenção"
        orcamento["equipamentos"][0]["Válvula de retenção"]["quantidade"] = 1
        orcamento["equipamentos"][0]["Válvula de retenção"]["valor"] = 60.00
        
        orcamento["equipamentos"][0]["Hidrômetro"]["descricao"] = "Hidrômetro"
        orcamento["equipamentos"][0]["Hidrômetro"]["quantidade"] = 1
        orcamento["equipamentos"][0]["Hidrômetro"]["valor"] = 160.00

        
        orcamento["equipamentos"][0]["Cimentação"]["descricao"] = "Cimentação espaço anular"
        orcamento["equipamentos"][0]["Cimentação"]["quantidade"] = 1
        orcamento["equipamentos"][0]["Cimentação"]["valor"] = 400.00

        orcamento["equipamentos"][0]["Corda Submersa"]["descricao"] = "Corda Submersa"
        orcamento["equipamentos"][0]["Corda Submersa"]["quantidade"] = 60
        orcamento["equipamentos"][0]["Corda Submersa"]["valor"] = 1.40


        

        print(f'Orçamento de perfuração e materiais.')
    # ---------materiais----------


    # ---------documentacao----------
    documentacaoescolhido = ["Requerimento de dispensa de Outorga"]

    n = -1
    for item in documentacao:
        n + 1
        orcamento["documentacao"].append(copy.deepcopy(item))

        if item["descricao"] in documentacaoescolhido:
            selected_itens["documentacao"].append(copy.deepcopy(item))
            selected_itens["documentacao"][n]["quantidade"] = 1


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