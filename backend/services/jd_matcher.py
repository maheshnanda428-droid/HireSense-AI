import os
import json

from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

MODEL = "llama-3.1-8b-instant"

def match_job_description(resume, jd):

    prompt = f"""
Compare this resume with the job description.

Return ONLY JSON.

{{
"match_score":0,
"matching_skills":[],
"missing_skills":[],
"recommendations":[]
}}

Resume:

{resume}

Job Description:

{jd}
"""

    response = client.chat.completions.create(

        model=MODEL,

        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ],

        response_format={"type":"json_object"},

        temperature=0.2

    )

    return json.loads(
        response.choices[0].message.content
    )