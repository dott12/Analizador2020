import csv
import random
from random import randint
import tkinter as tk
root = tk.Tk()
root.geometry("400x240")



###################################################################
#####################################DECLARACIÓN DE VARIABLES
###################################################################
csvTokenList = []
csvTokenTypeList=[]
globalWordList = []
wordListType = []


####Esta parte no está en una def() por que siempre se va a hacer
    ##Se abre el csv
with open('Tipos.csv', 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)

##Aqui se llenan las listas que se van a usar
        for line in csv_reader:
            csvTokenList.append(line[0])
            csvTokenTypeList.append(line[1])




###LABEL: Aqui se declara la pantalla
label = tk.Label(root, text="Inserte codigo")
label.pack()

###################################################################
#####################################DECLARACIÓN DE FUNCIONES
###################################################################




###Aqui se separa cada palabra del codigo y se pone en una lista
def splitText(txt):
    wordList = txt.split()
    print (wordList)
    categorize(wordList)
    printelementstokens()

#####################################################AQUÍ SE HACE EL TRIGGER DEL PROGRAMA
def getTextInput():
    result=textExample.get("1.0","end")
    print(result)
    splitText(result)
    ##print (TokenList)



def categorize(wordList):
    for element in wordList:
        globalWordList.append(element)
        isnumber = element.isnumeric()
        if (isnumber):
            wordListType.append("NUMERO")
        else:
            wordListType.append("Non")



def printelementstokens():

    print(len(wordListType))
    ###for i in range(len(wordListType)):

    print (globalWordList)
    print(wordListType)





###################################################################
#####################################MAIN PROGRAM
###################################################################


###Primer paso de la GUI
textExample=tk.Text(root, height=10)
textExample.pack()
btnRead=tk.Button(root, height=1, width=10, text="Read",
                    command=getTextInput)
btnRead.pack()

root.mainloop()

