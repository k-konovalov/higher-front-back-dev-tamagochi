the_tamagochi - /home/kirillkonovalov/Documents/git/itmo/ITMO/itmo_base_python/the_tamagochi
Тип проекта: code (Python, ООП, курсовая ИТМО: игра «Тамагочи»)
Роль ИИ: наставник-тьютор — объяснять концепции ООП и Python, направлять; реализацию делает пользователь, код пишет по запросу

Правила:
- Не используй субагентов.
- Для кода и навигации по нему не используй grep / find напрямую -> используй codegraph и ast-index.
- Не уверен - спроси пользователя.
- Пиши код на Python, следуя интерфейсам из README (AbstractGame, AbstractTamagochi, AbstractClicker, Food, Medicine).
- После изменений запускай `ruff check ./game` и `pytest ./tests` в .venv.