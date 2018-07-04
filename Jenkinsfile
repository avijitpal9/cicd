pipeline {
  agent any
  stages {

    stage('Build') {
      steps {
        echo 'Build Stage'
        sh 'python setup.py sdist --formats=gztar'
      }
    }

    stage('Test') {
      steps {
        echo 'Test Stage'
      }
    }

    stage('Build & Publish Image') {
      when {
        anyOf { branch 'master'; branch 'development' }
      }
      steps {
        echo 'Docker Build & Publish Stage'

        script {
              if (env.BRANCH_NAME == 'master') {
                    docker.withRegistry('https://index.docker.io/v1/', 'avijit-dockerhub') {
                    def customImage = docker.build("avijitpal9/myapp:${env.BUILD_ID}-dev")
                    customImage.push()
                    }
              } else if  (env.BRANCH_NAME == 'development') {
                    docker.withRegistry('https://index.docker.io/v1/', 'avijit-dockerhub') {
                    def customImage = docker.build("avijitpal9/myapp:${env.BUILD_ID}")
                    customImage.push()
                    customImage.push('latest')
                    }
              }
           }
        }
    }

    stage('Deploy') {
      when {
        anyOf { branch 'master'; branch 'development' }
      }

      steps {
        echo 'Deploy Stage'
        sh """
            sed -i "s/myapp:latest/myapp:${env.BUILD_ID}/g" k8s/deployment.yaml
            kubectl apply -f k8s/deployment.yaml
            """
      }
    }

  }
}
