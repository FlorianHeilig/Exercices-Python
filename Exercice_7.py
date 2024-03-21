def delta(tab):
    """delta encoding"""
    resultat = [tab[0]]
    for i in range(1, len(tab)):
        resultat.append(tab[i] - tab[i-1])
    return resultat

liste = delta([1000, 800, 802, 1000, 1003])

print(liste)
