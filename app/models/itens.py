from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, Column, ForeignKey, String,Float
from sqlalchemy.orm import  relationship

Base = declarative_base()



class itens(Base):
    __tablename__ = "itens"
    
    id = Column( Integer, primary_key= True, autoincrement= True, index= True)
    calorias = Column(Float, nullable= False, index= True)
    quantidade = Column(String, nullable= False, index= True)
    descricao = Column(String, nullable= False, index= True)
    tipo = Column(String, nullable= False, index= True)


    
    #RELACIONAMENTOS
    dieta =  relationship("dieta", back_populates="itens")