Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:

git clone https://github.com/ErendzhenovBair/api_final_yatube
cd api_final_yatube
Cоздать и активировать виртуальное окружение:

python -m venv env
source venv/Scripts/activate
Установить зависимости из файла requirements.txt:

pip install -r requirements.txt
Выполнить миграции:

python manage.py migrate
Запустить проект:

python manage.py runserver
