import os
from googletrans import Translator

def readfile():
    file = open("C:/Users/lab7-12/Desktop/movie.txt", "r")
    check = (file.read())
    return check



word = readfile()
translator = Translator()
translateword = translator.translate(word, dest="hi")
print(translateword)
