pipeline {
    agent { label 'dockeragent' }
    stages {
        stage('Fetching Files') {
            steps {
                echo 'fetching files from repo...'
                git branch: 'main', credentialsId: '4fc702e0-1746-4b7f-9cfe-bf463e5b8348', url: 'http://44.207.100.114/gitlab-instance-84acfba7/python-webapp'
            }
        }
        stage('Building Image') {
            steps {
                echo 'Building Image from dockerfile..'
                sh '[ "$(sudo docker ps -a | grep testing-webapp-c)" ] && sudo docker stop testing-webapp-c && sudo docker container rm testing-webapp-c'
                sh 'sudo docker build -t moodyomarz/testing-webapp .'
                sh 'sudo docker run -d --name testing-webapp-c -p 80:3000 testing-webapp'
            }
        }
        stage('Unit Testing') {
            steps {
                echo 'Running unit tests on app..'
                sh 'sleep 3 && python3 -m unittest'
                // sh 'sudo docker exec testing-webapp-c python3 -m unittest'
            }
        }
      stage('Pushing To DockerHub') {
            steps {
                echo 'Pushing image to dockerhub..'
                sh 'sudo chmod 666 /var/run/docker.sock'
                withDockerRegistry([ credentialsId: "211fc4dc-f432-4d43-ad4c-f086db50224a", url: "" ]) {
                    sh 'sudo docker push moodyomarz/testing-webapp'
                }
            }
        }
    }
    post {
        success {
            slackSend channel: 'builds', color: 'SUCCESS', message: 'Build Succeeded Madafucka !', teamDomain: 'jenkins-project'
        }
        failure {
            slackSend channel: 'devops-alerts', color: 'FAILURE', message: 'Build Failed :(', teamDomain: 'jenkins-project'
        }
    }
}