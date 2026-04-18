from app.database import SessionLocal
from app.models import Task

db = SessionLocal()

task1 = Task(title="Task1", is_done=True)

db.add(task1)
db.commit()
db.refresh(task1)

print(task1.id, task1.title)
db.close()
