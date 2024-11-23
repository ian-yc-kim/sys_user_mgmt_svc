import os
import unittest
from sqlalchemy.exc import IntegrityError
from sqlalchemy import text

os.environ['ENVIRONMENT'] = 'testing'

from sys_user_mgmt_svc.database import Base, engine, SessionLocal
from sys_user_mgmt_svc.models import User, Token

class TestDatabaseIntegration(unittest.TestCase):

    def setUp(self):
        Base.metadata.create_all(bind=engine)
        self.db = SessionLocal()

    def tearDown(self):
        self.db.close()
        Base.metadata.drop_all(bind=engine)

    def test_db_connection(self):
        try:
            self.db.execute(text('SELECT 1'))
        except Exception as e:
            self.fail(f"Database connection failed: {e}")

    def test_create_user(self):
        user = User(email='test@example.com', hashed_password='hashedpassword')
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        self.assertIsNotNone(user.id)
        self.assertEqual(user.email, 'test@example.com')

    def test_create_token(self):
        user = User(email='tokenuser@example.com', hashed_password='hashedpassword')
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)

        token = Token(user_id=user.id, token='secrettoken')
        self.db.add(token)
        self.db.commit()
        self.db.refresh(token)
        self.assertIsNotNone(token.id)
        self.assertEqual(token.user_id, user.id)
        self.assertEqual(token.token, 'secrettoken')

    def test_unique_email(self):
        user1 = User(email='unique@example.com', hashed_password='pass1')
        user2 = User(email='unique@example.com', hashed_password='pass2')
        self.db.add(user1)
        self.db.commit()

        self.db.add(user2)
        with self.assertRaises(IntegrityError):
            self.db.commit()
        self.db.rollback()

if __name__ == '__main__':
    unittest.main()
