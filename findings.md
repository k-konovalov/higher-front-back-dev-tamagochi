# Findings & Decisions

## Requirements
- Закрыть 20 комментариев «Надо исправить» из 5 review-файлов (game, models, tamagochi, clicker, main).
- «Можно лучше» (G9, вынос I/O из Game) — вне раунда (решение пользователя, 2026-11-10).
- Двигаться от маленьких изменений к крупным; докстринги и линтер — в конце (фаза 7).
- После изменений: `ruff check ./game` и `pytest ./tests` в .venv; код — по интерфейсам из README.

## Research Findings (проверено 2026-11-10)
- Код совпадает с версией из ревью (29.10) — ни одно из 20 замечаний «Надо исправить» ещё не исправлено.
- Базовая линия (перепроверена сегодня): `ruff check ./game` — OK; `pytest ./tests` — 28 passed (0.06 s).
- ruff.toml: line-length 79, tests/ исключены; D-правила не включены → формат докстрингов
  проверяется чеклистом ревьюера, а не линтером.
- tests/conftest.py: фабрика `make_game` создаёт `Game(tamagochi, clicker, all_food=..., all_medicine=...)`
  — сигнатура конструктора должна сохраниться.
- tests/test_logic.py гоняет меню Game через `fake_inputs`
  (test_game_buy_food_adds_inventory, test_game_feed_removes_selected_item_from_inventory,
  test_game_buy_medicine_adds_inventory) → не трогаем (G9 вне раунда).
- test_main_import_and_exit: `main()` при вводе «0» должен завершиться без исключений.
- test_game_feed_removes...: `selected = game.food[0]` затем `selected not in game.food` —
  останется работать, даже если property отдаст копию списка (сравнение элементов через `__eq__` датакласса).
- В `game/` нет `__init__.py` (namespace package), импорты работают, в ревью замечаний нет — не трогаем.
- Смерть питомца: `update()` уже бросает `TamagochiIsGone` при hp==0 (tamagochi.py:197-198);
  main не перехватывает его → сейчас это падение (main.py:61-86, match по действиям).
- `main.py:48` `if (not game.tamagochi.is_alive):` — баг (без вызова, bound method всегда truthy),
  смерть сейчас не обрабатывается вообще.
- `main.py:45` `if game.tamagochi.is_sick:` — та же проблема (без вызова, всегда truthy).
- M1 (models.py): ревью-комментарий один, на поле `Food.name`
  («Учебные и стандартные комментарии лучше удалить») — распространяется на все инлайн-
  комментарии полей (8 шт.: Food 3, Medicine 5).
- Формулировки ревьюера (review.game.py.md):
  - G4-G7: «Используй исключения, в `main` перехватывай и выводи текстовое сообщение с причиной через `output» —
    имена исключений ревьюер не задает, текстом причины служит `str(e)`.
  - G8: «Добавлять нужно копию» (ссылка на SO «Make copy of object instance in Python») —
    комментарий только к `buy_medicine`; Food в сумке не мутирует.
  - G9 («Можно лучше»): I/O в main, `Game.buy_food(index)` — вне раунда.

## Technical Decisions
| Decision | Rationale |
|----------|-----------|
| G9 («Можно лучше») вне раунда | Решение пользователя 2026-11-10 |
| Порядок фаз: маленькое → крупное (2→3→4→5→6→7) | Запрос пользователя |
| G1: `_tamagochi` + read-only `@property tamagochi` | Не рвать main.py:45,48 и тесты в фазах 4–6 |
| T3: `Medicine.use()` не инкрементирует `uses` при `is_empty()` | Пустое лекарство не «сгорает» повторно |
| G2: копии `list(...)` при хранении и отдаче | Позиция ревьюера: каталог статичен, одного владельца нет |
| Исключения: `EmptyCatalog` / `EmptyBag` (свёрнутая пара) | Ответ пользователя 2026-11-10; различие — в `str(e)` |
| G8: копия лекарства — метод `Medicine.copy()` | Ответ пользователя 2026-11-10; инкапсуляция в модели |

## Resolved Questions
1. Имена исключений (G4-G7): свёрнутая пара `EmptyCatalog`/`EmptyBag` (ответ пользователя).
2. G8: механизм копии — `Medicine.copy()` (ответ пользователя).
3. Возвраты предмета/дохода из методов Game: снят (G9 вне раунда).

## Issues Encountered
| Issue | Resolution |
|-------|------------|
| `main.py:48` — `is_alive` без вызова (всегда truthy), смерть не обрабатывается | Закроется в фазе 5 (N3): `update()` бросает `TamagochiIsGone`, main — try/except |
| `main.py:45` — `is_sick` без вызова | Закроется в фазе 5 (N2) |

## Resources
- review.game.py.md, review.models.py.md, review.tamagochi.md.md, review.clicker.py.md, review_main.py.md
- tests/test_code_structure.py, tests/test_logic.py, tests/conftest.py
- ruff.toml, pytest.ini, README.md (интерфейсы AbstractGame/AbstractTamagochi/AbstractClicker/Food/Medicine)
- Первоначальный план: .planning/2026-11-10-review-game-py-md/ (findings.md, progress.md)