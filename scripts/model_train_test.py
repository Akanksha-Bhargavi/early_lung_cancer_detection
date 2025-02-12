from scripts.utils import CLIENT, DB, COLLECTION, get_data_from_mongo
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

def prepare_data():
    data_df = get_data_from_mongo(CLIENT)
    
    categorical_cols = data_df.select_dtypes(include=['object']).columns.tolist()
    label_encoders = {col: LabelEncoder().fit(data_df[col]) for col in categorical_cols}
    for col, le in label_encoders.items():
        data_df[col] = le.transform(data_df[col])

    return data_df.drop('LUNG_CANCER', axis=1), data_df['LUNG_CANCER']

def split_data(X, y):
    if len(X) < 4:
        raise ValueError("Dataset is too small to split into train, validation, and test sets.")
    
    X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.30, random_state=42)
    if len(X_temp) < 2:
        raise ValueError("Not enough samples for validation and test sets after splitting.")
    
    X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.50, random_state=42)
    return X_train, X_val, X_test, y_train, y_val, y_test


def train_logistic_regression(X_train, y_train, X_val, y_val):
    log_reg = LogisticRegression(random_state=42)
    log_reg.fit(X_train, y_train)
    y_val_pred = log_reg.predict(X_val)
    return y_val_pred, log_reg

def train_random_forest(X_train, y_train, X_val, y_val):
    rf_clf = RandomForestClassifier(random_state=42)
    rf_clf.fit(X_train, y_train)
    y_val_pred = rf_clf.predict(X_val)
    return y_val_pred, rf_clf

def evaluate_model(y_val, y_val_pred):
    return {
        'Accuracy': accuracy_score(y_val, y_val_pred),
        'Precision': precision_score(y_val, y_val_pred),
        'Recall': recall_score(y_val, y_val_pred),
        'F1-Score': f1_score(y_val, y_val_pred),
    }

def main():
    X, y = prepare_data()
    
    X_train, X_val, X_test, y_train, y_val, y_test = split_data(X, y)
    
    y_val_pred1, _ = train_logistic_regression(X_train, y_train, X_val, y_val)
    y_val_pred2, _ = train_random_forest(X_train, y_train, X_val, y_val)
    
    print("\nLogistic Regression Evaluation:")
    print(evaluate_model(y_val, y_val_pred1))
    
    print("\nRandom Forest Evaluation:")
    print(evaluate_model(y_val, y_val_pred2))

if __name__ == "__main__":
    main()
