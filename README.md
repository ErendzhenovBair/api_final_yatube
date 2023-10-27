# API для Yatube

## Описание проекта

Yatube - социальная сеть для публикации дневников. Позволяет публиковать посты, комментировать посты, осуществлять подписку на авторов.
Для разработки API использован Django REST framework. Реализована аутентификация по JWT-токену.

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone [https://github.com/ErendzhenovBair/api_final_yatube]
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```

### Автор

Эрендженов Баир.
- Электронная почта: erendzhenovbair1990@yandex.ru
- Telegram: @BairErendzhenov
