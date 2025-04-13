pipeline{
    agent any

    stages {
        stage('Cloing Github Repo to Jenkins') {
            steps {
                script{
                    echo 'Cloning Github Repo to Jenkins.........'
                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github-token-test', url: 'https://github.com/Udaykumargajavalli/mlops_test.git']])
                }
            }
        }
    }
}