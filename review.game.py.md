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

1

`"""Модуль с интерфейсом и реализацией класса игры""" `

2

3

`from abc import ABC, abstractmethod `

4

`from typing import Any `

5

6

`from .tamagochi import AbstractTamagochi `

7

`from .clicker import AbstractClicker `

8

`from .models import Food, Medicine `

9

`from .exceptions import NotEnoughMoney `

10

11

12

`class AbstractGame(ABC): `

13

`     """Интерфейс для логики игры"""  `

14

15

`     @abstractmethod  `

16

`     def __init__(  `

17

`         self,  `

18

`         tamagochi: AbstractTamagochi,  `

19

`         clicker: AbstractClicker,  `

20

`         all_food: list[Food],  `

21

`         all_medicine: list[Medicine]  `

22

`     ):  `

23

`         """  `

24

`         Абстрактный метод инициализации класса игры  `

25

26

`         :param tamagochi: экземпляр тамагочи  `

27

`         :param clicker: экземпляр кликера  `

28

`         :param all_food: все доступные варианты еды  `

29

`         :param all_medicine: все доступные варианты лекарств  `

30

`         """  `

31

`         raise NotImplementedError  `

32

33

`     @abstractmethod  `

34

`     def work(self) -> int:  `

35

`         """  `

36

`         Абстрактный метод для логики действия «работа».  `

37

38

`         :return: количество заработанных монет  `

39

`         """  `

40

`         raise NotImplementedError  `

41

42

`     @abstractmethod  `

43

`     def buy_food(self) -> None:  `

44

`         """Абстрактный метод для покупки еды"""  `

45

`         raise NotImplementedError  `

46

47

`     @abstractmethod  `

48

`     def buy_medicine(self) -> None:  `

49

`         """Абстрактный метод для покупки лекарства"""  `

50

`         raise NotImplementedError  `

51

52

`     @abstractmethod  `

53

`     def feed_tamagochi(self) -> None:  `

54

`         """Абстрактный метод для кормления тамагочи"""  `

55

`         raise NotImplementedError  `

56

57

`     @abstractmethod  `

58

`     def heal_tamagochi(self) -> None:  `

59

`         """Абстрактный метод для лечения тамагочи"""  `

60

`         raise NotImplementedError  `

61

62

`     @abstractmethod  `

63

`     def rest_tamagochi(self) -> None:  `

64

`         """Абстрактный метод для отдыха тамагочи"""  `

65

`         raise NotImplementedError  `

66

67

`     @abstractmethod  `

68

`     def play_with_tamagochi(self) -> None:  `

69

`         """Абстрактный метод для игры с тамагочи"""  `

70

`         raise NotImplementedError  `

71

72

`     @abstractmethod  `

73

`     def get_status(self) -> dict[str, Any]:  `

74

`         """  `

75

`         Абстрактный метод для получения статуса (всех характеристик) тамагочи  `

76

77

`         :return: словарь со всеми характеристиками тамагочи  `

78

`         """  `

79

`         raise NotImplementedError  `

80

81

`     @property  `

82

`     @abstractmethod  `

83

`     def food(self) -> list[Food]:  `

84

`         """  `

85

`         Абстрактное свойство для доступа к сумке с едой  `

86

87

`         :return: список с имеющимися (купленными) объектами еды  `

88

`         """  `

89

`         raise NotImplementedError  `

90

91

`     @property  `

92

`     @abstractmethod  `

93

`     def medicine(self) -> list[Medicine]:  `

94

`         """  `

95

`         Абстрактное свойство для доступа к сумке с лекарствами  `

96

97

`         :return: список с имеющимися (купленными) объектами лекарств  `

98

`         """  `

99

`         raise NotImplementedError  `

100

101

102

`class Game(AbstractGame): `

103

`     """Реализация логики игры «Тамагочи»"""  `

104

105

`     def __init__(  `

106

`         self,  `

107

`         tamagochi: AbstractTamagochi,  `

108

`         clicker: AbstractClicker,  `

109

`         all_food: list[Food],  `

110

`         all_medicine: list[Medicine],  `

111

`     ) -> None:  `

112

`         """  `

113

`         Инициализатор класса игры.  `

114

115

`         :param tamagochi: экземпляр тамагочи  `

116

`         :param clicker: экземпляр кликера  `

117

`         :param all_food: все доступные варианты еды  `

118

`         :param all_medicine: все доступные варианты лекарств  `

119

`         """  `

120

`         self.tamagochi = tamagochi  `

