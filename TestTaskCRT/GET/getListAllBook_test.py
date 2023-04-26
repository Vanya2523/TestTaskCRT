import requests

from BaseFile import BaseFile

#Получение списка всех книг
def test_getListAllBook():
    response = requests.get(f'{BaseFile.baseURL}')
    assert response.status_code == 200
