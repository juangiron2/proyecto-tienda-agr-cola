from abc import ABC, abstractmethod

class ICrud(ABC):
    @abstractmethod
    def create(self, *args, **kwargs):
        pass

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def update(self, *args, **kwargs):
        pass

    @abstractmethod
    def delete(self, *args, **kwargs):
        pass
