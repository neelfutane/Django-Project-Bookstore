# 📚 Django Bookstore Management System

A full-featured Bookstore Management System built with **Django**, featuring user authentication, book catalog browsing, cart management via sessions, and fully Dockerized with CI/CD using **Jenkins**.

---

## 🌟 Project Overview

This is a full-stack web application developed as part of a Full Stack Python (Django) Application Development course. It allows users to:

- Register/Login/Logout
- View books with detailed publication info
- Add books to cart using session-based logic
- View & manage their cart
- Switch languages (English, Hindi, Marathi) seamlessly on each page

💡 *No use of Django Forms or Django Admin* — everything is handled manually using views and templates.

---

## 🔧 Prerequisites

- Python 3.10+
- Docker & Docker Compose
- Git
- Jenkins (Optional for CI/CD)

---

## 🛠 Tech Stack

- **Backend**: Django 4.x, Django REST Framework
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **Database**: PostgreSQL
- **Authentication**: Django Allauth
- **Deployment**: Docker, Nginx, Gunicorn
- **CI/CD**: Jenkins

---

## 🐳 Docker & Jenkins CI/CD

This project includes full Docker support for containerized deployment and a Jenkinsfile for automation.

### 📦 Docker Usage

Build and run the containers:

``bash
docker-compose up --build

### 🔄 Jenkins CI/CD

A Jenkins pipeline is configured to automatically manage the build and deployment process. On each push to the `main` branch, Jenkins will:

- 🔄 Pull the latest code from GitHub
- 🐳 Build Docker containers
- 🚀 Run the application

This ensures seamless integration and delivery with every update to the repository.
