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
                        accessKeyVariable: 'AWS_ACCESS_KEY_ID', 
                        secretKeyVariable: 'AWS_SECRET_ACCESS_KEY',
                        credentialsId: 'aws-jenkins'
                    ]]) {
                        sh 'aws ecr get-login-password --region eu-central-1 | docker login --username AWS --password-stdin 350073109551.dkr.ecr.eu-central-1.amazonaws.com'
                        sh 'docker push 350073109551.dkr.ecr.eu-central-1.amazonaws.com/email-sender:latest'
                    }
                }
            }
        }

        stage('Stop previous containers') {
            steps {
                sh 'docker ps -f name=email-sender --no-run-if-empty docker container stop'
                sh 'docker container ls -a -fname=email-sender -q | xargs -r docker container rm'
            }
        }
      
        stage('Docker Run') {
            steps{
                script {
                    sh 'docker run -d -p 8096:5000 --rm --name email-sender 350073109551.dkr.ecr.eu-central-1.amazonaws.com/email-sender:latest'
                }
            }
        }
    }
}