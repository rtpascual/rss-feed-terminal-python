import bs4
import requests
import rssreader


def request_urls():
    urls = []
    while True:
        user_input = input('Enter url of an rss feed (or q to quit):\n')
        if user_input == 'q':
            break
        urls.append(user_input)
    return urls

def print_items(url):
    rss_items = rssreader.rssReader(url).get_rss_items()
    for item in rss_items:
        print(f'Title: {item.title}')
        print(f'Description: {item.description}')
        print(f'Link: {item.link}')
        print('==================================\n')

def main():
    urls = request_urls()
    
    for url in urls:
        print_items(url)

if __name__ == '__main__':
    main()