pipeline {
    agent any

    parameters {
        string(name: 'TARGET_IP', defaultValue: '127.0.0.1', description: 'Target IP for scanning')
    }

    stages {
        stage('Clone Repo') {
            steps {
                git branch: 'main' 'https://github.com/MUGIWARA102/PortScanner.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Scan') {
            steps {
                sh "python main.py ${params.TARGET_IP} > scan_output.txt"
            }
        }

        stage('Archive Results') {
            steps {
                archiveArtifacts artifacts: 'scan_output.txt', fingerprint: true
            }
        }
    }
}