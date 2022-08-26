<b>Запуск проекта:</b><br />
<p>
  1) установка зависимостей - pip install -r req.txt <br />
  2) в файле .env установите ваши учетные данные
  3) python manage.py migrate - применяем миграции <br />
  4) python manage.py createsuperuser - создание супер юзера для работы в админ
  панели <br />
  5) python manage runserver - старт проекта 5) http://127.0.0.1:8000/api/parse/
  - перейдите по ссылке для наполнения БД актуальными новостями <br />
</p>
<br />

<b>Урлы:</b><br />
1) http://127.0.0.1:8000/api/parse/ - парсинг данных и наполнение БД <br />
2) http://127.0.0.1:8000/api/ - список доступных ендпоинтов (реализован crud ,
фильтрация, пагинация)<br />
3) http://127.0.0.1:8000/api/swagger/ - документация API <br />
<br>

<b>Комментарий:</b><br /><br>

ВАЖНО!!!! не получилось спарсить данные  онлайн с ресурса https://seller.ozon.ru/news/
(на сайте есть внутренняя защита, пробовал зайти через API, но API не предусматривает работу с новостями)<br>
Как результат , решил задачу сохряняя страницы с новостями , и парся их локально.<br>
По всей видимости задача решается используя библиотеку selenium, но я на данный момент не владею этой библиотекой<br>

https://qna.habr.com/q/1184134 - моя попытка найти решение проблемы на на habr ))

