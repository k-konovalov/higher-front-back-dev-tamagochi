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

<svg fill="none" height="33" width="42" xmlns="http://www.w3.org/2000/svg"><path clip-rule="evenodd" d="M41 32V11L32 1H1v31h40z" fill="#fff" fill-rule="evenodd" stroke="#81838C" stroke-width=".5"></path><path clip-rule="evenodd" d="M32 1v10h9" fill="#81838C" fill-rule="evenodd"></path><text fill="currentColor" stroke="currentColor" x="6" y="24">py</text></svg> tamagochi.py

4

1

`"""Модуль с интерфейсом и реализациями класса тамагочи""" `

2

3

`from abc import ABC, abstractmethod `

4

5

`from .models import Food, Medicine `

6

`from .exceptions import TamagochiIsGone `

7

8

9

`class AbstractTamagochi(ABC): `

10

`     """Интерфейс логики тамагочи"""  `

11

12

`     @abstractmethod  `

13

`     def feed(self, food: Food) -> None:  `

14

`         """  `

15

`         Абстрактный метод для кормления тамагочи  `

16

17

`         :param food: объект еды для кормления  `

18

`         """  `

19

`         raise NotImplementedError  `

20

21

`     @abstractmethod  `

22

`     def play(self) -> None:  `

23

`         """Абстрактный метод для игры с тамагочи"""  `

24

`         raise NotImplementedError  `

25

26

`     @abstractmethod  `

27

`     def rest(self) -> None:  `

28

`         """Абстрактный метод для отдыха тамагочи"""  `

29

`         raise NotImplementedError  `

30

31

`     @abstractmethod  `

32

`     def heal(self, medicine: Medicine) -> None:  `

33

`         """  `

34

`         Абстрактный метод для лечения тамагочи  `

35

36

`         :param medicine: лекарство для лечения  `

37

`         """  `

38

`         raise NotImplementedError  `

39

40

`     @property  `

41

`     @abstractmethod  `

42

`     def status(self) -> dict[str, int]:  `

43

`         """  `

44

`         Абстрактное свойство для доступа ко всем состояниям тамагочи  `

45

46

`         :return: словарь со всеми состояниями тамагочи  `

47

`         """  `

48

`         raise NotImplementedError  `

49

50

`     @abstractmethod  `

51

`     def is_alive(self) -> bool:  `

52

`         """  `

53

`         Абстрактный метод для проверки жив ли тамагочи  `

54

55

`         :return: True если жив, иначе False  `

56

`         """  `

57

`         raise NotImplementedError  `

58

59

`     @abstractmethod  `

60

`     def is_sick(self) -> bool:  `

61

`         """  `

62

`         Абстрактный метод для проверки, не заболел ли тамагочи  `

63

64

`         :return: True если тамагочи болеет, иначе False  `

65

`         """  `

66

`         raise NotImplementedError  `

67

68

`     @abstractmethod  `

69

`     def update(self) -> None:  `

70

`         """  `

71

`         Абстрактный метод для обновления состояний тамагочи.  `

72

`         Должен использоваться после каждого взаимодействия с тамагочи  `

73

`         """  `

74

`         raise NotImplementedError  `

75

76

77

`class BearTamagochi(AbstractTamagochi): `

78

`     """Реализация тамагочи — медвежонок"""  `

79

80

`     def __init__(self) -> None:  `

81

`         """  `

82

`         Инициализатор класса.  `

83

84

`         Создаёт питомца со стандартными параметрами:  `

85

`         голод=0 (сыт), энергия=100, здоровье=100, не болен.  `

86

`         """  `

87

`         self.name: str = "Медведь"  `

88

`         self._hp: int = 100  `

Значения контролируем константами.

Надо исправить

Игорь Шкодаревьюер

89

`         self._energy: int = 100  `

90

`         self._hunger: int = 0  `

91

`         self._sick: bool = False  `

92

93

`     @property  `

94

`     def status(self) -> dict[str, int]:  `

95

`         """  `

96

`         Свойство для доступа ко всем состояниям тамагочи.  `

97

98

`         :return: словарь с ключами 'hunger', 'hp', 'energy' (int)  `

99

`         """  `

100

`         return {  `

101

`             "hunger": self._hunger,  `

102

`             "hp": self._hp,  `

103

`             "energy": self._energy,  `

104

`         }  `

105

106

