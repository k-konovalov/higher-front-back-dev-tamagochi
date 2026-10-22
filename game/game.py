"""Модуль с интерфейсом и реализацией класса игры"""

from abc import ABC, abstractmethod
from typing import Any
from random import choice

from .tamagochi import AbstractTamagochi, BearTamagochi
from .clicker import AbstractClicker, DummyClicker
from .models import Food, Medicine


class AbstractGame(ABC):
    """Интерфейс для логики игры"""

    @abstractmethod
    def __init__(
        self,
        tamagochi: AbstractTamagochi,
        clicker: AbstractClicker,
        all_food: list[Food],
        all_medicine: list[Medicine]
    ):
        """
        Абстрактный метод инициализации класса игры

        :param tamagochi: экземпляр тамагочи
        :param clicker: экземпляр кликера
        :param all_food: все доступные варианты еды
        :param all_medicine: все доступные варианты лекарств
        """
        raise NotImplementedError

    @abstractmethod
    def work(self) -> int:
        """
        Абстрактный метод для логики действия "работа

        :return: количество заработанных монет
        """
        raise NotImplementedError

    @abstractmethod
    def buy_food(self) -> None:
        """Абстрактный метод для покупки еды"""
        raise NotImplementedError

    @abstractmethod
    def buy_medicine(self) -> None:
        """Абстрактный метод для покупки лекарства"""
        raise NotImplementedError

    @abstractmethod
    def feed_tamagochi(self) -> None:
        """Абстрактный метод для кормления тамагочи"""
        raise NotImplementedError

    @abstractmethod
    def heal_tamagochi(self) -> None:
        """Абстрактный метод для лечения тамагочи"""
        raise NotImplementedError

    @abstractmethod
    def rest_tamagochi(self):
        """Абстрактный метод для отдыха тамагочи"""
        raise NotImplementedError

    @abstractmethod
    def play_with_tamagochi(self):
        """Абстрактный метод для игры с тамагочи"""
        raise NotImplementedError

    @abstractmethod
    def get_status(self) -> dict[str, Any]:
        """
        Абстрактный метод для получения статуса (всех характеристик) тамагочи

        :return: словарь со всеми характеристиками тамагочи
        """
        raise NotImplementedError

    @property
    @abstractmethod
    def food(self) -> list[Food]:
        """
        Абстрактное свойство для доступа к сумке с едой

        :return: список с имеющимися (купленными) объектами еды
        """
        raise NotImplementedError

    @property
    @abstractmethod
    def medicine(self) -> list[Medicine]:
        """
        Абстрактное свойство для доступа к сумке с лекарствами

        :return: список с имеющимися (купленными) объектами лекарств
        """
        raise NotImplementedError


class Game(AbstractGame):
    """Логика игры"""

    _food_bag: list[Food] = []
    _medicine_bag: list[Medicine] = []

    def __init__(
        self,
        tamagochi: BearTamagochi,
        clicker: DummyClicker,
        all_food: list[Food],
        all_medicine: list[Medicine],
    ):
        self.tamagochi = tamagochi
        self.clicker = clicker
        self.all_food = all_food
        self.all_medicine = all_medicine

    def work(self) -> int:
        self.clicker.click()
        self.tamagochi.status['coins'] += self.clicker.income_per_click
        self.tamagochi.work()
        return self.clicker.income_per_click

    def random_buy(
        self,
        from_container: list[Food | Medicine],
        to_container: list[Food | Medicine],
    ) -> None:
        chosen_one: Food | Medicine = choice(from_container)
        if (self._coins < chosen_one.price):
            to_container.append(chosen_one)
            print(
                f'Вы наугад выбрали {chosen_one.name}',
                'и вам даже хватило денег!.'
            )
        else:
            print(
                f'Вы наугад выбрали {chosen_one.name}',
                'но вам не хватило денег.',
                'Увы.'
            )

    def buy_food(self) -> None:
        self.random_buy(
            fromContainer=self.all_food,
            toContainer=self._food_bag,
        )

    def buy_medicine(self) -> None:
        self.random_buy(
            fromContainer=self.all_medicine,
            toContainer=self._medicine_bag,
        )

    def feed_tamagochi(self) -> None:
        if len(self._food_bag) == 0:
            print('Кормить нечем')
        else:
            food: Food = self._food_bag.pop()
            print(f'Вы накормили его {food.name}.')
            self.tamagochi.feed()

    def heal_tamagochi(self) -> None:
        if len(self._medicine_bag) == 0:
            print('Лечить нечем')
        else:
            self.tamagochi.heal(self._medicine_bag.pop())

    def rest_tamagochi(self):
        self.tamagochi.rest()

    def play_with_tamagochi(self):
        self.tamagochi.play()

    def get_status(self) -> dict[str, Any]:
        return self.tamagochi.status

    @property
    def food(self) -> list[Food]:
        return self.all_food.copy()

    @property
    def medicine(self) -> list[Medicine]:
        return self.all_medicine.copy()
