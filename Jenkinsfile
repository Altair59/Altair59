node {
  stage('SCM') {
    checkout scm
  }
  stage('SonarQube Analysis') {
    def scannerHome = tool 'hjsproject'
    withSonarQubeEnv() {
      sh "${scannerHome}/bin/sonar-scanner"
    }
  }
  stage('Check Quality Gate') {
    def qualityGate = waitForQualityGate()
    if (qualityGate.status != 'OK') {
      error "Pipeline aborted due to quality gate failure: ${qualityGate.status}"
    } else {
      echo 'Quality gate passed, no critical issues found.'
    }
  }
  stage('Run Hadoop Job on Dataproc') {
    sh '''
      ./tmp/google-cloud-sdk/bin/gcloud compute ssh --zone "us-central1-c" "hadoop-m" --tunnel-through-iap --project "cmu-14848-434700"
    '''
    sh '''
      cd /tmp/mapreduce-source/
    '''
    sh '''
      git pull https://github.com/Altair59/Altair59.git
    '''
  }
}
