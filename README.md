# DRnoticias - Bot de Telegram para Cotações e Notícias Ambientais

O projeto **DRnoticias** é um script em Python que automatiza o envio de cotações de moedas e commodities, além de notícias ambientais relacionadas ao agronegócio, para um canal do Telegram utilizando um bot.

## 🌟 Funcionalidades

- Obtenção de cotações atualizadas para:
  - Dólar (USD), Euro (EUR) e Bitcoin (BTC).
- Raspagem de preços de commodities como:
  - Bezerro, boi gordo e soja.
- Coleta de notícias ambientais específicas da região do Mato Grosso do Sul relacionadas ao agronegócio.
- Envio automatizado de cotações e notícias para um canal do Telegram.

## 🛠️ Tecnologias Utilizadas

- **Linguagem de Programação**: Python
- **Bibliotecas Principais**:
  - `requests` para requisições HTTP.
  - `BeautifulSoup` para parsing de HTML.
  - `python-telegram-bot` para integração com o Telegram.

## 🚀 Como Configurar e Executar

### Pré-requisitos

- Python 3.8 ou superior instalado no sistema.
- Um bot do Telegram com o token configurado.

### Passos para Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/AndreRicartes/DRnoticias.git
   ```
2. Navegue até o diretório do projeto:
   ```bash
   cd DRnoticias
   ```
3. (Opcional) Crie um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```
4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
5. Configure as variáveis de ambiente:
   - Adicione o token do bot do Telegram.
   - Configure as URLs das APIs e fontes de dados utilizadas no script.

### Executando o Script

Execute o script principal para iniciar o envio de cotações e notícias:
```bash
python drnoticias.py
```

### Agendamento de Execução

Para automatizar a execução do script periodicamente:
- **Linux**: Use `cron` para agendar o script.
- **Windows**: Utilize o Agendador de Tarefas.

## 🗂️ Estrutura do Projeto

```
DRnoticias/
├── drnoticias.py          # Script principal
├── requirements.txt       # Dependências do projeto
└── README.md              # Documentação do projeto
```

## 📌 Melhorias Futuras

- Adicionar novas fontes de dados para cotações e notícias.
- Implementar suporte para múltiplos idiomas.
- Criar uma interface web para gerenciamento das configurações.
- Otimizar o consumo de recursos durante a execução.

## 📬 Contato

- **E-mail**: andrericartes@gmail.com


---

Contribuições são bem-vindas! Sinta-se à vontade para abrir *issues* ou enviar *pull requests*. Este é um trabalho em progresso, e melhorias são sempre bem-vindas!
