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
            steps {  
                script { 
                    docker.withRegistry("http://${registryURL}", registryCredential) {
                        dockerImage.push()
                    }
                }
            }
        }

        stage('Azure Login') {
            steps {
                script {
                    withCredentials([azureServicePrincipal(credentialsId: 'jenkins')]) {
                        if (!env.AZURE_CLIENT_ID || !env.AZURE_CLIENT_SECRET || !env.AZURE_TENANT_ID) {
                            error('Required environment variables not set: AZURE_CLIENT_ID, AZURE_CLIENT_SECRET, or AZURE_TENANT_ID')
                        }
                        // Wrap the azureCLI step with `sh` and remove the `azureCLI` block
                        sh '''
                            az login --service-principal -u $AZURE_CLIENT_ID -p $AZURE_CLIENT_SECRET --tenant $AZURE_TENANT_ID
                        '''
                    }
                }
            }
        }
    }
}
