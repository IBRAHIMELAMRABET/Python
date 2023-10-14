x=float(input("Entrez le premier nombre : "))
y=float(input("Entrez le premier nombre : "))
opp=input("Entrez l'opperrateur : ")

while (opp!="+")and(opp!="-")and(opp!="*")and(opp!="/")and(opp!="%"):
    opp=input("Opperateur non valide !, Entrez un autre opperrateur : ")
if opp=="+":
    print(f"resultat : {x+y}")
elif opp=="-":
    print(f"resultat : {x-y}")
elif opp=="*":
    print(f"resultat : {x*y}")
elif opp=="/":
    print(f"resultat : {x/y}")
else :
    print(f"resultat : {x%y}")
