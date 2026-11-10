# Task Plan: переработка «Тамагочи» по результатам ревью

## Goal
Закрыть все 21 комментарий «Надо исправить» из 5 review-файлов и рекомендацию «Можно лучше»
(вынести I/O из Game), двигаясь от маленьких изменений к крупным. Докстринги и линтер — на конец.

## Next Step
Получить ответы на 3 вопроса (Key Questions), затем Phase 2: микро-фиксы M1 → T4 → G3 → C2
(по одному изменению, ruff + pytest после каждого).

## Current Phase
Phase 2 (ждём ответы на 3 вопроса)

## Карта ревью-комментариев (21 шт.)
| ID | Файл (текущая строка) | Комментарий | Фаза |
|----|----------------------|-------------|------|
| M1  | game/models.py:4,14-16,28,37 | убрать «учебные» комментарии | 2 |
| T4  | game/tamagochi.py:117 | `self._hp == 0` → `is_alive()` | 2 |
| G3  | game/game.py:145 | `ValueError` в `_pick` | 2 |
| C2  | game/clicker.py:29 | дефолт `10` → константа | 2 |
| T1  | game/tamagochi.py:35-37,69,78,88,100,114 | магические числа → константы | 3 |
| T3  | game/tamagochi.py:106 + models.py | `medicine.uses += 1` → `Medicine.use()` | 3 |
| G1  | game/game.py:111 | `self.tamagochi` → `_tamagochi` | 4 |
| G2  | game/game.py:112-113,279,298 | каталог/сумки по ссылке → копии | 4 |
| G8  | game/game.py:194 | в сумку добавлять копию лекарства | 4 |
| G4-G7 | game/game.py:157,180,204,229 | print «пусто» → исключения | 5 |
| N5  | main.py:60 | перехват `NotEnoughMoney` (и новых) в main | 5 |
| N2  | main.py:50 | `is_sick` → `is_sick()` | 5 |
| N3  | main.py:51 | смерть: `TamagochiIsGone` из `update()`, main — try/except | 5 |
| N1  | main.py:41-44 | статус: шаблон + `format(**dict)`, без локальной переменной | 6 |
| N4  | main.py:52-59 | меню: одна константа модульного уровня | 6 |
| G9  | game/game.py (весь класс) | «Можно лучше»: I/O в main, Game принимает index | 7 |
| C1  | game/clicker.py:27 | докстринг PEP257 (точка) + проверить весь проект | 8 |
| T2  | game/tamagochi.py:69-71 | числа в докстринге `play` → ссылки на константы | 8 |

Базовая линия (2026-11-10, перевпроверена): `ruff check ./game` — OK; `pytest ./tests` — 28 passed.
Код совпадает с версией из ревью (29.10).

## Phases

### Phase 1: Разведка
- [x] Прочитаны все 5 review-файлов, комментарии сопоставлены с кодом
- [x] Прочитаны tests/ и conftest (ограничения для фазы 7)
- [x] Конфиги ruff.toml / pytest.ini (D-правила не включены)
- [x] Базовая линия ruff + pytest — зелёная
- **Status:** complete

### Phase 2: Локальные микро-фиксы (по одному, ruff+pytest после каждого)
- [ ] M1: models.py — убрать комментарии `# наименование` и т.п.
- [ ] T4: `update()`: `if not self.is_alive(): raise TamagochiIsGone`
- [ ] G3: `_pick()`: `try/except ValueError` → «неверный выбор», continue
- [ ] C2: clicker.py: `DEFAULT_INCOME_PER_CLICK = 10` в дефолте аргумента
- Менторские темы: защищённые атрибуты; обработка ошибки конвертации ввода
- **Status:** pending

### Phase 3: Константы и Medicine.use()
- [ ] T1: константы вверху tamagochi.py: начальные hp/energy, лимит голода, дельты play/rest/update/болезни
- [ ] (опц.) game.py: `WORK_CLICKS = 5` в `work()`; main.py: убрать явный `income_per_click=10` (дефолт кликера)
- [ ] T3: `Medicine.use()` в models.py (не инкрементить при `is_empty()`); `heal()` → `medicine.use()`
- Проверка: ruff + pytest
- Менторские темы: магические числа; инкапсуляция мутации модели
- **Status:** pending

### Phase 4: Инкапсуляция Game
- [ ] G1: `self._tamagochi` + read-only `@property tamagochi` (main.py:50-51 и тесты не ломаются)
- [ ] G2: `__init__`: `list(all_food)` / `list(all_medicine)`; свойства `food`/`medicine` → `list(self._food_bag)` / `list(self._medicine_bag)`
- [ ] G8: `buy_medicine`: добавить копию лекарства (механизм — вопрос 2)
- Проверка: ruff + pytest
- Менторские темы: public/protected, getter-property, копия списка vs копия объекта
- **Status:** pending

