from pydantic import BaseModel,ConfigDict
from database.data import Base
from sqlalchemy import Integer,Float,String, Column,relationship




class Pessoa (Base):

    __tablename__=  "pessoas"
    #base usuarios
    
    cpf = Column(Integer, primary_key= True, autoincrement= True, index= True)
    nome = Column(String, nullable= False, index= True)
    idade = Column(Integer, nullable= False, index= True)
    peso = Column(Float, nullable= False, index= True)
    altura = Column(Float,nullable= False, index= True)
#relacionamentos


    # Esse ralcionamento ele é que uma pessoa pode ter varias dietas 
    dieta = relationship("dieta", back_populates="pessoa")
 


class CreatePessoa(BaseModel):
    cpf : int 
    nome : str
    idade : int
    peso : float
    altura : float
