def recherche(tab, n):
    indice = None
    for i in range(1, len(tab)):
        if tab[i] == n:
            indice = i
            break
    return indice
    
resultat = recherche([10, 5, 4, 7, 9], 12)

print(resultat)