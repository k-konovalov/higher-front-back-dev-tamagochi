"""Модуль с интерфейсом и реализациями класса тамагочи."""

from abc import ABC, abstractmethod

from .constants import (
    ENERGY_LIMIT,
    HP_LIMIT,
    HUNGER_LIMIT,
    INITIAL_ENERGY,
    INITIAL_HP,
    PLAY_ENERGY_COST,
    PLAY_HUNGER_DELTA,
    REST_ENERGY_RESTORE,
    REST_ENERGY_RESTORE_SICK,
    SICK_HP_COST,
    UPDATE_ENERGY_COST,
    UPDATE_HUNGER_DELTA,
)
from .models import Food, Medicine
from .exceptions import TamagochiIsGone


class AbstractTamagochi(ABC):
    """Интерфейс логики тамагочи."""

    @abstractmethod
    def feed(self, food: Food) -> None:
        """
        Абстрактный метод для кормления тамагочи.

        :param food: объект еды для кормления
        """
        raise NotImplementedError

    @abstractmethod
    def play(self) -> None:
        """Абстрактный метод для игры с тамагочи."""
        raise NotImplementedError

    @abstractmethod
    def rest(self) -> None:
        """Абстрактный метод для отдыха тамагочи."""
        raise NotImplementedError

    @abstractmethod
    def heal(self, medicine: Medicine) -> None:
        """
        Абстрактный метод для лечения тамагочи.

        :param medicine: лекарство для лечения
        """
        raise NotImplementedError

    @property
    @abstractmethod
    def status(self) -> dict[str, int]:
        """
        Абстрактное свойство для доступа ко всем состояниям тамагочи.

        :return: словарь со всеми состояниями тамагочи
        """
        raise NotImplementedError

    @abstractmethod
    def is_alive(self) -> bool:
        """
        Абстрактный метод для проверки жив ли тамагочи.

        :return: True если жив, иначе False
        """
        raise NotImplementedError

    @abstractmethod
    def is_sick(self) -> bool:
        """
        Абстрактный метод для проверки, не заболел ли тамагочи.

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
    """Реализация тамагочи — медвежонок."""

    def __init__(self) -> None:
        """
        Инициализатор класса.

        Создаёт питомца со стандартными параметрами:
        голод=0 (сыт), энергия=INITIAL_ENERGY, здоровье=INITIAL_HP, не болен.
        """
        self.name: str = "Медведь"
        self._hp: int = INITIAL_HP
        self._energy: int = INITIAL_ENERGY
        self._hunger: int = 0
        self._sick: bool = False

    @property
    def status(self) -> dict[str, int]:
        """
        Свойство для доступа ко всем состояниям тамагочи.

        :return: словарь с ключами 'hunger', 'hp', 'energy' (int)
        """
        return {
            "hunger": self._hunger,
            "hp": self._hp,
            "energy": self._energy,
        }

    def is_alive(self) -> bool:
        """
        Проверка, жив ли тамагочи.

        :return: True если здоровье больше 0
        """
        return self._hp > 0

    def is_sick(self) -> bool:
        """
        Проверка, болен ли тамагочи.

        :return: True если тамагочи болеет
        """
        return self._sick

    @staticmethod
    def tamagochi_update(func):
        """
        Декоратор для автоматического вызова update() после действия.

        :param func: метод для обёртывания
        :return: обёрнутый метод
        """
        def wrapper(self, *args, **kwargs):
            func(self, *args, **kwargs)
            self.update()
        return wrapper

    def feed(self, food: Food) -> None:
        """
        Кормит тамагочи выбранной едой.

        Уменьшает голод на величину насыщения еды.

        :param food: объект еды для кормления
        """
        self._hunger = max(0, self._hunger - food.satiety)

    @tamagochi_update
    def play(self) -> None:
        """
        Игра с тамагочи.

        Увеличивает голод на PLAY_HUNGER_DELTA
        и уменьшает энергию на PLAY_ENERGY_COST.
        """
        self._hunger = min(HUNGER_LIMIT, self._hunger + PLAY_HUNGER_DELTA)
        self._energy = max(0, self._energy - PLAY_ENERGY_COST)

    @tamagochi_update
    def rest(self) -> None:
        """
        Отдых тамагочи.

        Восстанавливает энергию на REST_ENERGY_RESTORE
        (на REST_ENERGY_RESTORE_SICK, если болен).
        """
        restore = (
            REST_ENERGY_RESTORE_SICK
            if self._sick
            else REST_ENERGY_RESTORE
        )
        self._energy = min(ENERGY_LIMIT, self._energy + restore)

    @tamagochi_update
    def heal(self, medicine: Medicine) -> None:
        """
        Лечит тамагочи выбранной medicine.

        Применяет лекарство, восстанавливает hp,
        снимает статус болезни.

        :param medicine: лекарство для лечения
        """
        medicine.use()
        self._hp = min(HP_LIMIT, self._hp + medicine.heal_hp)
        self._sick = False

    def update(self) -> None:
        """
        Обновление состояния тамагочи (тик).

        1. голод += UPDATE_HUNGER_DELTA (макс. HUNGER_LIMIT)
        2. энергия -= UPDATE_ENERGY_COST (мин. 0)
        3. если голод==HUNGER_LIMIT или энергия==0 → болезнь
        4. если болен → здоровье -= SICK_HP_COST (мин. 0)
        """
        self._hunger = min(HUNGER_LIMIT, self._hunger + UPDATE_HUNGER_DELTA)
        self._energy = max(0, self._energy - UPDATE_ENERGY_COST)

        if self._hunger == HUNGER_LIMIT or self._energy == 0:
            self._sick = True

        if self._sick:
            self._hp = max(0, self._hp - SICK_HP_COST)

        if not self.is_alive():
            raise TamagochiIsGone("Тамагочи умер")
