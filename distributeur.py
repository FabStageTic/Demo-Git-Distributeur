LIMITE_MAX = 3

stock = []

stock.append(3)
stock.append(0)
stock.append(0)

nom = ["Eau", "Soda", "Orangeade"]

totalstock = sum(stock)

choix = 0

while totalstock > 0 and choix != 4:
    print("Veuillez sélection une boisson :")
    for i in range(LIMITE_MAX):
        print(f"{i+i}. {nom[i]}")
    print("4. Finir")

    choix = int(input())
    
    if choix != 4 :    
        if (stock[choix-1] > 0):
            print("A votre santé, voici votre Soda!")
            stock[choix-1] = stock[choix-1] - 1
        else:
            print("Sold out! Faîtes un autre choix")
    totalstock = sum(stock)
print("Merci d'utiliser distributeur 3000!")