from pydantic import BaseModel , Base
from sqlalchemy import Integer , Column, ForeignKey, relationship,String, Float



class itens(Base):
    id = Column( Integer, primary_key= True, autoincrement= True, index= True)
    calorias = Column(Float, nullable= False, index= True)
    quantidade = Column(String, nullable= False, index= True)
    descricao = Column(String, nullable= False, index= True)
    tipo = Column(String, nullable= False, index= True)


    
    #RELACIONAMENTOS
    dieta =  relationship("dieta", back_populates="itens")