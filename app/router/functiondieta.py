from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.dieta import Dieta,CreateDieta
from database.data import get_db


router =  APIRouter(prefix="/dieta", tags=["Dieta"])



@router.post("/create", response_model= CreateDieta)
def create(entrada:dict, db: Session = Depends(get_db)):
    cpf = entrada["cpf"]
    qtd_refeicoes = entrada["qtd_refeicoes"]

    try:


        nova_dieta = Dieta(
            cpf_pessoa = cpf,
            qtd_refeicoes = qtd_refeicoes
        )

        db.add(nova_dieta)
        db.commit()
        db.refresh(nova_dieta)

        return {
           "status": "Pessoa criada com sucesso"
       }
    
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Erro ao criar pessoa")
    



@router.post("/delete", response_model=CreateDieta)
def delete(entrada:dict, db: Session = Depends(get_db)):
    cpf =  entrada["cpf"] #cpf é o vinculo da dieta com a pessoa 

    dieta =  db.query(Dieta).filter(Dieta.cpf_pessoa == cpf).first()

    db.delete(dieta)
    db.commit()
    db.refresh(dieta)

    return {
        "dieta do cpf": f"{cpf} foi deletada com sucesso"
        }


#ANALISAR CODIGO, CODIGO VIA IA 
@router.post("/consultar")
def consultar(entrada: dict, db: Session = Depends(get_db)):
    try:
        cpf = entrada.get("cpf")  # .get() evita erro se a chave não existir
        if not cpf:
            return {"erro": "CPF não informado"}

        dieta = db.query(Dieta).filter(Dieta.cpf_pessoa == cpf).first()

        if not dieta:
            return {"erro": f"Nenhuma dieta encontrada para o CPF {cpf}"}

        return {
            "cpf_pessoa": dieta.cpf_pessoa,
            "qtd_refeicoes": dieta.qtd_refeicoes
        }

    except Exception as e:
        return {"erro": f"Ocorreu um erro ao consultar: {str(e)}"}