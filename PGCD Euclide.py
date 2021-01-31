def pgcd_euclide(a,b):
    """
    Renvoie le plus grand diviseur commun de a et b en utilisant la méthode
    d'Euclide
    """
    if a<b:
        a,b=b,a
    if b==0:
        return a
    else:
        return pgcd_euclide(a%b,b)

print(pgcd_euclide(30,300))