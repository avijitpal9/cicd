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
        branch 'master'
      }
      steps {
        echo 'Docker Build & Publish Stage'

        script {
           docker.withRegistry('https://docker.io/', 'avijit-dockerhub') {
           def customImage = docker.build("avijitpal9/myapp:${env.BUILD_ID}")
           customImage.push()
           customImage.push('latest')
         }
        }

      }
    }

    stage('Deploy') {
      steps {
        echo 'Deploy Stage'
      }
    }

  }
}
