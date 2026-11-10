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

<svg fill="none" height="33" width="42" xmlns="http://www.w3.org/2000/svg"><path clip-rule="evenodd" d="M41 32V11L32 1H1v31h40z" fill="#fff" fill-rule="evenodd" stroke="#81838C" stroke-width=".5"></path><path clip-rule="evenodd" d="M32 1v10h9" fill="#81838C" fill-rule="evenodd"></path><text fill="currentColor" stroke="currentColor" x="6" y="24">py</text></svg> clicker.py

2

<svg fill="none" height="33" width="42" xmlns="http://www.w3.org/2000/svg"><path clip-rule="evenodd" d="M41 32V11L32 1H1v31h40z" fill="#fff" fill-rule="evenodd" stroke="#81838C" stroke-width=".5"></path><path clip-rule="evenodd" d="M32 1v10h9" fill="#81838C" fill-rule="evenodd"></path><text fill="currentColor" stroke="currentColor" x="6" y="24">py</text></svg> exceptions.pyНет комментариев <svg fill="none" height="33" width="42" xmlns="http://www.w3.org/2000/svg"><path clip-rule="evenodd" d="M41 32V11L32 1H1v31h40z" fill="#fff" fill-rule="evenodd" stroke="#81838C" stroke-width=".5"></path><path clip-rule="evenodd" d="M32 1v10h9" fill="#81838C" fill-rule="evenodd"></path><text fill="currentColor" stroke="currentColor" x="6" y="24">py</text></svg> game.py

18

<svg fill="none" height="33" width="42" xmlns="http://www.w3.org/2000/svg"><path clip-rule="evenodd" d="M41 32V11L32 1H1v31h40z" fill="#fff" fill-rule="evenodd" stroke="#81838C" stroke-width=".5"></path><path clip-rule="evenodd" d="M32 1v10h9" fill="#81838C" fill-rule="evenodd"></path><text fill="currentColor" stroke="currentColor" x="6" y="24">py</text></svg> models.py

1

1

`"""Модуль с моделями""" `

2

3

`from dataclasses import dataclass `

4

5

6

`@dataclass(frozen=True, slots=True) `

7

`class Food: `

8

`     """Модель объекта еды"""  `

9

10

`     name: str  # наименование  `

Учебные и стандартные комментарии лучше удалить, так код будет легче читать.

Надо исправить

Игорь Шкодаревьюер

11

`     satiety: int  # на сколько единиц утоляет голод  `

12

`     price: int  # стоимость  `

13

14

`     def __repr__(self) -> str:  `

15

`         """Метод для красивого принтинга объекта"""  `

16

`         return (  `

17

`             f"{self.name} стоимость: {self.price}, "  `

18

`             f"утоляет голод на {self.satiety} единиц"  `

19

`         )  `

20

21

22

`@dataclass `

23

`class Medicine: `

24

`     """Модель объекта лекарства"""  `

25

26

`     name: str  # наименование  `

27

`     price: int  # стоимость  `

28

`     heal_hp: int  # сколько лечит HP  `

29

`     number_of_uses: int  # максимальное количество применений  `

30

`     uses: int = 0  # текущее количество применений  `

31

32

`     def is_empty(self) -> bool:  `

33

`         """  `

34

`         Проверяет, осталось ли еще лекарство  `

35

36

`         :return: True если осталось, иначе False  `

37

`         """  `

38

`         return self.uses >= self.number_of_uses  `

39

40

`     def __repr__(self) -> str:  `

41

`         """Метод для красивого принтинга объекта"""  `

42

`         return (  `

43

`             f'{self.name} стоимость: {self.price}, '  `

44

`             f'лечит на {self.heal_hp} HP, использований: '  `

45

`             f'{self.number_of_uses - self.uses}/{self.number_of_uses}'  `

46

`         )  `

47

<svg fill="none" height="33" width="42" xmlns="http://www.w3.org/2000/svg"><path clip-rule="evenodd" d="M41 32V11L32 1H1v31h40z" fill="#fff" fill-rule="evenodd" stroke="#81838C" stroke-width=".5"></path><path clip-rule="evenodd" d="M32 1v10h9" fill="#81838C" fill-rule="evenodd"></path><text fill="currentColor" stroke="currentColor" x="6" y="24">py</text></svg> tamagochi.py

4

tests

