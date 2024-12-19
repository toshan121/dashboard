pipeline {
    agent any

    stages {
        stage('Jenkinsfile Syntax Check') {
            steps {
                echo "Jenkinsfile Syntax Check..."
                // configFileProvider([configFile(fileId: 'your-jenkinsfile-id', variable: 'JENKINSFILE')]) {
                //     sh 'jenkins-cli groovy-lint "${JENKINSFILE}"'
                // }
            }
        }

        stage('Checkout Repo') {
            steps {
                // Replace with your actual Git repository URL and branch
                git branch: 'main', url: 'https://github.com/toshan121/dashboard.git' 
            }
        }


        stage('Build') {
            steps {
                echo 'Testing...'
                // Add your test commands here (if needed)
            }
        }

        

stage('Test PEX') {
    steps {
        echo 'Testing PEX file...'

        withPythonEnv('python3') {
            // Assuming your PEX file is named my_app.pex
            sh '''
                #!/bin/bash

                if [[ my_app.pex == *.pex ]]; then
                    echo "PEX file found."

                    # Run pytest within the PEX environment
                    pex my_app.pex -c "pytest mytest.py"
                else
                    echo "Not a PEX file. Skipping test."
                fi
            '''
        }
    }
}

        stage('SonarQube Static Analysis') {
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
