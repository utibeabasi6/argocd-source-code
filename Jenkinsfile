pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                checkout scm
                sh 'npm install'
            }
        }
    }
}