`     def is_alive(self) -> bool:  `

107

`         """  `

108

`         Проверка, жив ли тамагочи.  `

109

110

`         :return: True если здоровье больше 0  `

111

`         """  `

112

`         return self._hp > 0  `

113

114

`     def is_sick(self) -> bool:  `

115

`         """  `

116

`         Проверка, болен ли тамагочи.  `

117

118

`         :return: True если тамагочи болеет  `

119

`         """  `

120

`         return self._sick  `

121

122

`     @staticmethod  `

123

`     def tamagochi_update(func):  `

124

`         """  `

125

`         Декоратор для автоматического вызова update() после действия.  `

126

127

`         :param func: метод для обёртывания  `

128

`         :return: обёрнутый метод  `

129

`         """  `

130

`         def wrapper(self, *args, **kwargs):  `

131

`             func(self, *args, **kwargs)  `

132

`             self.update()  `

133

`         return wrapper  `

134

135

`     def feed(self, food: Food) -> None:  `

136

`         """  `

137

`         Кормит тамагочи выбранной едой.  `

138

139

`         Уменьшает голод на величину насыщения еды.  `

140

141

`         :param food: объект еды для кормления  `

142

`         """  `

143

`         self._hunger = max(0, self._hunger - food.satiety)  `

144

145

`     @tamagochi_update  `

146

`     def play(self) -> None:  `

147

`         """  `

148

`         Игра с тамагочи.  `

149

150

`         Увеличивает голод на 5 и уменьшает энергию на 10.  `

