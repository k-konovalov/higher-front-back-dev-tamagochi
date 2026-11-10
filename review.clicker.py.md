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

1

`"""Модуль с интерфейсом и реализацией кликера""" `

2

3

`from abc import ABC, abstractmethod `

4

5

6

`class AbstractClicker(ABC): `

7

`     """Интерфейс для кликера"""  `

8

9

`     @abstractmethod  `

10

`     def __init__(self) -> None:  `

11

`         """Абстрактный метод инициализации"""  `

12

`         raise NotImplementedError  `

13

14

`     @abstractmethod  `

15

`     def click(self) -> None:  `

16

`         """Абстрактный метод клика для накапливания монет"""  `

17

`         raise NotImplementedError  `

18

19

`     @property  `

20

`     @abstractmethod  `

21

`     def income_per_click(self) -> int:  `

22

`         """Абстрактное свойство для доступа к количеству монет за клик"""  `

23

`         raise NotImplementedError  `

24

25

26

`class DummyClicker(AbstractClicker): `

27

`     """Реализация кликера для заработка монет"""  `

Как правильно оформляется докстринг(небольшой чек-лист, далеко не полный):

- После открывающих тройных кавычек `"""` не должно быть пробела.
- **Докстринг начинается с заглавной буквы и заканчивается точкой**.
- Если докстринг не умещается в одну строку — можно разбить его на несколько строк. Отступы на новой строке должны выровнять текст по кавычкам.
- Если документируется класс — после строки документации оставляется пустая строка. В остальных случаях код должен начинаться сразу после докстринга.

