pipeline{
        agent any
        environment {
            app_version = 'v1'
            rollback = 'false'
        }
        stages{
            stage('Build Image'){
                steps{
                    script{
                        if (env.rollback == 'false'){
                            sh "docker-compose build"
                        }
                    }
                }
            }
            
        stage('Deploy App'){
            steps{
                sh "docker-compose pull && docker-compose up -d"
            }
        }
    }
}