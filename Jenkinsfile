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
                ansiblePlaybook credentialsId: 'f72ec555-5ef4-44d5-8035-7e6c4e73e66a', disableHostKeyChecking: true, installation: 'ansible', inventory: 'Ansible/playbook.yaml', playbook: 'Ansible/inventory.yaml'            }
        }


        
        stage('Deploy'){
            steps{
                sh "bash deploy-app.sh"
            }
        }
    }
}
