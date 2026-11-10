# Findings & Decisions

## Факты (проверено 2026-11-10)
- Код совпадает с версией из ревью (29.10) — ни одно из 21 замечаний ещё не исправлено.
- Базовая линия: `ruff check ./game` — OK; `pytest ./tests` — 28 passed (0.05 s).
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

## Решения
- Порядок фаз: маленькое → крупное (по запросу пользователя): 2 микро → 3 константы →
  4 инкапсуляция → 5 исключения → 6 читаемость main → 7 рефактор I/O → 8 докстринги/линт.
- G1: кроме `_tamagochi` делаем read-only `@property tamagochi`, чтобы не рвать main.py:50-51
  и тесты в фазах 4–6; полное отделение main'а от объекта тамагочи произойдёт в фазе 7.
- T3: `Medicine.use()` не инкрементирует `uses`, если `is_empty()`.
- G2: пока каталог статичен и у него один владелец — копии `list(...)` при хранении и отдаче
  (позиция ревьюера); при появлении ShopService можно перейти к ссылке.

## Вопросы к пользователю
1. Имена исключений для пустого каталога/сумки (G4-G7): 4 отдельных
   (NoFoodInCatalog/NoMedicineInCatalog/NoFoodInBag/NoMedicineInBag) или свёрнутая пара (EmptyCatalog/EmptyBag)?
2. G8: какой механизм копии лекарства — `copy.copy`, `dataclasses.replace` или метод `Medicine.copy()`?
3. Фаза 7: возвращать ли из методов Game предмет/доход, чтобы main печатал «Куплено: ...»,
   или вывод оставить единым через `output` (как сейчас)?