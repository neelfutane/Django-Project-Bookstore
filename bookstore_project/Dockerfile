# FROM python:3.10-slim

# WORKDIR /app

# COPY . /app

# RUN pip install --upgrade pip
# RUN pip install -r requirements.txt

# ENV DJANGO_SETTINGS_MODULE=bookstore_project.settings
# ENV PYTHONPATH="/app"  

# EXPOSE 8000

# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
FROM python:3.11-slim


RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    libpq-dev \
    default-libmysqlclient-dev \
    build-essential \
    netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
