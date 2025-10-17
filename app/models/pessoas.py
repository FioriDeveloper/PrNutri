from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, Column, ForeignKey,String, Float
from sqlalchemy.orm import  relationship
from pydantic import BaseModel

Base = declarative_base()




class Pessoa (Base):

    __tablename__=  "pessoas"
    #base usuarios
    
    cpf = Column(String(18), primary_key= True, index= True)
    nome = Column(String, nullable= False, index= True)
    idade = Column(Integer, nullable= False, index= True)
    peso = Column(Float, nullable= False, index= True)
    altura = Column(Float,nullable= False, index= True)
#relacionamentos


    # Esse ralcionamento ele é que uma pessoa pode ter varias dietas 
    dieta = relationship("dieta", back_populates="pessoa")
 


class CreatePessoa(BaseModel):
    cpf : str
    nome : str
    idade : int
    peso : float
    altura : float
    imc: int 



class DeletePessoa (BaseModel):
    cpf: str
