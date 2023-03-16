from main.py import getJson(id)
for mp10, mp25, O3, CO, NO2, SO2 in (data ["mp10"]["mp25"]["O3"]["CO2"]["NO2"]["SO2"]

def calcularPureza (mp10, mp25, O3, CO, NO2, SO2):
    if mp10 <= 50:
        qualidadeMp10 = 1
    elif 50 < mp10 <= 100:
        qualidadeMp10 = 2
    elif 100 < mp10 <= 150:
        qualidadeMp10 = 3
    elif 150 < mp10 <= 250:
        qualidadeMp10 = 4
    elif  mp10 > 250:
       qualidadeMp10 = 5

    if mp25 <= 25:
        qualidadeMp25 = 1
    elif 25 < mp25 <= 50:
        qualidadeMp25 = 2
    elif 50 < mp25 <= 75:
        qualidadeMp25 = 3
    elif 75 < mp25 <= 125:
        qualidadeMp25 = 4
    elif  mp25 > 125:
       qualidadeMp25 = 5

    if O3 <= 100:
        qualidadeO3 = 1
    elif 100 < O3 <= 130:
        qualidadeO3 = 2
    elif 130 < O3 <= 160:
        qualidadeO3 = 3
    elif 160 < O3 <= 200:
        qualidadeO3 = 4
    elif O3 > 200:
       qualidadeO3 = 5

    if CO <= 9:
        qualidadeCO = 1
    elif 9 < CO <= 11:
        qualidadeCO = 2
    elif 11 < CO <= 13:
        qualidadeCO = 3
    elif 13 < CO <= 15:
        qualidadeCO = 4
    elif  CO > 15:
       qualidadeCO = 5

    if NO2 <= 200:
        qualidadeNO2 = 1
    elif 200 < NO2 <= 240:
        qualidadeNO2 = 2
    elif 240 < NO2 <= 320:
        qualidadeNO2 = 3
    elif 320 < NO2 <= 1130:
        qualidadeNO2 = 4
    elif  NO2 > 1130:
       qualidadeNO2 = 5
    
    if SO2 <= 20:
        qualidadeSO2 = 1
    elif 20 < SO2 <= 40:
        qualidadeSO2 = 2
    elif 40 < SO2 <= 365:
        qualidadeSO2 = 3
    elif 365 < SO2 <= 800:
        qualidadeSO2 = 4
    elif  SO2 > 800:
       qualidadeSO2 = 5
    
    List = [qualidadeMp10, qualidade.Mp25, qualidadeO3, qualidadeCO,qualidadeNO2,qualidadeSO2]
    qualidade = 0
    for i in range(0,6):
        if List[i] > qualidade:
            qualidade = List[i]
    return qualidade
