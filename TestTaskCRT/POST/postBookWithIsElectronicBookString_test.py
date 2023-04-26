import requests
from BaseFile import BaseFile

#Заполнение поля isElectronicBook строковым значением
def test_postBookWithYearString(BaseFile=BaseFile):
    payload = {"name": "Метро 2033", "author": "Дмитрий Глуховский", "year": 2019, "isElectronicBook": "тест"}
    response = requests.post(f"{BaseFile.baseURL}", json=payload)
    assert response.status_code == 400
