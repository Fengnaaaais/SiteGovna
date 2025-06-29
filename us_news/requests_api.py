import requests

from NewsHub.settings import API_KEY
from us_news.models import Categories


request_params = {
    "apiKey": API_KEY,
    "country": "us",
}


def news_api(
    category_id: int = None,
    q: str = None,
    country: str = None,
):
    if category_id:
        request_params["category"] = Categories.objects.get(id=category_id).name
    if q:
        request_params["q"] = q
    if country:
        request_params["country"] = country

    article = requests.get(
        "https://newsapi.org/v2/top-headlines", params=request_params
    ).json()
    return article
