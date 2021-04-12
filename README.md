# Core-Practical-Project

        stage('Config'){
            steps{
                ansiblePlaybook credentialsId: 'f72ec555-5ef4-44d5-8035-7e6c4e73e66a', disableHostKeyChecking: true, installation: 'ansible', inventory: 'Ansible/inventory.yaml', playbook: 'Ansible/playbook.yaml'
            }
        }

        stage('Deploy'){
            steps{
                sh "bash deploy-app.sh"
            }
        }