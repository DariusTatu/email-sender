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
                
                def resourceGroupName = 'emailsender'
                def aciName = 'email-sender'
                def location = 'eastus'
                def dnsNameLabel = 'my-email-sender'
                def port = '8000'
                
                azureCLI commands: [[exportVariablesString: '', script: ''' 
                az login --service-principal -u $CLIENT_ID -p $CLIENT_SECRET --tenant $TENANT_ID
                az account set --subscription $SUBSCRIBTION_ID
                az container create
                    --resource-group ${resourceGroupName} 
                    --name ${aciName} 
                    --image ${registryURL}/${imageName} 
                    --registry-login-server ${registryURL} 
                    --registry-username ${registryCredential} 
                    --registry-password ${ACR_PASSWORD} 
                    --dns-name-label ${dnsNameLabel} 
                    --ports ${port} 
                    --ip-address public    
                ''']]
                }  
            }
        }
    }
}
