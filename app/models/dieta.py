from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Integer, Column, ForeignKey, String
from database.data import Base
from pydantic import BaseModel




class Dieta(Base):
    __tablename__ = "dieta"

    id = Column(Integer, primary_key=True, autoincrement=True)
    cpf_pessoa = Column(String, ForeignKey("pessoas.cpf"), nullable=False, unique = True)
    qtd_refeicoes = Column(Integer, nullable=False, index=True)

    # relacionamentos
    pessoas = relationship("Pessoa", back_populates="dieta")


class CreateDieta (BaseModel):

    cpf: str
    qtd_refeicoes: int


#USAREMOS COMO TESTE O (DICT) UM DICIONARIO EM PYTHON PARA PODER SIMPLIFICAR A ENTRADA DE DADOS.



#para deletar uma dieta vamos usar o cpf como instancia do objeto na hora de deletar 

    