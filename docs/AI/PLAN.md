# PLAN.md — План разработки игры «Тамагочи»

> План составлен совместно со студентом через наводящие вопросы (тьютор-сессия).
> Цель — декомпозировать задание из [`README.md`](../../README.md) на
> отдельные блоки логики, продумать модули, интерфейсы и базовую функциональность.

## 1. Дизайн-решения (зафиксировано в тьютор-сессии)

| Решение | Выбор |
|---|---|
| Питомец | Медвежонок **Филипп** |
| Баланс | Стандартный: `hp=100`, `energy=100`, `hunger=0` (0 — сыт, 100 — голод на максимуме); тик: `hunger+2`, `energy-1` |
| Болезнь | Детерминированная: болеет, когда `hunger == 100` ИЛИ `energy == 0`; лечится только лекарством |
| Работа | `work()` = 5 кликов через `clicker.click()`, доход = `5 × income_per_click` |
| Хранение монет | В **игре** (`Game`), а не в кликере — кликер считает клики и знает доход за клик |

## 2. Архитектура: где что лежит

Тесты (`tests/test_code_structure.py`) требуют, чтобы **конкретный класс-наследник
определялся в том же файле, что и интерфейс**:

| Файл | Что добавляем |
|---|---|
| `game/clicker.py` | `class Clicker(AbstractClicker)` |
| `game/tamagochi.py` | `class BearTamagochi(AbstractTamagochi)` — медвежонок Филипп |
| `game/game.py` | `class TamagochiGame(AbstractGame)` |
| `game/models.py` | уже готово (`Food`, `Medicine`) |
| `game/exceptions.py` | уже готовы (`TamagochiIsGone`, `NotEnoughMoney`) — использовать в логике |
| `main.py` | заменить инстанциирование абстракций на свои классы, завершать игру при смерти |

Ключевые контракты из тестов (`tests/conftest.py`, `tests/test_logic.py`):

- `BearTamagochi()` — конструктор **без обязательных аргументов**;
- `TamagochiGame(tamagochi, clicker, all_food=..., all_medicine=...)` — именно такая сигнатура;
- `get_status()` возвращает словарь с int-значениями `hunger`, `hp`, `energy`, `coins`;
- `work()` возвращает `int` и вызывает `clicker.click()` минимум один раз;
- `buy_food()` / `buy_medicine()` / `feed_tamagochi()` / `heal_tamagochi()` — интерактивный выбор через `input()`: меню с нумерацией, `0` — отмена;
- у `Game` должен быть публичный атрибут `tamagochi` (main.py вызывает `game.tamagochi.is_sick()`);
- после `feed_tamagochi()` съеденный объект **удаляется** из `game.food`;
- `Medicine.is_empty()` в `models.py` возвращает `True`, когда использований **больше нет** (`uses >= number_of_uses`), — несмотря на инверсный docstring «осталось ли ещё». В сумке такой предмет удалять.

## 3. `Clicker` (game/clicker.py)

```python
class Clicker(AbstractClicker):
    def __init__(self, income_per_click: int = 10) -> None: ...
```

- поля: `_income_per_click: int`, `_clicks: int = 0`;
- `click()` — `_clicks += 1` (монеты забирает игра, здесь только счётчик кликов);
- свойство `income_per_click -> int`.

## 4. `BearTamagochi` (game/tamagochi.py)

Поля: `name: str = "Филипп"`, `hp = 100`, `energy = 100`, `hunger = 0`,
`_sick: bool = False`. Лимиты: `hp`/`energy`/`hunger` зажимаются в `[0, 100]`.

| Метод | Правило |
|---|---|
| `feed(food)` | `hunger = max(0, hunger - food.satiety)` |
| `play()` | `hunger = min(100, hunger + 5)`, `energy = max(0, energy - 10)` |
| `rest()` | `energy = min(100, energy + 30)`; если `_sick` — только `+15` (см. подсказку в main.py: «Отдых действует менее эффективно») |
| `heal(medicine)` | `medicine.uses += 1`; `hp = min(100, hp + medicine.heal_hp)`; `_sick = False` |
| `status` (property) | `{"hunger": …, "hp": …, "energy": …}` — только int |
| `is_alive()` | `hp > 0` |
| `is_sick()` | `_sick` |
| `update()` | см. ниже |

Логика `update()` (вызывается каждый тик / после каждого действия):

