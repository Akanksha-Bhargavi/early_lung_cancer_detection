import logging
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from scripts.utils import connect_to_mongo, get_data_from_mongo, close_mongo_connection


logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def get_and_log_schema(data_df):
    schema = {key: type(value).__name__ for key, value in data_df.iloc[0].items()}
    logging.info("Schema: %s", schema)
    return data_df

def load_and_inspect_data(client):
    data_df = get_data_from_mongo(client)
    logging.info("First 5 rows of data:\n%s", data_df.head())
    logging.info("Dataset Info:\n")
    data_df.info()  
    logging.info("Summary Statistics:\n%s", data_df.describe())
    return data_df

def encode_categorical(data_df):
    categorical_cols = data_df.select_dtypes(include=['object']).columns.tolist()
    label_encoders = {col: LabelEncoder().fit(data_df[col]) for col in categorical_cols}
    for col, le in label_encoders.items():
        data_df[col] = le.transform(data_df[col])
    logging.info("Label Encoding Applied to: %s", categorical_cols)
    return data_df

def plot_correlation_heatmap(data_df):
    plt.figure(figsize=(10, 8))
    sns.heatmap(data_df.corr(), annot=True, cmap='coolwarm', fmt='.2f')
    plt.title('Correlation Matrix')
    plt.show()

def visualize_distributions(data_df):
    sns.histplot(data_df['AGE'], kde=True, bins=20)
    plt.title('Age Distribution')
    plt.show()

    sns.countplot(x='SMOKING', data=data_df)
    plt.title('Smoking Status')
    plt.show()

    sns.countplot(x='LUNG_CANCER', data=data_df)
    plt.title('Lung Cancer Diagnosis')
    plt.show()

if __name__ == "__main__":
    client = connect_to_mongo()
    try:
        data_df = get_data_from_mongo(client)
        data_df = get_and_log_schema(data_df)
        data_df = load_and_inspect_data(client)
        data_df = encode_categorical(data_df)
        plot_correlation_heatmap(data_df)
        visualize_distributions(data_df)
    finally:
        close_mongo_connection(client)
