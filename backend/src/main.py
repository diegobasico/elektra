from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy import select
from sqlalchemy.orm import Session

from pydantic import BaseModel
from typing import List

from orm.database import session as ses
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
    with ses.begin() as session:

        stmt = select(Consorcio)
        result = session.execute(stmt)
        consorcios = [consorcio.as_dict() for consorcio in result.scalars()]

        return consorcios


@app.get("/empresas")
async def empresas():
    with ses.begin() as session:

        stmt = select(Empresa)
        result = session.execute(stmt)
        empresas = [empresa.as_dict() for empresa in result.scalars()]

        return empresas


def map_name(ses: Session, name: str, table: Empresa | Consorcio):

    stmt = select(table).where(table.nombre == name)
    result = ses.execute(stmt).scalar().id

    return result


@app.post("/consorcios_empresas_m2m")
async def consorcios_empresas_m2m(data: Hot):
    table = data.table

    with ses.begin() as session:
        try:
            consorcios_empresas_m2m = [
                ConsorcioEmpresaM2M(
                    consorcio_id=map_name(session, row[0], Consorcio),
                    empresa_id=map_name(session, row[1], Empresa),
                    participación=row[2]
                ) for row in table if all(item is not None for item in row)
            ]
            if consorcios_empresas_m2m:
                print(consorcios_empresas_m2m)
                session.add_all(consorcios_empresas_m2m)
                session.commit()
        except Exception as e:
            session.rollback()
            raise e
