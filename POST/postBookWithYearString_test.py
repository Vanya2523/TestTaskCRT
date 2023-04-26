import requests
from BaseFile import BaseFile

#Заполнение поля year строковым значением
def test_postBookWithYearString(BaseFile=BaseFile):
    payload = {"name": "Метро 2033", "author": "Дмитрий Глуховский", "year": "тест", "isElectronicBook": True}
    response = requests.post(f"{BaseFile.baseURL}", json=payload)
    assert response.status_code == 400