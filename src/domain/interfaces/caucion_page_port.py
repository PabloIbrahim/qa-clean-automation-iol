from abc import ABC, abstractmethod

class CaucionPagePort(ABC):

    @abstractmethod
    def go_to_caucion(self):
        pass

    @abstractmethod
    def set_amount(self, amount):
        pass

    @abstractmethod
    def get_title(self):
        pass