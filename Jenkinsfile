pipeline {
    agent any

    stages {
        stage('Test') {
            steps {
                sh 'python3 -m unittest test_calculator.py'
            }
        }

        stage('Build Docker') {
            steps {
                sh 'docker build -t shrey1112/spe-mini-project .'
            }
        }

        stage('Push Docker') {
            steps {
                sh 'docker push shrey1112/spe-mini-project'
            }
        }
        stage('Pull Docker'){
            steps{
                sh 'ansible-playbook -i deploy.yml'
            }
        }
    }

    post {
        success {
            mail to: 'sdsomani27@gmail.com',
            subject: "Build SUCCESS: ${env.JOB_NAME}",
            body: "Build ${env.BUILD_NUMBER} completed successfully."
        }
        failure {
            mail to: 'sdsomani27@gmail.com',
            subject: "Build FAILED: ${env.JOB_NAME}",
            body: "Build ${env.BUILD_NUMBER} failed."
        }
    }
}
