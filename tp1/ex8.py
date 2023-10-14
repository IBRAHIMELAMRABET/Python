
somme=0
coeff=0
for i in range(4):
    note = float(input(f"Note {i + 1} : "))
    coefficient = float(input(f"Coefficient {i + 1} : "))
    somme+=note*coefficient
    coeff+=coefficient

moyenne = somme/coeff

print(f"Moyenne de ces 4 notes : {moyenne:.2f}")

if moyenne >= 10:
    print("Semestre validé")
elif moyenne >= 7:
    print("Rattrapage")
else:
    print("Non validé")
