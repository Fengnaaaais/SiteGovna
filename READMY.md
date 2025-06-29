```python
from us_news.models import Categories
categories = ["business", "entertainment", "general", "health", "science", "sports", "technology"]
for category in categoryies:
    Categories.objects.create(name=category)
```

