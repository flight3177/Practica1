pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Код получен из репозитория'
            }
        }
        stage('Setup') {
            steps {
                sh 'python3 -m venv venv'
                sh './venv/bin/pip install --upgrade pip'
                sh './venv/bin/pip install -r requirements.txt'
            }
        }
        stage('Build') {
            steps {
                sh './venv/bin/python -m py_compile app.py'
            }
        }
        stage('Test') {
            steps {
                sh './venv/bin/pytest --junitxml=result.xml'
            }
        }
    }
    post {
        always {
            junit 'result.xml'
        }
    }
}
