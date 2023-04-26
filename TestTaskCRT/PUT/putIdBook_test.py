import requests
from BaseFile import BaseFile

#Перезапись поля id
def test_putIdBook(BaseFile=BaseFile):
    payload = {"name": "Метро 2033", "author": "Дмитрий Глуховский", "year": 2019, "isElectronicBook": True}
    response = requests.post(f"{BaseFile.baseURL}", json=payload)
    assert response.status_code == 201
    idOfLastBook_afterPost = BaseFile.getIdOfLastBook(BaseFile)
    assert BaseFile.getNameOfLastBook(BaseFile) == 'Метро 2033'
    assert BaseFile.getAuthorOfLastBook(BaseFile) == 'Дмитрий Глуховский'
    assert BaseFile.getYearOfLastBook(BaseFile) == 2019
    assert BaseFile.getIsElectronicBookOfLastBook(BaseFile) == True

    payload = {"name": "Капитанская дочка", "author": "Александр Пушкин", "year": 1838, "isElectronicBook": False, "id": f"{BaseFile.getIdOfLastBook(BaseFile) + 1}"}
    response = requests.put(f"{BaseFile.baseURL}/{BaseFile.getIdOfLastBook(BaseFile)}", json=payload)
    assert response.status_code == 200
    idOfLastBook_afterPut = BaseFile.getIdOfLastBook(BaseFile)
    assert idOfLastBook_afterPost == idOfLastBook_afterPut
    BaseFile.deleteLastBook(BaseFile)