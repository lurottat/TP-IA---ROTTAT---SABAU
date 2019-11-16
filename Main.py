import numpy as np

def DocumentQuestion(FichierQuestion): 
    Questions = FichierQuestion.readlines()
    print(Questions)    
    FichierQuestion.close()
    
def DocumentPersonnage(FichierPersonnage):
    Personnages = FichierPersonnage.readlines()
    '''[i.split('|',1)[0] for i in Personnages]
    print(Personnages)
    FichierPersonnage.close()'''
    

FichierQuestion = open("Question.txt", "r")  
DocumentQuestion(FichierQuestion)

FichierPersonnage = open("Personnage.txt", "r")  
DocumentPersonnage(FichierPersonnage)

