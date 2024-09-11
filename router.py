from typing import Annotated

from repository import TaskRepository
from schemas import STaskAdd, STask, STaskId

from fastapi import APIRouter, Depends

router = APIRouter(
    prefix="/tasks",
    tags=["Таски"],
)


@router.post("/tasks")
async def add_tasks(
        task: Annotated[STaskAdd, Depends()]
) -> STaskId:
    task_id = await TaskRepository.add_one(task)
    return {"ok": True, "task_id": task_id}


@router.get("/tasks")
async def get_tasks() -> list[STask]:
    tasks = await TaskRepository.find_all()
    return tasks
