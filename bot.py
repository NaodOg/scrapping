from bs4 import BeautifulSoup
import requests
import io
import sys
import time

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

bot_token = '6761889248:AAE9f50GSCge70G66Dp-srWgu3_dMXINZUY'
chat_id = '273617764'

response = requests.get('https://qefira.com.et/listing-category/eletronics/')
soup = BeautifulSoup(response.text, 'html.parser')
electronics = soup.find_all('h4', class_='hp-listing__title')
details = soup.find_all('div', class_='hp-listing__content')
links = soup.find_all('div', class_='hp-listing__categories hp-listing__category')

def send_to_telegram(bot_token, chat_id, text):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    params = {
        'chat_id': chat_id,
        'text': text
    }
    response = requests.post(url, params=params)
    return response.json()

for index, entry in enumerate(electronics):
    title = entry.get_text(strip=True)
    des = details[index].get_text(strip=True)
    
    
    link = links[index].find('a', href=True)['href']
    
    texts = f"Electronics type: {title}\nDetails: {des}\nLink: https://qefira.com.et/listing-category/eletronics{link}\n"
    response = send_to_telegram(bot_token, chat_id, texts)
    print(response)
    time.sleep(30)

