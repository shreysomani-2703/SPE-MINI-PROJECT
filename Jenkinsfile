pipeline {
    agent any

    stages {

        stage('Clone') {
            steps {
                git 'https://github.com/shreysomani-2703/SPE-MINI-PROJECT.git'
            }
        }

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