import os
import sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from models import Base, engine

def setup_db():
    Base.metadata.create_all(engine)
    print("✅ Database and tables created.")

if __name__ == "__main__":
    setup_db()