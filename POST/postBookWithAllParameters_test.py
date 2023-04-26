import requests
from BaseFile import BaseFile

#Добавление книги со всеми имеющимися параметрами
def test_postBookWithAllParameters(BaseFile=BaseFile):
    payload = {"name": "Метро 2033", "author": "Дмитрий Глуховский", "year": 2019, "isElectronicBook": True}
    idOfLastBook_before = BaseFile.getIdOfLastBook(BaseFile)
    response = requests.post(f"{BaseFile.baseURL}", json=payload)
    assert response.status_code == 201
    idOfLastBook_after = BaseFile.getIdOfLastBook(BaseFile)
    assert idOfLastBook_after - idOfLastBook_before == 1
    assert BaseFile.getNameOfLastBook(BaseFile) == 'Метро 2033'
    assert BaseFile.getAuthorOfLastBook(BaseFile) == 'Дмитрий Глуховский'
    assert BaseFile.getYearOfLastBook(BaseFile) == 2019
    assert BaseFile.getIsElectronicBookOfLastBook(BaseFile) == True
    BaseFile.deleteLastBook(BaseFile)