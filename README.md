# Мини проект Блог на Fastapi

Создадим "ручки" по которым можно будет:
- регистрироваться
- авторизоваться
- добавлять посты (только авторизованные пользователи)
- искать
- удалять
- комментировать
- добавлять в избранное
- сделаем админку
- делиться на почту
- п.с. возможно расширю и прикручу мини интернет магазина в котором
  - по-мимо оформления заказа прикрутим систему оплату
  - не факт, но постараюсь написать простенького бота на PyTelegramBot который будет:
    - получать все свежие посты определенного автора
    - ну и создавать свои (а чтобы создавать, нужно авторизоваться)


**В целом не сложно, все это. после работы будем делать по чуть-чуть :-)
Так как писать будем в асинхроном виде, думаю бота нужно делать на AIOgramm**

## Используемые библиотеки
1. FastAPI
2. Postgres
3. SQLalchemy
3. Redis (либо RabbitMQ)
4. Celery
5. Flower
6. Docker
7. Docker Compose
8. Gunicorn


