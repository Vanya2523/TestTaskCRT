import requests
from BaseFile import BaseFile

#Добавление книги только с параметром name
def test_postBookWithOneParameters(BaseFile=BaseFile):
    payload = {"name": "Метро 2033"}
    idOfLastBook_before = BaseFile.getIdOfLastBook(BaseFile)
    response = requests.post(f"{BaseFile.baseURL}", json=payload)
    assert response.status_code == 201
    idOfLastBook_after = BaseFile.getIdOfLastBook(BaseFile)
    assert idOfLastBook_after - idOfLastBook_before == 1
    assert BaseFile.getNameOfLastBook(BaseFile) == 'Метро 2033'
    assert BaseFile.getAuthorOfLastBook(BaseFile) == ''
    assert BaseFile.getYearOfLastBook(BaseFile) == 0
    assert BaseFile.getIsElectronicBookOfLastBook(BaseFile) == False
    BaseFile.deleteLastBook(BaseFile)