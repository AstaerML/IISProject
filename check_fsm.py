import logging
logging.basicConfig(level=logging.INFO)
from orchestrator import Orchestrator

o = Orchestrator()
phrases = [
    "Какие обязательные разделы нужно включить в паспорт?", # Ожидаем analyst
    "В чем разница между руководством и инструкцией?",      # Ожидаем analyst
    "А ты точно в этом уверен?",                            # Ожидаем verifier
    "Перепроверь свой ответ",                               # Ожидаем попытку verifier -> verifier, ОТКАТ в analyst
    "asdf qwerty",                                          # Ожидаем analyst (fallback)
    "Сгенерируй текст для паспорта",                        # Ожидаем generator
    "Проверь сгенерированный текст на ошибки"               # Ожидаем verifier
]

for p in phrases:
    intent = o.detect_intent(p)
    role = o.route("test_session", intent)
    print(f"{p[:40]: <42} интент {intent: <12} роль {role}")

o.close()