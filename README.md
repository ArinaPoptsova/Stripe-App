# Stripe-App

Чтобы запустить данное приложение, необходимо создать файл, содержащий переменные среды SECRET_KEY, STRIPE_PUBLIC_KEY, 
STRIPE_SECRET_KEY, а также выполнить следующий набор команд.

python venv <virtual_environment_name> (создание виртуальной среды)

pip install -r requirements.txt (установка зависимостей проекта)

python manage.py migrate (миграции)

python manage.py createsuperuser (создание суперпользователя)

python manage.py runserver (запуск сервера)
