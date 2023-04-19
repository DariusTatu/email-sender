pipeline { 
    agent any 

    environment {
        registry = "350073109551.dkr.ecr.eu-central-1.amazonaws.com/email-sender"
    }
    stages { 
        stage('Docker Image'){
            steps {
                script {
                    dockerImage = docker.build registry
                    echo 'Docker image built'
                }
            }
        }
    }
}