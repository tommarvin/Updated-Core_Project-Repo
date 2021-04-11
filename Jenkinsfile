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
                dir("Project-Folder/Ansible"){
                sh "/home/jenkins/.local/bin/ansible-playbook -i inventory.yaml playbook.yaml"
                }
            }
        }
        
        stage('Deploy'){
            steps{
                sh "bash scripts/deploy-app.sh"
            }
        }
    }
}
