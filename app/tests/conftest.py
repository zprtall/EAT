import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


from app.models.models import Base
from app.core.database import get_session

SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(bind=engine)


from fastapi.testclient import TestClient
from app.main import app


@pytest.fixture
def client(override_get_session):
    app.dependency_overrides[get_session] = override_get_session
    with TestClient(app) as c:
        yield c

@pytest.fixture(scope="function")
def db_session():
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture
def override_get_session(db_session):
    def _override():
        yield db_session

    return _override