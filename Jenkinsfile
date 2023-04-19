pipeline { 
    agent any 
    stages { 
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build Docker Image'){
            steps {
                sh "docker build . -t email-sender-image"
                echo 'Docker image built'
            }
        }
    }
}