
from sqlalchemy import Column, Integer, String, Float, Date, LargeBinary, ForeignKey
from sqlalchemy.orm import DeclarativeBase

import logging


logging.basicConfig(
    filename="debug.log",
    filemode="a+",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)


class Base(DeclarativeBase):
    pass


class Entidad(Base):
    __tablename__ = "entidades"

    id = Column(Integer, primary_key=True)
    nombre = Column(String)

    def __repr__(self) -> str:
        return f"Entidad(id={self.id!r}, nombre={self.nombre!r})"


class Empresa(Base):
    __tablename__ = "empresas"

    id = Column(Integer, primary_key=True)
    nombre = Column(String, unique=True)
    ruc = Column(Integer, unique=True)

    def __repr__(self) -> str:
        return f"Empresa(id={self.id!r}, nombre={self.nombre!r}, ruc={self.ruc!r})"

    def as_dict(self) -> dict:
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}


class Consorcio(Base):
    __tablename__ = "consorcios"

    id = Column(Integer, primary_key=True)
    nombre = Column(String, unique=True)

    def __repr__(self) -> str:
        return f"Empresa(id={self.id!r}, nombre={self.nombre!r})"

    def as_dict(self) -> dict:
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}


class ConsorcioEmpresaM2M(Base):
    __tablename__ = "consorcios_empresas_m2m"

    id = Column(Integer, primary_key=True)
    consorcio_id = Column(Integer, ForeignKey("consorcios.id"), nullable=False)
    empresa_id = Column(Integer, ForeignKey("empresas.id"), nullable=False)
    participación = Column(Float, nullable=False)

    def __repr__(self) -> str:
        return f"ConsorcioEmpresaM2M(id={self.id!r}, consorcio_id={self.consorcio_id!r}, empresa_id={self.empresa_id!r}, participación={self.participación!r})"

    def as_dict(self) -> dict:
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}


class Obra(Base):
    __tablename__ = "obras"

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    consorcio_id = Column(Integer, ForeignKey("consorcios.id"))
    empresa_id = Column(Integer, ForeignKey("empresas.id"))
    monto = Column(Float)
    entidad_id = Column(Integer, ForeignKey("entidades.id"))
    fecha_contrato = Column(Date)
    fecha_recepción = Column(Date)

    def __repr__(self) -> str:
        return f"Obra(id={self.id!r})"

    def as_dict(self) -> dict:
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}


class Documento(Base):
    __tablename__ = "documentos"

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    obra_id = Column(Integer, ForeignKey("obras.id"), nullable=False)
    tipo_id = Column(Integer, ForeignKey("tipos_documento.id"), nullable=False)
    archivo = Column(LargeBinary)

    def __repr__(self) -> str:
        return f"Documento(id={self.id!r})"

    def as_dict(self) -> dict:
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}


class TipoDocumento(Base):
    __tablename__ = "tipos_documento"

    id = Column(Integer, primary_key=True)
    tipo = Column(String, nullable=False)

    def __repr__(self) -> str:
        return f"TipoDocumento(id={self.id!r}"

    def as_dict(self) -> dict:
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}
