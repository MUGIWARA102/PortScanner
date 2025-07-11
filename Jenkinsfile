pipeline {
    agent {
        docker {
            image 'python:3.10'  // Pulls official Python image
        }
    }

    parameters {
        string(name: 'TARGET_IP', defaultValue: '127.0.0.1', description: 'Target IP for scanning')
    }

    stages {
        stage('Clone Repo') {
            steps {
                git branch: 'main', url: 'https://github.com/MUGIWARA102/PortScanner.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Run Scan') {
            steps {
                sh "python3 portscanner.py ${params.TARGET_IP} > scan_output.txt"
            }
        }

        stage('Archive Results') {
            steps {
                archiveArtifacts artifacts: 'scan_output.txt', fingerprint: true
            }
        }
    }
}
