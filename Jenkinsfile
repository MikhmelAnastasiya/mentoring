pipeline {
  agent { docker { image 'python:3.8.2' } }
  stages {
   
    stage('Build1') {
      steps {
        sh 'pip3 install lxml'
      }
    }
     stage('Build2') {
      steps {
        sh 'pip install --upgrade lxml'
      }
    }
    stage('Build') {
      steps {
        sh 'python main.py'
      }
    }
  }

}


