import requests
import datetime
import locale
from unicodedata import normalize
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

locale.setlocale(locale.LC_TIME, '')  # the ru locale is installed


def get_yandex_data() -> list:
    def get_clean_data(tag):
        return normalize("NFKC", tag.getText(strip=True))

    yandex_main_url = 'https://market.yandex.ru/partners/news'
    req = requests.get(yandex_main_url).content
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
        req = requests.get(href).content
        soup = BeautifulSoup(req, 'lxml')

        # получаем таги
        div_tags = soup.find('div', 'news-info__tags')
        tags = [tag.getText().title().strip('#') for tag in
                div_tags.find_all('a')]
        tags_a_for_clean = soup.find_all('a')

        # убираем все ссылки из статьи для получения чистого текста статьи
        for a in tags_a_for_clean:
            a.extract()

        # преобразуем полученные данные в формат даты
        temp_date = soup.time.getText().split()
        temp_date[1] = temp_date[1][:3]
        temp_date = ' '.join(temp_date)
        date = datetime.datetime.strptime(temp_date, '%d %b %Y').date().strftime("%Y-%m-%d")

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


def get_ozon_news():
    main_url = 'https://seller.ozon.ru/news/'
    header = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582'
    r = requests.get(main_url, headers={'User-Agent': UserAgent().opera})
    # r = requests.get(main_url, headers={'User-Agent': header})
    print(r)  # Response [403]

    soup = BeautifulSoup(r.content, 'lxml')
    news_div = soup.find_all('div', class_='news-card')[:10]
    for div in news_div:
        date = div.find('span', class_='news-card__date')
        print(date)


get_ozon_news()
