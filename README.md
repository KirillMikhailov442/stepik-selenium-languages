# stepik-selenium-languages

Решение задания 3.6.10 курса «Автоматизация тестирования с помощью Selenium и Python».

Требуются Python 3 и установленный Google Chrome.

```sh
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest --language=es test_items.py
pytest --language=fr test_items.py
```

Параметр `--language` задаёт предпочитаемый язык браузера (по умолчанию `en`).
Фикстура `browser` создаёт Chrome и закрывает его после теста, включая случай ошибки.
Тест ожидает появления уникальной кнопки добавления товара в корзину и проверяет,
что она доступна. Selenium Manager автоматически подбирает драйвер Chrome.
