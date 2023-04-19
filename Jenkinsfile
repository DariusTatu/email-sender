pipeline { 
    agent any 
    stages { 
        stage('Build Docker Image'){
            steps {
                sh "docker build . -t email-sender-image"
                echo 'Docker image built'
            }
        }
    }
}