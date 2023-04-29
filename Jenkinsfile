pipeline { 
    agent any 

    environment {
        registryName = "sendercontainer"
        registryCredential = "ACR"
        registryURL = "sendercontainer.azurecr.io"
        imageName = "email-sender"
    }
    stages { 
        stage('Docker Image'){
            steps {
                script {
                    dockerImage = docker.build registryName + ":$imageName"
                    echo 'Docker image built'
                }
            }
        }
        stage('Pushing to ACR') {
            steps{  
                script{ 
                    docker.withRegistry("http://${registryURL}", registryCredential) {
                        dockerImage.push()
                    }
                }  
            }
        }
    }
}