# 🌾 Agro News Telegram Bot

Bot em Python que automatiza o envio de **cotações de moedas e commodities** e **notícias ambientais voltadas ao agronegócio**, diretamente para um canal no **Telegram**.

> Projeto originalmente desenvolvido para atender à demanda informativa da região do **Mato Grosso do Sul**, com foco no agronegócio e meio ambiente.

---

## 🚀 Funcionalidades

- 🔄 Coleta automatizada de **cotações atualizadas**:
  - Moedas: Dólar (USD), Euro (EUR), Bitcoin (BTC).
  - Commodities: Bezerro, boi gordo e soja.
- 📰 Raspagem de **notícias ambientais e agropecuárias**.
- 📤 Envio automático das informações para um **canal do Telegram**.
- ⏱️ Suporte a execução agendada via `cron` ou Agendador de Tarefas.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.8+**
- **Bibliotecas principais**:
  - [`requests`](https://pypi.org/project/requests/): Requisições HTTP.
  - [`BeautifulSoup`](https://pypi.org/project/beautifulsoup4/): Parsing e extração de dados HTML.
  - [`python-telegram-bot`](https://github.com/python-telegram-bot/python-telegram-bot): Integração com o Telegram.

---

## ⚙️ Instalação e Execução

### Pré-requisitos

- Python 3.8 ou superior.
- Conta no Telegram com um **bot criado** via [BotFather](https://t.me/BotFather).

### Passos para Configuração

```bash
# Clone o repositório
git clone https://github.com/AndreRicartes/agro-news-telegram-bot.git

# Acesse o diretório
cd agro-news-telegram-bot

# (Opcional) Crie um ambiente virtual
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt
