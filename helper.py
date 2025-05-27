from models import session

def create_record(obj):
    session.add(obj)
    session.commit()

def get_all(model):
    return session.query(model).all()

def get_by_id(model, id):
    return session.query(model).get(int(id))

def update_record(obj):
    session.commit()

def delete_by_id(model, id):
    obj = get_by_id(model, id)
    if obj:
        session.delete(obj)
        session.commit()
        return True
    return False

def find_by_name(model, name):
    return session.query(model).filter(model.name.ilike(f"%{name}%")).all()
