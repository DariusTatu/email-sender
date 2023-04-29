pipeline { 
    agent any 

    environment {
        registryName = "sendercontainer"
        registryCredential = "ACR"
        registryURL = "sendercontainer.azurecr.io"
    }
    stages { 
        stage('Docker Image'){
            steps {
                script {
                    dockerImage = docker.build registryName 
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