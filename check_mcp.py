from orchestrator import Orchestrator

o = Orchestrator()
# Первый вызов займет несколько секунд на запуск сервера и подъем индекса
for c in o.tools.search("Как правильно оформить таблицу регистрации изменений?"):
    page = f" (стр. {c.page})" if c.page else ""
    print(f"[{c.score:.3f}] {c.source}{page} [{c.category}]")

o.close()