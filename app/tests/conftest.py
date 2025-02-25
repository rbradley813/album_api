import pytest
from app import get_app

@pytest.fixture(scope="module")
def with_app():
    yield get_app()
