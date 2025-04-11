from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy import select

from pydantic import BaseModel
from typing import List

from orm.database import ses as Session
from orm.model import Consorcio, Empresa, ConsorcioEmpresaM2M

app = FastAPI()

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Hot(BaseModel):
    table: List[List]


@app.get("/")
async def main():
    return {"message": "Hello there"}


@app.get("/consorcios")
async def consorcios():
    with Session.begin() as session:

        stmt = select(Consorcio)
        result = session.execute(stmt)
        empresas = [consorcio.as_dict() for consorcio in result.scalars()]
        return empresas


@app.get("/empresas")
async def empresas():
    with Session.begin() as session:

        stmt = select(Empresa)
        result = session.execute(stmt)
        empresas = [empresa.as_dict() for empresa in result.scalars()]
        return empresas


@app.post("/consorcios_empresas_m2m")
async def consorcios_empresas_m2m(data: Hot):
    print(data.table)
    with Session.begin() as session:
        try:
            consorcios_empresas_m2m = [
                ConsorcioEmpresaM2M(
                    consorcio_id=index + 1,
                    empresa_id=index + 1,
                    participación=row[2]
                ) for index, row in enumerate(data.table) if row[2]
            ]
            print(consorcios_empresas_m2m)
            session.add_all(consorcios_empresas_m2m)
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
