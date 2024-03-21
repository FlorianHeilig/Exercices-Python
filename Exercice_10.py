def nombre_de_mots(phrase):
    mot = 0
    for i in range(len(phrase)):
        if phrase[i] in (" ", ".", "!", "?"):
            mot = mot + 1
    return mot

resultat = nombre_de_mots("Combien de mots dans cette phrase.")

print(resultat)