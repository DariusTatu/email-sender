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
                        if (!env.CLIENT_ID || !env.CLIENT_SECRET || !env.TENANT_ID) {
                            error("Required environment variables not set: CLIENT_ID, CLIENT_SECRET, or TENANT_ID")
                        }
                        azureCLI commands: [[exportVariablesString: '', script: ''' 
                            az login --service-principal -u $CLIENT_ID -p $CLIENT_SECRET --tenant $TENANT_ID
                        ''']]
                    }
                }
            }
        }
    }
}
