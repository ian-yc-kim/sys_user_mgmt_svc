import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from alembic.config import Config
from alembic import command
from src.sys_user_mgmt_svc.database import Base
from src.sys_user_mgmt_svc.models import User, Token

@pytest.fixture(scope='module')
def test_engine():
    engine = create_engine("sqlite:///:memory:")
    connection = engine.connect()
    # Bind Alembic to the connection
    alembic_cfg = Config("/home/aiagent/ai_agents/workspace/88326da9-748f-4637-acd6-1e3ea0457987/sys_user_mgmt_svc/alembic.ini")
    alembic_cfg.attributes['connection'] = connection
    command.upgrade(alembic_cfg, "head")
    yield engine
    connection.close()

@pytest.fixture(scope='module')
def session(test_engine):
    Session = sessionmaker(bind=test_engine)
    session = Session()
    yield session
    session.close()

def test_create_user(session):
    user = User(email="test@example.com", hashed_password="hashed_pwd")
    session.add(user)
    session.commit()
    assert user.id is not None
    assert user.email == "test@example.com"
    assert user.is_active is True

def test_create_token(session):
    user = User(email="user2@example.com", hashed_password="hashed_pwd2")
    session.add(user)
    session.commit()
    token = Token(user_id=user.id, token="token123")
    session.add(token)
    session.commit()
    assert token.id is not None
    assert token.user_id == user.id
    assert token.token == "token123"

def test_unique_email(session):
    user1 = User(email="unique@example.com", hashed_password="pwd1")
    user2 = User(email="unique@example.com", hashed_password="pwd2")
    session.add(user1)
    session.commit()
    session.add(user2)
    with pytest.raises(Exception):
        session.commit()
    session.rollback()

def test_unique_token(session):
    user = User(email="tokenuser@example.com", hashed_password="pwd3")
    session.add(user)
    session.commit()
    token1 = Token(user_id=user.id, token="unique_token")
    token2 = Token(user_id=user.id, token="unique_token")
    session.add(token1)
    session.commit()
    session.add(token2)
    with pytest.raises(Exception):
        session.commit()
    session.rollback()