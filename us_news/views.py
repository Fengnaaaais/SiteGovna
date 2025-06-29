from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import SearchForm
from .models import Categories
from .requests_api import news_api


def news(
    request,
    category_id: int = None,
    q: str = None,
    country: str = None,
):
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            sourse_q = form.cleaned_data["q"]
            return HttpResponseRedirect(reverse("us_news:q", args=[sourse_q]))
    else:
        form = SearchForm()

    articles = news_api(category_id, q, country)
    articles["categories"] = Categories.objects.all()
    articles["form"] = form
    return render(request, "us_news/index.html", articles)
