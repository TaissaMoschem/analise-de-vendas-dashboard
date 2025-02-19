from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker

# Cria conexão com SQLite
engine = create_engine('sqlite:///data/vendas.db')
Base = declarative_base()

# Define da tabela de vendas
class Venda(Base):
    __tablename__ = 'vendas'
    id = Column(Integer, primary_key=True)
    produto = Column(String, nullable=False)
    categoria = Column(String, nullable=False)
    preco = Column(Float, nullable=False)
    quantidade = Column(Integer, nullable=False)
    total = Column(Float, nullable=False)

# Cria a tabela no banco de dados
Base.metadata.create_all(engine)
print("Banco de dados criado com sucesso!")

# Insere dados fictícios
Session = sessionmaker(bind=engine)
session = Session()

vendas_exemplo = [
    Venda(produto="Notebook", categoria="Eletrônicos", preco=3500, quantidade=2, total=7000),
    Venda(produto="Mouse", categoria="Eletrônicos", preco=150, quantidade=5, total=750),
    Venda(produto="Teclado", categoria="Eletrônicos", preco=200, quantidade=3, total=600)
]

session.add_all(vendas_exemplo)
session.commit()
print("Dados inseridos no banco!")