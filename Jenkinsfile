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
                ansiblePlaybook credentialsId: 'private-key', disableHostKeyChecking: true, installation: 'ansible', inventory: 'Ansible/inventory.yaml', playbook: 'Ansible/playbook.yaml'            
            }        
        }


        stage('Deploy'){
            steps{
                sh "bash deploy-app.sh"
            }
        }
    }
}
