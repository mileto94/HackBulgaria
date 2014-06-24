from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, String, Column
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


Base = declarative_base()


class Player(Base):
    """docstring for Game"""
    __tablename__ = "player"
    user_id = Column(Integer, primary_key=True)
    name = Column(String)

    def __str__(self):
        return "{} - {}".format(self.user_id, self.name)


class Question(Base):
    """docstring for Question"""
    __tablename__ = "question"
    q_id = Column(Integer, primary_key=True)
    question = Column(String)
    answer = Column(String)

engine = create_engine("sqlite:///math_game.db")
Base.metadata.create_all(engine)

session = Session(bind=engine, autocommit=True)

session.add_all([Question(question='6*6', answer='36'), Question(question='6+6', answer='12')])

players = session.query(Player).all()
print(players)
