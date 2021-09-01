import requests
import bs4
import rssitem

class rssReader:
    def __init__(self, url):
        self.feed_url = url

    def get_data(self):
        try:
            response = requests.get(self.feed_url)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

    def parse_data_to_items(self):
        try:
            soup = bs4.BeautifulSoup(self.get_data().text,'html.parser')
            return soup.findAll('item')
        except Exception as e:
            raise SystemExit(e)

    def get_rss_items(self):
        items = self.parse_data_to_items()
        rss_items = []
        for item in items:
            obj = rssitem.rssItem(  title=item.title.text,
                                    description=item.description.text,
                                    link=item.link.find_next_sibling().text)
            rss_items.append(obj)
        return rss_items