from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, Column, ForeignKey,String, Float
from sqlalchemy.orm import  relationship
from pydantic import BaseModel
from conecDB import Base






Base = declarative_base()

class Pessoas(Base):
    __tablename__ = "pessoas"

    cpf = Column(String(18), primary_key=True, index=True, unique = True)
    nome = Column(String, nullable=False, index=True)
    idade = Column(Integer, nullable=False, index=True)
    peso = Column(Float, nullable=False, index=True)
    altura = Column(Float, nullable=False, index=True)
    imc = Column(Float, nullable=False, index=True)

    # Uma pessoa pode ter várias dietas
    dieta = relationship("dieta", back_populates="pessoas")


class CreatePessoa(BaseModel):
    cpf : int 
    nome : str
    idade : int
    peso : float
    altura : float
    imc : int 
