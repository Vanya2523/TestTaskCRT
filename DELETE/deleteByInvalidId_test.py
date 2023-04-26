import requests

from BaseFile import BaseFile

#Удаление книги по несуществующему id
def test_deleteByInvalidId(BaseFile=BaseFile):
    response = requests.delete(f'{BaseFile.baseURL}/{BaseFile.getIdOfLastBook(BaseFile)+1}')
    assert response.status_code == 404
