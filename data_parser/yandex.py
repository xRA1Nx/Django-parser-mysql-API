# -*- coding: utf-8 -*-
import requests

from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from data_parser.parse_core import get_clean_data, convert_str_to_date


def get_yandex_data() -> list:
    yandex_main_url = 'https://market.yandex.ru/partners/news'
    req = requests.get(yandex_main_url, headers={'User-Agent': UserAgent().chrome}).content

    s = BeautifulSoup(req, 'lxml')

    ya_list = []
    divs = s.find_all('div', class_="news-list__item")[:10]
    for div in divs:
        # получаем заголовок статьи
        link = div.find('a')
        title = get_clean_data(link.div)

        # получаем описание статьи
        description = get_clean_data(div.p)

        """
        проваливаемся внутрь статьи для получения остальных данных
        """

        href = 'https://market.yandex.ru/' + link.get('href')
        req = requests.get(href, headers={'User-Agent': UserAgent().chrome}).content
        soup = BeautifulSoup(req, 'lxml')

        # получаем таги
        div_tags = soup.find('div', 'news-info__tags')
        tags = [tag.getText().title().strip('#') for tag in
                div_tags.find_all('a')] if div_tags else ['Другое']


        # tags = convert_tags(div_tags.find_all('a'))

        # убираем все ссылки из статьи для получения чистого текста статьи
        tags_a_for_clean = soup.find_all('a')
        for a in tags_a_for_clean:
            a.extract()

        # преобразуем полученные данные в формат даты
        date = convert_str_to_date(soup.time.getText())
        post = get_clean_data(soup.find('div', class_='news-info__post-body html-content page-content'))

        # формируем словарь с данными новости
        div_dict = {
            'description': description,
            'title': title,
            'date': date,
            'text': post,
            'tags': tags,
            'source': 'ya',
        }
        ya_list.append(div_dict)

    return ya_list


if __name__ == "__main__":
    for i in get_yandex_data():
        print(i)
