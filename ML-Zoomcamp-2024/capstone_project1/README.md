# ML Zoomcamp Capstone Project: High Scoring Student - Education

--------------------------------------------------------------

### Problem Description:

Students come from different backgrounds and have differing learning styles, as an education provider it would be good to understand who's likey to score highly so that they can be put forward for further education or for competitions to represent our company. 

-----------------------------------------------------------------

### Data

The data is sourced from here: [Student Scoring Prediction Dataset on Kaggle](https://www.kaggle.com/datasets/lainguyn123/student-performance-factors?select=StudentPerformanceFactors.csv)

This is read in as part of the EDA process and you can find it in the code. 

The data includes the following columns: 

1. Hours_Studied: Number of hours spent studying per week.
2. Attendance: Percentage of classes attended.
3. Parental_Involvement:	Level of parental involvement in the student's education (Low, Medium, High).
4. Access_to_Resources:	Availability of educational resources (Low, Medium, High).
5. Extracurricular_Activities:	Participation in extracurricular activities (Yes, No).
6. Sleep_Hours:	Average number of hours of sleep per night.
7. Previous_Scores:	Scores from previous exams.
8. Motivation_Level:	Student's level of motivation (Low, Medium, High).
9. Internet_Access:	Availability of internet access (Yes, No).
10. Tutoring_Sessions:	Number of tutoring sessions attended per month.
11. Family_Income:	Family income level (Low, Medium, High).
12. Teacher_Quality:	Quality of the teachers (Low, Medium, High).
13. School_Type:	Type of school attended (Public, Private).
14. Peer_Influence:	Influence of peers on academic performance (Positive, Neutral, Negative).
15. Physical_Activity:	Average number of hours of physical activity per week.
16. Learning_Disabilities:	Presence of learning disabilities (Yes, No).
17. Parental_Education_Level:	Highest education level of parents (High School, College, Postgraduate).
18. Distance_from_Home:	Distance from home to school (Near, Moderate, Far).
19. Gender:	Gender of the student (Male, Female).
20. Exam_Score:	Final exam score.

-----------------------------------------------------------------

### EDA

The code that holds EDA is stored within this folder and called Capstone1_Project.ipynb: [Capstone1 Project Notebook](https://github.com/ManonRichards/ML-Zoomcamp-2024/blob/main/ML-Zoomcamp-2024/capstone_project1/Capstone1_Project.ipynb)

It includes feature importance and mutual information. 

Down to the point where it says ####One Hot Encoding

### Model Training and Tuning

In the same code as above, you will find the following training models:

1. Logisitc Regression
2. Decision Tree
3. Random Forest


Logistic Regression Performs best.

The script for training the Logistic Regression model is here: [Logistic Regression Training Model](https://github.com/ManonRichards/ML-Zoomcamp-2024/blob/main/ML-Zoomcamp-2024/capstone_project1/capstone1_log_reg_model.py)

### Deployment

Make sure you have the following installed:

- git
- docker
- python
- pipenv

# Clone the Repository
`git clone [https://github.com/username/repository-name.git](https://github.com/ManonRichards/ML-Zoomcamp-2024/tree/main/ML-Zoomcamp-2024/capstone_project1))
cd capstone_project1`

# Set up the environment
Run the following command to install the necessary Python Packages from Pipfile

`pipenv install`

Then activate the virtual environment: 

`pipenv shell`

Run the flask app:

`flask run`

# Docker File

run the following code to build the docker image:

`docker build -t capstone_project . `

Once the image is built, run the docker container:

`docker run -p 1911:1911 capstone_project `

If you'd like to test the model you can run the following:

`python predict_test.py `

If you'd like to stop the dcoker container remember to press CTRL + C in your terminal.



