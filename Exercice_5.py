def mot_a_trou(mot, mot_a_trou):
    for i in range (len(mot_a_trou)):
        if mot_a_trou[i] == "*":
            continue
        elif mot_a_trou[i] != mot[i]:
            return False
            
    return True

valeur = mot_a_trou("informatique", "info*mataq*e")

print(valeur)