### Phase 5: Исключения вместо print
- [ ] Новые исключения в exceptions.py (имена — вопрос 1)
- [ ] G4-G7: `raise` вместо `print/return` в buy_food/buy_medicine/feed_tamagochi/heal_tamagochi
- [ ] N5: main — try/except (`NotEnoughMoney`, новые, `TamagochiIsGone`) вокруг действий и `update()` → `output = str(e)`; при смерти — завершить игру
- [ ] N2: `game.tamagochi.is_sick()`
- [ ] N3: удалить `if not game.tamagochi.is_alive` из цикла main (смерть сигнализирует `update()`)
- Проверка: ruff + pytest (test_main_import_and_exit с «0» остаётся зелёным)
- Менторские темы: исключения vs ранние возвраты; кто бросает, кто ловит
- **Status:** pending

### Phase 6: Читаемость main
- [ ] N1: `STATUS_TEMPLATE` с именованными плейсхолдерами + `print(STATUS_TEMPLATE.format(**game.get_status()))`
- [ ] N4: `MENU` — одна строка модульного уровня (join "\n"), один print вместо восьми
- Проверка: ruff + pytest + ручной прогон
- **Status:** pending

### Phase 7: Крупный рефактор — I/O вне Game (G9, «Можно лучше»)
- [ ] AbstractGame: `buy_food(index)`, `buy_medicine(index)`, `feed_tamagochi(index)`, `heal_tamagochi(index)`
- [ ] Game: убрать `_pick` и все print/input; поведение методов — вопрос 3; исключения при неверном index / пустой сумке
- [ ] main: меню из `game.food`/`game.medicine`, чтение и разбор выбора (ValueError, вне диапазона, «0» = отмена), вызов по index, вывод результата
- [ ] Тесты: test_logic.py — `game.buy_food(0)` и т.д. вместо `fake_inputs`
- Проверка: ruff + pytest + ручной прогон игры
- Менторские темы: разделение логики и интерфейса (SRP); как подключится GUI
- **Status:** pending

### Phase 8: Техническая доводка
- [ ] C1: докстринг `DummyClicker` (добавить точку); прогнать PEP257-чеклист по всему проекту (models, exceptions, модульные докстринги)
- [ ] T2: докстринг `play()` — ссылки на константы вместо чисел
- [ ] (опц.) докстринг на обёртке `tamagochi_update`
- [ ] Финал: ruff check ./game, pytest ./tests, ручной прогон, проход по карте комментариев (все закрыты)
- **Status:** pending

## Key Questions
1. Имена исключений для пустого каталога/сумки (G4-G7): 4 отдельных
   (NoFoodInCatalog/NoMedicineInCatalog/NoFoodInBag/NoMedicineInBag) или свёрнутая пара (EmptyCatalog/EmptyBag)?
2. G8: какой механизм копии лекарства — `copy.copy`, `dataclasses.replace` или метод `Medicine.copy()`?
3. Фаза 7: возвращать ли из методов Game предмет/доход, чтобы main печатал «Куплено: ...»,
   или вывод оставить через print'ы Game (только ввод/выбор вынести в main)?

## Decisions Made
| Decision | Rationale |
|----------|-----------|
| Порядок фаз: маленькое → крупное (2→3→4→5→6→7→8) | Запрос пользователя |
| G1: `_tamagochi` + read-only `@property tamagochi` | Не рвать main.py:50-51 и тесты в фазах 4–6; полное отделение main'а от объекта тамагочи в фазе 7 |
| T3: `Medicine.use()` не инкрементирует `uses` при `is_empty()` | Пустое лекарство не «сгорает» повторно |
| G2: копии `list(...)` при хранении и отдаче | Позиция ревьюера: каталог статичен, одного владельца нет; при появлении ShopService — ссылка |

## Errors Encountered
| Error | Attempt | Resolution |
|-------|---------|------------|
| Пока нет | 1 | — |

## Notes
- После каждого изменения: `.venv/bin/ruff check ./game`, `.venv/bin/pytest ./tests`.
- Детальный первоначальный план: `.planning/2026-11-10-review-game-py-md/` (создан в тот же день);
  корневые файлы — рабочая копия, обновляем их.
- Роль ИИ: наставник-тьютор — объяснять концепции ООП/Python, направлять; код писать по запросу.