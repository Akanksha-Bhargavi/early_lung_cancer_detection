import pytest
from unittest.mock import patch, MagicMock
from scripts.utils import connect_to_mongo, load_json_data, DATA_PATH

@patch("scripts.utils.MongoClient")
def test_connect_to_mongo(mock_mongo_client):
  
    mock_client = MagicMock()  
    mock_mongo_client.return_value = mock_client

    client = connect_to_mongo()

    mock_mongo_client.assert_called_once()
    assert client == mock_client

@patch("scripts.utils.open")
@patch("scripts.utils.json.load")
def test_load_json_data(mock_json_load, mock_open):

    mock_json_load.return_value = [{"_id": 1, "name": "Test Patient"}]

    data = load_json_data(DATA_PATH)

    mock_open.assert_called_once_with(DATA_PATH, 'r')
    mock_json_load.assert_called_once()
    assert data == [{"_id": 1, "name": "Test Patient"}]
  