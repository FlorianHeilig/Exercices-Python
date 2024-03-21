def maximum_tableau(tab):
    nombre_max = 0
    for i in range(len(tab)):
        if tab[i] > nombre_max:
            nombre_max = tab[i]
    return nombre_max

liste = maximum_tableau([12, 3, 7, 150, 51])

print(liste)