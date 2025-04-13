pipeline{
    agent any

    environment{
        VENV_DIR = 'venv'
    }


    stages {
        stage('Cloing Github Repo to Jenkins') {
            steps {
                script{
                    echo 'Cloning Github Repo to Jenkins.........'
                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github-token-test', url: 'https://github.com/Udaykumargajavalli/mlops_test.git']])
                }
            }
        }

        stage('Setting up our virtual environment and installing dependencies') {
            steps {
                script{
                    echo 'Setting up our virtual environment and installing dependencies.........'
                    sh '''
                        python3 -m venv ${VENV_DIR}
                        . ${VENV_DIR}/bin/activate
                        pip install --upgrade pip
                        pip install -e .
                    '''


                 }
            }
        }
    }
}