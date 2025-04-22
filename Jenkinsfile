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
        PROJECT_NAME = 'bookstore_project' // change this if needed
    }

    stages {
        stage('Clean Up Old Containers') {
            steps {
                echo 'Cleaning up old Docker containers...'
                bat "docker-compose down || echo 'Nothing to clean'"
                bat "docker system prune -a -f || echo 'Cleanup failed'"
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                bat "docker-compose build"
            }
        }

        stage('Apply Migrations') {
            steps {
                echo 'Applying Django migrations...'
                bat "docker-compose run web python manage.py migrate"
            }
        }

        stage('Run Server') {
            steps {
                echo 'Starting the Django server...'
                bat "docker-compose up -d"
            }
        }

        stage('Check Logs') {
            steps {
                echo 'Dumping logs to docker_logs.txt...'
                bat "docker-compose logs --no-color > docker_logs.txt"
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished.'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}