[https://peps.python.org/pep-0257/](https://peps.python.org/pep-0257/).

****Проверь по всему проекту****

Надо исправить

Игорь Шкодаревьюер

28

29

`     def __init__(self, income_per_click: int = 10) -> None:  `

Значения контролируем константами.

Надо исправить

Игорь Шкодаревьюер

30

`         """  `

31

`         Инициализатор класса.  `

32

33

`         :param income_per_click: количество монет, зарабатываемых за один клик  `

34

`         """  `

35

`         self._income_per_click = income_per_click  `

36

`         self._clicks: int = 0  `

37

38

`     def click(self) -> None:  `

39

`         """  `

40

`         Метод клика для накапливания счётчика кликов.  `

41

42

`         Увеличивает счётчик кликов (монеты забирает игра).  `

43

`         """  `

44

`         self._clicks += 1  `

45

46

`     @property  `

47

`     def income_per_click(self) -> int:  `

48

`         """  `

49

`         Свойство для доступа к количеству монет за клик.  `

50

51

`         :return: количество монет, зарабатываемых за один клик  `

52

`         """  `

53

`         return self._income_per_click  `

54

<svg fill="none" height="33" width="42" xmlns="http://www.w3.org/2000/svg"><path clip-rule="evenodd" d="M41 32V11L32 1H1v31h40z" fill="#fff" fill-rule="evenodd" stroke="#81838C" stroke-width=".5"></path><path clip-rule="evenodd" d="M32 1v10h9" fill="#81838C" fill-rule="evenodd"></path><text fill="currentColor" stroke="currentColor" x="6" y="24">py</text></svg> exceptions.pyНет комментариев <svg fill="none" height="33" width="42" xmlns="http://www.w3.org/2000/svg"><path clip-rule="evenodd" d="M41 32V11L32 1H1v31h40z" fill="#fff" fill-rule="evenodd" stroke="#81838C" stroke-width=".5"></path><path clip-rule="evenodd" d="M32 1v10h9" fill="#81838C" fill-rule="evenodd"></path><text fill="currentColor" stroke="currentColor" x="6" y="24">py</text></svg> game.py

18

<svg fill="none" height="33" width="42" xmlns="http://www.w3.org/2000/svg"><path clip-rule="evenodd" d="M41 32V11L32 1H1v31h40z" fill="#fff" fill-rule="evenodd" stroke="#81838C" stroke-width=".5"></path><path clip-rule="evenodd" d="M32 1v10h9" fill="#81838C" fill-rule="evenodd"></path><text fill="currentColor" stroke="currentColor" x="6" y="24">py</text></svg> models.py

1

<svg fill="none" height="33" width="42" xmlns="http://www.w3.org/2000/svg"><path clip-rule="evenodd" d="M41 32V11L32 1H1v31h40z" fill="#fff" fill-rule="evenodd" stroke="#81838C" stroke-width=".5"></path><path clip-rule="evenodd" d="M32 1v10h9" fill="#81838C" fill-rule="evenodd"></path><text fill="currentColor" stroke="currentColor" x="6" y="24">py</text></svg> tamagochi.py

4

tests

Нет комментариев <svg fill="none" height="33" width="42" xmlns="http://www.w3.org/2000/svg"><path clip-rule="evenodd" d="M41 32V11L32 1H1v31h40z" fill="#fff" fill-rule="evenodd" stroke="#81838C" stroke-width=".5"></path><path clip-rule="evenodd" d="M32 1v10h9" fill="#81838C" fill-rule="evenodd"></path><text fill="currentColor" stroke="currentColor" x="6" y="24">gitignore</text></svg>.gitignoreНет комментариев <svg fill="none" height="33" width="42" xmlns="http://www.w3.org/2000/svg"><path clip-rule="evenodd" d="M41 32V11L32 1H1v31h40z" fill="#fff" fill-rule="evenodd" stroke="#81838C" stroke-width=".5"></path><path clip-rule="evenodd" d="M32 1v10h9" fill="#81838C" fill-rule="evenodd"></path><text fill="currentColor" stroke="currentColor" x="6" y="24">md</text></svg> README.mdНет комментариев <svg fill="none" height="33" width="42" xmlns="http://www.w3.org/2000/svg"><path clip-rule="evenodd" d="M41 32V11L32 1H1v31h40z" fill="#fff" fill-rule="evenodd" stroke="#81838C" stroke-width=".5"></path><path clip-rule="evenodd" d="M32 1v10h9" fill="#81838C" fill-rule="evenodd"></path><text fill="currentColor" stroke="currentColor" x="6" y="24">md</text></svg> agents.mdНет комментариев <svg fill="none" height="33" width="42" xmlns="http://www.w3.org/2000/svg"><path clip-rule="evenodd" d="M41 32V11L32 1H1v31h40z" fill="#fff" fill-rule="evenodd" stroke="#81838C" stroke-width=".5"></path><path clip-rule="evenodd" d="M32 1v10h9" fill="#81838C" fill-rule="evenodd"></path><text fill="currentColor" stroke="currentColor" x="6" y="24">py</text></svg> main.py

5

<svg fill="none" height="33" width="42" xmlns="http://www.w3.org/2000/svg"><path clip-rule="evenodd" d="M41 32V11L32 1H1v31h40z" fill="#fff" fill-rule="evenodd" stroke="#81838C" stroke-width=".5"></path><path clip-rule="evenodd" d="M32 1v10h9" fill="#81838C" fill-rule="evenodd"></path><text fill="currentColor" stroke="currentColor" x="6" y="24">json</text></svg> opencode.jsonНет комментариев <svg fill="none" height="33" width="42" xmlns="http://www.w3.org/2000/svg"><path clip-rule="evenodd" d="M41 32V11L32 1H1v31h40z" fill="#fff" fill-rule="evenodd" stroke="#81838C" stroke-width=".5"></path><path clip-rule="evenodd" d="M32 1v10h9" fill="#81838C" fill-rule="evenodd"></path><text fill="currentColor" stroke="currentColor" x="6" y="24">ini</text></svg> pytest.iniНет комментариев <svg fill="none" height="33" width="42" xmlns="http://www.w3.org/2000/svg"><path clip-rule="evenodd" d="M41 32V11L32 1H1v31h40z" fill="#fff" fill-rule="evenodd" stroke="#81838C" stroke-width=".5"></path><path clip-rule="evenodd" d="M32 1v10h9" fill="#81838C" fill-rule="evenodd"></path><text fill="currentColor" stroke="currentColor" x="6" y="24">txt</text></svg> requirements.txtНет комментариев <svg fill="none" height="33" width="42" xmlns="http://www.w3.org/2000/svg"><path clip-rule="evenodd" d="M41 32V11L32 1H1v31h40z" fill="#fff" fill-rule="evenodd" stroke="#81838C" stroke-width=".5"></path><path clip-rule="evenodd" d="M32 1v10h9" fill="#81838C" fill-rule="evenodd"></path><text fill="currentColor" stroke="currentColor" x="6" y="24">toml</text></svg> ruff.tomlНет комментариев <svg fill="none" height="33" width="42" xmlns="http://www.w3.org/2000/svg"><path clip-rule="evenodd" d="M41 32V11L32 1H1v31h40z" fill="#fff" fill-rule="evenodd" stroke="#81838C" stroke-width=".5"></path><path clip-rule="evenodd" d="M32 1v10h9" fill="#81838C" fill-rule="evenodd"></path><text fill="currentColor" stroke="currentColor" x="6" y="24">cfg</text></svg> setup.cfgНет комментариев

Как вам ревью? Оцените его качество.  
Это поможет нам улучшить ваше обучение.