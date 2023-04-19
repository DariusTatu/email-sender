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
        stage('Pushing to ECR') {
            steps{  
                script {
                    withCredentials([[
                        $class: 'AmazonWebServicesCredentialsBinding', 
                        accessKeyVariable: 'ACCESS_KEY_VARIABLE', 
                        secretKeyVariable: 'SECRET_KEY_VARIABLE',
                        credentialsId: '350073109551'
                    ]]) {
                        sh 'aws ecr get-login-password --region eu-central-1 | docker login --username dtatu --password adela@123 350073109551.dkr.ecr.eu-central-1.amazonaws.com'
                        sh 'docker push 350073109551.dkr.ecr.eu-central-1.amazonaws.com/email-sender:latest'
                    }
                }
            }
        }
    }
}