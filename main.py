"""
Module d'encodage ASCII Art basé sur un codage par tuples (caractère, occurrences).
"""

# Mandatory for the recursive solution to work on large inputs
import sys
sys.setrecursionlimit(2000)


def artcode_i(s):
    """
    Retourne la liste de tuples encodant une chaîne de caractères
    selon un algorithme itératif.

    Args:
        s (str): chaîne à encoder

    Returns:
        list: liste de tuples (caractère, occurrences)
    """
    if not s:
        return []

    caracteres = [s[0]]
    occurences = [1]

    k = 1
    longueur = len(s)

    while k < longueur:
        if s[k] == s[k - 1]:
            occurences[-1] += 1
        else:
            caracteres.append(s[k])
            occurences.append(1)
        k += 1

    return list(zip(caracteres, occurences))


def artcode_r(s):
    """
    Retourne la liste de tuples encodant une chaîne de caractères
    selon un algorithme récursif.

    Args:
        s (str): chaîne à encoder

    Returns:
        list: liste de tuples (caractère, occurrences)
    """
    if not s:
        return []
    if len(s) == 1:
        return [(s[0], 1)]

    premier = s[0]
    compteur = 1
    indice = 1
    longueur = len(s)

    while indice < longueur and s[indice] == premier:
        compteur += 1
        indice += 1

    reste = s[indice:]
    return [(premier, compteur)] + artcode_r(reste)


def main():
    """
    Fonction principale permettant de tester les fonctions d'encodage.
    """
    chaine = 'MMMMaaacXolloMM'
    print(artcode_i(chaine))
    print(artcode_r(chaine))


if __name__ == "__main__":
    main()
