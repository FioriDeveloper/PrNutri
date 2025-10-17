from fastapi import FastAPI, APIRouter
from database.data import  Base
from app.router import functiondieta,functionpessoas



app = FastAPI()



@app.get("/")
def home ():
    return {"STATUS API 200 OK"}


app.include_router(functiondieta.router)
app.include_router(functionpessoas.router)