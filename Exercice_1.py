def max_et_indice(tab):
    indice = 0
    valeur_max = tab[0]

    for i in range(1, len(tab)):
        if valeur_max < tab[i]:
            valeur_max = tab[i]
            indice = i
    return print("La valeur max : ", valeur_max, "Indice : ", indice)

liste = max_et_indice([1, 5, 12, 58, 12])

print(liste)