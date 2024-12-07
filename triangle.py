#longueurs des côtés d'un triangle et catégorisation en fonction

A = float(input("Quelle est la première longueur ? "))
B = float(input("Quelle est la deuxième longueur ? "))
C = float(input("Quelle est la troisième longueur ? "))

if A == B == C :
    print('Triangle équilatéral')
elif A == B or B == C or C == A :
    print('Triangle isocèle')
else :
    print('Triangle quelconque')    