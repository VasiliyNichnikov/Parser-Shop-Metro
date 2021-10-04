from abc import ABC, abstractmethod


class IParameter(ABC):
    @abstractmethod
    def get(self):
        pass
