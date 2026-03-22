class VisitaServicio:
    def __init__(self):
        self._visitantes = []  # Encapsulado

    def registrar(self, visitante):
        for v in self._visitantes:
            if v.cedula == visitante.cedula:
                return False
        self._visitantes.append(visitante)
        return True

    def listar(self):
        return self._visitantes

    def eliminar(self, cedula):
        for v in self._visitantes:
            if v.cedula == cedula:
                self._visitantes.remove(v)
                return True
        return False
