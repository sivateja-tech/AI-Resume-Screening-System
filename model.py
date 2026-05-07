import PyPDF2

skills = {
    'Python': ['python', 'flask', 'django'],
    'Java': ['java', 'spring'],
    'Web Development': ['html', 'css', 'javascript', 'react'],
    'Machine Learning': ['machine learning', 'tensorflow', 'scikit']
}


def extract_text_from_pdf(pdf_path):
    text = ''

    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)

        for page in reader.pages:
            text += page.extract_text()

    return text.lower()


def predict_resume(pdf_path):
    text = extract_text_from_pdf(pdf_path)

    matched_skills = []

    for category, keywords in skills.items():
        for keyword in keywords:
            if keyword in text:
                matched_skills.append(category)
                break

    if matched_skills:
        return f'Skills Detected: {", ".join(matched_skills)}'
    else:
        return 'No matching skills found'
