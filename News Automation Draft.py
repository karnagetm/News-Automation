import requests

API_KEY = 'e321312bab884f17938ea585826dfa13'
URL = 'https://newsapi.org/v2/top-headlines'

def get_articles_by_category(category):
    query_parameters = {
        "category": category,
        "country": "gb",
        "apiKey": API_KEY
    }
    return _get_articles(query_parameters)

def _get_articles(params):
    response = requests.get(URL, params=params)
    if response.status_code == 200:
        articles = response.json().get('articles', [])
        for article in articles:
            print(article.get('title'))
            print(article.get('url'))
            print('')
    else:
        print("Error fetching articles")

if __name__ == "__main__":
    get_articles_by_category("technology")

