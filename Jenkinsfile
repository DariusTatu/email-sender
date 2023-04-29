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

        stage('Stop previous containers') {
            steps {
                sh 'docker ps -f name=email-sender -q | xargs --no-run-if-empty docker container stop'
                sh 'docker container ls -a -fname=email-sender -q | xargs -r docker container rm'
            }
        }
      
        stage('Docker Run') {
            steps{
                script {
                    sh 'docker run -d -p 8096:8000 --rm --name email-sender ${registryUrl}/${registryName}'
                }
            }
        }
    }
}