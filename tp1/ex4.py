seconds=int(input("Entrez le nombre des secondes :"))

minuts=int(seconds/60)
seconds%=60
Hours=int(minuts/60)
minuts%=60

print(f"C'est : {Hours} h {minuts} min {seconds} sec")