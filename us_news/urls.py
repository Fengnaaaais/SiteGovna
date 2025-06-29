from django.urls import path

from .views import news

app_name = "us_news"

urlpatterns = [
    path("", news, name="news"),
    path("country/<str:country>/", news, name="news"),
    path("category/<int:category_id>/", news, name="category"),
    path("<str:q>/", news, name="q"),
]
