from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from orm.model import Base, Empresa, Consorcio
from orm.data import empresas, consorcios


engine = create_engine("sqlite:///data/database.db", echo=True)
ses = sessionmaker(bind=engine, autoflush=False, autocommit=False)


def fill_database(ses: sessionmaker[Session], empresas: list, consorcios: list):
    with ses.begin() as session:
        try:
            empresas = [Empresa(**entry) for entry in empresas]
            consorcios = [Consorcio(**entry) for entry in consorcios]
            session.add_all(empresas)
            session.add_all(consorcios)
            session.commit()
        except Exception as e:
            session.rollback()
            raise e


if __name__ == "__main__":
    Base.metadata.create_all(engine)
    fill_database(ses, empresas, consorcios)
