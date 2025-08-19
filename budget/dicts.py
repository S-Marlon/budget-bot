extras = {
    "validade_proposta":{},
    "localizacao":{},
    "data":{},
    "inclusos":{
        1:"✓ Prospecção geofísica e geológica",
        2:"✓ Perfuração do poço artesiano",
        3:"✓ Instalação de tubulação e estrutura",
        4:"✓ Documentação necessária",
        5:"✓ Prospecção geofísica e geológica"
    },
    "forma_pagamento":{},
    "data_inicio":{},
    "prazo_exec":{},
    "miudas":{
        1:'* Este é um orçamento estimado, sujeito a confirmação técnica no local.',
        2:'Obs.: O valor total refere-se à perfuração de até 60 metros. Caso ultrapasse essa metragem, será cobrado um valor adicional de R$ 280,00 por metro excedente.',
        3:'*Este orçamento é um orçamento preliminar de execução de serviço. o documento oficial será gerado apos a confirmação do cliente e será anexado ao contrato*'
        },
    'outros':'re'
}

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
    "descricao": "a definir",
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
    {"descricao": "1", "quantidade": 0, "valor": 1500.00},
    {"descricao": "2", "quantidade": 0, "valor": 2000.00},
    {"descricao": "Prospecção hidrogeológica", "quantidade": 0, "valor": 2500.00},
    {"descricao": "Prospecção geofísica e geológica", "quantidade": 0, "valor": 3000.00}
]

revestimento = [
    {"descricao": "Tubo de 10 1/4", "quantidade": 0, "valor": 1450.00},
    {"descricao": "Tubo galvanizado á fogo de 6", "quantidade": 0, "valor": 490.00},
    {"descricao": "Tubo DIN 2440 de 6", "quantidade": 0, "valor": 370.00},
    {"descricao": "Tubo geomecanico 5", "quantidade": 0, "valor": 350.00},
    {"descricao": "Tubo geomecanico 4", "quantidade": 0, "valor": 310.00}
]


documentacao = [
    {"descricao": "Requerimento de dispensa de Outorga", "quantidade": 0, "valor": 3500.00},
    {"descricao": "Requerimento de Outorga", "quantidade": 0, "valor": 4500.00},
    {"descricao": "Relatorio de Avaliação Hidrogeologica e Projeto construtivo", "quantidade": 0, "valor": 2000.00},
    {"descricao": "ART de Perfuração", "quantidade": 0, "valor": 1000.00}
]

forma_pagamento = [
    {"descricao": "30% de entrada mais 3x boleto", "quantidade": 0, "valor": 3500.00},
    {"descricao": "50% de ebtrada e mais 10x cartão sem juros", "quantidade": 0, "valor": 4500.00},
    {"descricao": "50% de entrada mais 4x no boleto", "quantidade": 0, "valor": 370.00}
]

modelo_perfuracao = [
    {
      "descricao": "Perfuração 6\" em sedimento - de 00 a 32 m",
      "quantidade": 32,
      "valor": 210
    },
    {
      "descricao": "Perfuração 6\" em fratura de rocha - de 32 a 40 m",
      "quantidade": 8,
      "valor": 205
    },
    {
      "descricao": "Perfuração 6\" em rocha sã - de 40 a 60 m",
      "quantidade": 20,
      "valor": 200
    },
    {
      "descricao": "Perfuração 6\" em rocha sã - de 60 a 100 m",
      "quantidade": 40,
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