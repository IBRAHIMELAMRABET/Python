totalHT=0

for i in range(2):
    produit = input(f"Donnez le nome du {i + 1}er produit : ")
    quantite = float(input(f"Donnez la quantité du {i + 1}er produit: "))
    prix = float(input(f"Donnez le prix du {i + 1}er produit: "))
    print(f"total pour le produit {produit} : {prix*quantite} DH")
    totalHT+=prix*quantite
    
print(f"total pour la facture {totalHT*1.2} DH")