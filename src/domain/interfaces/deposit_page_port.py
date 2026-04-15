from abc import ABC, abstractmethod

class DepositPagePort(ABC):

    @abstractmethod
    def go_to_deposit(self):
        pass

    @abstractmethod
    def get_title(self):
        pass