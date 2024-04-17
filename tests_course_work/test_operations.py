import os.path
from config import ROOT_DIR
from src.main import enterpretated_json, operations_executed, operation_data, operation_date_filtre, operations_from, operations_to
File_Json = os.path.join(ROOT_DIR, "operation.json")
def test_enterpretated_json():
    assert type(enterpretated_json(File_Json)) == list


def test_operations_executed():
    # Подготовка данных для теста
    list_input = [
        {'id': 1, 'state': 'EXECUTED'},
        {'id': 2, 'state': 'PENDING'},
        {'id': 3, 'state': 'EXECUTED'},
        {'id': 4, 'state': 'PENDING'}
    ]
    result = operations_executed(list_input)
    # Проверка результата
    assert len(result) == 2  # Проверяем, что список содержит только операции со статусом 'EXECUTED'

def test_operation_data():
    # Подготовка входных данных
    operation1 = {"id": 441945886, "state": "EXECUTED", "date": "2019-08-26T10:50:58.294041"}
    operation2 = {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"}

    # Ожидаемые результаты
    expected_result1 = "26.08.2019"
    expected_result2 = "03.07.2019"

    # Проверка для первой операции
    result1 = operation_data(operation1)
    assert result1 == expected_result1, f"Для операции 1 ожидалась дата {expected_result1}, получено {result1}"

    # Проверка для второй операции
    result2 = operation_data(operation2)
    assert result2 == expected_result2


    def test_operation_date_filtre():
        # Подготовка входных данных
        list_input = [
            {"id": 1, "date": "2023-01-01T10:00:00"},
            {"id": 2, "date": "2023-01-03T10:00:00"},
            {"id": 3, "date": "2023-01-02T10:00:00"},
            {"id": 4, "date": "2023-01-05T10:00:00"},
            {"id": 5, "date": "2023-01-04T10:00:00"}
        ]

        # Ожидаемый результат после сортировки по дате
        expected_result = [
            {"id": 4, "date": "2023-01-05T10:00:00"},
            {"id": 5, "date": "2023-01-04T10:00:00"},
            {"id": 2, "date": "2023-01-03T10:00:00"},
            {"id": 3, "date": "2023-01-02T10:00:00"},
            {"id": 1, "date": "2023-01-01T10:00:00"}
        ]

        # Вызов функции для тестирования
        result = operation_date_filtre(list_input)

        # Проверка ожидаемого результата
        assert result == expected_result


def test_operations_from():
    # Тестирование когда информация об отправителе указана
    operation_with_sender = {
        "from": "Саша Шляпа 1234567890123456",
        "to": "Jane Smith 9876543210987654"
    }
    expected_result_with_sender = "СашаШляпа 1234 56 ** **** 3456"
    assert operations_from(operation_with_sender) == expected_result_with_sender

    # Тестирование когда информация об отправителе не указана
    operation_without_sender = {
        "to": "Jane Smith 9876543210987654"
    }
    expected_result_without_sender = "Инкогнито"
    assert operations_from(operation_without_sender) == expected_result_without_sender


def test_operations_to():
    operation_with_sender = {
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188"
    }
    expected_result_with_sender = "Счет: ** 4188"
    assert operations_to(operation_with_sender) == expected_result_with_sender
