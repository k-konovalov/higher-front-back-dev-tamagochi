---
title: "Яндекс Практикум"
source: "https://practicum.yandex.ru/learn/cloud-services-engineer/courses/259ab8e4-9937-400d-92e7-e38f6a178ed5/sprints/1085007/topics/7afc9d56-f04c-4306-b9a8-ca1a88ece607/lessons/b801698e-18a2-4933-b0ce-3273aa0ec9cc/"
author:
published:
created: 2026-11-10
description:
tags:
  - "clippings"
---
Задание

Ревью

Чат по проекту

История

Шаг 3/3

Ревьюер проверил ваше задание и оставил замечания.

Поправьте их и отправьте задание снова

Github настроен

Задание отправлено

Есть замечания

## Задание не принято

Ваш результат

3/ 10

Привет) Хорошая работа. Оставил подробные комментарии.

Игорь Шкодаревьюер

## Ваш проект c комментариями

Проектная работа «Тамагочи»

Проверена 29 октября

higher-front-back-dev-tamagochi-main

120

.codegraph

Нет комментариев

docs

Нет комментариев

game

115

tests

Нет комментариев <svg fill="none" height="33" width="42" xmlns="http://www.w3.org/2000/svg"><path clip-rule="evenodd" d="M41 32V11L32 1H1v31h40z" fill="#fff" fill-rule="evenodd" stroke="#81838C" stroke-width=".5"></path><path clip-rule="evenodd" d="M32 1v10h9" fill="#81838C" fill-rule="evenodd"></path><text fill="currentColor" stroke="currentColor" x="6" y="24">gitignore</text></svg>.gitignoreНет комментариев <svg fill="none" height="33" width="42" xmlns="http://www.w3.org/2000/svg"><path clip-rule="evenodd" d="M41 32V11L32 1H1v31h40z" fill="#fff" fill-rule="evenodd" stroke="#81838C" stroke-width=".5"></path><path clip-rule="evenodd" d="M32 1v10h9" fill="#81838C" fill-rule="evenodd"></path><text fill="currentColor" stroke="currentColor" x="6" y="24">md</text></svg> README.mdНет комментариев <svg fill="none" height="33" width="42" xmlns="http://www.w3.org/2000/svg"><path clip-rule="evenodd" d="M41 32V11L32 1H1v31h40z" fill="#fff" fill-rule="evenodd" stroke="#81838C" stroke-width=".5"></path><path clip-rule="evenodd" d="M32 1v10h9" fill="#81838C" fill-rule="evenodd"></path><text fill="currentColor" stroke="currentColor" x="6" y="24">md</text></svg> agents.mdНет комментариев <svg fill="none" height="33" width="42" xmlns="http://www.w3.org/2000/svg"><path clip-rule="evenodd" d="M41 32V11L32 1H1v31h40z" fill="#fff" fill-rule="evenodd" stroke="#81838C" stroke-width=".5"></path><path clip-rule="evenodd" d="M32 1v10h9" fill="#81838C" fill-rule="evenodd"></path><text fill="currentColor" stroke="currentColor" x="6" y="24">py</text></svg> main.py

5

1

`import os `

2

3

`from game.models import Food, Medicine `

4

`from game.tamagochi import BearTamagochi `

5

`from game.clicker import DummyClicker `

6

`from game.game import Game `

7

8

9

`def main() -> None: `

10

`     """Основная функция для запуска игры"""  `

11

`     all_food = [  `

12

`         Food(name='Бургер', satiety=20, price=40),  `

13

`         Food(name='Салат', satiety=10, price=20),  `

14

`         Food(name='Яблоко', satiety=10, price=15)  `

15

`     ]  `

16

17

`     all_medicine = [  `

18

`         Medicine(name='Ибупрофен', price=30, heal_hp=20, number_of_uses=1)  `

19

`     ]  `

20

21

`     tamagochi = BearTamagochi()  `

22

`     clicker = DummyClicker(income_per_click=10)  `

23

`     game = Game(  `

24

`         tamagochi,  `

25

`         clicker,  `

26

`         all_food=all_food,  `

27

`         all_medicine=all_medicine  `

28

`     )  `

29

30

`     print("Добро пожаловать в Тамагочи-кликер!")  `

31

`     output = ''  `

32

33

`     while True:  `

34

`         print(output)  `

35

`         print('=======')  `

36

37

`         print(f"Сумка с едой: {game.food}")  `

38

`         print(f"Сумка с лекарствами: {game.medicine}")  `

39

40

`         status = game.get_status()  `

41

`         print(  `

42

`             f"\nСтатус: голод {status['hunger']}, здоровье {status['hp']},"  `

43

`             f"энергия {status['energy']}, монет {status['coins']}\n"  `

