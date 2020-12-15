import csv
import random
from random import randint
from tkinter import *
from word import Word
import tokens





###################################################################
#####################################DECLARACIÓN DE VARIABLES
###################################################################
csvTokenList = []
csvTokenTypeList=[]


####Esta parte no está en una def() por que siempre se va a hacer
    ##Se abre el csv
with open('Tipos.csv', 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)

##Aqui se llenan las listas que se van a usar
        for line in csv_reader:
            csvTokenList.append(line[0])
            csvTokenTypeList.append(line[1])





###################################################################
#####################################DECLARACIÓN DE FUNCIONES
###################################################################

#####################################################AQUÍ SE HACE EL TRIGGER DEL PROGRAMA
def getTextInput():
    result = textExample.get("1.0","end")
    result = result.upper()
    print(result)
    analyzetext(result)
    tokens.analyze(result)
    #print (TokenList)

###Aqui se separa cada palabra del codigo y se pone en una lista
# JK: Cambie esta funcion de split a Analyze, porque es aqui donde se hacen las llamadas a las distintas funciones, y agregue un par de cosas nuevas
def analyzetext(txt):

    wordList = txt.split()
    testarrayobj = categorize(wordList)

    printelementstokens(testarrayobj)



# JK: Modifique Categorize para que cree la lista de objetos de tipo Word
def categorize(wordList):
    words = []
    for element in wordList:
        # isnumber = element.isnumeric()
        word = tokenize(element)
        words.append(word)
    return words


# JK: Nueva funcion para crear objetos con el nuevo tipo Word.
# Se comparan con el listado de tokens que se parsea desde el CSV,
# pero seguramente podria hacerse desde el mismo word.py
def tokenize(word):

#IV: Se movió el código para primero detectar si es número
#Si es así, envía directamente la data de que el token es tipo número
    isnumber = word.isnumeric()

    if (isnumber):
        tokenized = Word(word, "NUMERO")
        return tokenized

    else:
        try:
            for token in csvTokenList:
                if (word == token):
                #print("[+] DEBUG: word=" + word + " token=" + token)
                    tokenized = Word(token, csvTokenTypeList[csvTokenList.index(token)])
                return tokenized
        except:
            tokenized = Word(word, "CADENA")
            return tokenized
            #else:
            #    print("[+] DEBUG: word=" + word + " token=" + token)
            #    tokenized = Word(token, "Non")
            #    return tokenized


# TODO: Encontrar una mejor manera de recibir feedback
def printelementstokens(words):
    print(len(words))
    for word in words:
        print ("[+] DEBUG: token=" + word.token + " lexema=" + word.lexema)





###################################################################
#####################################MAIN PROGRAM
###################################################################

root = Tk()

pane = Frame(root)
pane.pack(fill = BOTH, expand = True)

###LABEL: Aqui se declara la pantalla
label = Label(root, text="Inserte codigo")
label.pack(fill = BOTH, expand = True)

###Primer paso de la GUI
textExample = Text(root, height=10)
textExample.pack(side = TOP, expand = True, fill = BOTH)
btnRead = Button(root, height=1, width=10, text="Read", command=getTextInput)
btnRead.pack(side = TOP, expand = True, fill = BOTH)

root.mainloop()