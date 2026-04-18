from app.database import SessionLocal
from app.models import Task

db = SessionLocal()

tasks = [
    Task(title="Sport"),
    Task(title="Cook", is_done=True),
    Task(title="eat", is_done=True),
]

db.add_all(tasks)
db.commit()
for task in tasks:
    db.refresh(task)
    print(task.id, task.title)

db.close()
