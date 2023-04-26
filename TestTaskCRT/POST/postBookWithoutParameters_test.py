import requests
from BaseFile import BaseFile

#Добавление книги без параметров
def test_postBookWithoutParameters(BaseFile=BaseFile):
    payload = {}
    response = requests.post(f"{BaseFile.baseURL}", json=payload)
    assert response.status_code == 400