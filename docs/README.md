# **Early Detection of Lung Cancer Risk Using Prediction Models**

## **Project Overview**
The Lung Cancer Early Detection Project leverages data science and machine learning techniques to develop a predictive model for assessing the risk of lung cancer. Lung cancer is one of the leading causes of cancer-related deaths worldwide, primarily due to delayed diagnoses. This project aims to create a non-invasive, cost-effective solution for early detection by analyzing patient data, including demographics, medical history, and lifestyle factors.

## **Objectives**
- Develop a Predictive Model: Build a machine learning model to identify high-risk individuals based on historical patient data.
- Establish a Data Pipeline: Implement a pipeline for efficient data processing, feature engineering, and model training.
- Enhance Early Detection: Provide a valuable tool for healthcare professionals to improve lung cancer outcomes through early diagnosis.

## **Project Workflow**

### **1. MongoDB Setup**
- **Account and Cluster Creation**: Created a MongoDB Atlas account and set up a cluster.
- **Data Upload**: Uploaded the lung cancer dataset (stored in `data/processed/dataset.json`) to MongoDB.
- **Database and Collection**: The data is stored in MongoDB under the database `Lungcancer` and collection `Patients`.

### **2. Data Access and Exploration**
- **Reading Data**: Accessed the dataset in MongoDB using PyMongo.
- **Exploratory Data Analysis (EDA)**: Conducted EDA in the `1.0_initial_data_exploration.ipynb` notebook to explore key patterns and distributions.
- **Data Preprocessing**: Cleaned and prepared the data for modeling by handling missing values and performing feature engineering.

### **3. Data Pipeline Creation**
- **Data Grouping and Viewing**: Built a pipeline in MongoDB to process and group the dataset for deeper insights.

### **4. MongoDB-Databricks Connection Setup**
- **Connection Setup**: Established a connection between MongoDB and Databricks.
- **Data Transformation with PySpark**: Applied transformations in Databricks using PySpark (see `2.0_pyspark_preprocessing.ipynb` for more details) to prepare data for model training.

### **5. Model Training and Evaluation**
- **Train-Test Split**: Divided the data into training and testing sets.
- **Evaluation Metrics**: Evaluated model performance using accuracy, precision, recall, and F1-score.
- **Model Selection**: Trained Logistic Regression and Random Forest models on the processed dataset, with evaluation conducted in `4.0_preprocessing_model_training_testing.ipynb`.

## **Setup Instructions**
Instructions for MongoDB-Databricks connection are available in the `docs` folder, along with the Code of Conduct and Teamwork Contract.

---

### **Additional Documentation**
- **Project Proposal**: Detailed project objectives, timeline, and methodology are outlined in `reports/final_proposal.pdf`.

---

### **Team Members**
- Akansha Bhargavi Bommu 
- Harman Saggu
- Shaharyaar Kutchi
