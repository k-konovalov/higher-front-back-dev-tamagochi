# Task Plan: переработка «Тамагочи» по результатам ревью

## Goal
Закрыть 20 комментариев «Надо исправить» из 5 review-файлов, двигаясь от маленьких изменений
к крупным. Рекомендация «Можно лучше» (G9, вынести I/O из Game) — вне раунда
(решение пользователя, 2026-11-10). Докстринги и линтер — на конец.

## Next Step
Phase 6: N1 (`STATUS_TEMPLATE` + `format(**dict)`) → N4 (`MENU` — одна строка модульного уровня).

## Карта ревью-комментариев (21 шт.; G9 — вне раунда)
| ID | Файл (текущая строка) | Комментарий | Фаза |
|----|----------------------|-------------|------|
| M1  | game/models.py:10-12,26-30 | убрать инлайн-комментарии полей (`# наименование` и т.п.) | 2 |
| T4  | game/tamagochi.py:197 | `self._hp == 0` → `is_alive()` | 2 |
| G3  | game/game.py:155 | `ValueError` в `_pick` | 2 |
| C2  | game/clicker.py:29 | дефолт `10` → константа | 2 |
| T1  | game/tamagochi.py:88-90,143,152-153,162-163,188-195 | магические числа → константы | 3 |
| T3  | game/tamagochi.py:175 + models.py | `medicine.uses += 1` → `Medicine.use()` | 3 |
| G1  | game/game.py:120 | `self.tamagochi` → `_tamagochi` | 4 |
| G2  | game/game.py:122-123,289,298 | каталог/сумки по ссылке → копии | 4 |
| G8  | game/game.py:204 | в сумку добавлять копию лекарства (`Medicine.copy()`) | 4 |
| G4-G7 | game/game.py:167,191,215,240 | print «пусто» → исключения | 5 |
| N5  | main.py:61-86 | перехват `NotEnoughMoney` (и новых) в main | 5 |
| N2  | main.py:45 | `is_sick` → `is_sick()` | 5 |
| N3  | main.py:48-51 | смерть: `TamagochiIsGone` из `update()`, main — try/except | 5 |
| N1  | main.py:40-44 | статус: шаблон + `format(**dict)`, без локальной переменной | 6 |
| N4  | main.py:52-59 | меню: одна константа модульного уровня | 6 |
| G9  | game/game.py (весь класс) | «Можно лучше»: I/O в main, Game принимает index | — (вне раунда) |
| C1  | game/clicker.py:27 | докстринг PEP257 (точка) + проверить весь проект | 7 |
| T2  | game/tamagochi.py:148-151 | числа в докстринге `play` → ссылки на константы | 7 |

Базовая линия (2026-11-10, HEAD `5e72fb9 F-4: review-1 - 2`): `ruff check ./game` — OK;
`pytest ./tests` — 28 passed.
Докстринги и `__repr__` добавлены в F-4-коммитах (частичное закрытие C1); 20 «Надо исправить» остаются.

## Phases

### Phase 1: Разведка
- [x] Прочитаны все 5 review-файлов, комментарии сопоставлены с кодом
- [x] Прочитаны tests/ и conftest (ограничения для фазы 7)
- [x] Конфиги ruff.toml / pytest.ini (D-правила не включены)
- [x] Базовая линия ruff + pytest — зелёная
- **Status:** complete

### Phase 2: Локальные микро-фиксы (по одному, ruff+pytest после каждого)
- [x] M1: models.py — убраны 8 инлайн-комментариев полей (ruff OK, 28 passed)
- [x] T4: tamagochi.py `update()`: `if self._hp == 0` → `if not self.is_alive()` (ruff OK, 28 passed)
- [x] G3: game.py `_pick()`: `try/except ValueError` вокруг `int(choice)` → «Неверный выбор», continue (ruff OK, 28 passed, ручной прогон)
- [x] C2: clicker.py: `DEFAULT_INCOME_PER_CLICK = 10` вверху модуля, дефолт аргумента — константа (ruff OK, 28 passed)
- Менторские темы: защищённые атрибуты; обработка ошибки конвертации ввода
- **Status:** complete

### Phase 3: Константы и Medicine.use()
- [x] T1: константы (INITIAL_*, *_LIMIT, дельты play/rest/update/болезни) — ruff OK, 28 passed
- [x] (опц.) `WORK_CLICKS = 5` в `work()`; main.py: `DummyClicker()` без явного income — ruff OK, 28 passed
- [x] T3: `Medicine.use()` в models.py (не инкрементит при `is_empty()`); `heal()` → `medicine.use()` — ruff OK, 28 passed
- [x] Постфактум (решение 2026-11-10): все константы перенесены в `game/constants.py`
      (12 из tamagochi.py + WORK_CLICKS из game.py + DEFAULT_INCOME_PER_CLICK из clicker.py),
      модули импортируют от туда — ruff OK, 28 passed
