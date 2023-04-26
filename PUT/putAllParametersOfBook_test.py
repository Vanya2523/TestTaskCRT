import requests
from BaseFile import BaseFile

#Обновление книги со всеми имеющимися параметрами
def test_putAllParametersBook(BaseFile=BaseFile):
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

    payload = {"name": "Капитанская дочка", "author": "Александр Пушкин", "year": 1838, "isElectronicBook": False}
    response = requests.put(f"{BaseFile.baseURL}/{BaseFile.getIdOfLastBook(BaseFile)}", json=payload)
    assert response.status_code == 200
    assert BaseFile.getNameOfLastBook(BaseFile) == 'Капитанская дочка'
    assert BaseFile.getAuthorOfLastBook(BaseFile) == 'Александр Пушкин'
    assert BaseFile.getYearOfLastBook(BaseFile) == 1838
    assert BaseFile.getIsElectronicBookOfLastBook(BaseFile) == False
    BaseFile.deleteLastBook(BaseFile)