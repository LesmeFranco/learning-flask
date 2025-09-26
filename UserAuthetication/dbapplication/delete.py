from models import User
from app import db

User.query.delete()
db.session.commit()
print("Todos los usuarios han sido eliminados.")