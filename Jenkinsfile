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

        stage('Deploy to Azure Container Instance') {
            steps {
                script {
                    // Define variables
                    def resourceGroupName = "emailsender"
                    def aciName = "emailsenderinstance"
                    def location = "EastUS"
                    def dnsNameLabel = "my-email-sender"
                    def port = "8000"

                    // Login to Azure
                    sh 'az login --service-principal -u <sendercontainer> -p <5h5UAhIENU56XKKPC9anRO5+FSbVvJy/dtoXZjpiyW+ACRDXaDFL> --tenant <bf37c963-c21a-4893-bef3-2a9c983a0050>'

                    // Create ACI
                    sh '''
                    az container create \
                        --resource-group ${resourceGroupName} \
                        --name ${aciName} \
                        --image ${registryURL}/${imageName} \
                        --registry-login-server ${registryURL} \
                        --registry-username ${registryCredential} \
                        --registry-password ${ACR_PASSWORD} \
                        --dns-name-label ${dnsNameLabel} \
                        --ports ${port} \
                        --ip-address public
                    '''
                }
            }
        }
    }
}