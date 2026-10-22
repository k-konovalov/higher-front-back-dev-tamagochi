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
        """
        Инициализатор класса

        :param income_per_click: количество монет, зарабатываемых за один клик
        """
        self._income_per_click = income_per_click
        self._click_total = 0

    def click(self) -> None:
        """
        Метод клика для накапливания монет

        Увеличивает счётчик кликов и выводит заработок в консоль
        """
        self._click_total += 1
        print(f'Клик. Заработано {self.income_per_click * self._click_total} монет')  # noqa

    def reset(self) -> None:
        """Сбрасывает накопленное количество кликов до нуля"""
        self._click_total = 0

    @property
    def income_per_click(self) -> int:
        """
        Свойство для доступа к количеству монет за клик

        :return: количество монет, зарабатываемых за один клик
        """
        return self._income_per_click

    @property
    def get_clicks(self) -> int:
        """
        Свойство для доступа к общему количеству кликов

        :return: суммарное число выполненных кликов
        """
        return self._click_total
