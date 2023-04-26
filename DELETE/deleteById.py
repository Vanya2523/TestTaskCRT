from BaseFile import BaseFile

#Удаление последнего элемента в списке книг
def test_deleteById(BaseFile=BaseFile):
    BaseFile.deleteLastBook(BaseFile)
