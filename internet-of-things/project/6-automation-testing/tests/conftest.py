import pytest
from cores.broker import Broker

@pytest.fixture
def setup_database():
    redis = Broker(db=9)
    yield
    redis.flush_all_data(force=True)