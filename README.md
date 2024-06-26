# TestProject
Тестовое задание

## Описание задания
1. Синтезировать данные для базы данных:

Таблица клиентов:
- Номер счета
- Фамилия
- Имя
- Отчество
- Дата рождения
- ИНН
- ФИО ответственного
- Статус (по умолчанию «Не в работе»)

Таблица пользователей:
- ФИО
- Логин
- Пароль

2. Создать интерфейс для обращения к синтезированным данным:
- Форма для авторизации по паре логин/пароль
- После показать таблицу клиентов авторизованного пользователя по связи ФИО из таблицы пользователей – ФИО ответственного
- Пользователь должен иметь возможность изменить статус клиента на «В работе», «Отказ», «Сделка закрыта»


## Как запустить
Проект был разработан в среде разработки [PyCharm](https://www.jetbrains.com/ru-ru/pycharm/)
Проект написан на Python 3.9 c использованием фреймворка Flask и библиотек pymongo, bson, faker.
Скачайте [Python3.9](https://www.python.org/downloads/release/python-390/)

Затем склонируйте проект в рабочую директорию:
```git
git clone https://github.com/Goshansky/TestProject.git
```
Установите необходимые библиотеки:
```python
pip install Flask pymongo bson faker
```
В качестве СУБД использовалась MongoDB, которая хранится в докер контейнере.
Поэтому также понадобится скачать [Docker Desktop](https://www.docker.com/products/docker-desktop/)

Создадим образ mongoDB через консоль:
```
docker pull mongo
```
Запустим docker-контейнер с примонтированной директорией dump:
```
docker run --name some-mongo -p 27017:27017 -v /dump:/dump -d mongo
```
Перенесем дамп БД в докер-контейнер:
```
docker cp ./dump/db some-mongo:/dump/
```
Зайдем в контейнер в интерактивном режиме:
```
docker exec -it some-mongo bash
```
В открывшейся консоли восстановим БД по дампу:
```
mongorestore --uri="mongodb://localhost:27017/db" "/dump/db"
```
Готово!
Теперь можно запускать приложение:
```
python app.py
```
Вот срез с базы данных. Для авторизации можете использовать любую пару login/password.

| full_name | login | password |
| -------- | -------- | -------- |
| Фортунат Архипович Колесников  | samsonbirjukov  | V2BNM9Z2  |
| Исакова Людмила Наумовна  | terentevevgraf  | v7bj1kZe  |
| Семенова Элеонора Харитоновна  | artem_87  | 62IwSvSq  |
| Карп Игнатьевич Исаев  | moise_62  | wrI8N6jp  |

При изменении статуса на сайте, он автоматически меняется в БД.
