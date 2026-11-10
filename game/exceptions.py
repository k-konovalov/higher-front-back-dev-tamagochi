"""Модуль с исключениями."""


class TamagochiIsGone(Exception):
    """Ошибка при смерти тамагочи."""


class NotEnoughMoney(Exception):
    """Ошибка когда не хватает монет для покупки."""


class EmptyCatalog(Exception):
    """Ошибка при пустом каталоге (нет еды или лекарств для покупки)."""


class EmptyBag(Exception):
    """Ошибка при пустой сумке (нет еды или лекарств для использования)."""
