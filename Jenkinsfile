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



stage('Deploy to Agent') {
    steps {
        echo "Deploying to agent..."
        sshPublisher(publishers: [
            sshPublisherDesc(
                configName: 'your-ssh-config-name',
                transfers: [
                    sshTransfer(
                        sourceFiles: 'main.py',
                        remoteDirectory: '~/deployments/${JOB_NAME}',
                        execCommand: '''
                            #!/bin/bash
                            cd ~/deployments/"${JOB_NAME}"

                            # Check if a process with the same name is already running
                            if pm2 status my-app | grep -q "online"; then
                                echo "Application is already running. Skipping deployment."
                            else
                                pm2 start main.py --name my-app --interpreter python3
                            fi
                        '''
                    )
                ]
            )
        ])
    }
}
    }
}
