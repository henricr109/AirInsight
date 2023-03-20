from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import json
from pydantic import BaseModel

class tester(BaseModel):
    number:int
class Samples(BaseModel):
    id:int 
    so2:int
    co:int
    mp10:int
    mp25:int
    no2:int 
    o3:int


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/samples")
async def home():
    dataSamples = open('data.json')
    return json.load(dataSamples)
def createMessage(X):
    if X == 1:
        return "Qualidade do ar boa"
    elif X == 2:
        return "Qualidade do ar moderada"
    elif X == 3:
        return "Qualidade do ar ruim"
    elif X == 4:
        return "Qualidade do ar muito ruim"
    elif X == 5:
        return "Qualidade do ar pessima"
    
def calcularPureza (mp10, mp25, o3, co, no2, so2):
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

    if o3 <= 100:
        qualidadeo3 = 1
    elif 100 < o3 <= 130:
        qualidadeo3 = 2
    elif 130 < o3 <= 160:
        qualidadeo3 = 3
    elif 160 < o3 <= 200:
        qualidadeo3 = 4
    elif  o3 > 200:
       qualidadeo3 = 5

    if co <= 9:
        qualidadeco = 1
    elif 9 < co <= 11:
        qualidadeco = 2
    elif 11 < co <= 13:
        qualidadeco = 3
    elif 13 < co <= 15:
        qualidadeco = 4
    elif  co > 15:
       qualidadeco = 5

    if no2 <= 200:
        qualidadeno2 = 1
    elif 200 < no2 <= 240:
        qualidadeno2 = 2
    elif 240 < no2 <= 320:
        qualidadeno2 = 3
    elif 320 < no2 <= 1130:
        qualidadeno2 = 4
    elif  no2 > 1130:
       qualidadeno2 = 5
    
    if so2 <= 20:
        qualidadeso2 = 1
    elif 20 < so2 <= 40:
        qualidadeso2 = 2
    elif 40 < so2 <= 365:
        qualidadeso2 = 3
    elif 365 < so2 <= 800:
        qualidadeso2 = 4
    elif  so2 > 800:
       qualidadeso2 = 5
    
    List = [qualidadeMp10, qualidadeMp25, qualidadeo3, qualidadeco,qualidadeno2,qualidadeso2]
    qualidade = 0
    for i in range(0,6):
        if List[i] > qualidade:
            qualidade = List[i]
    return qualidade
        
@app.post("/samples")
async def calcPurity(amostra:Samples):
    res = calcularPureza(amostra.mp10,amostra.mp25,amostra.o3,amostra.co,amostra.no2,amostra.so2)
    res = createMessage(res)
    return json.dumps({"mensagem":f"Resposta: {res}"})

@app.post("/teste")
def testeCalc(num:tester):
    nmr = num.number * 5
    print(nmr,"AEEEE krlhoooo")
    return nmr

