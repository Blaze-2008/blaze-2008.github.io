import requests
from bs4 import BeautifulSoup
import csv

def parse_medium_articles():
    url = "https://medium.com/tag/startups"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    articles = []
    for item in soup.select('article'):
        title = item.select_one('h2').text.strip()
        link = item.find('a', {'aria-label': 'Post Preview Title'})['href']
        articles.append({
            "name": title,
            "category": "Статьи",
            "url": f"https://medium.com{link}",
            "description": "Полезные материалы для стартапов"
        })
    
    # Сохраняем в CSV
    with open('tools.csv', 'a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["name", "category", "url", "description"])
        writer.writerows(articles)

parse_medium_articles()