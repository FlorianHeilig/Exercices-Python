def verifie(tab):
    """Verifie si la liste est trié dans l'ordre croissant"""
    etat = True
    nombre = 0
    for i in range(len(tab)):
        if nombre < tab[i]:
            nombre = tab[i]
        else:
            etat = False
    return etat

liste = verifie([12, 13, 14, 15, 51])

print(liste)