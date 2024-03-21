def recherche_min(tab):

    valeur_maximum = tab[0] 
    index_maximum = 0  

    for i in range(1, len(tab)):
        if tab[i] > valeur_maximum: 
            valeur_maximum = tab[i] 
            index_maximum = i

    return index_maximum

tableau = [2, 8, 5, 7, 4]

valeur = recherche_min(tableau)

print(valeur)