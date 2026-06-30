from fastapi import APIRouter
from pydantic import BaseModel

from services.jd_matcher import match_job_description

router = APIRouter()

class JobRequest(BaseModel):
    resume_text: str
    job_description: str

@router.post("/job-match")
def job_match(request: JobRequest):

    return match_job_description(
        request.resume_text,
        request.job_description
    )