- Проверка: ruff + pytest
- Менторские темы: магические числа; инкапсуляция мутации модели
- **Status:** complete

### Phase 4: Инкапсуляция Game
- [x] G1: `self._tamagochi` + read-only `@property tamagochi` — ruff OK, 28 passed
- [x] G2: `__init__`: `list(all_food)` / `list(all_medicine)`; свойства `food`/`medicine` → `list(...)` — ruff OK, 28 passed
- [x] G8: `Medicine.copy()` в models.py; `buy_medicine`: `self._medicine_bag.append(medicine.copy())` — ruff OK, 28 passed
- Менторские темы: инкапсуляция; мутабельные коллекции по ссылке
- Примечание: часть G1/G2 пользователь успел сделать параллельно в HEAD 5e72fb9
  (`_coins`, `_food_bag`, `_all_food`); дороботаны property `tamagochi`, копии каталога
  и свойств сумок, `Medicine.copy()`.
- **Status:** complete

### Phase 5: Исключения вместо print
- [x] Новые исключения `EmptyCatalog`, `EmptyBag` в exceptions.py (свёрнутая пара, решение 2026-11-10)
- [x] G4-G7: `raise` вместо `print/return` в buy_food/buy_medicine/feed_tamagochi/heal_tamagochi
- [x] N5+N3: main — match в try/except: `TamagochiIsGone` → «Тамагочи умер», break;
      `NotEnoughMoney`/`EmptyCatalog`/`EmptyBag` → `output = str(e)`.
      Блок `if (not game.tamagochi.is_alive)` удалён: смерть теперь всегда приходит
      исключением из `update()`, который вызывается декоратором `@tamagochi_update`
      после play/rest/heal (уточнение пользователя 2026-11-10: update в main не вызывается)
- [x] N2: main — `game.tamagochi.is_sick()` (is_sick — метод с HEAD 5e72fb9)
- Проверка: ruff + pytest (28 passed) + ручной прогон: смерть, нехватка монет, пустая сумка
- Менторские темы: исключения vs ранние возвраты; кто бросает, кто ловит
- **Status:** complete

### Phase 6: Читаемость main
- [ ] N1: `STATUS_TEMPLATE` с именованными плейсхолдерами + `print(STATUS_TEMPLATE.format(**game.get_status()))`
- [ ] N4: `MENU` — одна строка модульного уровня, один print вместо восьми
- Проверка: ruff + pytest + ручной прогон
- **Status:** pending

### Phase 7: Техническая доводка (бывшая фаза 8)
- [ ] C1: докстринг `DummyClicker` (добавить точку); PEP257-чеклист по всему проекту (models, exceptions, модульные докстринги)
- [ ] T2: докстринг `play()` — ссылки на константы вместо чисел
- [ ] (опц.) докстринг на обёртке `tamagochi_update`
- [ ] Финал: ruff check ./game, pytest ./tests, ручной прогон, проход по карте (20/20 закрыты)
- **Status:** pending

## Resolved Questions (ответы пользователя, 2026-11-10)
1. Исключения G4-G7: свёрнутая пара `EmptyCatalog` / `EmptyBag`;
   еда/лекарство различается текстом причины (`str(e)`).
2. G8: копия лекарства — метод `Medicine.copy()` в models.py.
3. (Бывш. вопрос о возвратах предмета/дохода из методов Game) — снят: G9 вне раунда.
4. Константы — не в модулях, а в общем `game/constants.py` (решение пользователя).

## Decisions Made
| Decision | Rationale |
|----------|-----------|
| G9 («Можно лучше») вне раунда | Решение пользователя 2026-11-10; `_pick` остаётся в Game, тесты с `fake_inputs` не трогаем |
| Порядок фаз: маленькое → крупное (2→3→4→5→6→7) | Запрос пользователя |
| G1: `_tamagochi` + read-only `@property tamagochi` | Не рвать main.py:45,48 и тесты в фазах 4–6 |
| T3: `Medicine.use()` не инкрементирует `uses` при `is_empty()` | Пустое лекарство не «сгорает» повторно |
| G2: копии `list(...)` при хранении и отдаче | Позиция ревьюера: каталог статичен, одного владельца нет |
| Имена исключений: `EmptyCatalog`/`EmptyBag` | Ответ пользователя (свёрнутая пара) |
| G8: `Medicine.copy()` | Ответ пользователя: копия инкапсулируется в модели |
| Константы в `game/constants.py` | Решение пользователя: баланс игры — в одном модуле, не размазан по трём |

## Errors Encountered
| Error | Attempt | Resolution |
|-------|---------|------------|
| Пока нет | 1 | — |

## Notes
- После каждого изменения: `.venv/bin/ruff check ./game`, `.venv/bin/pytest ./tests`.
- Первоначальный план: `.planning/2026-11-10-review-game-py-md/`; корневые файлы — рабочая копия, обновляем их.
- Роль ИИ: наставник-тьютор — объяснять концепции ООП/Python, направлять; код писать по запросу.