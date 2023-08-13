# Django Origin Base

------------------

## Usage

---

### Run for dev

- install requirements

```
python3 -m venv venv
source venv/bin/activate 
pip install -r requirements.txt 
```

- Run server

```
python manage.py runserver
```

- Run worker

```
celery -A goku worker --loglevel=info
```

- Run beat

```
celery -A goku beat --loglevel=info
```

### Run for docker

```
docker-compose --compatibility up --build -d
```

## Run check pep8

```python
flake8
```