1. `hunger = min(100, hunger + 2)`;
2. `energy = max(0, energy - 1)`;
3. если `hunger == 100` ИЛИ `energy == 0` → `_sick = True` (болезнь «залипает» до лечения);
4. если `_sick` → `hp = max(0, hp - 5)`.

Смерть: `hp` уходит в 0, `is_alive()` → `False`. Исключение `TamagochiIsGone`
бросать не обязательно (тесты принимают оба варианта). В задании сказано
«здоровье ниже 0», но по контракту тестов `hp` зажимается в `[0, 100]` и
смерть наступает при `hp == 0`.

Проверка темпа: с нуля, без заботы Филипп болеет на ~50-м тике (`hunger`
достигает 100) и умирает на ~70-м (`hp 100 → 0` по `-5`/тик) — это укладывается
в лимиты тестов (300 и 500 вызовов `update()`).

## 5. `TamagochiGame` (game/game.py)

Поля: `tamagochi` (публичное), `_clicker`, `_all_food`, `_all_medicine`,
`_coins: int = 0`, `_food_bag: list[Food] = []`, `_medicine_bag: list[Medicine] = []`.

| Метод | Логика |
|---|---|
| `work() -> int` | `income = 5 * _clicker.income_per_click`; 5 раз `_clicker.click()`; `_coins += income`; вернуть `income` |
| `buy_food()` | меню `_all_food` (номера с 1, `0` — отмена); если `_coins < food.price` → `raise NotEnoughMoney`; иначе `_coins -= price`, `_food_bag.append(food)` |
| `buy_medicine()` | аналогично для `_all_medicine` |
| `feed_tamagochi()` | если `_food_bag` пуст — показать сообщение и выйти; меню сумки; `tamagochi.feed(item)`; `item` **удаляется** из сумки |
| `heal_tamagochi()` | меню сумки; если `item.is_empty()` → показать «пусто» и убрать из сумки; иначе `tamagochi.heal(item)`; если после использования `is_empty()` → убрать из сумки |
| `rest_tamagochi()` | `tamagochi.rest()` |
| `play_with_tamagochi()` | `tamagochi.play()` |
| `get_status()` | `{**tamagochi.status, "coins": _coins}` |
| `food` (property) | `_food_bag` |
| `medicine` (property) | `_medicine_bag` |

Общий помощник `_pick(items, title) -> index | None`: печатает список с
нумерацией, читает строку; `0` → `None` (отмена); не число / вне диапазона →
повторить. Используется во всех интерактивных методах.

Обвязка смертей: после действий с питомцем (и в конце каждого тика main.py)
проверять `tamagochi.is_alive()` — если `False`, завершать игровой цикл.

## 6. `main.py`

- импортировать `Clicker`, `BearTamagochi`, `TamagochiGame` и создать их вместо абстракций (`Clicker(income_per_click=10)`);
- после каждого действия вызывать `game.tamagochi.update()` (сейчас вызывается только для «работы» — унифицировать);
- при `not game.tamagochi.is_alive()` напечатать «Филипп умер» и `break` из цикла;
- оставить обработку исключений `NotEnoughMoney` / `TamagochiIsGone` через `try/except` и печатание понятного сообщения.

## 7. Порядок реализации

1. `Clicker` в `game/clicker.py`;
2. `BearTamagochi` в `game/tamagochi.py`;
3. `TamagochiGame` в `game/game.py`;
4. правки `main.py`;
5. проверка: `ruff check ./game` (и `ruff check main.py`) → `flake8 ./game` → `pytest ./tests` (в `.venv`);
6. сверка с чек-листом code style (раздел 8) перед отправкой.

## 8. Code style (чек-лист задания)

- docstring у каждого метода: описание, `:param:`, `:return:`, исключения (если бросаются) — по стилю абстрактных интерфейсов из шаблона;
- type hints у всех аргументов и return (включая properties и `__init__`);
- понятные имена переменных и методов, отражающие суть данных;
- только стандартная библиотека в runtime-коде (без сторонних зависимостей; `pytest`/`ruff`/`flake8` — только dev-инструменты).

## 9. Критерий готовности

- `pytest ./tests` — все тесты зелёные;
- `ruff check ./game` и `flake8 ./game` — без ошибок;
- чек-лист code style (раздел 8) соблюдён;
- в консоли: Филипп живёт, болеет, лечится, умирает; меню покупки/кормления
  работает, монеты считаются, неверный ввод не роняет игру.