import requests
import json
def live_news():
    url = "http://newsapi.org/v2/everything?q=corona virus&apiKey=985a8cc4c2dc4e5b8ff2a295884a166f"
    response =requests.get(url)
    data =(json.loads(response.text))
    urls = data['articles']
    return {'links':urls[:3]}
