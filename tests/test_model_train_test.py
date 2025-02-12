import pytest
import json
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from scripts.model_train_test import (
    split_data,
    train_logistic_regression,
    train_random_forest,
    evaluate_model,
)

@pytest.fixture(scope="module")
def dataset():
    with open("../data/dataset.json") as f:
        data = json.load(f)
    return pd.DataFrame(data)

@pytest.fixture(params=[
    lambda df: df.head(3), 
    lambda df: df.head(4), 
])
def sample_data(request, dataset):
    return request.param(dataset)

@pytest.fixture
def prepared_data(sample_data):
    data_df = sample_data.copy()

    categorical_cols = data_df.select_dtypes(include=["object"]).columns.tolist()
    label_encoders = {col: LabelEncoder().fit(data_df[col]) for col in categorical_cols}
    for col, le in label_encoders.items():
        data_df[col] = le.transform(data_df[col])

    X = data_df.drop("LUNG_CANCER", axis=1)
    y = data_df["LUNG_CANCER"]

    return X, y


def test_split_data(prepared_data, sample_data):
    X, y = prepared_data

    if len(sample_data) < 4:        
        with pytest.raises(ValueError, match="Dataset is too small to split"):
            split_data(X, y)
    else:       
        X_train, X_val, X_test, y_train, y_val, y_test = split_data(X, y)

        assert len(X_train) > 0, "Training set should not be empty"
        assert len(X_val) > 0, "Validation set should not be empty"
        assert len(X_test) > 0, "Test set should not be empty"


def test_train_logistic_regression(prepared_data, sample_data):
    X, y = prepared_data

    if len(sample_data) < 4:        
        with pytest.raises(ValueError, match="Dataset is too small to split"):
            split_data(X, y)
    else:
        X_train, X_val, _, y_train, y_val, _ = split_data(X, y)
        y_val_pred, model = train_logistic_regression(X_train, y_train, X_val, y_val)

        assert len(y_val_pred) == len(y_val), "Predictions should match validation set size"
        assert isinstance(model, LogisticRegression), "Model should be LogisticRegression"


def test_train_random_forest(prepared_data, sample_data):
    X, y = prepared_data

    if len(sample_data) < 4:      
        with pytest.raises(ValueError, match="Dataset is too small to split"):
            split_data(X, y)
    else:
        X_train, X_val, _, y_train, y_val, _ = split_data(X, y)
        y_val_pred, model = train_random_forest(X_train, y_train, X_val, y_val)

        assert len(y_val_pred) == len(y_val), "Predictions should match validation set size"
        assert isinstance(model, RandomForestClassifier), "Model should be RandomForestClassifier"

def test_evaluate_model():
    y_true = [1, 0, 1]
    y_pred = [1, 0, 0]
       
    metrics = evaluate_model(y_true, y_pred)

    assert set(metrics.keys()) == {"Accuracy", "Precision", "Recall", "F1-Score"}, "All metrics should be calculated"
    assert metrics["Accuracy"] == 2 / 3, "Accuracy should be 2/3"
    assert metrics["Precision"] == 1.0, "Precision should be 1.0"
    assert metrics["Recall"] == 0.5, "Recall should be 0.5"
    assert metrics["F1-Score"] == pytest.approx(2 / 3, rel=1e-2), "F1-Score should be approximately 2/3"
