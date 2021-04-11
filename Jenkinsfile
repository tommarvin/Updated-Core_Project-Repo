pipeline{
    agent any
    environment {
        app_version = 'v1'
        rollback = 'false'
    }

    stages{

        stage('Build'){
            steps{
                sh "docker-compose down --rmi all && docker-compose build"
                sh "docker-compose up -d"
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

                sh "/home/jenkins/.local/bin/ansible-playbook -i inventory.yaml playbook.yaml "
            }
        }
        
        stage('Deploy'){
            steps{
                sh "docker stack deploy --compose file docker-compose.yaml"
            }
        }
    }
}
