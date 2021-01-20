from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Gamelog(Base):
    __tablename__ = 'gamelog'

    id = Column(Integer, primary_key=True)
    time = Column(DateTime)
    username = Column(String)
    action_string = Column(String)
    payload = Column(String)

    def __repr__(self):
        return ('<Gamelog('
                'id={}, time={}, username="{}", action_string="{}", payload="{}")>'
                ).format(
            self.id, self.time, self.username,
            self.action_string, self.payload)


ENGINE = create_engine('sqlite:///gamelog.db',
                       echo=False,
                       connect_args={'check_same_thread': False})
Base.metadata.create_all(ENGINE)


class GameDB():

    def __init__(self):
        self.session = sessionmaker(bind=ENGINE)()

    def add_gamelog(self, time, username, action_type, payload):
        gamelog = Gamelog(
            time=time,
            username=username,
            action_string=action_type,
            payload=payload)
        self.session.add(gamelog)
        return gamelog

    def commit(self):
        self.session.commit()