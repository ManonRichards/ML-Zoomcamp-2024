# ML Zoomcamp Midterm Project: Customer Churn - Banking

--------------------------------------------------------------

### Problem Description:

Customer churn is a major concern for the banking industry representing a loss of revenue and impacting long-term growth. This happens through the loss of customers to the bank, which means customers closing accounts, moving to a competitiors bank and reducing the usage of the bank's services. This lost revenue leads to higher acquisition costs to replace the customers who churned as well as a potential damage to brand reputation. 

The goal of this project is to predict which customers are most likely to churn so that the bank can take proactive measures to retain them as customers. These proactive measures could include things like tailored incentives, improving services or addressing dissatisfaction. This would also save the bank money by lowering customer aquisition costs and improving overall customer lifetime value. 

-----------------------------------------------------------------

### Data

The data is sourced from here: [Bank Customer Churn Prediction Dataset on Kaggle](https://www.kaggle.com/datasets/shubhammeshram579/bank-customer-churn-prediction/data)

This is read in as part of the EDA process and you can find it in the code. 

The data includes the following columns: 

1. Customer ID: A unique identifier for each customer
2. Surname: The customer's surname or last name
3. Credit Score: A numerical value representing the customer's credit score
4. Geography: The country where the customer resides (France, Spain or Germany)
5. Gender: The customer's gender (Male or Female)
6. Age: The customer's age.
7. Tenure: The number of years the customer has been with the bank
8. Balance: The customer's account balance
9. NumOfProducts: The number of bank products the customer uses (e.g., savings account, credit card)
10. HasCrCard: Whether the customer has a credit card (1 = yes, 0 = no)
11. IsActiveMember: Whether the customer is an active member (1 = yes, 0 = no)
12. EstimatedSalary: The estimated salary of the customer
13. Exited: Whether the customer has churned (1 = yes, 0 = no)

-----------------------------------------------------------------

### EDA

The code that holds EDA is stored within this folder and called MidTerm_Project.ipynb: [Midterm Project Notebook](https://github.com/ManonRichards/ML-Zoomcamp-2024/blob/main/Midterm_Project/MidTerm_Project.ipynb)

It includes feature importance and mutual information. 

Down to the point where it says ####One Hot Encoding

### Model Training and Tuning

In the same code as above, you will find the following training models:

1. Logisitc Regression
2. Decision Tree
3. Random Forest
4. XGBoost

XGBoost performs best. 

The script for training the XGBoost model is here: [Midterm Project Notebook](https://github.com/ManonRichards/ML-Zoomcamp-2024/blob/main/Midterm_Project/MidTerm_Project_XGBoost_Model.ipynb)

### Deployment

Make sure you have the following installed:

- git
- docker
- python
- pipenv

# Clone the Repository
git clone [https://github.com/username/repository-name.git](https://github.com/ManonRichards/ML-Zoomcamp-2024/tree/main/Midterm_Project)
cd Midterm_Project

# Set up the environment
Run the following command to install the necessary Python Packages from Pipfile

`pipenv install`

Then activate the virtual environment: 

`pipenv shell`

Run the flask app:

`flask run`

# Docker File

run the following code to build the docker image:

`docker build -t midterm-project-mr . `

Once the image is built, run the docker container:

`docker run -p 1911:1911 midterm-project-mr `

If you'd like to test the model you can run the following:

`python predict_test.py `

This will output either: sending promo email to xyz-123 or not sending promo email to xyz-123

If you'd like to stop the dcoker container remember to press CTRL + C in your terminal.


