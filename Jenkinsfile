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

    stage('Package') {
      echo 'Docker Package Stage'
      
    }

    stage('Deploy') {
      steps {
        echo 'Deploy Stage'
      }
    }

  }
}
