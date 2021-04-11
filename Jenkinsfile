pipeline{
    agent any
    environment {
        app_version = 'v1'
        rollback = 'false'
    }
    stages{

        stage('Build'){
            steps{
                sh "docker-compose build && docker-compose push"
            }
        }

        stage('Configuration'){
            steps{
                sh "cd Ansible && ansible-playbook -i inventory.yaml playbook.yaml"
            }
        }
        
        stage('Deploy'){
            steps{
                sh "bash scripts/deploy-app.sh"
            }
        }
    }
}
