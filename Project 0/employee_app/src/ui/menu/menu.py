from abc import ABC, abstractmethod

class Menu(ABC):
    @staticmethod
    @abstractmethod
    def open():
        ...
    
    @staticmethod
    @abstractmethod
    def exit():
        ...