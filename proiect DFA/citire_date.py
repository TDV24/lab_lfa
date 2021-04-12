def citire(stringCitire):
    nr_noduri=0
    nr_tranzitii=0
    stari=[]
    input=[]
    tranzitii=[]
    stare_initiala=0
    stari_finale=[]
    lista_cuvinte=[]
    with open(stringCitire) as fis:
        linii=fis.readlines()
        for i in range(len(linii)):
            linii[i]=linii[i].replace('\n','')
        for i in range(len(linii)):
            if i==0:
                numere=linii[i].split()
                nr_noduri=int(numere[0])
                nr_tranzitii=int(numere[1])
            elif i<=nr_tranzitii+1:
                tranzitie=linii[i].split()
                if int(tranzitie[0]) not in stari:
                    stari.append(int(tranzitie[0]))
                if int(tranzitie[1]) not in stari:
                    stari.append(int(tranzitie[1]))
                if tranzitie[2] not in input:
                    input.append(tranzitie[2])
                tranzitii.append(tranzitie)
            elif i==nr_tranzitii+2:
                stare_initiala=linii[i]
            elif i==nr_tranzitii+3:
                stari_finale_1=linii[i].split()
                for x in range(1, len(stari_finale_1)):
                    stari_finale.append(int(stari_finale_1[x]))
            elif i>nr_tranzitii+4:
                lista_cuvinte.append(linii[i])
    return stari, input, tranzitii, stare_initiala, stari_finale, lista_cuvinte