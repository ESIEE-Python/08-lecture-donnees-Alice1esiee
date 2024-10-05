"""Imports et définition des variables globales"""
#import random

FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    """retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 list par ligne)
    """
    l = []
    with open(filename, mode='r',encoding='utf8') as f:
        for i in f:
            new = []
            nb = ""
            for j in i.rstrip() :
                if j != ';':
                    nb += j
                elif j == ';' :
                    new.append(int(nb))
                    nb = ""
            if nb:
                new.append(int(nb))
            l.append(new)
    return l

def get_list_k(data, k):
    """Prend en argument la liste de listes 
    retournée par read_data() et un indice k et retourne la kième liste"""
    return data[k]

def get_first(l):
    """Prend en argument une liste et retourne le premier élément de cette liste"""
    return l[0]

def get_last(l):
    """Prend en argument une liste et retourne le dernier élément de cette liste"""
    return l[-1]

def get_max(l):
    """Prend en argument une liste et retourne le maximum de cette liste"""
    return max(l)

def get_min(l):
    """Prend en argument une liste et retourne le minimum de cette liste"""
    return min(l)

def get_sum(l):
    """Prend en argument une liste et retourne la somme de cette liste"""
    tot = 0
    for i in l:
        tot+= i
    return tot


#### Fonction principale


def main():
    """Affiche la liste ligne par ligne et affiche la ligne 38"""
    data = read_data(FILENAME)
    for i, l in enumerate(data):
        print(i, l)
    k = 37
    print(k, get_list_k(data, 37))



if __name__ == "__main__":
    main()
