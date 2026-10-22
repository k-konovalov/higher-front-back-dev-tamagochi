"""Модуль с интерфейсом и реализациями класса тамагочи"""

from abc import ABC, abstractmethod

from models import Food, Medicine


class AbstractTamagochi(ABC):
    """Интерфейс логики тамагочи"""

    @abstractmethod
    def feed(self, food: Food) -> None:
        """
        Абстрактный метод для кормления тамагочи

        :param food: объект еды для кормления
        """
        raise NotImplementedError

    @abstractmethod
    def play(self) -> None:
        """Абстрактный метод для игры с тамагочи"""
        raise NotImplementedError

    @abstractmethod
    def rest(self) -> None:
        """Абстрактный метод для отдыха тамагочи"""
        raise NotImplementedError

    @abstractmethod
    def heal(self, medicine: Medicine) -> None:
        """
        Абстрактный метод для лечения тамагочи

        :param medicine: лекарство для лечения
        """
        raise NotImplementedError

    @property
    @abstractmethod
    def status(self) -> dict[str, int]:
        """
        Абстрактное свойство для доступа ко всем состояниям тамагочи

        :return: словарь со всеми состояниями тамагочи
        """
        raise NotImplementedError

    @abstractmethod
    def is_alive(self) -> bool:
        """
        Абстрактный метод для проверки жив ли тамагочи

        :return: True если жив, иначе False
        """
        raise NotImplementedError

    @abstractmethod
    def is_sick(self) -> bool:
        """
        Абстрактный метод для проверки, не заболел ли тамагочи

        :return: True если тамагочи болеет, иначе False
        """
        raise NotImplementedError

    @abstractmethod
    def update(self) -> None:
        """
        Абстрактный метод для обновления состояний тамагочи.
        Должен использоваться после каждого взаимодействия с тамагочи
        """
        raise NotImplementedError


class BearTamagochi(AbstractTamagochi):
    """Реализация тамагочи-медведя"""

    def __init__(self) -> None:
        """Инициализатор класса"""
        self._status = {
            'hunger': 100,
            'happiness': 100,
            'health': 100
        }

    @property
    def status(self) -> dict[str, int]:
        """
        Свойство для доступа ко всем состояниям тамагочи

        :return: словарь со всеми состояниями тамагочи
        """
        return self._status

    @property
    def is_alive(self) -> bool:
        """
        Метод для проверки жив ли тамагочи

        :return: True если жив, иначе False
        """
        return self.status['health'] > 0

    @property
    def is_sick(self) -> bool:
        """
        Метод для проверки, не заболел ли тамагочи

        :return: True если тамагочи болеет, иначе False
        """
        return self.status['health'] < 50

    def feed(self, food: Food) -> None:
        """
        Метод для кормления тамагочи

        :param food: объект еды для кормления
        """
        self.status['hunger'] += food.satiety

    def play(self) -> None:
        """Метод для игры с тамагочи"""
        self.status['happiness'] += 10
        self.status['hunger'] -= 10

    def rest(self) -> None:
        """Метод для отдыха тамагочи"""
        self.status['health'] += 30
        self.status['hunger'] -= 10

    def heal(self, medicine: Medicine) -> None:
        """
        Метод для лечения тамагочи

        :param medicine: лекарство для лечения
        """
        self.status['health'] += medicine.heal_hp

    def update(self) -> None:
        """
        Метод для обновления состояний тамагочи.
        Должен использоваться после каждого взаимодействия с тамагочи
        """
        raise NotImplementedError()
