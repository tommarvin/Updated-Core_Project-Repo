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
            }
        }

        stage('Push'){
            steps{
                sh "docker ps && docker images"
                sh "docker-compose push"
            }
        }
        
        stage('Deploy'){
            steps{
                sh './scripts/deploy-app.sh'
            }
        }
    }
}
