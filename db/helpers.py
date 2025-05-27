from models import session

def create_record(record):
    """Add a new record to the database and commit."""
    session.add(record)
    session.commit()
    return record

def get_all(model):
    """Return all records of a given model."""
    return session.query(model).all()

def get_by_id(model, id):
    """Return a single record by ID or None if not found."""
    return session.get(model, id)

def update_record():
    """Just a placeholder to trigger session.commit() after manual changes."""
    session.commit()

def delete_by_id(model, id):
    """Delete a record by ID if it exists."""
    instance = get_by_id(model, id)
    if instance:
        session.delete(instance)
        session.commit()
        return True
    return False

def find_by_name(model, name):
    """Find records by name column (if exists)."""
    return session.query(model).filter(model.name.ilike(f"%{name}%")).all()
