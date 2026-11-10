# Progress Log

## Session: 2026-11-10
- Создан именованный план `.planning/2026-11-10-review-game-py-md/` (разведка: 5 review-файлов,
  21 комментарий сопоставлен с кодом; прочитаны tests/, conftest.py, ruff.toml, pytest.ini).
- `pwf_init` (без имени): рабочая копия плана в корне проекта, mode legacy, attested no.
- Решение пользователя: G9 («Можно лучше», крупный рефактор I/O) — вне раунда.
- Ответы пользователя: исключения — свёрнутая пара `EmptyCatalog`/`EmptyBag`;
  копия лекарства — `Medicine.copy()`.
- ВАЖНО: между чтениями HEAD сместился до `5e72fb9 F-4: review-1 - 2` —
  докстринги/`__repr__` уже в коммитах (частичное C1), есть stash `WIP on features/game`.
  Базовая линия перепроверена на HEAD: ruff OK, 28 passed. Карта строк актуальна.
  Замечено: main.py:48 `game.tamagochi.is_alive` — метод как свойство (всегда False) — закрывается N3.
- Фаза 2 завершена (M1, T4, G3, C2); ruff + pytest зелёные после каждого шага,
  G3 проверен ручным прогоном (non-numeric input → повтор).

## Test Results
| Test | Input | Expected | Actual | Status |
|------|-------|----------|--------|--------|
| ruff check ./game | .venv, HEAD 5e72fb9 | All checks passed | All checks passed! | OK |
| pytest ./tests | .venv, HEAD 5e72fb9 | 28 passed | 28 passed | OK |
| ruff+pytest | после M1 (models.py) | green | green | OK |
| ruff+pytest | после T4 (tamagochi.py) | green | green | OK |
| ruff+pytest | после G3 (game.py) | green | green | OK |
| ручной прогон _pick | input "abc"→"1" | повтор запроса, покупка | как ожидается | OK |
| ruff+pytest | после C2 (clicker.py) | green | green | OK |

## Error Log
| Timestamp | Error | Attempt | Resolution |
|-----------|-------|---------|------------|
| 2026-11-10 | Дубль `DEFAULT_INCOME_PER_CLICK` в clicker.py (два edit) | 1 | Второй блок удалён, константа вверху модуля |

## 5-Question Reboot Check
| Question | Answer |
|----------|--------|
| Where am I? | Phase 2 complete, Phase 3 next (T1 → T3) |
| Where am I going? | Phases 3–7 (карта в task_plan.md) |
| What's the goal? | Закрыть 20 «Надо исправить»; G9 вне раунда |
| What have I learned? | findings.md; HEAD=5e72fb9 (F-4 review-1/2 уже в коде) |
| What have I done? | M1, T4, G3, C2 — см. Phase 2 task_plan.md |

## Next Step
Phase 3: T1 (константы в tamagochi.py: INITIAL_HP/INITIAL_ENERGY, HUNGER_LIMIT, дельты) →
опц. `WORK_CLICKS` в game.py и убрать явный `income_per_click=10` в main.py →
T3 (`Medicine.use()`, не инкрементить при `is_empty()`; `heal()` → `medicine.use()`).