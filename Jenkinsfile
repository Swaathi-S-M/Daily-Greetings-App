pipeline {
    agent any

    environment {
        STREAMLIT_SUPPRESS_PROMPT = 'true'
    }

    stages {

        stage('Clone Repo') {
            steps {
                echo "Repository already checked out by Jenkins"
            }
        }

        stage('Install Dependencies') {
            steps {
                bat "python -m venv venv"
                bat "venv\\Scripts\\pip install -r requirements.txt"
            }
        }

        stage('Run Streamlit App') {
            steps {
                bat """
                start "" venv\\Scripts\\python -m streamlit run streamlit_app.py --server.port 8501 --server.headless true
                """
            }
        }
    }
}
