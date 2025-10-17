from sqlalchemy import create_engine   
from sqlalchemy.orm import sessionmaker, declarative_base


SQLALCHEMY_DATABASE_URL = "///./tabela.db"


Base =  declarative_base


engine = create_engine(SQLALCHEMY_DATABASE_URL)


#ligação com o banco vem do BIND= ENGINE(BIND significa LIGAR) o resto é mais configuraçoões ao iniciar a sessão com o db. 
SessionLocal = sessionmaker(autoflush=False, autocommit = False, bind =  engine )



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
