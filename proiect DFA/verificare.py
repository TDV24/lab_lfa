import citire_date

stari, input, tranzitii, stare_initiala, stari_finale, lista_cuvinte=citire_date.citire("citire.txt")
for cuvant in lista_cuvinte:
    stare_actuala=int(stare_initiala)
    parcurgere=[]
    parcurgere.append(int(stare_actuala))
    for i in range(len(cuvant)):
        verif=0
        for tranzitie in tranzitii:
            if cuvant[i]==tranzitie[2] and stare_actuala==int(tranzitie[0]):
                stare_actuala=int(tranzitie[1])
                parcurgere.append(int(stare_actuala))
                verif=1
                if stare_actuala in stari_finale and len(cuvant)-i==1:
                    print("DA")
                    print("Traseu: ", end="")
                    print(*parcurgere)
                else:
                    break
        if verif==0:
            print("NU")
            break


