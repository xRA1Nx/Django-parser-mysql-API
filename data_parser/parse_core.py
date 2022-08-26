from unicodedata import normalize
import locale
import datetime

locale.setlocale(locale.LC_TIME, '')  # the ru locale is installed


def get_clean_data(tag):
    return normalize("NFKC", tag.getText(strip=True))


def convert_str_to_date(str_to_date):
    temp_date = str_to_date.split()
    if len(temp_date) == 2:
        temp_date.append('2022')
    temp_date[1] = temp_date[1][:3]
    temp_date = ' '.join(temp_date)
    print(temp_date)
    return datetime.datetime.strptime(temp_date, '%d %b %Y').date().strftime("%Y-%m-%d")
