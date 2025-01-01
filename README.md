Bankruptcy Prediction Project

Overview
This project focuses on predicting bankruptcy for companies using machine learning techniques. It provides tools for exploratory data analysis (EDA), model building, and deployment, with the goal of distinguishing between bankrupt and solvent companies.

Features
Exploratory Data Analysis: Analyze trends, patterns, and important features in the dataset.

Machine Learning Model: Build and train a Random Forest model to classify companies.

Web App: Deploy the model using a Python-based application.

Folder Structure
Bankruptcy_project/
|
|-- app.py                             # Deployment script
|-- Bankrupt vs Solvent prediction.ipynb # Notebook for prediction workflow
|-- Bankruptcy Prediction.csv          # Dataset used for predictions
|-- Bankruptcy(EDA).ipynb              # Notebook for exploratory data analysis
|-- Bankruptcy_train_model(RF).joblib  # Trained Random Forest model file
|-- Bankuptcy(model building).ipynb    # Notebook for model building
|-- final_data.csv                     # Processed dataset
|-- .ipynb_checkpoints/                # Auto-saved notebook checkpoints


Installation
To set up the project locally:

Clone the repository from GitHub:

git clone <repository-url>
Navigate to the project directory:

cd Bankruptcy_project

Install the required dependencies:

pip install -r requirements.txt
Usage
Exploratory Data Analysis:

Open and run Bankruptcy(EDA).ipynb in Jupyter Notebook or JupyterLab.

Model Training:

Use Bankuptcy(model building).ipynb to train and save the machine learning model.

Model Prediction:

Run Bankrupt vs Solvent prediction.ipynb to make predictions using the trained model.

Deploy the Application:

Execute app.py to deploy the model as a web application.

Dataset
Bankruptcy Prediction.csv: The dataset used to train and test the machine learning model.

final_data.csv: A cleaned and processed version of the dataset.

Dependencies
Python 3.8 or later

Libraries: pandas, numpy, sklearn, joblib, flask (if applicable), and others listed in requirements.txt.

License
This project is open-source and available under the MIT License.
