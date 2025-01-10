import requests as req

headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"}

data = {
    "q": "http",
    "target_type": "posts",
    "order": "relevance",
    # "format": "json",
}

request = req.get("https://habr.com/ru/search/", data=data, headers=headers)


print(request.text)
