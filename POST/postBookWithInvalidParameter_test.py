import requests
from BaseFile import BaseFile

#Добавление книги с несуществующим параметром
def test_postBookWithInvalidParameter(BaseFile=BaseFile):
    payload = {"name": "Метро 2033", "author": "Дмитрий Глуховский", "year": 2019, "isElectronicBook": True, "test" : "test"}
    response = requests.post(f"{BaseFile.baseURL}", json=payload)
    assert response.status_code == 201
    BaseFile.deleteLastBook(BaseFile)