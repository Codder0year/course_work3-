from src.main import enterpretated_json


from src.main import enterpretated_json


def test_enterpretated_json():
    assert type(enterpretated_json("operation.json")) == list
    assert enterpretated_json("test_data.json") == {"test": "test"}
