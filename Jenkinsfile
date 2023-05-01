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
                    if (!registryName || !imageName) {
                        error("Required variables not set: registryName or imageName")
                    }
                    dockerImage = docker.build "${registryName}:${imageName}"
                    echo 'Docker image built'
                }
            }
        }
        
        stage('Pushing to ACR') {
            steps{  
                script{ 
                    if (!dockerImage) {
                        error("Docker image not built")
                    }
                    if (!registryURL || !registryCredential) {
                        error("Required variables not set: registryURL or registryCredential")
                    }
                    docker.withRegistry("http://${registryURL}", registryCredential) {
                        dockerImage.push()
                    }
                }  
            }
        }

        stage('Deploy to ACI') {
            steps{  
                script{
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
