from src_app.frameworks_database.memory_database import MemoryDatabase
from src_app.adapters.repositories.memory_pedido_repository import MemoryPedidoRepository
from src_app.use_cases.criar_pedido import CriarPedido
from src_app.presenters.pedido_presenter import PedidoPresenter
from src_app.adapters.controllers.pedido_controller import PedidoController

if __name__ == "__main__":
    database = MemoryDatabase()
    repository = MemoryPedidoRepository(database)
    use_case = CriarPedido(repository)
    presenter = PedidoPresenter()
    controller = PedidoController(use_case, presenter)

    # Criar pedidos
    controller.criar_pedido("Cliente Normal", 100.0, "normal")
    controller.criar_pedido("Cliente VIP", 100.0, "vip")
    controller.criar_pedido("Cliente Premium", 100.0, "premium")

    # Listar pedidos formatados pelo Presenter
    pedidos = controller.listar_pedidos()
    for p in pedidos:
        print(p)