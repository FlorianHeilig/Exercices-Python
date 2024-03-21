def min_et_max(tab):
    Valeur_min = tab[0]
    Valeur_max = tab[0] 
    for i in range(len(tab)):
        if Valeur_max < tab[i]:
            Valeur_max = tab[i]
        if Valeur_min > tab[i]:
            Valeur_min = tab[i]
    return "min : ", Valeur_min,"max : ", Valeur_max 

liste = min_et_max([2, 4, 1, -31, 62, 8, 16])

print(liste)


        
