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
                ansiblePlaybook disableHostKeyChecking: true, inventory: '/home/pc/Project-Folder/Ansible/inventory.yaml', playbook: '/home/pc/Project-Folder/Ansible/play-book.yaml'            
            }        
        }


        
        stage('Deploy'){
            steps{
                sh "bash deploy-app.sh"
            }
        }
    }
}
