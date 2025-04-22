# 📚 Django Bookstore Management System

A full-featured Bookstore Management System built with **Django**, featuring user authentication, book catalog browsing, cart management via sessions and fully Dockerized with CI/CD using **Jenkins**.

---

## 🌟 Project Overview

This is a full-stack web application developed as part of a Full Stack Python (Django) Application Development course. It allows users to:

- Register/Login/Logout
- View books with detailed publication info
- Add books to cart using session-based logic
- View & manage their cart
- Switch languages (English, Hindi, Marathi) seamlessly on each page

💡 No use of Django Forms or Django Admin — everything is handled manually using views and templates.

---

### 🔧 Prerequisites

- Python 3.10+
- Docker & Docker Compose
- Git
- Jenkins (Optional for CI/CD)

## Tech Stack

- **Backend**: Django 4.x, Django REST Framework
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **Database**: PostgreSQL
- **Authentication**: Django Allauth
- **Deployment**: Docker, Nginx, Gunicorn
- **CI/CD**: Jenkins

🐳 Docker & Jenkins CI/CD
-This project includes full Docker support for containerized deployment and a Jenkinsfile for automation:

📦 Docker Usage
-Build and run the containers:
-bash :
docker-compose up --build
-The app will be accessible at:
http://localhost:8000/

🔄 Jenkins CI/CD
-A Jenkins pipeline is configured to:

-Pull the latest code from GitHub
-Build Docker containers
-Run the app
-This ensures automatic build and deployment on every push to the main branch.
