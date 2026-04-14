from fastapi import APIRouter, HTTPException

from app.schemas import ProjectCreate, ProjectUpdate

router = APIRouter(prefix="/projects", tags=["Projects"])


projects = []
project_id_counter = 0


@router.post("/", status_code=201)
def create_project(project: ProjectCreate):
    global project_id_counter
    project_id_counter += 1

    created_project = {"id": project_id_counter, **project.model_dump()}
    projects.append(created_project)

    return created_project


@router.get("/")
def check_projects():
    return projects


@router.get("/{project_id}")
def check_project_by_id(project_id: int):
    for project in projects:
        if project["id"] == project_id:
            return project

    raise HTTPException(status_code=404, detail="Project not found")


@router.put("/{project_id}")
def update_projects(project_id: int, new_project: ProjectUpdate):
    for project in projects:
        if project["id"] == project_id:
            project.update(new_project.model_dump())
            return project

    raise HTTPException(status_code=404, detail="Project not found")


@router.delete("/{project_id}")
def delete_project(project_id: int):
    for project in projects:
        if project["id"] == project_id:
            projects.remove(project)
            return {"message": "Project deleted!"}

    raise HTTPException(status_code=404, detail="Project not found")