Значение <<5 и 10>> может поменяться, документация будет врать. Либо удаляем, либо читаем тут как поправить этот момент [https://stackoverflow.com/a/36091548](https://stackoverflow.com/a/36091548).

Надо исправить

Игорь Шкодаревьюер

151

`         """  `

152

`         self._hunger = min(100, self._hunger + 5)  `

153

`         self._energy = max(0, self._energy - 10)  `

154

155

`     @tamagochi_update  `

156

`     def rest(self) -> None:  `

157

`         """  `

158

`         Отдых тамагочи.  `

159

160

`         Восстанавливает энергию на 30 (на 15, если болен).  `

161

`         """  `

162

`         restore = 15 if self._sick else 30  `

163

`         self._energy = min(100, self._energy + restore)  `

164

165

`     @tamagochi_update  `

166

`     def heal(self, medicine: Medicine) -> None:  `

167

`         """  `

168

`         Лечит тамагочи выбранной medicine.  `

169

170

`         Увеличивает uses лекарства на 1, восстанавливает hp,  `

171

`         снимает статус болезни.  `

172

173

`         :param medicine: лекарство для лечения  `

174

`         """  `

175

`         medicine.uses += 1  `

`Tamagochi.heal()` меняет `medicine.uses += 1` в обход модели `Medicine`. Нужно добавить `Medicine.use()`, который проверяет `is_empty()` и увеличивает `uses`. В `Tamagochi.heal()` вызывать `medicine.use()`

Надо исправить

Игорь Шкодаревьюер

176

`         self._hp = min(100, self._hp + medicine.heal_hp)  `

177

`         self._sick = False  `

178

179

`     def update(self) -> None:  `

180

`         """  `

181

`         Обновление состояния тамагочи (тик).  `

182

183

`         1. голод += 2 (макс. 100)  `

184

`         2. энергия -= 1 (мин. 0)  `

185

`         3. если голод==100 или энергия==0 → болезнь  `

186

`         4. если болен → здоровье -= 5 (мин. 0)  `

187

`         """  `

188

`         self._hunger = min(100, self._hunger + 2)  `

189

`         self._energy = max(0, self._energy - 1)  `

190

191

`         if self._hunger == 100 or self._energy == 0:  `

192

`             self._sick = True  `

193

194

`         if self._sick:  `

195

`             self._hp = max(0, self._hp - 5)  `

196

197

`         if self._hp == 0:  `

Есть `is_alive`

Надо исправить

Игорь Шкодаревьюер

198

`             raise TamagochiIsGone("Тамагочи умер")  `

199

tests

Нет комментариев <svg fill="none" height="33" width="42" xmlns="http://www.w3.org/2000/svg"><path clip-rule="evenodd" d="M41 32V11L32 1H1v31h40z" fill="#fff" fill-rule="evenodd" stroke="#81838C" stroke-width=".5"></path><path clip-rule="evenodd" d="M32 1v10h9" fill="#81838C" fill-rule="evenodd"></path><text fill="currentColor" stroke="currentColor" x="6" y="24">gitignore</text></svg>.gitignoreНет комментариев <svg fill="none" height="33" width="42" xmlns="http://www.w3.org/2000/svg"><path clip-rule="evenodd" d="M41 32V11L32 1H1v31h40z" fill="#fff" fill-rule="evenodd" stroke="#81838C" stroke-width=".5"></path><path clip-rule="evenodd" d="M32 1v10h9" fill="#81838C" fill-rule="evenodd"></path><text fill="currentColor" stroke="currentColor" x="6" y="24">md</text></svg> README.mdНет комментариев <svg fill="none" height="33" width="42" xmlns="http://www.w3.org/2000/svg"><path clip-rule="evenodd" d="M41 32V11L32 1H1v31h40z" fill="#fff" fill-rule="evenodd" stroke="#81838C" stroke-width=".5"></path><path clip-rule="evenodd" d="M32 1v10h9" fill="#81838C" fill-rule="evenodd"></path><text fill="currentColor" stroke="currentColor" x="6" y="24">md</text></svg> agents.mdНет комментариев <svg fill="none" height="33" width="42" xmlns="http://www.w3.org/2000/svg"><path clip-rule="evenodd" d="M41 32V11L32 1H1v31h40z" fill="#fff" fill-rule="evenodd" stroke="#81838C" stroke-width=".5"></path><path clip-rule="evenodd" d="M32 1v10h9" fill="#81838C" fill-rule="evenodd"></path><text fill="currentColor" stroke="currentColor" x="6" y="24">py</text></svg> main.py

5

<svg fill="none" height="33" width="42" xmlns="http://www.w3.org/2000/svg"><path clip-rule="evenodd" d="M41 32V11L32 1H1v31h40z" fill="#fff" fill-rule="evenodd" stroke="#81838C" stroke-width=".5"></path><path clip-rule="evenodd" d="M32 1v10h9" fill="#81838C" fill-rule="evenodd"></path><text fill="currentColor" stroke="currentColor" x="6" y="24">json</text></svg> opencode.jsonНет комментариев <svg fill="none" height="33" width="42" xmlns="http://www.w3.org/2000/svg"><path clip-rule="evenodd" d="M41 32V11L32 1H1v31h40z" fill="#fff" fill-rule="evenodd" stroke="#81838C" stroke-width=".5"></path><path clip-rule="evenodd" d="M32 1v10h9" fill="#81838C" fill-rule="evenodd"></path><text fill="currentColor" stroke="currentColor" x="6" y="24">ini</text></svg> pytest.iniНет комментариев <svg fill="none" height="33" width="42" xmlns="http://www.w3.org/2000/svg"><path clip-rule="evenodd" d="M41 32V11L32 1H1v31h40z" fill="#fff" fill-rule="evenodd" stroke="#81838C" stroke-width=".5"></path><path clip-rule="evenodd" d="M32 1v10h9" fill="#81838C" fill-rule="evenodd"></path><text fill="currentColor" stroke="currentColor" x="6" y="24">txt</text></svg> requirements.txtНет комментариев <svg fill="none" height="33" width="42" xmlns="http://www.w3.org/2000/svg"><path clip-rule="evenodd" d="M41 32V11L32 1H1v31h40z" fill="#fff" fill-rule="evenodd" stroke="#81838C" stroke-width=".5"></path><path clip-rule="evenodd" d="M32 1v10h9" fill="#81838C" fill-rule="evenodd"></path><text fill="currentColor" stroke="currentColor" x="6" y="24">toml</text></svg> ruff.tomlНет комментариев <svg fill="none" height="33" width="42" xmlns="http://www.w3.org/2000/svg"><path clip-rule="evenodd" d="M41 32V11L32 1H1v31h40z" fill="#fff" fill-rule="evenodd" stroke="#81838C" stroke-width=".5"></path><path clip-rule="evenodd" d="M32 1v10h9" fill="#81838C" fill-rule="evenodd"></path><text fill="currentColor" stroke="currentColor" x="6" y="24">cfg</text></svg> setup.cfgНет комментариев

Как вам ревью? Оцените его качество.  
Это поможет нам улучшить ваше обучение.