Нет комментариев <svg fill="none" height="33" width="42" xmlns="http://www.w3.org/2000/svg"><path clip-rule="evenodd" d="M41 32V11L32 1H1v31h40z" fill="#fff" fill-rule="evenodd" stroke="#81838C" stroke-width=".5"></path><path clip-rule="evenodd" d="M32 1v10h9" fill="#81838C" fill-rule="evenodd"></path><text fill="currentColor" stroke="currentColor" x="6" y="24">gitignore</text></svg>.gitignoreНет комментариев <svg fill="none" height="33" width="42" xmlns="http://www.w3.org/2000/svg"><path clip-rule="evenodd" d="M41 32V11L32 1H1v31h40z" fill="#fff" fill-rule="evenodd" stroke="#81838C" stroke-width=".5"></path><path clip-rule="evenodd" d="M32 1v10h9" fill="#81838C" fill-rule="evenodd"></path><text fill="currentColor" stroke="currentColor" x="6" y="24">md</text></svg> README.mdНет комментариев <svg fill="none" height="33" width="42" xmlns="http://www.w3.org/2000/svg"><path clip-rule="evenodd" d="M41 32V11L32 1H1v31h40z" fill="#fff" fill-rule="evenodd" stroke="#81838C" stroke-width=".5"></path><path clip-rule="evenodd" d="M32 1v10h9" fill="#81838C" fill-rule="evenodd"></path><text fill="currentColor" stroke="currentColor" x="6" y="24">md</text></svg> agents.mdНет комментариев <svg fill="none" height="33" width="42" xmlns="http://www.w3.org/2000/svg"><path clip-rule="evenodd" d="M41 32V11L32 1H1v31h40z" fill="#fff" fill-rule="evenodd" stroke="#81838C" stroke-width=".5"></path><path clip-rule="evenodd" d="M32 1v10h9" fill="#81838C" fill-rule="evenodd"></path><text fill="currentColor" stroke="currentColor" x="6" y="24">py</text></svg> main.py

5

<svg fill="none" height="33" width="42" xmlns="http://www.w3.org/2000/svg"><path clip-rule="evenodd" d="M41 32V11L32 1H1v31h40z" fill="#fff" fill-rule="evenodd" stroke="#81838C" stroke-width=".5"></path><path clip-rule="evenodd" d="M32 1v10h9" fill="#81838C" fill-rule="evenodd"></path><text fill="currentColor" stroke="currentColor" x="6" y="24">json</text></svg> opencode.jsonНет комментариев <svg fill="none" height="33" width="42" xmlns="http://www.w3.org/2000/svg"><path clip-rule="evenodd" d="M41 32V11L32 1H1v31h40z" fill="#fff" fill-rule="evenodd" stroke="#81838C" stroke-width=".5"></path><path clip-rule="evenodd" d="M32 1v10h9" fill="#81838C" fill-rule="evenodd"></path><text fill="currentColor" stroke="currentColor" x="6" y="24">ini</text></svg> pytest.iniНет комментариев <svg fill="none" height="33" width="42" xmlns="http://www.w3.org/2000/svg"><path clip-rule="evenodd" d="M41 32V11L32 1H1v31h40z" fill="#fff" fill-rule="evenodd" stroke="#81838C" stroke-width=".5"></path><path clip-rule="evenodd" d="M32 1v10h9" fill="#81838C" fill-rule="evenodd"></path><text fill="currentColor" stroke="currentColor" x="6" y="24">txt</text></svg> requirements.txtНет комментариев <svg fill="none" height="33" width="42" xmlns="http://www.w3.org/2000/svg"><path clip-rule="evenodd" d="M41 32V11L32 1H1v31h40z" fill="#fff" fill-rule="evenodd" stroke="#81838C" stroke-width=".5"></path><path clip-rule="evenodd" d="M32 1v10h9" fill="#81838C" fill-rule="evenodd"></path><text fill="currentColor" stroke="currentColor" x="6" y="24">toml</text></svg> ruff.tomlНет комментариев <svg fill="none" height="33" width="42" xmlns="http://www.w3.org/2000/svg"><path clip-rule="evenodd" d="M41 32V11L32 1H1v31h40z" fill="#fff" fill-rule="evenodd" stroke="#81838C" stroke-width=".5"></path><path clip-rule="evenodd" d="M32 1v10h9" fill="#81838C" fill-rule="evenodd"></path><text fill="currentColor" stroke="currentColor" x="6" y="24">cfg</text></svg> setup.cfgНет комментариев

Как вам ревью? Оцените его качество.  
Это поможет нам улучшить ваше обучение.