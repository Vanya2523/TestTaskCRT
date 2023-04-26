import requests
from BaseFile import BaseFile

#Обновление несуществующей книги
def test_putBookByInvalidId(BaseFile=BaseFile):
    payload = {"name": "Капитанская дочка", "author": "Александр Пушкин", "year": 1838,"isElectronicBook": False}
    response = requests.put(f"{BaseFile.baseURL}/{BaseFile.getIdOfLastBook(BaseFile) + 1}", json=payload)
    assert response.status_code == 404