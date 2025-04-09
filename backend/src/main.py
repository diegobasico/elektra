from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:5173",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def main():
    return {"message": "Hello World"}


@app.get("/consorcios")
async def consorcios():
    data = [
        "Consorcio Cemayo",
        "Consorcio Complejo Deportivo",
        "Consorcio Constructor/POLIFAP",
        "Consorcio Constructor/Máncora",
        "Consorcio Cumbre III",
        "Consorcio del Norte/El Imperial",
        "Consorcio del Norte/Mochumí",
        "Consorcio del Norte/MMUVALL",
        "Consorcio del Norte/Tecapa",
        "Consorcio del Norte/Lambayeque",
        "Consorcio Dos",
        "Consorcio Econvisa",
        "Consorcio Edifica Perú",
        "Consorcio Imperial",
        "Consorcio Ingeniería/Seoane",
        "Consorcio Ingeniería/Mochumí",
        "Consorcio Ingenieros",
        "Consorcio Jaén",
        "Consorcio Jotoro",
        "Consorcio La Mezcladora",
        "Consorcio La Unión",
        "Consorcio Nimaos",
        "Consorcio Nueva Arica",
        "Consorcio Ejecutor Salvador",
        "Consorcio San Antonio",
        "Consorcio San Carlos",
        "Consorcio San José/Parque",
        "Consorcio San José/La Pava",
        "Consorcio San Juan Masías",
        "Consorcio Santa Rosa/C-8",
        "Consorcio Santa Rosa/Diego Ferré",
        "Consorcio Tres",
        "Consorcio Uno",
        "Consorcio Vial Cúneo",
        "Consorcio Vial Ingeniería/Huarmey",
        "Consorcio Vial Ingeniería/Túcume",
        "Consorcio Vial Ingeniería/Paita",
        "Consorcio Vial Tarapoto",
        "Consorcio Vial Valle Hermoso",
        "Consorcio Victoria/Olmos",
        "Consorcio Victoria/Mochumí",
        "Consorcio Virgen de Fátima",
    ]
    return data


@app.get("/empresas")
async def empresas():
    data = [
        "Diego Antonio Ugaz Medina",
        "Ugaz & Ugaz Ingenieros"
    ]
    return data
