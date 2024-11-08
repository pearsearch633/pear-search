# crawler.py
import requests
from bs4 import BeautifulSoup

def crawl(url, depth=2):
    if depth == 0:
        return []
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        links = []
        for a_tag in soup.find_all('a', href=True):
            href = a_tag['href']
            if href.startswith('http'):
                links.append(href)
        return links[:10]  # Beperkt tot 10 links
    except Exception as e:
        print(f"Error crawling {url}: {e}")
        return []
