from conecDB import Base, engine
from pessoas import Base 



Base.metadata.create_all(bind=engine)
print("Tabelas criadas com sucesso!")