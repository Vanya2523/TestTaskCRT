import pytest
import requests

#Вывод списка книг в консоль
def getListAllBook():
    response = requests.get('http://localhost:5000/api/books')
    assert response.status_code == 200
    print(response.json())

getListAllBook()







