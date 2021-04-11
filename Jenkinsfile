pipeline{
    agent any
    environment {
        app_version = 'v1'
        rollback = 'false'
    }

    stages{

        stage('Build'){
            steps{
                sh "bash scripts/build-app.sh"
            }
        }

        stage('Configuration'){
            steps{
                sh 'ansible-galaxy collection install community.docker'
                sh 'cd Ansible && ansible-playbook -i inventory.yaml playbook.yaml' 
            }
        }
        
        stage('Deploy'){
            steps{
                sh "bash scripts/deploy-app.sh"
            }
        }
    }
}
