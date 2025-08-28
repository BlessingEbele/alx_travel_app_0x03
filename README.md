alx_travel_app_0x03
Setup Instructions
Install dependencies: pip install -r requirements.txt

Start RabbitMQ: sudo systemctl start rabbitmq-server

Run migrations: python manage.py migrate

Start Celery worker: celery -A alx_travel_app worker -l info

Start Django server: python manage.py runserver

Test:

Create a booking via API
Check email inbox for confirmation
