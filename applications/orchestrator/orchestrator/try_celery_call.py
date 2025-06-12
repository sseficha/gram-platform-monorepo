from orchestrator.workers.tasks.create_process import foo

res = foo.delay()
print(f"Task ID: {res.id}")
print(f"Task Result: {res.get(timeout=2)}")
