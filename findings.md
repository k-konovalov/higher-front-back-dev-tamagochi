# Findings & Decisions

## Requirements
- Закрыть 21 комментарий «Надо исправить» из 5 review-файлов (game, models, tamagochi, clicker, main).
- Закрыть рекомендацию «Можно лучше» (G9): вынести I/O из Game в main.
- Двигаться от маленьких изменений к крупным; докстринги и линтер — в конце (фаза 8).
- После изменений: `ruff check ./game` и `pytest ./tests` в .venv; код — по интерфейсам из README.

## Research Findings (проверено 2026-11-10)
- Код совпадает с версией из ревью (29.10) — ни одно из 21 замечаний ещё не исправлено.
- Базовая линия (перепроверена сегодня): `ruff check ./game` — OK; `pytest ./tests` — 28 passed (0.06 s).
- ruff.toml: line-length 79, tests/ исключены; D-правила не включены → формат докстрингов
  проверяется чеклистом ревьюера, а не линтером.
- tests/conftest.py: фабрика `make_game` создаёт `Game(tamagochi, clicker, all_food=..., all_medicine=...)`
  — сигнатура конструктора должна сохраниться.
- tests/test_logic.py гоняет меню Game через `fake_inputs`
  (test_game_buy_food_adds_inventory, test_game_feed_removes_selected_item_from_inventory,
  test_game_buy_medicine_adds_inventory) → в фазе 7 эти тесты придётся переписать на прямые вызовы по index.
- test_main_import_and_exit: `main()` при вводе «0» должен завершиться без исключений.
- test_game_feed_removes...: `selected = game.food[0]` затем `selected not in game.food` —
  останется работать, даже если property отдаст копию списка (сравнение элементов через `__eq__` датакласса).
- В `game/` нет `__init__.py` (namespace package), импорты работают, в ревью замечаний нет — не трогаем.
- Смерть питомца: `update()` уже бросает `TamagochiIsGone` при hp==0 (tamagochi.py:117-118);
  main не перехватывает его → сейчас это падение (main.py:67).
- `main.py:51` `if (not game.tamagochi.is_alive):` — баг (без вызова, bound method всегда truthy),
  смерть сейчас не обрабатывается вообще.
- Формулировки ревьюера (review.game.py.md):
  - G4-G7: «Используй исключения, в `main` перехватывай и выводи текстовое сообщение с причиной через `output» —
    имена исключений ревьюер не задает, текстом причины служит `str(e)`.
  - G8: «Добавлять нужно копию» (ссылка на SO «Make copy of object instance in Python») —
    механизм копии ревьюер не задает. Копия нужна именно для Medicine (его мутирует `heal`);
    Food в сумке не мутирует, комментарий только к `buy_medicine`.
  - G9 («Можно лучше»): «За вывод должен отвечать интерфейс, в данной реализации это `main`.
    `Game` должен только принимать данные и менять состояние. Например: `Game.buy_food(index)`
    достаёт объект из своего каталога и делает бизнес-логику» — возврат предмета/дохода ревьюер
    явно не требует, но вывод целиком переносится в main.

## Technical Decisions
| Decision | Rationale |
|----------|-----------|
| Порядок фаз: маленькое → крупное (2→3→4→5→6→7→8) | Запрос пользователя |
| G1: `_tamagochi` + read-only `@property tamagochi` | Не рвать main.py:50-51 и тесты в фазах 4–6; полное отделение в фазе 7 |
| T3: `Medicine.use()` не инкрементирует `uses` при `is_empty()` | Пустое лекарство не «сгорает» повторно |
| G2: копии `list(...)` при хранении и отдаче | Позиция ревьюера: каталог статичен, одного владельца нет |

## Open Questions (к пользователю)
1. Имена исключений (G4-G7): 4 отдельных (NoFoodInCatalog/NoMedicineInCatalog/NoFoodInBag/NoMedicineInBag)
   или свёрнутая пара (EmptyCatalog/EmptyBag)?
2. G8: механизм копии лекарства — `copy.copy`, `dataclasses.replace` или `Medicine.copy()`?
3. Фаза 7: методы Game возвращают предмет/доход (main печатает «Куплено: ...»)
   или print'ы остаются в Game (в main выносится только ввод/выбор)?

## Issues Encountered
| Issue | Resolution |
|-------|------------|
| `main.py:51` — `is_alive` без вызова (всегда truthy), смерть не обрабатывается | Закроется в фазе 5 (N3): `update()` бросает `TamagochiIsGone`, main — try/except |

## Resources
- review.game.py.md, review.models.py.md, review.tamagochi.md.md, review.clicker.py.md, review_main.py.md
- tests/test_code_structure.py, tests/test_logic.py, tests/conftest.py
- ruff.toml, pytest.ini, README.md (интерфейсы AbstractGame/AbstractTamagochi/AbstractClicker/Food/Medicine)
- Первоначальный план: .planning/2026-11-10-review-game-py-md/ (findings.md, progress.md)