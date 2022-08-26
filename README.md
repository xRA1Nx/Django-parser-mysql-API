<b>Запуск проекта(поступательно):</b><br />
<p>
  1) в settings.py укажите ваш SECRET KEY <br>
  2) docker-compose up  - (Предзапуск проекта)    <br />
  3) введите следующие команды во 2-й консоли :<br>
    - docker exec -i app python manage.py migrate (применяем миграции)<br> 
    - docker-compose down - останавливаем контенер, для дальнейшего перезапуска с примененными миграциями<br>
  4) docker-compose up -d - (-d = запуск проекта в фоновом режиме) <br>
  5) docker compose run web python manage.py createsuperuser  - создание супер юзера для работы в админ  панели (<b>выполнять при запущенном compose</b> <br />
  6) http://127.0.0.1:8000/api/parse/  - перейдите по ссылке для наполнения БД актуальными новостями   <br>
   <br />

</p>
<br />

<b>Урлы:</b><br />
1) http://127.0.0.1:8000/api/parse/ - парсинг данных и наполнение БД <br />
2) http://127.0.0.1:8000/api/ - список доступных ендпоинтов (реализован crud ,
фильтрация, пагинация)<br />
3) http://127.0.0.1:8000/api/swagger/ - документация API <br />
<br>

<b>Комментарий:</b><br /><br>

не получилось спарсить данные в режиме онлайн с ресурса https://seller.ozon.ru/news/<br>
(на сайте есть внутренняя защита, пробовал зайти через API, но API не предусматривает работу с новостями)<br>
Как результат , решил задачу сохряняя страницы с новостями , и парся их локально.<br>
Предполагаю , что для онлайн парсинга нужна библиотека selenium, но я на данный момент не владею этой библиотекой<br>

https://qna.habr.com/q/1184134 - моя попытка найти решение проблемы на на habr ))


