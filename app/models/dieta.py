from pydantic import BaseModel, Base
from sqlalchemy import Integer, Column, ForeignKey, relationship,String
class dieta(Base):

    __tablename__=  "dieta"
    id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    qtd_refeicoes = Column(Integer, nullable= False, index= True)

    #relacionamentos
    cpf = relationship("pessoa", back_populates="dieta")
    itens =  relationship("itens", back_populates="dieta")