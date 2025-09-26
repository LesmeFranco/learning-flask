from app import db

class Person(db.Model):
    __tablename__ = 'people'

    # Columns
    pid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    job = db.Column(db.Text)

    def __repr__(self):
        return f'Person with name {self.name} age {self.age}'