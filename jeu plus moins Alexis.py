# Créé par Alexis Chatelain, le 14/07/2018 en Python 3.4
from random import randint
import os
e=0
while e!=2:
    ok=0
    a=0
    b=0
    c=0
    d=0
    e=0
    print("____________________________________________________\n")
    print("niveau 1 nombre entre 1 et 50")
    print("niveau 2 nombre entre 1 et 100")
    print("niveau 3 nombre entre 1 et 200")
    print("niveau 4 personnalisable : entrez les bornes")
    print("____________________________________________________\n")
    while(ok!=1):
        try:
            a = int(input("quel niveau choisissez-vous? "))
        except ValueError:
            print ("\nLa valeur saisie n'est pas un niveau valide\n")
        else:
            if type(a)==int and a>0 and a<5:
                ok=1
            else:
                print ("\nLe nombre saisi n'est pas un niveau valide\n")
    if a==1:
        b=50
        L=randint(1,b)
    elif a==2: # contraction de else if
        b=100
        L=randint(1,b)
    elif a==3:
        b=200
        L=randint(1,b)
    elif a==4:
        ok=0
        print("\nvous avez choisi le niveau personnalisable")
        while(ok!=1):
            try:
                b=int(input("entrez la borne max:"))
            except ValueError:
                print ("La valeur saisie n'est pas numérique\n")
            else:
               if type(b)==int and b>0:
                   ok=1
               else:
                   print ("Le nombre saisi n'est pas une borne max valide\n")
        if b>=1000:
           print ("\nvous êtes fou, vous n'avez que ça à faire?")
        L=randint(1,b)
    print ("\nle nombre à trouver est donc entre 1 et",b,"\n")
    #print(L)
    while(c!=L):
        try:
            c=int(input("\nquel est ce nombre?\n"))
        except ValueError:
            print ("La valeur saisie n'est pas numérique\n")
        else:
            if type(c)==int and c>0 and c<b:
               if(c==L):
                   break
               elif(c>L):
                    print("c'est moins!")
                    d=d+1
               else:
                   print("c'est plus!")
                   d=d+1
            else:
                print ("Le nombre saisi n'est pas dans les bornes\n")
    print("Bravo vous avez gagné (en",d+1, "coups) !")
    print("____________________________________________________\n")
    print("1.rejouer")
    print("2.j'arrête")
    print("____________________________________________________\n")
    while(e!=1 and e!=2):
       try:
           e=int(input("\nque choisissez vous?"))
       except ValueError:
            print ("Veuillez inscrire 1 ou 2 selon votre choix")
       else:
            if e!=1 and e!=2:
                print("Veuillez inscrire 1 ou 2 selon votre choix")
            else:
                if e==1:
                    print("\nvous avez décidé de rejouer\n")
                    os.system("pause")
                    os.system("cls")
                elif e==2:
                    print("\nvous avez décidé de quitter le jeu. Au revoir et à bientôt\n")
                    os.system("pause")