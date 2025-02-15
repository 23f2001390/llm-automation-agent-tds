from fastapi import APIRouter, HTTPException
from models.task import RunTaskRequest, RunTaskResponse
from core.tasks import execute_task

router = APIRouter()


@router.post("/run", response_model=RunTaskResponse)
async def run_task(request: RunTaskRequest) -> RunTaskResponse:
    """Runs a specified task."""
    response = execute_task(request)
    if response.error:
        #  Raise an HTTPException that will return a 500 status code.
        raise HTTPException(status_code=500, detail=f"Execution error: {response.error}")
    return response 