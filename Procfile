web: gunicorn backend.wsgi
worker: celery -A backend worker -l info --pool=solo
beat: celery -A backend beat -l INFO