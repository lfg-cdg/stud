from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Task
from app.schemas import CreateTask, PatchTask, ResponseTask, UpdateTask

router = APIRouter(prefix="/tasks", tags=["Tasks"])


def get_task_or_404(task_id: int, db: Session = Depends(get_db)) -> Task:
    task = db.query(Task).filter(Task.id == task_id).first()

    if not task:
        raise HTTPException(status_code=404, detail="Task not found!")

    return task


@router.post("/", response_model=ResponseTask, status_code=201)
def create_task(task: CreateTask, db: Session = Depends(get_db)):
    new_task = Task(**task.model_dump())

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task


@router.get("/", response_model=list[ResponseTask])
def get_all_tasks(db: Session = Depends(get_db)):
    tasks = db.query(Task).all()

    return tasks


@router.get("/active", response_model=list[ResponseTask])
def get_active_tasks(db: Session = Depends(get_db)):
    tasks = db.query(Task).filter(Task.is_done.is_(False)).all()

    return tasks


@router.get("/{task_id}", response_model=ResponseTask)
def get_task_by_id(task_id: int, db: Session = Depends(get_db)):
    task = get_task_or_404(task_id, db)

    return task


@router.put("/{task_id}", response_model=ResponseTask)
def update_task(task_id: int, new_task: UpdateTask, db: Session = Depends(get_db)):
    task = get_task_or_404(task_id, db)

    for key, value in new_task.model_dump().items():
        setattr(task, key, value)

    db.commit()
    db.refresh(task)

    return task


@router.patch("/{task_id}", response_model=ResponseTask)
def patch_task(task_id: int, patch: PatchTask, db: Session = Depends(get_db)):
    task = get_task_or_404(task_id, db)

    new_task = patch.model_dump(exclude_unset=True)
    for key, value in new_task.items():
        setattr(task, key, value)

    db.commit()
    db.refresh(task)

    return task


@router.delete("/{task_id}", status_code=200)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = get_task_or_404(task_id, db)

    db.delete(task)
    db.commit()

    return {"message": "Task deleted!"}
