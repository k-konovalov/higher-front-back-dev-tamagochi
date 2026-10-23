"""Модуль с интерфейсом и реализацией класса игры"""

from abc import ABC, abstractmethod
from typing import Any

from .tamagochi import AbstractTamagochi
from .clicker import AbstractClicker
from .models import Food, Medicine
from .exceptions import NotEnoughMoney, TamagochiIsGone


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
        Абстрактный метод для логики действия «работа».

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
    def rest_tamagochi(self) -> None:
        """Абстрактный метод для отдыха тамагочи"""
        raise NotImplementedError

    @abstractmethod
    def play_with_tamagochi(self) -> None:
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
    """Реализация логики игры «Тамагочи»"""

    def __init__(
        self,
        tamagochi: AbstractTamagochi,
        clicker: AbstractClicker,
        all_food: list[Food],
        all_medicine: list[Medicine],
    ) -> None:
        """
        Инициализатор класса игры.

        :param tamagochi: экземпляр тамагочи
        :param clicker: экземпляр кликера
        :param all_food: все доступные варианты еды
        :param all_medicine: все доступные варианты лекарств
        """
        self.tamagochi = tamagochi
        self._clicker = clicker
        self._all_food = all_food
        self._all_medicine = all_medicine
        self._coins: int = 0
        self._food_bag: list[Food] = []
        self._medicine_bag: list[Medicine] = []

    def work(self) -> int:
        """
        Идти на работу: 5 кликов, доход = 5 * income_per_click.

        :return: количество заработанных монет
        """
        income = 5 * self._clicker.income_per_click
        for _ in range(5):
            self._clicker.click()
        self._coins += income
        return income

    def _pick(self, items: list, title: str) -> int | None:
        """
        Показать меню с нумерацией и прочитать выбор пользователя.

        :param items: список объектов для отображения в меню
        :param title: заголовок меню
        :return: индекс выбранного элемента (0-based) или None при отмене
        """
        while True:
            print(f"\n{title}:")
            for i, item in enumerate(items, 1):
                print(f"  {i}. {item}")
            choice = input("Ваш выбор: ")
            if choice == "0":
                return None
            idx = int(choice) - 1
            if idx in range(0, len(items)):
                return idx

    def buy_food(self) -> None:
        """
        Интерактивная покупка еды.

        Показывает меню доступной еды, читает выбор пользователя.
        При недостатке монет выбрасывает NotEnoughMoney.
        """
        if not self._all_food:
            print("Нет доступной еды для покупки.")
            return

        idx = self._pick(self._all_food, "Доступная еда")
        if idx is None:
            return

        food = self._all_food[idx]
        if self._coins < food.price:
            raise NotEnoughMoney(
                f"Не хватает монет: нужно {food.price}, есть {self._coins}."
            )
        self._coins -= food.price
        self._food_bag.append(food)
        print(f"Куплено: {food}")

    def buy_medicine(self) -> None:
        """
        Интерактивная покупка лекарства.

        Показывает меню доступных лекарств, читает выбор пользователя.
        При недостатке монет выбрасывает NotEnoughMoney.
        """
        if not self._all_medicine:
            print("Нет доступных лекарств для покупки.")
            return

        idx = self._pick(self._all_medicine, "Доступные лекарства")
        if idx is None:
            return

        medicine = self._all_medicine[idx]
        if self._coins < medicine.price:
            raise NotEnoughMoney(
                f"Не хватает монет: нужно {medicine.price}, есть {self._coins}."
            )
        self._coins -= medicine.price
        self._medicine_bag.append(medicine)
        print(f"Куплено: {medicine}")

    def feed_tamagochi(self) -> None:
        """
        Интерактивное кормление тамагочи.

        Показывает меню еды в сумке, читает выбор.
        Съеденный предмет удаляется из сумки.
        """
        if not self._food_bag:
            print("В сумке нет еды.")
            return

        idx = self._pick(self._food_bag, "Еда в сумке")
        if idx is None:
            return

        food = self._food_bag.pop(idx)
        self.tamagochi.feed(food)
        print(f"Питомец съел: {food}")

    def heal_tamagochi(self) -> None:
        """
        Интерактивное лечение тамагочи.

        Показывает меню лекарств в сумке, читает выбор.
        Пустые лекарства удаляются. После использования пустое лекарство
        также удаляется.
        """
        # Убираем пустые лекарства из сумки
        self._medicine_bag = [
            m for m in self._medicine_bag if not m.is_empty()
        ]

        if not self._medicine_bag:
            print("В сумке нет лекарств.")
            return

        idx = self._pick(self._medicine_bag, "Лекарства в сумке")
        if idx is None:
            return

        medicine = self._medicine_bag.pop(idx)
        self.tamagochi.heal(medicine)
        print(f"Применено: {medicine}")

        if medicine.is_empty():
            print(f"{medicine.name} закончился.")

    def rest_tamagochi(self) -> None:
        """
        Отдых тамагочи.

        Восстанавливает энергию питомца.
        """
        self.tamagochi.rest()
        print("Питомец отдохнул")

    def play_with_tamagochi(self) -> None:
        """
        Игра с тамагочи.

        Меняет состояние питомца (голод, энергия).
        """
        self.tamagochi.play()
        print("Вы поиграли с питомцем")

    def get_status(self) -> dict[str, Any]:
        """
        Получение полного статуса игры.

        :return: словарь с показателями питомца и количеством монет
        """
        status = dict(self.tamagochi.status)
        status["coins"] = self._coins
        return status

    @property
    def food(self) -> list[Food]:
        """
        Список еды в сумке.

        :return: копия списка еды
        """
        return list(self._food_bag)

    @property
    def medicine(self) -> list[Medicine]:
        """
        Список лекарств в сумке.

        :return: копия списка лекарств
        """
        return list(self._medicine_bag)
