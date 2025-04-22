// pipeline {
//     agent any

//     stages {
//         stage('Cleanup') {
//             steps {
//                 bat 'docker system prune -a -f || echo "Cleanup failed"'
//                 bat 'docker-compose down --remove-orphans || echo "No containers to remove"'
//             }
//         }

//         stage('Checkout') {
//             steps {
//                 git branch: 'main', 
//                     url: 'https://github.com/neelfutane/Django-Project-Bookstore.git'
//             }
//         }

//         stage('Build Docker Image') {
//             steps {
//                 echo 'Building Docker containers...'
//                 retry(3) {
//                     bat 'docker-compose build --no-cache'
//                 }
//             }
//         }

//         stage('Apply Migrations') {
//             steps {
//                 bat 'docker-compose run web python manage.py migrate'
//             }
//         }

//         stage('Run Server') {
//             steps {
//                 bat 'docker-compose up -d'
//             }
//         }
//     }

//     post {
//         always {
//             bat 'docker-compose logs --no-color > docker_logs.txt'
//             archiveArtifacts artifacts: 'docker_logs.txt'
//         }
//     }
// }

pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Building the project...'
            }
        }
        stage('Test') {
            steps {
                echo 'Running tests...'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying the project...'
            }
        }
    }
}
