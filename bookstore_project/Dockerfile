
# FROM python:3.11-slim


# RUN apt-get update --fix-missing && \
#     apt-get install -y \
#     gcc \
#     g++ \
#     libpq-dev \
#     default-libmysqlclient-dev \
#     build-essential \
#     netcat-openbsd && \
#     rm -rf /var/lib/apt/lists/*


# WORKDIR /app

# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# COPY . .

# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

FROM python:3.11-slim

# Set noninteractive mode to avoid prompts and fix unreliable mirrors
ENV DEBIAN_FRONTEND=noninteractive

# Replace default apt sources with more stable ones (optional but helpful)
RUN sed -i 's|http://deb.debian.org|http://deb.archive.ubuntu.com|g' /etc/apt/sources.list || true

# Update and install required packages with fixes
RUN apt-get update --fix-missing && \
    apt-get install -y --no-install-recommends \
    gcc \
    g++ \
    libpq-dev \
    default-libmysqlclient-dev \
    build-essential \
    netcat-openbsd \
    && apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set work directory
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Default command
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
