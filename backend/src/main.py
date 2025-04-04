from sqlalchemy import MetaData, Table, ForeignKey, Column, Integer, String, Float, Date, LargeBinary
import logging

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

logging.basicConfig(
    filename="debug.log",
    filemode="a+",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

db_path = "data/database.db"
engine = create_engine(f"sqlite:///{db_path}", echo=True)
metadata = MetaData()

entidades_table = Table(
    "entidades",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("nombre", String),
)

empresas_table = Table(
    "empresas",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("nombre", String),
    Column("ruc", Integer),
)

consorcios_table = Table(
    "consorcios",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("nombre", String),
)

consorcios_empresas__m2m_table = Table(
    "consorcios_empresas_m2m",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("empresa_id", ForeignKey("empresas.id"), nullable=False),
    Column("consorcio_id", ForeignKey("consorcios.id"), nullable=False),
)

obras_table = Table(
    "obras",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("nombre", String),
    Column("consorcio", ForeignKey("consorcios.id")),
    Column("empresa", ForeignKey("empresas.id")),
    Column("monto", Float),
    Column("entidad", ForeignKey("entidades.id")),
    Column("fecha_contrato", Date),
    Column("fecha_recepción", Date),
)

documentos_table = Table(
    "documentos",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("nombre", String),
    Column("obra_id", ForeignKey("obras.id")),
    Column("tipo_id", ForeignKey("tipos_documento.id")),
    Column("archivo", LargeBinary),
)

tipos_documentos_table = Table(
    "tipos_documento",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("tipo", String, nullable=False)
)

metadata.create_all(engine)