from src_app.entities.desconto import Desconto

class Pedido:
    def __init__(self, cliente: str, valor_original: float, desconto: Desconto):
        self.cliente = cliente
        self.valor_original = valor_original
        self.desconto = desconto

    def valor_desconto(self) -> float:
        return self.desconto.calcular(self.valor_original)

    def valor_final(self) -> float:
        return self.valor_original - self.valor_desconto()