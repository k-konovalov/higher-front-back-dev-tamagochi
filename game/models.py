"""Модуль с моделями"""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Food:
    """Модель объекта еды"""

    name: str
    satiety: int
    price: int

    def __repr__(self) -> str:
        """Метод для красивого принтинга объекта"""
        return (
            f"{self.name} стоимость: {self.price}, "
            f"утоляет голод на {self.satiety} единиц"
        )


@dataclass
class Medicine:
    """Модель объекта лекарства"""

    name: str
    price: int
    heal_hp: int
    number_of_uses: int
    uses: int = 0

    def is_empty(self) -> bool:
        """
        Проверяет, осталось ли еще лекарство

        :return: True если осталось, иначе False
        """
        return self.uses >= self.number_of_uses

    def copy(self) -> "Medicine":
        """
        Копия лекарства с текущим состоянием.

        :return: новый экземпляр Medicine
        """
        return Medicine(
            name=self.name,
            price=self.price,
            heal_hp=self.heal_hp,
            number_of_uses=self.number_of_uses,
            uses=self.uses,
        )

    def use(self) -> None:
        """
        Применяет лекарство: увеличивает счётчик применений.

        Если лекарство уже не осталось, количество применений
        не меняется.
        """
        if not self.is_empty():
            self.uses += 1

    def __repr__(self) -> str:
        """Метод для красивого принтинга объекта"""
        return (
            f'{self.name} стоимость: {self.price}, '
            f'лечит на {self.heal_hp} HP, использований: '
            f'{self.number_of_uses - self.uses}/{self.number_of_uses}'
        )
