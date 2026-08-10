from sqlmodel import create_engine, SQLModel

DATABASE_URL = "sqlite:///database.db"
engine = create_engine(DATABASE_URL, echo = True)

def init_db():
    SQLModel.metadata.create_all(engine)

def close_db():
    engine.dispose()