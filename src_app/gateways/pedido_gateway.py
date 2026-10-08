from abc import ABC, abstractmethod
from typing import List
from src_app.entities.pedido import Pedido

class PedidoGateway(ABC):
    @abstractmethod
    def salvar(self, pedido: Pedido) -> None:
        pass

    @abstractmethod
    def listar(self) -> List[Pedido]:
        pass