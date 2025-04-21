// pipeline {
//     agent any

//     environment {
//         DOCKER_BUILDKIT = 1
//     }

//     stages {
//         stage('Clone Repo') {
//             steps {
//                 echo 'Cloning repository...'
//             }
//         }

//         stage('Build Docker Image') {
//             steps {
//                 echo 'Building Docker containers...'
//                 sh 'docker-compose build'
//             }
//         }

//         stage('Apply Migrations') {
//             steps {
//                 echo 'Running Django migrations...'
//                 sh 'docker-compose run web python manage.py migrate'
//             }
//         }

//         stage('Run Server') {
//             steps {
//                 echo 'Starting Django app...'
//                 sh 'docker-compose up -d'
//             }
//         }
//     }
// }

pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Cloning repository...'
                git branch: 'main',
                    url: 'https://github.com/neelfutane/Django-Project-Bookstore.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker containers...'
                bat 'docker-compose build' // Use 'bat' for Windows
            }
        }

        stage('Apply Migrations') {
            steps {
                echo 'Running Django migrations...'
                bat 'docker-compose run web python manage.py migrate' // Use 'bat' for Windows
            }
        }

        stage('Run Server') {
            steps {
                echo 'Starting Django app...'
                bat 'docker-compose up -d' // Use 'bat' for Windows
            }
        }
    }
}
