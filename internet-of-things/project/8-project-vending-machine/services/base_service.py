from abc import ABC, abstractmethod
from uuid import uuid4
from cores.config import Config


class BaseService(ABC):
    config: Config
    
    def __init__(self):
        self.config = Config()

    @abstractmethod
    def execute(self):
        pass

    def generate_uuid(self):
        return str(uuid4())
