import os
from urllib.request import urlopen
def read_file():
    #changing the working directory
    cwd=os.chdir("C:\\Users\\lab7-12\\Desktop")
    #print(cwd)
    #open file
    quotes=open(os.getcwd()+"\movie.txt")
    #read file
    contents_file=quotes.read()
    print(contents_file)
    check_bad_word(contents_file)

def check_bad_word(words_to_check):
    response=urlopen('http:\\www.wdylike.appspot.com/?q='+"words_to_check")
    output=response.read()
    print(output)

read_file()


