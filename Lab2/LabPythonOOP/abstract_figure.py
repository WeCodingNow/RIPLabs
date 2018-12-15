from abc import ABC, abstractmethod


class Figure(ABC):
    @abstractmethod
    def surface(self):
        pass
