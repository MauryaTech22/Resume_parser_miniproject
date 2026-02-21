import re
import spacy

nlp = spacy.load("en_core_web_sm")

SKILLS_DB = [
    "Python", "Java", "C++", "SQL", "Machine Learning",
    "Deep Learning", "Data Analysis", "HTML", "CSS",
    "JavaScript", "React", "Django", "Flask"
]

def extract_name(text):
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return ent.text
    return None


def extract_email(text):
    pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    match = re.search(pattern, text)
    return match.group(0) if match else None


def extract_phone(text):
    pattern = r'\+?\d[\d -]{8,12}\d'
    match = re.search(pattern, text)
    return match.group(0) if match else None


def extract_skills(text):
    found_skills = []
    for skill in SKILLS_DB:
        if skill.lower() in text.lower():
            found_skills.append(skill)
    return list(set(found_skills))


def extract_education(text):
    education_keywords = ["B.Tech", "BSc", "MSc", "Bachelor", "Master", "PhD"]
    education = []
    for word in education_keywords:
        if word.lower() in text.lower():
            education.append(word)
    return list(set(education))


def extract_experience(text):
    pattern = r'(\d+)\+?\s*(years|yrs)'
    matches = re.findall(pattern, text.lower())
    return matches


def parse_resume(text):
    data = {
        "Name": extract_name(text),
        "Email": extract_email(text),
        "Phone": extract_phone(text),
        "Skills": extract_skills(text),
        "Education": extract_education(text),
        "Experience": extract_experience(text)
    }
    return data