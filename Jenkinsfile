pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo "Building..."
                // Add your build commands here (if needed)zz
            }
        }

        stage('Checkout') {
            steps {
                // Replace with your actual Git repository URL and branch
                git branch: 'main', url: 'https://github.com/toshan121/dashboard.git' 
            }
        }



        stage('Test') {
            steps {
                echo 'Testing...'
                // Add your test commands here (if needed)
            }
        }

        
stage('SonarQube Analysis') {
    steps {
        script {
            def scannerHome = tool 'sonarqube'
            withSonarQubeEnv() {
                sh "${scannerHome}/bin/sonar-scanner"
            }
        }
    }
}




        stage('Publish to Nexus') {
            steps {
                echo "Publishing to Nexus..."
                nexusArtifactUploader(
                    artifacts: [[
                        artifactId: 'dashboard', 
                        classifier: '',
                        file: 'main.py', 
                        type: 'file'
                    ]],
                    credentialsId: 'nexus',
                    groupId: 'com.example.project', 
                    nexusUrl: '192.168.0.61:8081',
                    nexusVersion: 'nexus3',
                    protocol: 'http',
                    repository: 'raw-release', 
                    version: '1.0.0'
                )
            }
        }

        // Stage 4 : Print some information (removed since we don't have Maven)

        // Stage 5 and 6 (Deploy to Tomcat and Docker) are commented out
    }
}
