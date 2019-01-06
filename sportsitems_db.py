# configuration
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

# configuration
Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    first_name = Column(String(250), nullable=False)
    second_name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship(User)

    @property
    def serialize(self):
        return {
            "name": self.name,
            "id": self.id
        }

class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    desc = Column(String(500))
    qty = Column(Integer, nullable=False)
    cat_id = Column(Integer, ForeignKey("cat.id"))
    cat = relationship(Category)
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship(User)

    @property
    def serialize(self):
        return {
            "name": self.name,
            "id": self.id,
            "desc": self.desc,
            "qty": self.qty,
            "cat_id": self.cat_id
        }

def main():
    # configuration end of file
    #engine = create_engine('sqlite:///restaurantmenuwithusers.db')
    # for PostgreSQL
    engine = create_engine("sqllite:///sportsitems", echo=True)
    Base.metadata.create_all(engine)

class CRUD:
    def __init__(self):
        engine = create_engine("sqllite:///sportsitems", echo=True)
        Base.metadata.bind = engine
        DBsession = sessionmaker(bind=engine)
        self.session = DBsession()

    def newUser(self, login_session):
        nUser = User(name=login_session["username"],
                     email=login_session["email"])
        self.session.add(nUser)
        self.session.commit()
        user = self.session.query(User)\
               .filter_by(email=login_session["email"])\
               .one()
        return user.id

    def


if __name__ == "__main__":
    main()

