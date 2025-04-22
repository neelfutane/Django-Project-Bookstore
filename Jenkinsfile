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
        PROJECT_DIR = '.' 
    }

    stages {
        stage('Build') {
            steps {
                echo '🔧 Building Docker containers...'
                dir("${env.PROJECT_DIR}") {
                    bat 'docker-compose build'
                }
            }
        }

       stage('Test') {
    steps {
        echo '✅ Running Django tests...'
        dir("${WORKSPACE}") {
            bat 'docker-compose run web python manage.py test'
        }
    }
}


        stage('Deploy') {
            steps {
                echo '🚀 Deploying the app using Docker Compose...'
                dir("${env.PROJECT_DIR}") {
                    bat 'docker-compose up -d'
                }
            }
        }
    }
}
