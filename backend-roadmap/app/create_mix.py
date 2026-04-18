from app.database import SessionLocal
from app.models import Task, User

task1 = Task(title="task1", is_done=True)
user1 = User(username="huesos", email="jopa@yandex.ru")

db = SessionLocal()

db.add(task1)
db.add(user1)
db.commit()
db.refresh(task1)
db.refresh(user1)

print(task1.id, task1.title)
print(user1.id, user1.username, user1.email)

db.close()