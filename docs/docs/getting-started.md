Here’s a detailed setup guide for your `getting-started.md` file:
# Getting Started

## Prerequisites
To replicate this project on your local machine, make sure you have the following:

1. **Python 3.12**: This project is built using Python 3.12. Ensure that this version is installed on your system.
2. **MongoDB Atlas Account**: We use MongoDB Atlas to store and manage the lung cancer dataset.

## Setup Instructions

### 1. Install Python 3.12
Follow the steps below to install Python 3.12:

- **For Windows**: Download the installer from [Python.org](https://www.python.org/downloads/), run it, and make sure to check the "Add Python to PATH" option.
- **For macOS**: Use [Homebrew](https://brew.sh/) by running:
  ```bash
  brew install python@3.12
  ```
- **For Linux**: Follow the instructions on the [official Python documentation](https://www.python.org/downloads/source/).

Verify the installation by running:
```bash
python3.12 --version
```

### 2. Install Required Python Packages
With Python installed, create a virtual environment and install the necessary packages.

1. **Create a virtual environment**:
   ```bash
   python3.12 -m venv venv
   ```
2. **Activate the virtual environment**:
   - **Windows**: `venv\Scripts\activate`
   - **macOS/Linux**: `source venv/bin/activate`

3. **Install dependencies** from `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

### 3. Set Up MongoDB Atlas Separately
The dataset for this project is stored on MongoDB Atlas. Follow these steps to set up your MongoDB Atlas environment:

1. **Create an Account**: Sign up at [MongoDB Atlas](https://www.mongodb.com/cloud/atlas).
2. **Create a Cluster**: Once signed in, create a cluster and configure your IP whitelist to allow connections from your local IP.
3. **Add a Database and Collection**:
   - Create a database named `Lungcancer`.
   - Inside `Lungcancer`, create a collection named `Patients`.
4. **Upload the Dataset**:
   - In the `data/processed` folder of this project, you’ll find `dataset.json`.
   - Use MongoDB Atlas’s Data Import feature to upload `dataset.json` to the `Patients` collection.

For Databricks and MongoDB Atlas Setup Guide, refer to the `setup_databricks_mongodb.md`.

### 4. Run the Project's Jupyter Notebooks and Scripts
The project contains two main folders:

- **notebooks**: This folder has Jupyter notebooks for data exploration, preprocessing, pipeline creation, and model training.
- **lung_cancer_prediction**: This folder contains Python scripts that handle different stages of the project pipeline.

#### Notebooks Execution Order:
Each notebook is numbered to indicate the recommended execution order:

1. **`1.0_abb_initial_data_exploration.ipynb`**: 
   - This notebook performs initial Exploratory Data Analysis (EDA) on the lung cancer dataset, including visualizing distributions and examining key features.
   
2. **`2.0_abb_pyspark_preprocessing.ipynb`**:
   - This notebook covers data preprocessing using PySpark. It prepares the data by handling missing values, encoding categorical variables, and performing other transformations.

3. **`3.0_hs_pipeline_analysis.ipynb`**:
   - This notebook creates and analyzes the data pipeline, preparing the data for modeling and evaluating different feature engineering techniques.

4. **`4.0_sk_preprocessing_model_training_testing.ipynb`**:
   - This notebook handles model training and evaluation using Scikit-Learn. It trains and evaluates Logistic Regression and Random Forest models on the processed dataset.

#### Python Scripts Execution Order:
After setting up MongoDB, run the Python scripts in the following order. Each script is located in the `lung_cancer_prediction` directory and performs a specific function in the pipeline:

1. **`config.py`**:
   - Stores configuration variables, such as MongoDB credentials and dataset paths, used across the project.

2. **`eda.py`**:
   - Conducts exploratory data analysis on the lung cancer dataset, including data loading from MongoDB and visualizations of key features.

3. **`pipeline.py`**:
   - Sets up a data pipeline that organizes the flow from data ingestion to processing, allowing for easy transformations and model-ready data preparation.

4. **`pyspark_processing.py`**:
   - Handles data preprocessing tasks using PySpark. This script prepares the data for model training by managing missing values, encoding categorical features, and standardizing numerical values.

5. **`model_train_test.py`**:
   - Contains code for training and testing the machine learning models. It evaluates model performance using metrics like accuracy, precision, recall, and F1-score.

### Additional Notes
Once you have followed these steps, you can proceed to experiment with different models, data transformations, and analyses. This setup should equip you with all the resources you need to replicate and explore the project locally.

Happy experimenting!
