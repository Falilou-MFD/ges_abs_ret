pipeline {
    agent any

    environment {
        DOCKER_USERNAME = "koji2112"
        IMAGE_VERSION = "1.${BUILD_NUMBER}"
        DOCKER_IMAGE = "${DOCKER_USERNAME}/tp-app:${IMAGE_VERSION}"
        DOCKER_CONTAINER = "jenkins"
    }

    stages {
        stage("Checkout") {
            steps {
                git branch: 'jenkins_koji', url: 'https://github.com/Falilou-MFD/ges_abs_ret.git'
            }
        }

        stage("Test") {
            steps {
                echo "Tests en cours"
            }
        }

        stage("Build Docker Image") {
            steps {
                script {
                    bat "docker build -t $DOCKER_IMAGE ."
                }
            }
        }

        stage("Push image to Docker Hub") {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'koji2112', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASSWORD')]) {
                        bat """
                        docker login -u ${DOCKER_USER} -p ${DOCKER_PASSWORD}
                        echo 'Docker login successful'
                        docker push $DOCKER_IMAGE
                        """
                    }
                }
            }
        }

        stage("Deploy") {
            steps {
                script {
                    bat """
                    docker container stop $DOCKER_CONTAINER || true
                    docker container rm $DOCKER_CONTAINER || true
                    docker container run -d --name $DOCKER_CONTAINER -p 8080:80 $DOCKER_IMAGE
                    """
                }
            }
        }
    }

    post {
        success {
            mail to: 'falilou1999@gmail.com , maimounasow1410@gmail.com , kubuyaphilemon4@gmail.com , robinyonli2@gmail.com',
                 subject: "✅ Succès du pipeline : ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                 body: "Le pipeline a été exécuté avec succès.\nVoir les détails ici : ${env.BUILD_URL}"
        }

        failure {
            mail to: 'destinataire@example.com',
                 subject: "❌ Échec du pipeline : ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                 body: "Le pipeline a échoué.\nVoir les logs ici : ${env.BUILD_URL}"
        }

        always {
            echo 'Notification e-mail envoyée.'
        }
    }
}
