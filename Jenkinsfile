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
      cd /tmp/Altair59/
      git pull https://github.com/Altair59/Altair59.git
      /tmp/google-cloud-sdk/bin/gcloud compute scp /tmp/Altair59/mapper.py hadoop-m:/tmp/mapreduce-source --tunnel-through-iap --zone us-central1-c --project cmu-14848-434700
      /tmp/google-cloud-sdk/bin/gcloud compute scp /tmp/Altair59/reducer.py hadoop-m:/tmp/mapreduce-source --tunnel-through-iap --zone us-central1-c --project cmu-14848-434700
      /tmp/google-cloud-sdk/bin/gcloud compute ssh --zone "us-central1-c" "hadoop-m" --tunnel-through-iap --project "cmu-14848-434700" --command '
        cd /tmp/mapreduce-source/
        cat mapper.py
        cat reducer.py
      '
    '''
  }
}
