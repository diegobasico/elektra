from sqlalchemy import MetaData
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import Session

import logging

logging.basicConfig(
    filename="debug.log",
    filemode="a+",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

db_path = "data/database.db"
engine = create_engine(f"sqlite:///{db_path}", echo=False)
inspector = inspect(engine)
metadata = MetaData()
metadata.reflect(bind=engine)

with Session(engine) as session:
    try:
        empresas = metadata.tables["empresas"]
        consorcios = metadata.tables["consorcios"]
        entidades = metadata.tables["entidades"]
        tipos_documento = metadata.tables["tipos_documento"]

        ins = empresas.insert().values(
            [
                {"nombre": "Diego Antonio Ugaz Medina"},
                {"nombre": "Ugaz & Ugaz Ingenieros"}
            ]
        )

        session.execute(ins)

        ins = consorcios.insert().values(
            [
                {"nombre": "Consorcio Cemayo"},
                {"nombre": "Consorcio Complejo Pítipo"},
                {"nombre": "Consorcio Constructor"},
                {"nombre": "Consorcio Cumbre III"},
                {"nombre": "Consorcio del Norte"},
                {"nombre": "Consorcio Dos"},
                {"nombre": "Consorcio Econvisa"},
                {"nombre": "Consorcio Edifica Perú"},
                {"nombre": "Consorcio Imperial"},
                {"nombre": "Consorcio Ingeniería"},
                {"nombre": "Consorcio Ingenieros"},
                {"nombre": "Consorcio Jaén"},
                {"nombre": "Consorcio Jotoro"},
                {"nombre": "Consorcio La Mezcladora"},
                {"nombre": "Consorcio La Unión"},
                {"nombre": "Consorcio Nimaos"},
                {"nombre": "Consorcio Nueva Arica"},
                {"nombre": "Consorcio Salvador"},
                {"nombre": "Consorcio San Antonio"},
                {"nombre": "Consorcio San Carlos"},
                {"nombre": "Consorcio San José"},
                {"nombre": "Consorcio San José"},
                {"nombre": "Consorcio San Juan Masías"},
                {"nombre": "Consorcio Santa Rosa"},
                {"nombre": "Consorcio Tres"},
                {"nombre": "Consorcio Uno"},
                {"nombre": "Consorcio Vial Cúneo"},
                {"nombre": "Consorcio Vial Ingeniería Huarmey"},
                {"nombre": "Consorcio Vial Ingeniería Túcume"},
                {"nombre": "Consorcio Vial Ingeniería Vivienda"},
                {"nombre": "Consorcio Vial Tarapoto"},
                {"nombre": "Consorcio Vial Valle Hermoso"},
                {"nombre": "Consorcio Victoria"},
                {"nombre": "Consorcio Virgen de Fátima"},
            ]
        )

        session.commit()
    except Exception as e:
        session.rollback()
        raise Exception
