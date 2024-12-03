pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo "Building..."
                // Add your build commands here (if needed)
            }
        }

        // stage('Checkout') {
        //     steps {
        //         // Replace with your actual Git repository URL and branch
        //         git branch: 'main', url: 'https://github.com/toshan121/dashboard.git' 
        //     }
        // }



        stage('Test') {
            steps {
                echo 'Testing...'
                // Add your test commands here (if needed)
            }
        }

    stage('SonarQube analysis') {
      // requires SonarQube Scanner 2.8+
      def scannerHome = tool 'SonarQube Scanner 2.8';
      withSonarQubeEnv('My SonarQube Server') {
        sh "${scannerHome}/bin/sonar-scanner"
      }
    }


        stage('Publish to Nexus') {
            steps {
                echo "Publishing to Nexus..."
                nexusArtifactUploader(
                    artifacts: [[
                        artifactId: 'my-artifact',  // Replace with your artifact ID
                        classifier: '',
                        file: 'main.py', 
                        type: 'file'
                    ]],
                    credentialsId: '35e9b26e-269a-4804-a70d-6b2ec7a608ce',
                    groupId: 'my-group',  // Replace with your group ID
                    nexusUrl: '192.168.0.61:8081',
                    nexusVersion: 'nexus3',
                    protocol: 'http',
                    repository: 'raw-release',  // Or your desired repository
                    version: '1.0.0'  // Replace with your version number
                )
            }
        }

        // Stage 4 : Print some information (removed since we don't have Maven)

        // Stage 5 and 6 (Deploy to Tomcat and Docker) are commented out
    }
}
