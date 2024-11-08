# indexer.py
import re
import requests

index = {}

def add_to_index(url, content):
    words = re.findall(r'\w+', content.lower())
    for word in words:
        if word not in index:
            index[word] = []
        index[word].append(url)

def index_page(url):
    try:
        response = requests.get(url)
        content = response.text
        add_to_index(url, content)
    except Exception as e:
        print(f"Error indexing {url}: {e}")
