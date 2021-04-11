pipeline{
    agent any
    environment {
        app_version = 'v1'
        rollback = 'false'
    }

    stages{

        stage('Build'){
            steps{
                sh "docker-compose build"
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

                sh "ansiblePlaybook become: true, credentialsId: '18713c3f-91c1-4111-b0ba-d148751741d6', installation: 'ansible', inventory: '/home/pc/Project-Folder/Ansible/inventory.yaml', playbook: '/home/pc/Project-Folder/Ansible/playbook.yaml' "
            }
        }
        
        stage('Deploy'){
            steps{
                sh "docker stack deploy --compose file docker-compose.yaml 1-service"
            }
        }
    }
}
