pipeline {
    agent {
        docker {
            image 'mcr.microsoft.com/azure-cli'
            args '-u root' // Use root user to avoid permission issues
        }
    }
    environment {
        registryName = "sendercontainer"
        registryCredential = "ACR"
        registryURL = "sendercontainer.azurecr.io"
        imageName = "email-sender"
        AZURE_APP_ID = credentials('AZURE-APP-ID')
        AZURE_SECRET = credentials('AZURE-SECRET')
        AZURE_TENANT_ID = credentials('AZURE-TENANT-ID')
    }
    stages {
        stage('Build Docker Image') {
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
                    docker.withRegistry("https://${registryURL}", registryCredential) {
                        dockerImage.push()
                    }
                }
            }
        }
        stage('Deploy to Azure Container Instance') {
            steps {
                sh '''
                    # Login to Azure using the provided credentials
                    az login --service-principal -u $AZURE_APP_ID -p $AZURE_SECRET -t $AZURE_TENANT_ID

                    # Create an Azure Container Instance
                    az container create --resource-group emailsender --name email-sender --image ${registryURL}/${registryName}:${imageName} --dns-name-label my-email-sender --ports 8000
                '''
            }
        }
    }
}

