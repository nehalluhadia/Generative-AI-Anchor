# news_api.py
import requests
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta

load_dotenv()

api_key = os.getenv('NEWS_API_KEY')

class NewsAPI:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_news(self, query, num_news):
        today = datetime.today().strftime('%Y-%m-%d')
        week_ago = (datetime.today() - timedelta(days=7)).strftime('%Y-%m-%d')

        url = (
            f'https://newsapi.org/v2/everything?q={query}'
            f'&from={week_ago}&to={today}'
            f'&sortBy=popularity&pageSize={num_news}&language=en&apiKey={self.api_key}'
        )

        response = requests.get(url)

        if response.status_code == 200:
            news_data = response.json()
            return news_data.get("articles", [])
        else:
            return []

    def get_news_descriptions(self, query, num_news):
        news = self.get_news(query, num_news)
        desc_list = [news_item['description'] for news_item in news if news_item.get('description')]
        return desc_list

    def get_news_string(self, query, num_news):
        desc_list = self.get_news_descriptions(query, num_news)
        desc_string = ". ".join(desc_list)
        return desc_string
