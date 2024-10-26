import csv
import random

# Define study plans for different levels
study_plans = {
    "Basic": """
Basic Level Study Plan: Data Science and Machine Learning
Week 1-2: Introduction to Data Science and Machine Learning
Goal: Understand the basic concepts and types of machine learning.
Key Concepts:
- Introduction to data science and machine learning
- Difference between supervised, unsupervised, and reinforcement learning
- Understanding basic terms like dataset, features, labels, and models
Resources:
- Coursera: Introduction to Data Science by IBM
- YouTube: Data School - What is Machine Learning?

Week 3-4: Python for Data Science
Goal: Get familiar with Python, a popular language for data science.
Key Concepts:
- Python basics: data types, loops, functions, and libraries
- Introduction to essential libraries: NumPy, Pandas, Matplotlib
- Loading and manipulating datasets with Pandas
Resources:
- Python for Data Analysis by Wes McKinney
- Kaggle: Python Course
...
""",
    "Intermediate": """
Intermediate Level Study Plan: Data Science and Machine Learning
Week 1-2: Data Analysis and Data Wrangling
Goal: Strengthen data manipulation and analysis skills.
Key Concepts:
- Data wrangling with Pandas and NumPy
- Handling missing values, data cleaning, and transformations
Resources:
- Kaggle: Pandas Course
- YouTube: Corey Schafer - Data Analysis with Pandas

Week 3-4: Exploratory Data Analysis and Visualization
Goal: Improve skills in visualizing and interpreting data.
Key Concepts:
- Using Seaborn and Matplotlib for EDA
- Statistical analysis and correlation studies
Resources:
- Udacity: Data Visualization in Python
- Towards Data Science: EDA Tutorial
...
""",
    "Advanced": """
Advanced Level Study Plan: Data Science and Machine Learning
Week 1-2: Feature Engineering and Data Preparation
Goal: Master feature engineering techniques for model optimization.
Key Concepts:
- Advanced feature engineering methods
- Scaling, normalization, and encoding
Resources:
- Coursera: Feature Engineering for Machine Learning by University of Washington
- YouTube: StatQuest with Josh Starmer - Feature Engineering

Week 3-4: Advanced Machine Learning Models
Goal: Deep dive into complex machine learning models.
Key Concepts:
- Ensemble methods, boosting, and bagging
- Support Vector Machines, XGBoost, Random Forest
Resources:
- Coursera: Advanced Machine Learning Specialization by HSE University
- Book: Hands-On Machine Learning with Scikit-Learn and TensorFlow by Aurélien Géron
...
""",
    "Expert": """
Expert Level Study Plan: Data Science and Machine Learning
Week 1-2: Research Methods and Algorithm Optimization
Goal: Conduct research and optimize algorithms.
Key Concepts:
- Advanced research methodologies
- Hyperparameter tuning, optimization techniques
Resources:
- Coursera: Machine Learning Specialization by Andrew Ng
- Research Papers on arXiv

Week 3-4: Deploying Machine Learning Models
Goal: Learn how to deploy machine learning models in production.
Key Concepts:
- Model deployment techniques
- Building APIs and using cloud platforms
Resources:
- FastAPI Documentation
- AWS Machine Learning Services
...
"""
}

# Define score to level mapping
score_to_level = {
    0: "Basic",
    20: "Basic",
    40: "Intermediate",
    60: "Intermediate",
    80: "Advanced",
    100: "Expert"
}

# Function to create dataset
def create_dataset(file_name, num_records=100):
    with open(file_name, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["prompt", "completion"])  # Header

        for _ in range(num_records):
            score = random.choice([0, 20, 40, 60, 80, 100])
            level = score_to_level[score]

            prompt = f"Student scored {score}% in the Data Science and Machine Learning quiz. " \
                     f"Provide a study plan for the {level} level, focusing on key concepts and resources."

            completion = study_plans[level].strip()
            writer.writerow([prompt, completion])

# Create the dataset
create_dataset("study_plan_dataset.csv", num_records=100)
print("Dataset created successfully as 'study_plans.csv'")
