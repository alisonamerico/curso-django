from pypro.modulos.models import Aula, Modulo
from typing import List


def listar_modulos_ordenados() -> List[Modulo]:
    """Lista módulos ordenados por títulos
    Returns:
    """
    return list(Modulo.objects.order_by('order').all())


def encontrar_modulo(slug: str) -> Modulo:
    return Modulo.objects.get(slug=slug)


def listar_aulas_de_modulo_ordenadas(modulo: Modulo):
    return list(modulo.aula_set.order_by('order').all())


def encontrar_aula(slug: str) -> Aula:
    return Aula.objects.select_related('modulo').get(slug=slug)
