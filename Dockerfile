FROM python:3.10-slim

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENV DJANGO_SETTINGS_MODULE=bookstore_project.settings
ENV PYTHONPATH="/app:${PYTHONPATH}"

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
