from app.database import SessionLocal
from app.models import Task

db = SessionLocal()

tasks = [
    Task(title="Sport"),
    Task(title="Cook", is_done=True),
    Task(title="eat", is_done=True),
]

db.add_all(tasks)
for task in tasks:
    db.commit()
    print(task.id, task.title)

db.close()