import requests
from unicodedata import normalize
from bs4 import BeautifulSoup


def get_yandex_data() -> list:
    yandex_main_url = 'https://market.yandex.ru/partners/news'
    req = requests.get(yandex_main_url).content
    s = BeautifulSoup(req, 'lxml')
    ya_list = []
    divs = s.find_all('div', class_="news-list__item")[:10]
    for div in divs:

        # получаем заголовок статьи
        link = div.find('a')
        title = normalize("NFKD", link.div.getText())

        # получаем описание статьи
        description = normalize("NFKD", div.p.getText())

        """
        проваливаемся внутрь статьи для получения остальных данных
        """

        href = 'https://market.yandex.ru/' + link.get('href')
        req = requests.get(href).content
        soup = BeautifulSoup(req, 'lxml')

        # получаем таги
        div_tags = soup.find('div', 'news-info__tags')
        tags = [tag.getText() for tag in
                div_tags.find_all('a')]
        tags_a_for_clean = soup.find_all('a')

        # убираем все ссылки из статьи для получения чистого текста статьи
        for a in tags_a_for_clean:
            a.extract()
        date = soup.time.getText()
        post = normalize("NFKD", soup.find('div', class_='news-info__post-body html-content page-content').getText())

        # формируем словарь с данными новости
        div_dict = {
            'description': description,
            'title': title,
            'date': date,
            'text': post,
            'tags': tags
        }
        ya_list.append(div_dict)

    return ya_list



# def get_ozon_news():
#     main_url = 'https://seller.ozon.ru/news/'
#
#     r = requests.get(main_url).content
#
#     soup = BeautifulSoup(r, 'lxml')
#
#     body = soup.body
#
#     noux = body.find('div', id='__nuxt')
#     print(noux)
#     section = soup.find('section', class_='news-list')
#
#
#     # news_div = s.find_all('div', class_='news-card')[:10]
#     # for div in news_div:
#     #     date = div.find('span', class_='news-card__date')
#     #     print(date)
#
#
# get_ozon_news()
