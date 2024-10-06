node {
  stage('SCM') {
    checkout scm
  }
  stage('SonarQube Analysis') {
    def scannerHome = tool 'hjsproject';
    withSonarQubeEnv() {
      sh "${scannerHome}/bin/sonar-scanner"
    }
  }
  stage('Check Quality Gate') {
    def qualityGate = waitForQualityGate()
    if (qualityGate.status != 'OK') {
      error "Pipeline aborted due to quality gate failure: ${qualityGate.status}"
    } else {
      echo "Quality gate passed, no critical issues found."
    }
  }
}
