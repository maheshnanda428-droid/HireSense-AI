import re


def analyze_resume(text):

    text = text.lower()

    result = {}

    result["python"] = "python" in text
    result["c"] = "c" in text
    result["c++"] = "c++" in text
    result["sql"] = "sql" in text
    result["git"] = "git" in text
    result["github"] = "github" in text
    result["machine_learning"] = "machine learning" in text
    result["internship"] = "intern" in text
    result["leadership"] = "lead" in text
    result["projects"] = "project" in text
    result["certifications"] = "certification" in text

    return result