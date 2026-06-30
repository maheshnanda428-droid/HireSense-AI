import re

def calculate_score(text):

    text = text.lower()

    score = 0
    suggestions = []

    # Professional Summary
    if "summary" in text or "objective" in text:
        score += 15
    else:
        suggestions.append("Add a Professional Summary.")

    # Skills
    skills = [
        "python","c","c++","java","javascript",
        "html","css","sql","react","node",
        "fastapi","machine learning","tensorflow",
        "opencv","git","github"
    ]

    found = sum(1 for skill in skills if skill in text)

    skill_score = min(found * 2, 20)
    score += skill_score

    if skill_score < 12:
        suggestions.append("Add more relevant technical skills.")

    # Projects
    project_words = [
        "project",
        "developed",
        "implemented",
        "designed",
        "built"
    ]

    project_score = 0

    for word in project_words:
        if word in text:
            project_score += 5

    project_score = min(project_score, 25)

    score += project_score

    if project_score < 15:
        suggestions.append("Describe projects using action verbs and measurable outcomes.")

    # Education
    if "b.e" in text or "b.tech" in text or "cgpa" in text:
        score += 10
    else:
        suggestions.append("Complete your education details.")

    # Internship / Experience
    if "intern" in text or "experience" in text:
        score += 15
    else:
        suggestions.append("Mention internship or work experience.")

    # Certifications
    if "certification" in text or "nptel" in text:
        score += 10
    else:
        suggestions.append("Add certifications.")

    # GitHub / LinkedIn
    if "github.com" in text:
        score += 3
    else:
        suggestions.append("Add your GitHub profile.")

    if "linkedin.com" in text:
        score += 2
    else:
        suggestions.append("Add your LinkedIn profile.")

    score = min(score, 100)

    return score, suggestions