pipeline {
    agent any

    environment {
        VIRTUAL_ENV = 'venv'
    }

    stages {
        stage('Setup') {
            steps {
                script {
                    if (!fileExists("${env.WORKSPACE}\\${VIRTUAL_ENV}")) {
                        bat "python -m venv ${VIRTUAL_ENV}"
                    }
                    bat "call ${VIRTUAL_ENV}\\Scripts\\activate && pip install -r requirements.txt"
                }
            }
        }

        stage('Lint') {
            steps {
                script {
                    bat "call ${VIRTUAL_ENV}\\Scripts\\activate && flake8 app.py"
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    bat "call ${VIRTUAL_ENV}\\Scripts\\activate && pytest"
                }
            }
        }

        stage('Coverage') {
            steps {
                script {
                    bat """
                        call ${VIRTUAL_ENV}\\Scripts\\activate
                        coverage run -m pytest
                        coverage report -m
                    """
                }
            }
        }

        stage('Security Scan') {
            steps {
                script {
                    bat """
                        call ${VIRTUAL_ENV}\\Scripts\\activate
                        bandit -r . -f json -o bandit_report.json
                        type bandit_report.json
                    """
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    bat """
                        echo Deploying application...
                        if not exist deploy mkdir deploy
                        copy app.py deploy\\app.py /Y
                        echo Application deployed to the 'deploy' folder.
                    """
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