[Инкапсуляция нарушена](https://proproprogs.ru/python_oop/rezhimy-dostupa-public-private-protected-settery-i-gettery): поле объявлено публичным, стоит сделать "защищенным".

Надо исправить

Игорь Шкодаревьюер

121

`         self._clicker = clicker  `

122

`         self._all_food = all_food  `

Каталоги магазина(`all_food`, `all_medicine`) сейчас хранятся по ссылке, а не копией.  
Сейчас список лежит и в main, и в игре(тут просто еще одна ссылка на список, но внутри класса): любая из сторон может изменить его. Инкапсуляция не соблюдена - данные должны быть внутри классов.  
Следует в `__init__` передавать `list(all_food)` (хранение), а в `@property` возвращать `list(self._food)` (отдача), пока каталог статичный и одного владельца нет. Если появится сервис, например ShopService, который будет управлять каталогами, то копию можно будет убрать и работать со ссылкой на сервис.

Надо исправить

Игорь Шкодаревьюер

123

`         self._all_medicine = all_medicine  `

124

`         self._coins: int = 0  `

125

`         self._food_bag: list[Food] = []  `

126

`         self._medicine_bag: list[Medicine] = []  `

127

128

`     def work(self) -> int:  `

129

`         """  `

130

`         Идти на работу: 5 кликов, доход = 5 * income_per_click.  `

131

132

`         :return: количество заработанных монет  `

133

`         """  `

134

`         income = 5 * self._clicker.income_per_click  `

135

`         for _ in range(5):  `

136

`             self._clicker.click()  `

137

`         self._coins += income  `

138

`         return income  `

139

140

`     def _pick(self, items: list, title: str) -> int | None:  `

141

`         """  `

142

`         Показать меню с нумерацией и прочитать выбор пользователя.  `

143

144

`         :param items: список объектов для отображения в меню  `

145

`         :param title: заголовок меню  `

146

`         :return: индекс выбранного элемента (0-based) или None при отмене  `

147

`         """  `

148

`         while True:  `

149

`             print(f"\n{title}:")  `

150

`             for i, item in enumerate(items, 1):  `

151

`                 print(f"  {i}. {item}")  `

152

`             choice = input("Ваш выбор: ")  `

153

`             if choice == "0":  `

154

`                 return None  `

155

`             idx = int(choice) - 1  `

Нужна обработка `ValueError` - программа упадет при "abc".

Надо исправить

Игорь Шкодаревьюер

156

`             if idx in range(0, len(items)):  `

157

`                 return idx  `

158

159

`     def buy_food(self) -> None:  `

160

`         """  `

161

`         Интерактивная покупка еды.  `

162

163

`         Показывает меню доступной еды, читает выбор пользователя.  `

164

`         При недостатке монет выбрасывает NotEnoughMoney.  `

165

`         """  `

166

`         if not self._all_food:  `

167

`             print("Нет доступной еды для покупки.")  `

Используй исключения, в `main` перехватывай и выводи текстовое сообщение с причиной через `output`.

Надо исправить

Игорь Шкодаревьюер

168

`             return  `

169

170

`         idx = self._pick(self._all_food, "Доступная еда")  `

171

`         if idx is None:  `

172

`             return  `

173

174

`         food = self._all_food[idx]  `

175

`         if self._coins < food.price:  `

176

`             raise NotEnoughMoney(  `

177

`                 f"Не хватает монет: нужно {food.price}, есть {self._coins}."  `

178

`             )  `

179

`         self._coins -= food.price  `

180

`         self._food_bag.append(food)  `

181

`         print(f"Куплено: {food}")  `

182

183

`     def buy_medicine(self) -> None:  `

184

`         """  `

185

`         Интерактивная покупка лекарства.  `

186

187

`         Показывает меню доступных лекарств, читает выбор пользователя.  `

188

`         При недостатке монет выбрасывает NotEnoughMoney.  `

189

`         """  `

190

`         if not self._all_medicine:  `

191

`             print("Нет доступных лекарств для покупки.")  `

Используй исключения, в `main` перехватывай и выводи текстовое сообщение с причиной через `output`.

Надо исправить

Игорь Шкодаревьюер

192

`             return  `

193

194

`         idx = self._pick(self._all_medicine, "Доступные лекарства")  `

195

`         if idx is None:  `

196

`             return  `

197

198

`         medicine = self._all_medicine[idx]  `

199

`         if self._coins < medicine.price:  `

200

`             raise NotEnoughMoney(  `

201

`                 f"Не хватает монет: нужно {medicine.price}, есть {self._coins}."  `

202

`             )  `

203

`         self._coins -= medicine.price  `

204

`         self._medicine_bag.append(medicine)  `

Если просто тут добавить лекарство, взятое из списка `self._all_medicine`, то при изменении какого-либо атрибута само лекарство мутирует и в `all_medicine` тоже. [Добавлять нужно копию](https://stackoverflow.com/questions/42143461/make-copy-of-object-instance-in-python).

Надо исправить

Игорь Шкодаревьюер

205

`         print(f"Куплено: {medicine}")  `

206

207

`     def feed_tamagochi(self) -> None:  `

208

`         """  `

209

`         Интерактивное кормление тамагочи.  `

210

211

`         Показывает меню еды в сумке, читает выбор.  `

212

`         Съеденный предмет удаляется из сумки.  `

213

`         """  `

214

`         if not self._food_bag:  `

215

`             print("В сумке нет еды.")  `

Используй исключения, в `main` перехватывай и выводи текстовое сообщение с причиной через `output`.

Надо исправить

Игорь Шкодаревьюер

216

`             return  `

217

218

`         idx = self._pick(self._food_bag, "Еда в сумке")  `

219

`         if idx is None:  `

220

`             return  `

221

222

`         food = self._food_bag.pop(idx)  `

223

`         self.tamagochi.feed(food)  `

224

`         print(f"Питомец съел: {food}")  `

225

226

`     def heal_tamagochi(self) -> None:  `

227

`         """  `

228

`         Интерактивное лечение тамагочи.  `

229

230

`         Показывает меню лекарств в сумке, читает выбор.  `

231

`         Пустые лекарства удаляются. После использования пустое лекарство  `

232

`         также удаляется.  `

233

`         """  `

234

`         # Убираем пустые лекарства из сумки  `

235

`         self._medicine_bag = [  `

236

`             m for m in self._medicine_bag if not m.is_empty()  `

237

`         ]  `

238

239

`         if not self._medicine_bag:  `

240

`             print("В сумке нет лекарств.")  `

Используй исключения, в `main` перехватывай и выводи текстовое сообщение с причиной через `output`.

Надо исправить

Игорь Шкодаревьюер

241

`             return  `

242

243

`         idx = self._pick(self._medicine_bag, "Лекарства в сумке")  `

244

`         if idx is None:  `

245

`             return  `

246

247

`         medicine = self._medicine_bag.pop(idx)  `

248

`         self.tamagochi.heal(medicine)  `

249

`         print(f"Применено: {medicine}")  `

250

251

`         if medicine.is_empty():  `

252

`             print(f"{medicine.name} закончился.")  `

253

Рекомендация:  
Общее для методов класса - сейчас в методах Game вшиты и ввод и вывод консоли, это не очень хорошо. Если завтра игра переедет в GUI или веб-интерфейс, `print/input` станут мусоромм и их придется выпиливать. То есть класс придется переработать.  
За вывод должен отвечать интерфейс, в данной реализации это `main`. Следует вынести ввод/вывод в `main` (или в отдельный `console.py`), а `Game` должен только принимать данные и менять состояние. Например: в `main` спрашивать номер, `Game.buy_food(index)` достаёт объект из своего каталога и делает бизнес-логику.

Можно лучше

Игорь Шкодаревьюер

254

`     def rest_tamagochi(self) -> None:  `

255

`         """  `

256

`         Отдых тамагочи.  `

257

258

`         Восстанавливает энергию питомца.  `

259

`         """  `

260

`         self.tamagochi.rest()  `

261

`         print("Питомец отдохнул")  `

262

263

`     def play_with_tamagochi(self) -> None:  `

264

`         """  `

265

`         Игра с тамагочи.  `

266

267

`         Меняет состояние питомца (голод, энергия).  `

268

`         """  `

269

`         self.tamagochi.play()  `

270

`         print("Вы поиграли с питомцем")  `

271

272

`     def get_status(self) -> dict[str, Any]:  `

273

`         """  `

274

`         Получение полного статуса игры.  `

275

276

`         :return: словарь с показателями питомца и количеством монет  `

277

`         """  `

278

`         status = dict(self.tamagochi.status)  `

279

`         status["coins"] = self._coins  `

280

`         return status  `

281

282

`     @property  `

283

`     def food(self) -> list[Food]:  `

284

`         """  `

285

`         Список еды в сумке.  `

286

287

`         :return: список еды  `

288

`         """  `

289

`         return self._food_bag  `

290

291

`     @property  `

292

`     def medicine(self) -> list[Medicine]:  `

293

`         """  `

294

`         Список лекарств в сумке.  `

295

296

`         :return: список лекарств  `

297

`         """  `

298

`         return self._medicine_bag  `

299

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