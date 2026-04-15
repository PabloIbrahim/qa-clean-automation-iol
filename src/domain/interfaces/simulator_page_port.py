from abc import ABC, abstractmethod

class SimulatorPagePort(ABC):

    @abstractmethod
    def go_to_simulator(self):
        pass

    @abstractmethod
    def click_buy(self):
        pass

    @abstractmethod
    def get_title(self):
        pass