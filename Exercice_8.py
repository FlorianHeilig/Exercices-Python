def moyenne(notes):
    """Calcule la moyenne des notes associée à un coefficient"""
    somme = 0
    coeffs = 0
    for elt in notes:
        note, coeff = elt
        somme += note * coeff
        coeffs +=coeff
    
    return somme/coeffs

liste = moyenne([(8, 2), (12, 1), (13.5, 3), (15, 2)])

print(liste)