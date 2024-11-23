import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sys_user_mgmt_svc.database import Base
from sys_user_mgmt_svc.models import User, Token

@pytest.fixture(scope='module')
def setup_test_engine():
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    session = scoped_session(Session)
    yield session
    session.remove()
    Base.metadata.drop_all(bind=engine)

def test_create_user(setup_test_engine):
    session = setup_test_engine
    user = User(email='integration_test@example.com', hashed_password='hashed_password')
    session.add(user)
    session.commit()
    session.refresh(user)
    assert user.id is not None
    assert user.email == 'integration_test@example.com'
    assert user.is_active is True


def test_create_token(setup_test_engine):
    session = setup_test_engine
    user = User(email='token_test@example.com', hashed_password='hashed_password')
    session.add(user)
    session.commit()
    session.refresh(user)

    token = Token(user_id=user.id, token='secrettoken123')
    session.add(token)
    session.commit()
    session.refresh(token)
    assert token.id is not None
    assert token.user_id == user.id
    assert token.token == 'secrettoken123'


def test_unique_email(setup_test_engine):
    session = setup_test_engine
    user1 = User(email='unique@example.com', hashed_password='password1')
    user2 = User(email='unique@example.com', hashed_password='password2')
    session.add(user1)
    session.commit()
    session.add(user2)
    with pytest.raises(Exception):
        session.commit()
    session.rollback()
