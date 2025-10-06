from fastapi import FastAPI
from database.data import  Base



app = FastAPI()



app.get("/")
def home ():
    return {"STATUS API 200 OK"}