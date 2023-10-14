grade=input("saisir votre grade : ")

while (grade!="A")and(grade!="B")and(grade!="C")and(grade!="D")and(grade!="E")  :
    grade=input("La dernier grade est non valide saisir votre grade : ")
heur=float(input("saisir le nombre d’heure du travaill : "))
if grade=="A":
    print(f"Votre payement est : {(200*heur) + (1000*(heur/20))} DH")
elif grade=="B":
    print(f"Votre payement est : {(150*heur) + (800*(heur/20))} DH")
elif grade=="C":
    print(f"Votre payement est : {(120*heur) + (500*(heur/15))} DH")
elif grade=="D":
    print(f"Votre payement est : {(100*heur) + (350*(heur/15))} DH")
else:
    print(f"Votre payement est : {(80*heur) + (100*(heur/10))} DH")
