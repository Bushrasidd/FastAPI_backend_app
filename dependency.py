from database import DBSession
from sqlalchemy.orm import session

def get_db():
    db = DBSession()
    try:
        yield db
    finally:
        db.close()