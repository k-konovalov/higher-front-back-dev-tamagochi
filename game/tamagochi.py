"""Модуль с интерфейсом и реализациями класса тамагочи"""

from abc import ABC, abstractmethod

from .models import Food, Medicine
from .exceptions import TamagochiIsGone


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
    """Реализация тамагочи — медвежонок"""

    def __init__(self) -> None:
        """
        Инициализатор класса.

        Создаёт питомца со стандартными параметрами:
        голод=0 (сыт), энергия=100, здоровье=100, не болен.
        """
        self.name: str = "Медведь"
        self._hp: int = 100
        self._energy: int = 100
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

        Увеличивает голод на 5 и уменьшает энергию на 10.
        """
        self._hunger = min(100, self._hunger + 5)
        self._energy = max(0, self._energy - 10)

    @tamagochi_update
    def rest(self) -> None:
        """
        Отдых тамагочи.

        Восстанавливает энергию на 30 (на 15, если болен).
        """
        restore = 15 if self._sick else 30
        self._energy = min(100, self._energy + restore)

    @tamagochi_update
    def heal(self, medicine: Medicine) -> None:
        """
        Лечит тамагочи выбранной medicine.

        Увеличивает uses лекарства на 1, восстанавливает hp,
        снимает статус болезни.

        :param medicine: лекарство для лечения
        """
        medicine.uses += 1
        self._hp = min(100, self._hp + medicine.heal_hp)
        self._sick = False

    def update(self) -> None:
        """
        Обновление состояния тамагочи (тик).

        1. голод += 2 (макс. 100)
        2. энергия -= 1 (мин. 0)
        3. если голод==100 или энергия==0 → болезнь
        4. если болен → здоровье -= 5 (мин. 0)
        """
        self._hunger = min(100, self._hunger + 2)
        self._energy = max(0, self._energy - 1)

        if self._hunger == 100 or self._energy == 0:
            self._sick = True

        if self._sick:
            self._hp = max(0, self._hp - 5)

        if self._hp == 0:
            raise TamagochiIsGone("Тамагочи умер")
