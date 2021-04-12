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
                ansiblePlaybook credentialsId: 'c08bcb13-9ffb-43e5-986d-ed069cdd9698', disableHostKeyChecking: true, installation: 'ansible', inventory: 'Ansible/playbook.yaml', playbook: 'Ansible/inventory.yaml'
            }
        }

        
        stage('Deploy'){
            steps{
                sh "bash deploy-app.sh"
            }
        }
    }
}
