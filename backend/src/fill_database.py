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
                {"nombre": "Diego Antonio Ugaz Medina", "ruc": "10166550373"},
                {"nombre": "Ugaz & Ugaz Ingenieros", "ruc": "20561275344"}
            ]
        )

        session.execute(ins)

        ins = consorcios.insert().values(
            [
                {"nombre": "Consorcio Cemayo"},
                {"nombre": "Consorcio Complejo Deportivo"},
                {"nombre": "Consorcio Constructor/POLIFAP"},
                {"nombre": "Consorcio Constructor/Máncora"},
                {"nombre": "Consorcio Cumbre III"},
                {"nombre": "Consorcio del Norte/El Imperial"},
                {"nombre": "Consorcio del Norte/Mochumí"},
                {"nombre": "Consorcio del Norte/MMUVALL"},
                {"nombre": "Consorcio del Norte/Tecapa"},
                {"nombre": "Consorcio del Norte/Lambayeque"},
                {"nombre": "Consorcio Dos"},
                {"nombre": "Consorcio Econvisa"},
                {"nombre": "Consorcio Edifica Perú"},
                {"nombre": "Consorcio Imperial"},
                {"nombre": "Consorcio Ingeniería/Seoane"},
                {"nombre": "Consorcio Ingeniería/Mochumí"},
                {"nombre": "Consorcio Ingenieros"},
                {"nombre": "Consorcio Jaén"},
                {"nombre": "Consorcio Jotoro"},
                {"nombre": "Consorcio La Mezcladora"},
                {"nombre": "Consorcio La Unión"},
                {"nombre": "Consorcio Nimaos"},
                {"nombre": "Consorcio Nueva Arica"},
                {"nombre": "Consorcio Ejecutor Salvador"},
                {"nombre": "Consorcio San Antonio"},
                {"nombre": "Consorcio San Carlos"},
                {"nombre": "Consorcio San José/Parque"},
                {"nombre": "Consorcio San José/La Pava"},
                {"nombre": "Consorcio San Juan Masías"},
                {"nombre": "Consorcio Santa Rosa/C-8"},
                {"nombre": "Consorcio Santa Rosa/Diego Ferré"},
                {"nombre": "Consorcio Tres"},
                {"nombre": "Consorcio Uno"},
                {"nombre": "Consorcio Vial Cúneo"},
                {"nombre": "Consorcio Vial Ingeniería/Huarmey"},
                {"nombre": "Consorcio Vial Ingeniería/Túcume"},
                {"nombre": "Consorcio Vial Ingeniería/Paita"},
                {"nombre": "Consorcio Vial Tarapoto"},
                {"nombre": "Consorcio Vial Valle Hermoso"},
                {"nombre": "Consorcio Victoria/Olmos"},
                {"nombre": "Consorcio Victoria/Mochumí"},
                {"nombre": "Consorcio Virgen de Fátima"},
            ]
        )

        session.execute(ins)

        session.commit()
    except Exception as e:
        session.rollback()
        raise Exception
