"""Модуль с интерфейсом и реализацией кликера"""

from abc import ABC, abstractmethod


class AbstractClicker(ABC):
    """Интерфейс для кликера"""

    @abstractmethod
    def __init__(self) -> None:
        """Абстрактный метод инициализации"""
        raise NotImplementedError

    @abstractmethod
    def click(self) -> None:
        """Абстрактный метод клика для накапливания монет"""
        raise NotImplementedError

    @property
    @abstractmethod
    def income_per_click(self) -> int:
        """Абстрактное свойство для доступа к количеству монет за клик"""
        raise NotImplementedError


class DummyClicker(AbstractClicker):
    """Реализация кликера для заработка монет"""

    def __init__(self, income_per_click: int = 10) -> None:
        """
        Инициализатор класса.

        :param income_per_click: количество монет, зарабатываемых за один клик
        """
        self._income_per_click = income_per_click
        self._clicks: int = 0

    def click(self) -> None:
        """
        Метод клика для накапливания счётчика кликов.

        Увеличивает счётчик кликов (монеты забирает игра).
        """
        self._clicks += 1

    @property
    def income_per_click(self) -> int:
        """
        Свойство для доступа к количеству монет за клик.

        :return: количество монет, зарабатываемых за один клик
        """
        return self._income_per_click
