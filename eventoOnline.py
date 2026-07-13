from evento import Evento

class EventoOnline(Evento):
    def __init__(self, nome, data, _=""):
        local = f"http://eventomaneiro.com/eventos?{EventoOnline.id}"
        Evento.__init__(self, nome, data, local)

    def imprimeInformacoes(self):
        print(f"--------------------------------")
        print(f"Nome do Evento Online: {self.nome}")
        print(f"Data: {self.data}")
        print(f"Link de acesso: {self.local}")
        print(f"ID: {self.id}")
        print(f"--------------------------------\n")

