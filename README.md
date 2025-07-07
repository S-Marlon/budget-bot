# 🤖 Mini-bot (Python Bot)

Este projeto tem como objetivo criar um chatbot inteligente que recebe mensagens via **Telegram** ou **WhatsApp**, interpreta automaticamente os dados enviados por um vendedor em campo (como tipo de serviço, materiais, metragem, etc.), e retorna um **orçamento em PDF** formatado, pronto para ser enviado ao cliente.

---

## 📌 Funcionalidades

- 🧠 Interpretação automática de mensagens de texto usando IA
- 📊 Extração de variáveis como tipo de serviço, metragem, bombas, filtros, cidade, etc.
- 💰 Consulta de preços em base local (CSV, Excel ou banco de dados)
- 📄 Geração automática de orçamentos em PDF
- 📩 Retorno do orçamento ao vendedor via Telegram ou WhatsApp

---

## 🔧 Tecnologias Utilizadas

| Camada           | Ferramenta                              |
|------------------|------------------------------------------|
| Linguagem        | Python 3.11+                             |
| Bot de Mensagem  | Telegram Bot API (ou Z-API para WhatsApp)|
| IA / NLP         | OpenAI GPT-4 API (ou local com spaCy)    |
| Backend          | Flask (API REST)                         |
| Geração de PDF   | pdfkit + HTML/CSS                        |
| Base de Dados    | CSV ou SQLite (inicialmente)             |

---

## 🗃 Estrutura do Projeto
```bash
Mini-bot/
│
├── app.py                  # Arquivo principal (Flask)
├── bot/                    # Lógica do bot (Telegram/WhatsApp)
│   └── telegram_bot.py
├── ia/                     # Funções de NLP e integração com OpenAI
│   └── interpretador.py
├── orcamentos/             # Lógica de geração de orçamento
│   ├── gerador_pdf.py
│   └── precos.csv
├── templates/              # Templates HTML usados para gerar PDFs
│   └── orcamento.html
├── .env                    # Variáveis de ambiente (não subir para o Git)
├── requirements.txt        # Bibliotecas usadas
└── README.md
```

## ✅ Próximas Etapas
 - Conectar base de dados com painel web de histórico

 - Implementar cadastro de clientes e contratos

 - Integração com WhatsApp (via API comercial)

## 🤝 Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou um pull request.
