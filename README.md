# idagroup-test-task

Upload any images to http://127.0.0.1:8000/images/upload

## Startup guide

```pip install -r requirements.txt```
(Using venv is highly recommended)

```python manage.py runserver 127.0.0.1:8000```

In any browser:

```http://127.0.0.1:8000/images/upload```

## Points of interest

./image_app/models.py

./image_app/views.py

./image_app/forms.py

### P.S.

This task was made with purely developing in mind, so there is no DevOps things such as production deploy
