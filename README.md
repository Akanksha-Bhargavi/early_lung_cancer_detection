<<<<<<< HEAD
# **Early Detection of Lung Cancer Risk Using Prediction Models**
Welcome to our Early Detection of Lung Cancer Risk project, where we use data science and machine learning to assess lung cancer risk. This predictive model aims to support healthcare professionals in identifying high-risk individuals for earlier diagnosis and improved patient outcomes.

Dive into the sections below to discover more about our project:

- [Team](#team)
- [Project Overview](#project-overview)
- [Objectives](#objectives)
- [Installation](#installation)
- [Usage](#usage)
---
### **Team**
Our team comprises Post-Baccalaureate students in Applied Data Science at Thompson Rivers University, working under the guidance of Professor Quan Nguyen.
- Akansha Bhargavi Bommu 
- Harman Saggu
- Shaharyaar Kutchi
 --- 
## **Project Overview**
The Lung Cancer Early Detection Project leverages data science and machine learning techniques to develop a predictive model for assessing the risk of lung cancer. Lung cancer is one of the leading causes of cancer-related deaths worldwide, primarily due to delayed diagnoses. This project aims to create a non-invasive, cost-effective solution for early detection by analyzing patient data, including demographics, medical history, and lifestyle factors.

---
## **Objectives**
- Develop a Predictive Model: Build a machine learning model to identify high-risk individuals based on historical patient data.
- Establish a Data Pipeline: Implement a pipeline for efficient data processing, feature engineering, and model training.
- Enhance Early Detection: Provide a valuable tool for healthcare professionals to improve lung cancer outcomes through early diagnosis.
---
## **Installation**
Ensure you have the following tools installed:
- VS Code
---
## **Usage**
**README files**
[README file for repository structure](docs/README_repository_structure.md)

**Local Setup**
Follow the instructions below to run the prediction pipeline locally.

1. Clone the repo:
```bash
git clone https://github.com/TRU-PBADS/adsc3910-project-group-6.git
```

2. Navigate to the project:
```bash
cd adsc3910-project-group-6
```

3. Install and activate the required environment:
```bash
conda env create --file config/environment.yaml
conda activate lung_cancer_env
```

4. Raw data required to run the pipeline is already downloaded and saved to `data/dataset.json`.

5. MongoDB Setup
- Account and Cluster Creation: Created a MongoDB Atlas account and set up a cluster using `config/credentials_mongodb.json`.
- Data Upload: Uploaded the lung cancer dataset stored in `data/dataset.json` to MongoDB.
- Database and Collection: The data is stored in MongoDB under the database `Lungcancer` and collection `Patients`.

6. Data Access and Exploration
- Reading Data: Accessed the dataset in MongoDB using PyMongo.
- Exploratory Data Analysis (EDA): Conducted EDA in the `notebooks/1.0_initial_data_exploration.ipynb` notebook to explore key patterns and distributions.
- Data Preprocessing: Cleaned and prepared the data for modeling by handling missing values and performing feature engineering.

7. Data Pipeline Creation
- Data Grouping and Viewing: Built a pipeline in MongoDB to process and group the dataset for deeper insights check `notebooks/3.0_pipeline_analysis.ipynb`.

8. MongoDB-Databricks Connection Setup
- Connection Setup: Established a connection between MongoDB and Databricks.View `docs/mongodb_databricks_connection.md`
- Data Transformation with PySpark: Applied transformations in Databricks using PySpark (see `notebooks/2.0_pyspark_preprocessing.ipynb` for more details )to prepare data for model training.

9. Model Training and Evaluation
- Train-Test Split: Divided the data into training and testing sets.
- Evaluation Metrics: Evaluated model performance using accuracy, precision, recall, and F1-score.
- Model Selection: Trained Logistic Regression and Random Forest models on the processed dataset, with an evaluation conducted in `notebooks/4.0_preprocessing_model_training_testing.ipynb`.

10. Run the scripts
- To complete the pipeline, navigate to `scripts` and run the following in order:
- `scripts/utils.py`: Uploads and reads data from MongoDB.
- The following scripts should be run from the root directory as utils.py is used globally
- `scripts/eda.py`: Performs data exploration and visualization ```python -m scripts.eda ```.
- `scripts/pipeline.py`: Groups data for analysis ```python -m scripts.pipeline```.
- `scripts/model_train_test.py`: Trains and tests prediction models ```python -m scripts.model_train_test```.

11. Run the unit tests
- To complete the testing, navigate to `tests` and run the following in order:
- To run you need to use pytest filename.py to test [Eg. pytest test_utils.py]
- `tests/test_utils.py`: It tests the utils.py file which is in scripts folder. 
- `tests/test_eda.py`: It tests the eda.py file which is in scripts folder. Moreover, we intentionally fail few cases to showcase how we are handling error. 
- `tests/test_pipeline.py`: It tests the pipeline.py file which is in scripts folder. 
- `tests/test_model_train_test.py`: It tests the model_train_test.py file which is in scripts folder. 


---
### **Dependencies**
For the Python dependencies and the conda environment creation file, please check [here](config/environment.yaml)


---

### **Additional Documentation**
- **Project Proposal**: Detailed project objectives, timeline, and methodology are outlined in `reports/final_proposal.pdf`.



=======
# **Early Detection of Lung Cancer Risk Using Prediction Models**
Welcome to our Early Detection of Lung Cancer Risk project, where we use data science and machine learning to assess lung cancer risk. This predictive model aims to support healthcare professionals in identifying high-risk individuals for earlier diagnosis and improved patient outcomes.

Dive into the sections below to discover more about our project:

- [Team](#team)
- [Project Overview](#project-overview)
- [Objectives](#objectives)
- [Installation](#installation)
- [Usage](#usage)
---
### **Team**
Our team comprises Post-Baccalaureate students in Applied Data Science at Thompson Rivers University, working under the guidance of Professor Quan Nguyen.
- Akansha Bhargavi Bommu 
- Harman Saggu
- Shaharyaar Kutchi
 --- 
## **Project Overview**
The Lung Cancer Early Detection Project leverages data science and machine learning techniques to develop a predictive model for assessing the risk of lung cancer. Lung cancer is one of the leading causes of cancer-related deaths worldwide, primarily due to delayed diagnoses. This project aims to create a non-invasive, cost-effective solution for early detection by analyzing patient data, including demographics, medical history, and lifestyle factors.

---
## **Objectives**
- Develop a Predictive Model: Build a machine learning model to identify high-risk individuals based on historical patient data.
- Establish a Data Pipeline: Implement a pipeline for efficient data processing, feature engineering, and model training.
- Enhance Early Detection: Provide a valuable tool for healthcare professionals to improve lung cancer outcomes through early diagnosis.
---
## **Installation**
Ensure you have the following tools installed:
- VS Code
---
## **Usage**
**README files**
[README file for repository structure](docs/README_repository_structure.md)

**Local Setup**
Follow the instructions below to run the prediction pipeline locally.

1. Clone the repo:
```bash
git clone https://github.com/TRU-PBADS/adsc3910-project-group-6.git
```

2. Navigate to the project:
```bash
cd adsc3910-project-group-6
```

3. Install and activate the required environment:
```bash
conda env create --file config/environment.yaml
conda activate lung_cancer_env
```

4. Raw data required to run the pipeline is already downloaded and saved to `data/dataset.json`.

5. MongoDB Setup
- Account and Cluster Creation: Created a MongoDB Atlas account and set up a cluster using `config/credentials_mongodb.json`.
- Data Upload: Uploaded the lung cancer dataset stored in `data/dataset.json` to MongoDB.
- Database and Collection: The data is stored in MongoDB under the database `Lungcancer` and collection `Patients`.

6. Data Access and Exploration
- Reading Data: Accessed the dataset in MongoDB using PyMongo.
- Exploratory Data Analysis (EDA): Conducted EDA in the `notebooks/1.0_initial_data_exploration.ipynb` notebook to explore key patterns and distributions.
- Data Preprocessing: Cleaned and prepared the data for modeling by handling missing values and performing feature engineering.

7. Data Pipeline Creation
- Data Grouping and Viewing: Built a pipeline in MongoDB to process and group the dataset for deeper insights check `notebooks/3.0_pipeline_analysis.ipynb`.

8. MongoDB-Databricks Connection Setup
- Connection Setup: Established a connection between MongoDB and Databricks.View `docs/mongodb_databricks_connection.md`
- Data Transformation with PySpark: Applied transformations in Databricks using PySpark (see `notebooks/2.0_pyspark_preprocessing.ipynb` for more details )to prepare data for model training.

9. Model Training and Evaluation
- Train-Test Split: Divided the data into training and testing sets.
- Evaluation Metrics: Evaluated model performance using accuracy, precision, recall, and F1-score.
- Model Selection: Trained Logistic Regression and Random Forest models on the processed dataset, with an evaluation conducted in `notebooks/4.0_preprocessing_model_training_testing.ipynb`.

10. Run the scripts
- To complete the pipeline, navigate to `scripts` and run the following in order:
- `scripts/utils.py`: Uploads and reads data from MongoDB.
- The following scripts should be run from the root directory as utils.py is used globally
- `scripts/eda.py`: Performs data exploration and visualization ```python -m scripts.eda ```.
- `scripts/pipeline.py`: Groups data for analysis ```python -m scripts.pipeline```.
- `scripts/model_train_test.py`: Trains and tests prediction models ```python -m scripts.model_train_test```.

11. Run the unit tests
- To complete the testing, navigate to `tests` and run the following in order:
- To run you need to use pytest filename.py to test [Eg. pytest test_utils.py]
- `tests/test_utils.py`: It tests the utils.py file which is in scripts folder. 
- `tests/test_eda.py`: It tests the eda.py file which is in scripts folder. Moreover, we intentionally fail few cases to showcase how we are handling error. 
- `tests/test_pipeline.py`: It tests the pipeline.py file which is in scripts folder. 
- `tests/test_model_train_test.py`: It tests the model_train_test.py file which is in scripts folder. 


---
### **Dependencies**
For the Python dependencies and the conda environment creation file, please check [here](config/environment.yaml)


---

### **Additional Documentation**
- **Project Proposal**: Detailed project objectives, timeline, and methodology are outlined in `reports/final_proposal.pdf`.



>>>>>>> 0745549057de8905e260b5b6e99fa49a14654eb6
