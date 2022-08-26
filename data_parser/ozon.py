# -*- coding: utf-8 -*-
import datetime
import os.path
from bs4 import BeautifulSoup
from data_parser.parse_core import get_clean_data, convert_str_to_date

cur_path = os.path.dirname(os.path.abspath(__file__))
res_path = os.path.join(cur_path, 'resources')


def get_ozon_data():
    ozon_list = []

    path = os.path.join(res_path, 'ozon_main.html')
    with open(path, encoding='utf-8') as f:
        data = f.read()
    soup = BeautifulSoup(data.encode(), "lxml")

    divs = soup.find_all('div', class_="news-card")[:10]
    for i in range(10):
        div = divs[i]

        # Получаем Заголовок
        h3 = div.find('h3', class_='news-card__title')
        title = get_clean_data(h3)

        # Получаем Дату
        span = soup.find('span', class_='news-card__date')
        date = convert_str_to_date(span.getText())


        # Получаем Таги новостей
        tag_divs = div.find_all('div', class_='news-card__mark')
        tags = [tag.getText().title().strip('#') for tag in tag_divs] if tag_divs else ['Другое']

        # открываем html с новостью и парсим от туда данные для статьи
        path = os.path.join(res_path, f'page{1+i}.html')
        with open(path, encoding='utf-8') as f:
            post_data = f.read()
        post_soup = BeautifulSoup(post_data.encode(), "lxml")

        post_section = post_soup.find('section', class_='new-section html-content_Ol8P9')
        post = get_clean_data(post_section)

        # первый параграф - краткое описание статьи
        p = post_section.find('p')
        description = get_clean_data(p)

        div_dict = {
            'description': description,
            'title': title,
            'date': date,
            'text': post,
            'tags': tags,
            'source': 'ya',
        }

        ozon_list.append(div_dict)

    return ozon_list



if __name__ == '__main__':
    for i in get_ozon_data():
        print(i)
