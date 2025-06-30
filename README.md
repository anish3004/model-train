# model-train
This project demonstrates how to perform feature engineering on customer activity data using Snowflake, and train a machine learning model in Python to predict active customers.

Project Structure :
fetch_features.py – Fetches features from the Snowflake table CUSTOMER_FEATURES
train_model.py – Trains a Random Forest classifier using the extracted features
snowflake_config.py – Contains connection logic for Snowflake
README.md – You’re reading it!
presentation.pptx – Final presentation explaining the project workflow

What’s Covered :
Connection to Snowflake using `snowflake-connector-python`
SQL-based feature engineering on customer login/transaction data
Feature retrieval into Pandas
Creating binary labels (`IS_ACTIVE`) based on simple logic
Training a Random Forest model using `scikit-learn`
Model evaluation using classification report (precision, recall, F1-score)

Tech Stack :
Python (pandas, scikit-learn)
Snowflake
VS Code
Git & GitHub
