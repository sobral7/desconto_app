from src.app.frameworks_database.memory_database import MemoryDatabase
from src.app.adapters.repositories.memory_pedido_repository import MemoryPedidoRepository
from src.app.use_cases.criar_pedido import CriarPedido
from src.app.adapters.controllers.pedido_controller import PedidoController

if __name__ == "__main__":
    # 1. Base de dados em memória
    database = MemoryDatabase()

    # 2. Repositório concreto (Adapter) recebendo a BD
    pedido_repository = MemoryPedidoRepository(database)

    # 3. Caso de Uso recebendo o Repositório (via interface Gateway)
    criar_pedido_use_case = CriarPedido(pedido_repository)

    # 4. Controller recebendo o Caso de Uso
    controller = PedidoController(criar_pedido_use_case)

    # 5. Execução do fluxo via Controller
    controller.criar_pedido("Cliente Normal", 100.0, "normal")
    controller.criar_pedido("Cliente VIP", 100.0, "vip")
    controller.criar_pedido("Cliente Premium", 100.0, "premium")

    # 6. Exibição dos pedidos guardados
    pedidos = controller.listar_pedidos()
    for p in pedidos:
        print(f"Cliente: {p.cliente} | Valor Original: {p.valor_original} | Valor Final: {p.valor_final()}")