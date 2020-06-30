pipeline {
    agent any

    stages {
        stage('Check schematic') {
            steps {
                echo 'Checking schematic status..'
                sh 'python3 ./test/schematic.py'
            }
        }
        stage('Check PCB') {
            steps {
                echo 'Checking PCB status..'
                sh 'python3 ./test/pcb.py'
            }
        }
        stage('Check documentation') {
            
            steps {
                echo 'Checking documentation..'
                sh 'python3 ./test/documents.py'
            }
        }
        stage('Check manufacturing data') {
            steps {
                echo 'Checking manufacturing data..'
                sh 'python3 ./test/manufacturing.py'
            }
        }
    }
}
