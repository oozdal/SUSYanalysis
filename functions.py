def closest(List, Number):
        aux = []
        for valor in List:
            aux.append(abs(Number-valor))

        return aux.index(min(aux))


### neutLHC.masshh2[closest(neutLHC.masshh1,122)]
