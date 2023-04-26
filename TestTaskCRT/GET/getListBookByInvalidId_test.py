import pytest
import requests
from BaseFile import BaseFile

#Получение книги по несуществующему id
def test_getListBookByInvalidId(BaseFile=BaseFile):
    response = requests.get(f'{BaseFile.baseURL}{BaseFile.getIdOfLastBook(BaseFile)+1}')
    assert response.status_code == 404