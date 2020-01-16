from project.api.models import User
from project import db


def seed_database():
    db.session.add(User(username='bernardohrl', email="bernardohrl@gmail.com", password="senha123"))
    db.session.add(User(username='henrique', email="henrique@gmail.org", password="senha123"))
    db.session.add(User(username='rosa', email="rosa@gmail.org", password="senha123"))
    db.session.add(User(username='lima', email="lima@gmail.org", password="senha123"))
    db.session.commit()
