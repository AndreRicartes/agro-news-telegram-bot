import telebot
import pandas as pd
import pandas_datareader.data as pdr
from pyparsing import html_comment
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import requests
from bs4 import BeautifulSoup
import time
import json
from datetime import datetime
from sistema import CHAVE_API



requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

requisicao_dic = requisicao.json()
cotacao_dolar = requisicao_dic["USDBRL"]["bid"]
cotacao_euro = requisicao_dic["EURBRL"]["bid"]
cotacao_btc = requisicao_dic["BTCBRL"]["bid"]

cotacao = str(f"Cotação atualizada. {datetime.now()}\nDólar: R${cotacao_dolar}\nEuro: R${cotacao_euro}\nBTC: R${cotacao_btc}")


url_bezerro = "https://www.cepea.esalq.usp.br/br/indicador/bezerro.aspx"
url_boi_gordo = "https://www.cepea.esalq.usp.br/br/indicador/boi-gordo.aspx"
url_soja = "https://www.cepea.esalq.usp.br/br/indicador/soja.aspx"

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0"}

options = Options()
options.headless = True
options.add_argument('--disable-extensions')
driver = webdriver.Firefox(options=options)

driver.get(url_bezerro)
time.sleep(5)

element = driver.find_element(By.XPATH, "//div[@class='imagenet-table-responsiva']//table")
html_content = element.get_attribute('outerHTML')
soup = BeautifulSoup(html_content, 'html.parser')
table = soup.find(name='table')

df_full = pd.read_html(str(table))[0].head(1)
df_full.columns = ['data', 'valor', 'vardia', 'varmes', 'valorus']
df = df_full.to_dict('records')

bezerro = {}
bezerro['points'] = df


driver.get(url_boi_gordo)
time.sleep(5)

element = driver.find_element(By.XPATH, "//div[@class='imagenet-table-responsiva']//table")
html_content = element.get_attribute('outerHTML')
soup = BeautifulSoup(html_content, 'html.parser')
table = soup.find(name='table')

df_full = pd.read_html(str(table))[0].head(1)
df_full.columns = ['data', 'valor', 'vardia', 'varmes', 'valorus']
df = df_full.to_dict('records')

boi_gordo = {}
boi_gordo['points'] = df



driver.get(url_soja)
time.sleep(5)

element = driver.find_element(By.XPATH, "//div[@class='imagenet-table-responsiva']//table")
html_content = element.get_attribute('outerHTML')
soup = BeautifulSoup(html_content, 'html.parser')
table = soup.find(name='table')

df_full = pd.read_html(str(table))[0].head(1)
df_full.columns = ['data', 'valor', 'vardia', 'varmes', 'valorus']
df = df_full.to_dict('records')

soja = {}
soja['points'] = df



driver.quit()

#Salva os dados em um arquivo json
'''
js = json.dumps(bezerro)
with open('cotacao_bezerro.json', 'w') as fp: 
    fp.write(js)

js = json.dumps(boi_gordo)
with open('cotacao_boi_gordo.json', 'w') as fp:
    fp.write(js)

js = json.dumps(soja)
with open('cotacao_soja.json', 'w') as fp:
    fp.write(js) 
'''
#-------------------------------------------------

bezerro_data = (bezerro['points'][0]['data'])
bezerro_valor = (bezerro['points'][0]['valor'])
boi_gordo_data = (boi_gordo['points'][0]['data'])
boi_gordo_valor = (boi_gordo['points'][0]['valor'])
soja_data = (soja['points'][0]['data'])
soja_valor = (soja['points'][0]['valor'])


telegram_bezerro = "O valor do bezerro ESALQ/BM&FBOVESPA - Mato Grosso do Sul na data de: " + " " + bezerro_data + " " + "é de R$" + bezerro_valor
telegram_boi_gordo = "O valor do boi gordo CEPEA/B3 na data de: " + " " + boi_gordo_data + " " + "é de R$" + str(float(boi_gordo_valor)/100)
telegram_soja_paranagua = "O valor da saca de 60kg de soja ESALQ/BM&FBOVESPA - PARANAGUÁ na data de: " + " " + soja_data + " " + "é de R$" + str(float(soja_valor)/100)
telegram_cotacao = cotacao


def get_news():
    url_imasul = "https://www.imasul.ms.gov.br/noticias/"
    headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0"}  # Adicionar headers

    response = requests.get(url_imasul, headers=headers)  # Usar requests.get() e passar headers
    soup = BeautifulSoup(response.content, 'html.parser')  # Usar response.content

    noticias_imasul = soup.find_all('div', class_='col-3')  # Seletor mais específico

    noticias = []
    for item in noticias_imasul:
        link = item.find('a')['href']
        texto = item.find('a').text
        noticias.append({'link': link, 'texto': texto})

    return noticias

noticias = get_news()

imasul_noticia = (noticias[0]['texto'])
imasul_link = (noticias[0]['link'])


#Faz o bot responder mensagens
'''
bot = telebot.TeleBot(CHAVE_API)

def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    bot.reply_to(mensagem, imasul_link)
    
bot.polling()

def send_message(CHAVE_API, chat_id, message):
    try:
        data = {"chat_id" : chat_id, "text": msg}
        url = "https://api.telegram.org/bot{}/sendMessage".format(CHAVE_API)
        requests.post(url, data)
    except Exception as e:
        print("Erro no sendMessage:", e)
'''    
#------------------------------------------------------------------------------

bot = telebot.TeleBot(CHAVE_API)

message_cotacao1 = telegram_cotacao
bot.send_message('@DR_noticias', message_cotacao1)

message_bezerro = telegram_bezerro
bot.send_message('@DR_noticias', message_bezerro)

message_boi_gordo = telegram_boi_gordo
bot.send_message('@DR_noticias', message_boi_gordo)

message_soja_paranagua = telegram_soja_paranagua
bot.send_message('@DR_noticias', message_soja_paranagua)

message_imasul = imasul_link
bot.send_message('@DR_noticias', message_imasul)

