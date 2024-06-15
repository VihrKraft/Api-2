import requests
from urllib.parse import urlparse
import os
from dotenv import load_dotenv
import argparse


def is_bitlink(token, link):
    bitlink = urlparse(link)
    bitlink = f'{bitlink.netloc}{bitlink.path}'
    url = f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}'
    headers = {
        'Authorization': 'Bearer {0}'.format(token)
    }
    response = requests.get(url, headers=headers)
    return response.ok

def shorten_link(token, link):
    url = 'https://api-ssl.bitly.com/v4/shorten'
    headers = {
        'Authorization': 'Bearer {0}'.format(token)
    }
    payload = {
        "long_url": link
    }
    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()
    return response.json()['link']


def count_clicks(token, link):
    bitlink = urlparse(link)
    bitlink = f'{bitlink.netloc}{bitlink.path}'
    url = f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary'
    headers = {
        'Authorization': 'Bearer {0}'.format(token)
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()['total_clicks']


def main():
    load_dotenv()
    parser = argparse.ArgumentParser(
        description='Программа для сокращения ссылок и подсчета кликов по ней'
    )
    parser.add_argument('link', help='Ваша ссылка')
    args = parser.parse_args()
    token = os.environ('BITLY_TOKEN')
    try:
        if is_bitlink(token, args.link):
            clicks_count = count_clicks(token, args.link)
            print(f'Колличество кликов = {clicks_count}')
        else:
            bitlink = shorten_link(token, args.link)
            print(f'Сокращенная ссылка: {bitlink}')
    except requests.exceptions.HTTPError:
        print('Неправильная ссылка')


if __name__ == "__main__":
    main()