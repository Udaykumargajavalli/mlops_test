pipeline{
    agent any

    environment{
        VENV_DIR = 'venv'
        GCP_PROJECT ='studious-saga-455906-v3'
        GCLOUD_PATH = '/var/jenkins_home/gcloud-cloud-sdk/bin/'
    }


    stages {
        stage('Cloing Github Repo to Jenkins') {
            steps {
                script{
                    echo 'Cloning Github Repo to Jenkins.........'
                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github-token', url: 'https://github.com/Udaykumargajavalli/mlops_test.git']])
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


        stage('Building and pushing docker image to GCR') {
            steps {
                withCredentials([file(credentialsId :'gcp-test-key', variable:'GOOGLE_APPLICATION_CREDENTIALS')]){
                    script{
                        echo 'Building and pushing docker image to GCR.........'
                        sh '''
                            export PATH=$PATH:${GCLOUD_PATH}

                            glcoud auth activate-service-account --key-file=${GOOGLE_APPLICATION_CREDENTIALS}

                            glcoud config set project ${GCP_PROJECT}

                            gcloud auth configure-docker --quiet

                            docker build -t gcr.io/${GCP_PROJECT}/mlops_test:latest .

                            docker push gcr.io/${GCP_PROJECT}/mlops_test:latest
                        '''
                    }

                }

            }
        }
    }
}