from conecDB import  engine
from dieta import Base


Base.metadata.create_all(bind=engine)
print("Tabelas criadas com sucesso!")