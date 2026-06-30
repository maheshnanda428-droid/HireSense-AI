import os
import json
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

MODEL = "llama-3.1-8b-instant"


def evaluate_resume(resume_text):

    prompt = f"""
You are an expert ATS (Applicant Tracking System), Senior HR Recruiter, and Technical Interviewer with over 15 years of experience hiring Software Engineers.

Analyze the resume professionally.

Evaluate ONLY these sections:

1. Professional Summary
2. Technical Skills
3. Projects
4. Education
5. Internship / Experience
6. Certifications

For every section:
- Give a rating out of 10.
- Mention strengths.
- Mention weaknesses.
- Suggest improvements.

Then provide:

1. Overall Evaluation
2. ATS Readiness Score (0-100)
3. Top Strengths
4. Key Weaknesses
5. Recommendations
6. Five interview questions based on the resume.
7. Rewrite the Professional Summary to industry standards.

Return ONLY valid JSON in EXACTLY this format:

{{
    "overall_evaluation": "",

    "ats_score": 0,

    "section_ratings": {{
        "professional_summary": 0,
        "technical_skills": 0,
        "projects": 0,
        "education": 0,
        "experience": 0,
        "certifications": 0
    }},

    "strengths": [],

    "weaknesses": [],

    "recommendations": [],

    "interview_questions": [],

    "resume_summary": ""
}}

Rules:

- Return ONLY valid JSON.
- Do NOT use markdown.
- Do NOT explain outside JSON.
- strengths should contain exactly 5 concise points.
- weaknesses should contain exactly 5 concise points.
- recommendations should contain exactly 5 actionable points.
- interview_questions should contain exactly 5 software engineering interview questions based on the resume.
- resume_summary should be between 80 and 120 words.
- ats_score should realistically reflect the resume quality.
- Ratings must be realistic and consistent with the ATS score.

Resume:

{resume_text}
"""

    try:

        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.2,
            response_format={"type": "json_object"}
        )

        print("\n========== GROQ RESPONSE ==========\n")
        print(response.choices[0].message.content)

        ai_result = json.loads(
            response.choices[0].message.content
        )

        return ai_result

    except Exception as e:

        print("AI Error:", e)

        return {
            "overall_evaluation": "Unable to analyze the resume at the moment.",

            "ats_score": 0,

            "section_ratings": {
                "professional_summary": 0,
                "technical_skills": 0,
                "projects": 0,
                "education": 0,
                "experience": 0,
                "certifications": 0
            },

            "strengths": [],

            "weaknesses": [],

            "recommendations": [],

            "interview_questions": [],

            "resume_summary": ""
        }