from abc import ABC, abstractmethod
from typing import List
from src.app.entities.pedido import Pedido

class IPedidoGateway(ABC):
    @abstractmethod
    def salvar(self, pedido: Pedido) -> None:
        pass

    @abstractmethod
    def listar(self) -> List[Pedido]:
        pass