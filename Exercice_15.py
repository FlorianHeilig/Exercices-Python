def nb_repetitions(elt, tab):
    """Renvoie le nombre de fois ou l'élément apparaît dans le tableau"""
    conteur = 0
    for i in range(len(tab)):
        if tab[i] == elt:
            conteur += 1

    return conteur 

valeur = nb_repetitions(1, [3, 4,1, 3, 6, 8, 3]) 

print(valeur)