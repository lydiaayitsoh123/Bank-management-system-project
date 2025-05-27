from models import Base, engine

def setup_db():
    Base.metadata.create_all(engine)

if __name__ == '__main__':
    setup_db()
