"""Algorithme Exo09 - Distributeur

Variable    stockSoda, stockOrangeade, stockEau, choix : Entier

DEBUT
    
    stockSoda <- 3
    stockOrangeade <- 5
    stockEau <- 0

    Ecrire("Veuillez sélectionner une boisson :")
    Ecrire("1. Soda")
    Ecrire("2. Orangeade")
    Ecrire("3. Eau")
    Lire(choix)
    SELONQUE choix VAUT
        1 : SI stockSoda > 0 ALORS
                Ecrire("A votre santé, voici votre Soda!")
                stockSoda <- stockSoda - 1
            SINON
                Ecrire("Sold out! Faîtes un autre choix...")
            FINSI
        
        2 : SI stockOrangeade > 0 ALORS
                Ecrire("A votre santé, voici votre orangeade!")
                stockOrangeade <- stockOrangeade - 1
            SINON
                Ecrire("Sold out! Faîtes un autre choix...")
            FINSI
        3 :  SI stockEau > 0 ALORS
                Ecrire("A votre santé, voici votre eau!")
                stockEau <- stockEau - 1
            SINON
                Ecrire("Sold out! Faîtes un autre choix...")
            FINSI
        SINON : Ecrire("Erreur, boisson non-disponible...")
    FINSQ
    
    


FIN
"""

stockSoda = 3
stockOrangeade = 5
stockEau = 0

choix = print(input("Veuillez sélection une boisson : \n1. Soda\n2.Orangeade\n3. Eau"))
match choix:
    case "Soda":
        if stockSoda > 0:
            print("A votre santé, voici votre Soda!")
            stockSoda = stockSoda - 1
        else:
            print("Sold out! Faîtes un autre choix")
    case "Orangeande":
        if stockOrangeade > 0:
            print("A votre santé, voici votre orangeade!")
            stockOrangeade = stockOrangeade - 1
        else:
            print("Sold out! Faîtes un autre choix")
    case "Eau":
        if stockEau > 0:
            print("A votre santé, voici votre eau!")
            stockEau = stockEau - 1
        else:
            print("Sold out! Faîtes un autre choix")
    case _:
        print("Erreur, boisson non disponible...")
