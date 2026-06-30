from fastapi import APIRouter
from fastapi.responses import FileResponse

from services.pdf_report import generate_pdf

router = APIRouter()


@router.post("/download-report")
def download_report(data: dict):

    pdf = generate_pdf(data)

    return FileResponse(
        pdf,
        filename="HireSense_Report.pdf"
    )