from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import Session
from models.pessoas import Pessoa,CreatePessoa, DeletePessoa





#Prefixo da rota, ela organiza e identifica as rotas/funções de pessoas, que são um CRUD .
router =  APIRouter("/pessoas", tags=["Pessoas"])

@router.post("/", response_model=CreatePessoa)
def create_pessoa(pessoa: CreatePessoa, db: Session = Depends(get_db)):
    
    try: 

       nova_pessoa =  Pessoa(
        cpf = pessoa.cpf,
        nome = pessoa.nome ,
        idade =  pessoa.idade,
        peso = pessoa.peso,  
        altura =  pessoa.altura 
       )

       db.add(nova_pessoa)
       db.commit()
       db.refresh(nova_pessoa)

       return {
           "status": "Pessoa criada com sucesso"
       }
    
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Erro ao criar pessoa")
    


@router.post("/", response_model= DeletePessoa)
def get_pessoa(entrada:dict, db: Session = Depends(get_db)):

    cpf =  entrada["cpf"]

    pessoa = db.query(Pessoa).filter(Pessoa.cpf == cpf ).first()


    if not pessoa:
        raise HTTPException(status_code=404, detail="Pessoa não encontrada")
    

    return pessoa
    



router.post("/deletar_user", response_model= DeletePessoa)
def delete_pessoa(entrada:dict, db: Session = Depends(get_db)):

    cpf =  entrada["cpf"]



    pessoa = db.query(Pessoa).filter(Pessoa.cpf == cpf ).first()


    if not pessoa:
        raise HTTPException(status_code=404, detail="Pessoa não encontrada")
    

    db.delete(pessoa)
    db.commit()
    db.refresh(pessoa)



    return{
        "Status": f"{cpf} Pessoa deletada com sucesso"
    }
