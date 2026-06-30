import os

from fastapi import APIRouter, UploadFile, File, HTTPException

from services.parser import extract_text
from services.ats import calculate_score
from services.ai_service import evaluate_resume

router = APIRouter()

UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@router.post("/upload")
async def upload_resume(file: UploadFile = File(...)):

    try:

        # Save uploaded PDF
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)

        with open(filepath, "wb") as f:
            f.write(await file.read())

        # Extract text from PDF
        text = extract_text(filepath)

        if not text.strip():
            raise HTTPException(
                status_code=400,
                detail="No readable text found inside PDF."
            )

        # ATS Score
        score, suggestions = calculate_score(text)

        # AI Analysis
        ai_feedback = evaluate_resume(text)
        print(ai_feedback)

        # Return complete response
        return {
            "score": score,
            "suggestions": suggestions,
            "ai": ai_feedback,
            "resume_text": text
        }

    except Exception as e:

        print("Error:", e)

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )