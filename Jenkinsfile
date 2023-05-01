pipeline { 
    agent any 
    // Setting global variables  
    environment {
        registryName = "sendercontainer"
        registryCredential = "ACR"
        registryURL = "sendercontainer.azurecr.io"
        imageName = "email-sender"
    }

    stages { 
        stage('Build Docker Image'){
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

        stage('Deploy to ACI') {
            steps{  
                script{ 
                    azureContainerInstance(credentialsId: 'sendercontainer', resourceGroup: 'emailsender', region: 'eastus', containerGroupName: 'sendercontainer', imageName: 'email-sender', memory: '1.5', cpu: '1', dnsNameLabel: 'my-email-sender')                        
                }  
            }
        }
    }
}
