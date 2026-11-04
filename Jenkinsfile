pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Verify Microservices') {
            steps {
                sh '''
                    echo "Checking microservices files..."
                    test -f user-service/app.py
                    test -f product-service/app.py
                    test -f order-service/app.py
                '''
            }
        }

        stage('Build') {
            steps {
                echo 'Microservices source validation completed'
            }
        }

        stage('Test') {
            steps {
                sh '''
                    python3 -m py_compile user-service/app.py
                    python3 -m py_compile product-service/app.py
                    python3 -m py_compile order-service/app.py
                '''
            }
        }

        stage('Deployment Preparation') {
            steps {
                echo 'Microservices ready for future AWS deployment'
            }
        }
    }

    post {
        success {
            echo 'Jenkins pipeline completed successfully!'
        }
        failure {
            echo 'Jenkins pipeline failed!'
        }
    }
}