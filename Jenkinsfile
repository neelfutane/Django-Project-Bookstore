// pipeline {
//     agent any
//     stages {
//         stage('Build') {
//             steps {
//                 echo 'Building the project...'
//             }
//         }
//         stage('Test') {
//             steps {
//                 echo 'Running tests...'
//             }
//         }
//         stage('Deploy') {
//             steps {
//                 echo 'Deploying the project...'
//             }
//         }
//     }
// }
pipeline {
    agent any

    environment {
        PROJECT_DIR = 'bookstore_project' // Adjust if your Django project folder is named differently
    }

    stages {
        stage('Build') {
            steps {
                echo '🔧 Building Docker containers...'
                bat 'docker-compose build'
            }
        }

        stage('Test') {
            steps {
                echo '✅ Running Django tests...'
                bat 'docker-compose run web python manage.py test'
            }
        }

        stage('Deploy') {
            steps {
                echo '🚀 Deploying the app using Docker Compose...'
                bat 'docker-compose down'
                bat 'docker-compose up -d --build'
            }
        }
    }
}
