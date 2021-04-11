pipeline{
    agent any
    environment {
        app_version = 'v1'
        rollback = 'false'
    }

    stages{

        stage('Build'){
            steps{
                sh "docker-compose up --build"
            }
        }

        stage('Push'){
            steps{
                sh "docker ps && docker images"
                sh "docker-compose push"
            }
        }


        stage('Config'){
            steps{                          

                sh "~/ansible-playbook -i inventory.yaml playbook.yaml "
            }
        }
        
        stage('Deploy'){
            steps{
                sh "docker stack deploy --compose file docker-compose.yaml 1-service"
            }
        }
    }
}
