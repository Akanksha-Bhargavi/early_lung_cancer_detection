import pytest
from unittest.mock import MagicMock, patch
from scripts.pipeline import (
    peer_pressure_analysis,
    lc_gender,
    lung_cancer_chronic_disease,
    lc_smokers_chronic_disease,
)

@pytest.fixture
def mock_collection():
    """Fixture to provide a mock MongoDB collection."""
    return MagicMock()

@patch("scripts.pipeline.COLLECTION")
def test_peer_pressure_analysis(mock_collection):
    mock_collection.aggregate.return_value = [
        {"gender": "M", "peer_pressure": 1, "total": 10, "smokers": 7, "smoking_percentage": 70.0},
        {"gender": "F", "peer_pressure": 2, "total": 5, "smokers": 2, "smoking_percentage": 40.0},
    ]

    peer_pressure_analysis()

    mock_collection.aggregate.assert_called_once()
    print("\nPeer Pressure Analysis Test Passed!")

@patch("scripts.pipeline.COLLECTION")
def test_lc_gender(mock_collection):
    mock_collection.aggregate.return_value = [
        {"gender": "M", "smoking": 1, "total": 10, "lung_cancer_yes": 3, "lung_cancer_percentage": 30.0},
        {"gender": "F", "smoking": 0, "total": 8, "lung_cancer_yes": 1, "lung_cancer_percentage": 12.5},
    ]

    lc_gender()

    mock_collection.aggregate.assert_called_once()
    print("\nLung Cancer by Gender Test Passed!")

@patch("scripts.pipeline.COLLECTION")
def test_lung_cancer_chronic_disease(mock_collection):
    mock_collection.aggregate.return_value = [
        {"gender": "M", "chronic_disease": 1, "total": 15, "lung_cancer_yes": 5, "lung_cancer_no": 10, "lung_cancer_percentage": 33.33},
        {"gender": "F", "chronic_disease": 2, "total": 12, "lung_cancer_yes": 6, "lung_cancer_no": 6, "lung_cancer_percentage": 50.0},
    ]

    lung_cancer_chronic_disease()

    mock_collection.aggregate.assert_called_once()
    print("\nLung Cancer and Chronic Disease Test Passed!")

@patch("scripts.pipeline.COLLECTION")
def test_lc_smokers_chronic_disease(mock_collection):
    mock_collection.aggregate.return_value = [
        {"gender": "M", "total": 20, "lung_cancer_yes": 10, "lung_cancer_percentage": 50.0},
        {"gender": "F", "total": 15, "lung_cancer_yes": 5, "lung_cancer_percentage": 33.33},
    ]

    lc_smokers_chronic_disease()

    mock_collection.aggregate.assert_called_once()
    print("\nSmokers with Chronic Disease and Lung Cancer Test Passed!")
