Health Insurance Cost and Risk Analysis

Introduction
This project analyzes how different factors such as age, lifestyle, and health conditions influence health insurance costs. It includes data cleaning, visualization, and machine learning to predict insurance charges.

Project Structure
health-insurance-analysis/

data/

health_insurance_cost_and_risk_dataset.csv
cleaned_insurance_data.csv

notebook/

analysis.ipynb

src/

cleaning.py

README.md
requirements.txt

Project Workflow

Load and explore the dataset
Clean and preprocess the data
Perform exploratory data analysis
Visualize relationships and patterns
Train a machine learning model
Evaluate model performance

Key Features
Data cleaning and preprocessing
Handling missing values
Encoding categorical variables
Feature engineering such as risk score and lifestyle index
Data visualization including distributions and correlations
Linear Regression model for prediction
Random Forest for feature importance analysis

Components

Data Cleaning (src/cleaning.py)
Handles missing values, removes duplicates, and prepares data for analysis

Analysis Notebook (notebook/analysis.ipynb)
Includes exploratory data analysis, visualizations, and model training

Dataset (data/)
Contains raw dataset and cleaned dataset after preprocessing

Machine Learning Models
Primary model is Linear Regression
Additional model is Random Forest for feature importance

Model Performance
Mean Absolute Error approximately 4200
R2 Score approximately 0.78

How to Run the Project

Clone or download the project
git clone https://github.com/your-username/health-insurance-analysis.git
Go to project folder
cd health-insurance-analysis
Install required libraries
pip install -r requirements.txt
Run Jupyter Notebook
jupyter notebook
Open notebook/analysis.ipynb and run all cells

Output
Cleaned dataset
Visualizations
Model performance results

Workflow Summary
Load dataset
Clean and preprocess data
Perform analysis
Train model
Evaluate results

Key Insights
Smoking significantly increases insurance cost
BMI and age are strong predictors
Pre existing conditions increase charges
Lifestyle has more impact than region

Future Improvements
Use advanced models such as Random Forest and XGBoost
Perform hyperparameter tuning
Build a web application for predictions
Deploy the model

Tech Stack
Python
Pandas
NumPy
Matplotlib
Seaborn
Scikit learn

Contributing
You can fork this project and improve it

License
This project is licensed under the MIT License

Author
SriVarshini Sannidhanam