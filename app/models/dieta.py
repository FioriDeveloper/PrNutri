from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, Column, ForeignKey ,String
from sqlalchemy.orm import  relationship

import pessoas

Base = declarative_base()

class dieta(Base):

    __tablename__=  "dieta"
    id = Column(Integer, ForeignKey("pessoas.cpf"), primary_key=True)
    qtd_refeicoes = Column(Integer, nullable= False, index= True)

    #relacionamentos
    cpf = relationship("pessoas", back_populates="dieta")
    itens =  relationship("itens", back_populates="dieta")