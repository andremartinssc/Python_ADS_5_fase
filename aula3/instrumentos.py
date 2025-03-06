from abc import ABC, abstractmethod

class InstrumentoMusical(ABC):
    @abstractmethod
    
    def tocar(self):
            pass
        
class Violao(InstrumentoMusical):
    def tocar(self):
        print("Tocou Violao")
        
class Piano(InstrumentoMusical):
    def tocar(self):
        print("Tocou Piano")
        
        
violao = Violao()
piano = Piano()

violao.tocar()
piano.tocar()