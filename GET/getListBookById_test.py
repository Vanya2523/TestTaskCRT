import requests
from BaseFile import BaseFile

#Получение книги по id
def test_getListBookById(BaseFile=BaseFile):
    response = requests.get(f'{BaseFile.baseURL}/{BaseFile.getIdOfLastBook(BaseFile)}')
    assert response.status_code == 200