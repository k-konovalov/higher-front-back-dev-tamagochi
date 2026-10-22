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
    """Реализация кликера-работы"""
    def __init__(self, income_per_click: int) -> None:
        """Инициализатор класса"""
        self._income_per_click = income_per_click
        self._click_total = 0

    def click(self) -> None:
        self._click_total += 1
        print(f'Клик. Заработано {self.income_per_click * self._click_total} монет')  # noqa

    def reset(self) -> None:
        self._click_total = 0

    @property
    def income_per_click(self) -> int:
        return self._income_per_click

    @property
    def get_clicks(self) -> int:
        return self._click_total
