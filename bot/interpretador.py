from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import pandas as pd
import os
import re


if os.path.exists("db.sqlite3"):
    os.remove("db.sqlite3")

print("Olá eu sou o Budget-bot e vou te auxiliar!")




keywords = {
  "prospeccao": {
    "Visita técnica ao local": ["visita técnica", "visita", "local"],
    "Sondagem geofísica": ["geofísica", "sondagem elétrica", "teste com eletrodo"],
    "Prospecção Radiestésica": ["radiestesia", "radiestésico", "forquilha"],
    "Relatório técnico": ["relatório técnico", "laudo técnico", "documento técnico"]
  },
  "perfuracao": {
    "Perfuração 6\" em sedimento - de 00 a 32 m": ["sedimento", "até 32", "mole", "solo"],
    "Perfuração 6\" em rocha sã - de 32 a 40 m": ["rocha", "de 32 a 40"],
    "Perfuração 6\" em rocha sã - de 40 a 100 m": ["rocha", "40 metros", "profundo", "sã"],
    "Perfuração 4\" em rocha sã - de 100 a 150 m": ["4 polegadas", "de 100 a 150", "profundo"],
  },
  "equipamentos": {
    "Bomba submersa 1.5 CV": ["bomba", "submersa", "1.5cv", "motor d'água"],
    "painel elétrico": ["painel", "painel de comando", "quadro elétrico"],
    "Válvula de retenção": ["válvula", "retenção", "válvula d'água"],
    "Cabos elétricos submersos": ["cabo", "cabos", "fio submerso", "fiação"],
    "tubo de recalque": ["recalque", "tubo de saída", "cano recalque"],
  },
  "documentacao": {
    "Outorga": ["outorga", "liberação", "autorização"],
    "Cadastro no órgão ambiental (DAEE, ANA, etc.)": ["cadastro", "daee", "ana"],
    "Relatório hidrogeológico ou laudo técnico": ["hidrogeológico", "laudo", "relatório de solo"],
    "Anotação de Responsabilidade Técnica (ART)": ["art", "engenheiro", "anotação"],
  }
}



def detectar_verbo(mensagem):
    mensagem = mensagem.lower()

    for categoria, itens in keywords.items():
        for descricao, palavras in itens.items():
         for palavra in palavras:
            if palavra in mensagem:
                print(f"⚙️ Adicionar: [{categoria}] -> {descricao}")
                return f"⚙️ Adicionar: [{categoria}] -> {descricao}"


def tratamento_inicial(contexto):
    return detectar_verbo(contexto)


while True:
    user_input = input("Você: ")

    if user_input.lower() in ["sair", "exit", "e" , "x", "z" ]:
        break
    else:
       print("IA:", tratamento_inicial(user_input))
       

