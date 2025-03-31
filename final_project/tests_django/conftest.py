# tests/conftest.py
import pytest

@pytest.fixture(autouse=True)
def enable_db_access_for_all_tests(db):
    """
    Enables database access in all tests by default.
    """
    pass
