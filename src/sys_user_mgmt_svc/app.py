"""
Application initialization module.

This module provides the `create_app` function, which initializes and configures the application.

Note:
- Implement the application initialization logic within the `create_app` function.
- Set up dependencies such as databases, caches, and external services.
- Configure components like middleware, routes, and error handlers as needed.
- Ensure that the returned `app` object has a `run()` method to start the application.
"""

from sys_user_mgmt_svc.config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from .database import Base
from fastapi import FastAPI


def create_app():
    # Initialize the FastAPI application instance
    app = FastAPI()

    # Set up the database engine and session
    engine = create_engine(settings.DATABASE_URL, echo=settings.DEBUG)
    SessionLocal = scoped_session(sessionmaker(bind=engine))

    # Create all tables
    Base.metadata.create_all(bind=engine)

    # Dependency to get DB session
    def get_db():
        db = SessionLocal()
        try:
            yield db
        finally:
            db.close()

    # Include routers (assuming routers are defined elsewhere)
    from .routers import user_router, token_router
    app.include_router(user_router, prefix="/users", tags=["Users"])
    app.include_router(token_router, prefix="/tokens", tags=["Tokens"])

    @app.on_event("startup")
    async def startup_event():
        # Initialize resources, e.g., connect to DB
        print("Database connected.")

    @app.on_event("shutdown")
    async def shutdown_event():
        # Close resources, e.g., disconnect from DB
        SessionLocal.remove()
        print("Database connection closed.")

    return app
