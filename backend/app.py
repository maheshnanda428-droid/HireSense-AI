from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.report import router as report_router
from routes.resume import router as resume_router
from routes.job import router as job_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "https://hire-sense-ai-iota.vercel.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(report_router)
app.include_router(resume_router)
app.include_router(job_router)