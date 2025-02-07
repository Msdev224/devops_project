################################
'''SIMULER UN JEU DE DONNEES'''
###############################
import os
import random
 
 
def generationDonnees():
    nomDossier=input("Entrer le nom du dossier à créer : ")
    os.mkdir("C:/"+nomDossier)
    fichier="DataSet_DIT_2025_Patient.csv"
    os.chdir("C:/"+nomDossier)
    f=open(fichier,"w")
    code="DIT_"
    nom=['DIOP','NDIAYE','Faye','Fall','Traore','Gassama','Tall','Thiam','Sow','Sy']
    prenom=['Seydou','Moussa','Fatou','Ndeye','Jean','Robert','Papa','Kine','Fata']
    numeroDossier="Dossier_"
    pathologie="pathologie_Patient_"
    sep=";"
    for i in range(10000):
        age=random.randint(0,100)
        tension=random.randint(9,14)
        temperature=random.randint(35,37)
        sexe=random.choice(['M','F'])
        services=random.choice(['Pédiatrie','Cardiologie','Chirurgie','Neurologie'])
        patient=(code+str(i))+sep+(random.choice(nom))+sep+(random.choice(prenom))+sep+(numeroDossier+str(i))+sep+(pathologie+str(i))+sep+str(age)+sep+str(tension)+sep+str(temperature)+sep+sexe+sep+services+"\n"        
        f.write(patient)
    f.close()
generationDonnees()

 