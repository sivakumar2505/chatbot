from GoogleNews import GoogleNews


def news_live():
    googlenews = GoogleNews()
    googlenews = GoogleNews(lang='en')
    googlenews.set_period('1d')
    googlenews.set_encode('utf-8')
    googlenews.get_news('corona virus')
    links = googlenews.get_links()
    googlenews.clear()
    return {'links':links[:3]}
