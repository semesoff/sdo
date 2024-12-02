from typing import Union

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from app.config.config import init_config
from sqlalchemy import Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

cfg = init_config()['database']
DATABASE_URL = f"postgresql://{cfg['user']}:{cfg['password']}@{cfg['host']}:{cfg['port']}/{cfg['name']}"
engine = create_engine(DATABASE_URL, echo=False)
Session = sessionmaker(bind=engine)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    username = Column(String(64), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    roletype = Column(String(255), nullable=False, default='student')
    studygroup = Column(String(32))


def validate_user(username: str, password: str) -> Union[dict, bool]:
    """
    Validates the username and password of a user.

    :param username: The username of the user.
    :param password: The password of the user.
    :return: True if the username and password match, False otherwise.
    """
    with Session() as session:
        user = session.query(User).filter_by(username=username).first()
        if user and user.password == password:
            return {
                "username": user.username,
                "roletype": user.roletype,
                "studygroup": user.studygroup
            }
        return False