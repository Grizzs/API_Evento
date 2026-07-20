import json

class Evento:

    id = 0

    def __init__(self, nome, data, local=""):
        self.nome = nome
        self.data = data
        self.local = local
        Evento.id += 1
        self.id = Evento.id

    def toJSON(self):
        return json.dumps(self.__dict__)

    @staticmethod
    def calcula_limite_publico(area):
        if 5 <= area < 10:
            return 5 
        elif 10 <= area < 20:
            return 15
        elif area >= 20:
            return 30
        else:
            return 0
    
    def setter(self, nome=None, local=None, data=None):
        if nome is not None:
            self.nome = nome
        if data is not None:
            self.data = data
        if local is not None:
            self.local = local
