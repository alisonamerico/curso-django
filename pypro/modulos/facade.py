from pypro.modulos.models import Modulo
from typing import List


def listar_modulos_ordenados() -> List[Modulo]:
    """Lista módulos ordenados por títulos
    Returns:
    """
    return list(Modulo.objects.order_by('titulo').all())


def encontrar_modulo(slug: str) -> Modulo:
    return Modulo.objects.get(slug=slug)
