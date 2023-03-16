from fastapi.responses import JSONResponse
from fastapi import FastAPI
import json
from fastapi.middleware.cors import CORSMiddleware
import html2text

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
  
@app.get("/samples")
def home():
    dataSamples = open('data.json')
    return json.load(dataSamples)
    
@app.post("/getJson/<int:id>")
    def getJson(id):
    


@app.post("/air/")
async def create_air():
    from calculo_da_pureza import calcularPureza()
    air_quali = calcularPureza()
    return air_quali