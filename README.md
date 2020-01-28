# Django Celery  - Models save

### Run Locally
Works fine with recent versions of django and celery.
```bash
git clone https://github.com/Reymond190/django-celery-myex.git
```

```
pip install -r requirements.txt
```

```
python manage.py makemigrations
```

```
python manage.py migrate
```

```
python manage.py runserver
```

```
celery -A mysite worker -l info
```

Check whether rabbitmq is running 

```
rabbitmq-server
```

