import pytest
import requests

class BaseFile:
    baseURL = 'http://localhost:5000/api/books'

    def getLastBook(self):
        response = requests.get(f'{self.baseURL}')
        assert response.status_code == 200
        x = response.json()
        infLastBook = ''
        for value in x.items():
            print(value[-1][-1])

    def getIdOfLastBook(self):
        response = requests.get(f'{self.baseURL}')
        assert response.status_code == 200
        x = response.json()
        infLastBook = ''
        for value in x.items():
            return value[-1][-1]['id']

    def getNameOfLastBook(self):
        response = requests.get(f'{self.baseURL}')
        assert response.status_code == 200
        x = response.json()
        infLastBook = ''
        for value in x.items():
            return value[-1][-1]['name']

    def getAuthorOfLastBook(self):
        response = requests.get(f'{self.baseURL}')
        assert response.status_code == 200
        x = response.json()
        infLastBook = ''
        for value in x.items():
            return value[-1][-1]['author']

    def getYearOfLastBook(self):
        response = requests.get(f'{self.baseURL}')
        assert response.status_code == 200
        x = response.json()
        infLastBook = ''
        for value in x.items():
            return value[-1][-1]['year']

    def getIsElectronicBookOfLastBook(self):
        response = requests.get(f'{self.baseURL}')
        assert response.status_code == 200
        x = response.json()
        infLastBook = ''
        for value in x.items():
            return value[-1][-1]['isElectronicBook']

    def deleteLastBook(self):
        response = requests.delete(f'{self.baseURL}/{self.getIdOfLastBook(self)}')
        assert response.status_code == 200