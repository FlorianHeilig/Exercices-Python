def recherche(tab, n):
    """Renvoir la dernière occurrence de l'élément cherché"""
    indice = None
    for i in range(len(tab)):
        if tab[i] == n:
            indice = i
    return indice
    
resultat = recherche([1, 4, 6, 7, 9], 10)

print(resultat)