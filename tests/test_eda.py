import pytest
import pandas as pd
from pandas.testing import assert_frame_equal
from scripts.eda import (
    get_and_log_schema,
    load_and_inspect_data,
    encode_categorical,
    plot_correlation_heatmap,
    visualize_distributions,
)

@pytest.fixture
def sample_data():
    data = {
        'GENDER': ['M', 'F', 'M'],
        'AGE': [65, 45, 35],
        'SMOKING': [1, 0, 1],
        'YELLOW_FINGERS': [1, 0, 1],
        'ANXIETY': [1, 1, 0],
        'PEER_PRESSURE': [2, 1, 2],
        'CHRONIC_DISEASE': [2, 0, 1],
        'FATIGUE': [1, 1, 0],
        'ALLERGY': [2, 0, 2],
        'WHEEZING': [2, 1, 2],
        'ALCOHOL_CONSUMING': [2, 0, 1],
        'COUGHING': [2, 1, 2],
        'SHORTNESS_OF_BREATH': [2, 0, 1],
        'SWALLOWING_DIFFICULTY': [2, 1, 0],
        'CHEST_PAIN': [1, 0, 1],
        'LUNG_CANCER': ['NO', 'YES', 'NO']
    }
    return pd.DataFrame(data)


def test_get_and_log_schema(sample_data):
    result_df = get_and_log_schema(sample_data)

    expected_schema = {
        'GENDER': 'str',
        'AGE': 'int',
        'SMOKING': 'int',
        'YELLOW_FINGERS': 'int',
        'ANXIETY': 'int',
        'PEER_PRESSURE': 'int',
        'CHRONIC_DISEASE': 'int',
        'FATIGUE': 'int',
        'ALLERGY': 'int',
        'WHEEZING': 'int',
        'ALCOHOL_CONSUMING': 'int',
        'COUGHING': 'int',
        'SHORTNESS_OF_BREATH': 'int',
        'SWALLOWING_DIFFICULTY': 'int',
        'CHEST_PAIN': 'int',
        'LUNG_CANCER': 'str'
    }

    schema = {key: type(value).__name__ for key, value in sample_data.iloc[0].items()}
    assert schema == expected_schema, f"Expected {expected_schema}, but got {schema}"

    assert_frame_equal(result_df, sample_data)

def test_encode_categorical(sample_data):
    result_df = encode_categorical(sample_data.copy())

    assert result_df['GENDER'].dtype in ['int32', 'int64'], "GENDER column not encoded properly"
    assert result_df['LUNG_CANCER'].dtype in ['int32', 'int64'], "LUNG_CANCER column not encoded properly"

    expected_values = {
        'GENDER': [1, 0, 1],
        'LUNG_CANCER': [0, 1, 0]
    }
    for col, expected in expected_values.items():
        assert result_df[col].tolist() == expected, f"Expected {expected} for {col}, but got {result_df[col].tolist()}"