Можно в сообщении подготовить [именованные позиции](https://pythonru.com/osnovy/formatirovanie-v-python-s-pomoshhju-format) и применив метод format просто распаковать словарь. Более того, от переменной `status` можно избавиться, так как она "транзитная".  
  
Также заготовку текста выносим в константу.

Надо исправить

Игорь Шкодаревьюер

44

`         )  `

45

`         if game.tamagochi.is_sick:  `

Не хватает вызова метода.

Надо исправить

Игорь Шкодаревьюер

46

`             print("=======Тамагочи болеет======")  `

47

`             print("=======Отдых действует менее эффективно=======")  `

48

`         if (not game.tamagochi.is_alive):  `

За проверку состояния питомца должен отвечать сам питомец: смерть не событие, а флаг, который сейчас `main` проверяет каждый цикл, даже если ничего не произошло, да и исключение `TamagochiIsGone` объявлено, но не используется. Проверку `is_alive()` следует перенести в `update()`, бросать `TamagochiIsGone`, ловить в `main` через `try/except`.

Надо исправить

Игорь Шкодаревьюер

49

`             print("=======Тамагочи умер======")  `

50

`             print("Живи теперь с этим. Или заведи нового.")  `

51

`             break  `

52

`         print("1. Пойти на работу")  `

53

`         print("2. Купить еду")  `

54

`         print("3. Купить лекарство")  `

55

`         print("4. Покормить")  `

56

`         print("5. Вылечить")  `

57

`         print("6. Играть")  `

58

`         print("7. Отдых")  `

59

`         print("0. Выход")  `

Замени множества принтов на подготовку всего одной строки методом `join` с разделителем `\n` и один раз распечатать ее. Будет эффективнее по времени. При чем лучше это сделать один раз в константу на уровне модуля, а циклично.

Надо исправить

Игорь Шкодаревьюер

60

Не хватает обработки исключений, например `NotEnoughMoney` Не хватает обработки исключений, например `TamagochiIsGone`, питомец по логике может умереть, при этом игра должна завершиться.

Надо исправить

Игорь Шкодаревьюер

61

`         match input("Выберите действие: "):  `

62

`             case "1":  `

63

`                 income = game.work()  `

64

`                 output = f'Вы заработали {income} монет'  `

65

`             case "2":  `

66

`                 game.buy_food()  `

67

`                 output = 'Вы сходили в магазин'  `

68

`             case "3":  `

69

`                 game.buy_medicine()  `

70

`                 output = 'Вы сходили в аптеку'  `

71

`             case "4":  `

72

`                 game.feed_tamagochi()  `

73

`                 output = 'Вы попытались покормить тамагочи'  `

74

`             case "5":  `

75

`                 game.heal_tamagochi()  `

76

`                 output = 'Вы попытались вылечить тамагочи'  `

77

`             case "6":  `

78

`                 game.play_with_tamagochi()  `

79

`                 output = 'Вы поиграли с питомцем'  `

80

`             case "7":  `

81

`                 game.rest_tamagochi()  `

82

`                 output = 'Питомец отдохнул'  `

83

`             case "0":  `

84

`                 break  `

85

`             case _:  `

86

`                 output = "Неверная команда"  `

87

`         os.system('clear')  `

88

`     print('=======')  `

89

`     print('The end!')  `

90

91

92

`if __name__ == "__main__": `

93

`     main()  `

94

<svg fill="none" height="33" width="42" xmlns="http://www.w3.org/2000/svg"><path clip-rule="evenodd" d="M41 32V11L32 1H1v31h40z" fill="#fff" fill-rule="evenodd" stroke="#81838C" stroke-width=".5"></path><path clip-rule="evenodd" d="M32 1v10h9" fill="#81838C" fill-rule="evenodd"></path><text fill="currentColor" stroke="currentColor" x="6" y="24">json</text></svg> opencode.jsonНет комментариев <svg fill="none" height="33" width="42" xmlns="http://www.w3.org/2000/svg"><path clip-rule="evenodd" d="M41 32V11L32 1H1v31h40z" fill="#fff" fill-rule="evenodd" stroke="#81838C" stroke-width=".5"></path><path clip-rule="evenodd" d="M32 1v10h9" fill="#81838C" fill-rule="evenodd"></path><text fill="currentColor" stroke="currentColor" x="6" y="24">ini</text></svg> pytest.iniНет комментариев <svg fill="none" height="33" width="42" xmlns="http://www.w3.org/2000/svg"><path clip-rule="evenodd" d="M41 32V11L32 1H1v31h40z" fill="#fff" fill-rule="evenodd" stroke="#81838C" stroke-width=".5"></path><path clip-rule="evenodd" d="M32 1v10h9" fill="#81838C" fill-rule="evenodd"></path><text fill="currentColor" stroke="currentColor" x="6" y="24">txt</text></svg> requirements.txtНет комментариев <svg fill="none" height="33" width="42" xmlns="http://www.w3.org/2000/svg"><path clip-rule="evenodd" d="M41 32V11L32 1H1v31h40z" fill="#fff" fill-rule="evenodd" stroke="#81838C" stroke-width=".5"></path><path clip-rule="evenodd" d="M32 1v10h9" fill="#81838C" fill-rule="evenodd"></path><text fill="currentColor" stroke="currentColor" x="6" y="24">toml</text></svg> ruff.tomlНет комментариев <svg fill="none" height="33" width="42" xmlns="http://www.w3.org/2000/svg"><path clip-rule="evenodd" d="M41 32V11L32 1H1v31h40z" fill="#fff" fill-rule="evenodd" stroke="#81838C" stroke-width=".5"></path><path clip-rule="evenodd" d="M32 1v10h9" fill="#81838C" fill-rule="evenodd"></path><text fill="currentColor" stroke="currentColor" x="6" y="24">cfg</text></svg> setup.cfgНет комментариев

Как вам ревью? Оцените его качество.  
Это поможет нам улучшить ваше обучение.