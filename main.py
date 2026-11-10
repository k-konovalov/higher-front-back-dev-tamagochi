import os

from game.models import Food, Medicine
from game.tamagochi import BearTamagochi
from game.clicker import DummyClicker
from game.game import Game
from game.exceptions import (
    EmptyBag,
    EmptyCatalog,
    NotEnoughMoney,
    TamagochiIsGone,
)

STATUS_TEMPLATE = (
    "\nСтатус: голод {hunger}, здоровье {hp}, энергия {energy}, монет {coins}\n"
)
MENU = """1. Пойти на работу
2. Купить еду
3. Купить лекарство
4. Покормить тамагочи
5. Вылечить тамагочи
6. Играть с тамагочи
7. Отдых тамагочи
0. Выход"""


def main() -> None:
    """Основная функция для запуска игры."""
    all_food = [
        Food(name='Бургер', satiety=20, price=40),
        Food(name='Салат', satiety=10, price=20),
        Food(name='Яблоко', satiety=10, price=15)
    ]

    all_medicine = [
        Medicine(name='Ибупрофен', price=30, heal_hp=20, number_of_uses=1)
    ]

    tamagochi = BearTamagochi()
    clicker = DummyClicker()
    game = Game(
        tamagochi,
        clicker,
        all_food=all_food,
        all_medicine=all_medicine
    )

    print("Добро пожаловать в Тамагочи-кликер!")
    output = ''

    while True:
        print(output)
        print('=======')

        print(f"Сумка с едой: {game.food}")
        print(f"Сумка с лекарствами: {game.medicine}")

        print(STATUS_TEMPLATE.format(**game.get_status()))
        if game.tamagochi.is_sick():
            print("=======Тамагочи болеет======")
            print("=======Отдых действует менее эффективно=======")
        print(MENU)

        try:
            match input("Выберите действие: "):
                case "1":
                    income = game.work()
                    output = f'Вы заработали {income} монет'
                case "2":
                    game.buy_food()
                    output = 'Вы сходили в магазин'
                case "3":
                    game.buy_medicine()
                    output = 'Вы сходили в аптеку'
                case "4":
                    game.feed_tamagochi()
                    output = 'Вы попытались покормить тамагочи'
                case "5":
                    game.heal_tamagochi()
                    output = 'Вы попытались вылечить тамагочи'
                case "6":
                    game.play_with_tamagochi()
                    output = 'Вы поиграли с питомцем'
                case "7":
                    game.rest_tamagochi()
                    output = 'Питомец отдохнул'
                case "0":
                    break
                case _:
                    output = "Неверная команда"
        except TamagochiIsGone:
            print("=======Тамагочи умер======")
            print("Живи теперь с этим. Или заведи нового.")
            break
        except (NotEnoughMoney, EmptyCatalog, EmptyBag) as e:
            output = str(e)
        os.system('clear')
    print('=======')
    print('The end!')


if __name__ == "__main__":
    main()
