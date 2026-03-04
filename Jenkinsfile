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
    }
}