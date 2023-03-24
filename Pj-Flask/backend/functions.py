indice = []
# samples ordem [co, so2, no2, o3, mp25, mp10]
samples =[[9,11,13,15],[20,40,365,800],[200,240,320,1130],[100,130,160,200],[25,50,75,125],[50,100,150,250]]

def calcSamples(amostra,comparar1,comparar2,comparar3,comparar4):
    null =''
    try:
        if amostra==null:
            amostra=0
            indice.append(1)
        elif amostra>=0 and amostra <= comparar1:
            indice.append(1)
        elif comparar1 < amostra <= comparar2:
            indice.append(2)
        elif comparar2 < amostra <= comparar3:
            indice.append(3)
        elif comparar3 < amostra <= comparar4:
            indice.append(4)
        elif  amostra > comparar4:
            indice.append(5)
        return amostra
    except:
        print("Erro na função calcSamples")
    
def calcularPureza (co,so2,no2,o3,mp25,mp10):
    co = calcSamples(co,samples[0][0],samples[0][1],samples[0][2],samples[0][3])
    so2 = calcSamples(so2,samples[1][0],samples[1][1],samples[1][2],samples[1][3])
    no2 = calcSamples(no2,samples[2][0],samples[2][1],samples[2][2],samples[2][3])
    o3 = calcSamples(o3,samples[3][0],samples[3][1],samples[3][2],samples[3][3])
    mp25 = calcSamples(mp25,samples[4][0],samples[4][1],samples[4][2],samples[4][3])
    mp10 = calcSamples(mp10,samples[5][0],samples[5][1],samples[5][2],samples[5][3])
    nbmr = max(indice)
    return nbmr
