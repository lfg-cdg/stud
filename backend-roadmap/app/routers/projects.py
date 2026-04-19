from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Project
from app.schemas import ProjectCreate, ProjectResponse, ProjectUpdate

router = APIRouter(prefix="/projects", tags=["Projects"])


def get_project_or_404(project_id: int, db: Session = Depends(get_db)) -> Project:
    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found!")

    return project


@router.post("/", status_code=201, response_model=ProjectResponse)
def create_project(project: ProjectCreate, db: Session = Depends(get_db)):
    new_project = Project(**project.model_dump())

    db.add(new_project)
    db.commit()
    db.refresh(new_project)

    return new_project


@router.get("/", response_model=list[ProjectResponse])
def get_projects(db: Session = Depends(get_db)):
    projects = db.query(Project).all()
    return projects


@router.get("/done", response_model=list[ProjectResponse])
def get_done_projects(db: Session = Depends(get_db)):
    done_projects = db.query(Project).filter(Project.is_done.is_(True)).all()

    return done_projects


@router.get("/{project_id}", response_model=ProjectResponse)
def get_project_by_id(project_id: int, db: Session = Depends(get_db)):
    return get_project_or_404(project_id, db)


@router.delete("/{project_id}", status_code=200)
def delete_project(project_id: int, db: Session = Depends(get_db)):
    project = get_project_or_404(project_id, db)

    db.delete(project)
    db.commit()

    return {"message": "project deleted!"}


@router.put("/{project_id}", response_model=ProjectResponse)
def update_projects(project_id: int, new_project: ProjectUpdate, db: Session = Depends(get_db)):
    project = get_project_or_404(project_id, db)

    for key, value in new_project.model_dump().items():
        setattr(project, key, value)

    db.commit()
    db.refresh(project)

    return project
