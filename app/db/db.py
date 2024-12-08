from typing import Union, Set

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from app.config.config import init_config
from sqlalchemy import Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base

from app.schemas.auth import RegisterRequest
from app.schemas.users import User as UserSchema

Base = declarative_base()

cfg = init_config()['database']
DATABASE_URL = f"postgresql://{cfg['user']}:{cfg['password']}@{cfg['host']}:{cfg['port']}/{cfg['name']}"
engine = create_engine(DATABASE_URL, echo=False)
Session = sessionmaker(bind=engine)


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(64), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    roletype = Column(String(255), nullable=False, default='student')
    studygroup = Column(String(32))
    form_education = Column(String(255))
    faculty = Column(String(255))


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


def get_user_data(username: str) -> UserSchema | None:
    """
    Retrieves all information of a user by username.

    :param username: The username of the user.
    :return: A dictionary with user information if the user exists, None otherwise.
    """
    with Session() as session:
        user = session.query(User).filter_by(username=username).first()
        if user:
            return UserSchema(
                username=user.username,
                password=user.password,
                roletype=user.roletype,
                studygroup=user.studygroup,
                form_education=user.form_education,
                faculty=user.faculty
            )

        return None


def add_user(register_data: RegisterRequest) -> Union[dict, str]:
    """
    Adds a new user to the database.

    :param register_data: The data of the user to be added.
    :param username: The username of the user.
    :param password: The password of the user.
    :param studygroup: The study group of the user.
    :return: A dictionary with user information if the user is added successfully, or an error message.
    """
    new_user = User(
        username=register_data.username,
        password=register_data.password,
        roletype='student',  # Default role type
        studygroup=register_data.group_name,
        form_education='Бюджет',
        faculty='Информационные системы и технологии'  # Default faculty
    )
    with Session() as session:
        try:
            session.add(new_user)
            session.commit()
            return {
                "username": new_user.username,
                "roletype": new_user.roletype,
                "studygroup": new_user.studygroup,
                "form_education": new_user.form_education,
                "faculty": new_user.faculty
            }
        except IntegrityError:
            session.rollback()
            return "User not added"