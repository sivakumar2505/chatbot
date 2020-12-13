import requests
import json


def twitter_api():
    urls = []
    url = "https://api.twitter.com/2/tweets/search/recent?query=lang:en corona virus&max_results=10&tweet.fields=created_at&expansions=author_id"
    header = {
        'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAAOJkKgEAAAAAiRCEQoX9hZajRJP1nvOAdBHQoPI%3DdhvcUnF8T3VvAwel2RWAzLmT0hbuzWE2vRP03rNTHIyhfLpUys'
    }
    data = requests.get(url, headers=header)
    data_set = json.loads(data.text)
    for i in data_set['data']:
        urls.append('https://twitter.com/' + i['author_id'] + '/status/' + i['id'])
    return urls

