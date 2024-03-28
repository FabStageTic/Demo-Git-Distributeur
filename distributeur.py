"""Algorithme Distributeur de boissons

Variable stock1, stock2, stock3, choix : Entier

DEBUT
    stock1 <- 0
    stock2 <- 2
    stock3 <- 3
    FAIRE
        Ecrire("Choisissez une boisson. Boisson1: 1, Boisson2: 2, Boisson3: 3, FINIR : 4")
        Lire(choix)
        SI choix == 1 ALORS
            SI stock1 > 0 ALORS
                Ecrire("Voici votre boisson1 , santé!")
                stock1 <- stock1 - 1
            SINON
                Ecrire("Plus de boisson1")
            FINSI
        SINONSI choix == 2 ALORS
            SI stock2 > 0 ALORS
                Ecrire("Voici votre boisson2 , santé!")
                stock2 <- stock2 - 1
            SINON
                Ecrire("Plus de boisson2")
            FINSI
        SINONSI choix == 3 ALORS
            SI stock3 > 0 ALORS
                Ecrire("Voici votre boisson3 , santé!")
                stock3 <- stock3 - 1
            SINON
                Ecrire("Plus de boisson3")
            FINSI
        FINSI        
    TANTQUE ((stock1 + stock 2 + stock 3) > 0) ET (choix != 4) FINTQ
    Ecrire("Merci d'utiliser distributeur 3000!")
FIN
"""

stockSoda = 3
stockOrangeade = 5
stockEau = 0

choix = 0

while (stockSoda + stockOrangeade + stockEau) > 0 and choix != 4:
    choix = print(int(input("Veuillez sélection une boisson : \n1. Soda\n2.Orangeade\n3. Eau\n 4. Finir")))
    match choix:
        case 1:
            if stockSoda > 0:
                print("A votre santé, voici votre Soda!")
                stockSoda = stockSoda - 1
            else:
                print("Sold out! Faîtes un autre choix")
        case 2:
            if stockOrangeade > 0:
                print("A votre santé, voici votre orangeade!")
                stockOrangeade = stockOrangeade - 1
            else:
                print("Sold out! Faîtes un autre choix")
        case 3:
            if stockEau > 0:
                print("A votre santé, voici votre eau!")
                stockEau = stockEau - 1
            else:
                print("Sold out! Faîtes un autre choix")
        case 4:
            print("Merci d'utiliser distributeur 3000!")
        case _:
            print("Erreur, boisson non disponible...")
