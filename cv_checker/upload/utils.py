import pdfplumber
import re
from .models import JDKeyword


# Extract text from any PDF
def extract_text_from_pdf(file_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text


#  Normalize text: lowercase, remove symbols, split into words
def normalize(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    return set(text.split())


#  Keyword-based ATS using predefined JDKeyword table
def keyword_ats(resume_text):
    resume_text = resume_text.lower()
    keywords = JDKeyword.objects.all()

    matched = []
    missing = []

    for k in keywords:
        if k.keyword.lower() in resume_text:
            matched.append(k.keyword)
        else:
            missing.append(k.keyword)

    total = keywords.count()
    score = int((len(matched) / total) * 100) if total > 0 else 0

    return score, matched, missing


#  CV vs Ideal CV 
def compare_cvs(user_text, ideal_text):
    user_words = normalize(user_text)
    ideal_words = normalize(ideal_text)

    if not ideal_words:
        return 0, [], []

    matched = user_words & ideal_words
    missing = ideal_words - user_words

    score = int((len(matched) / len(ideal_words)) * 100)

    return score, list(matched), list(missing)
