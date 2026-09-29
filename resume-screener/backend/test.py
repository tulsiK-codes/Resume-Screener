from parser import extract_txt_pdf
from skill_extractor import extract_skills
from compare_skills import check_matched
from calculate_match import calculate_match_score

pdf_path = r"C:\Users\tulsi\Desktop\TulsiKumari-Documents\TULSI KUMARI-NEW_CV.pdf"

with open(pdf_path, "rb") as file:
    raw_bytes = file.read() # Reads the file as pure binary data
extracted_txt_from_path = extract_txt_pdf(raw_bytes)
# print(extracted_txt_from_path)


text = """ Education: A degree in computer science or related hands-on coding experience.Front-End Skills: Strong knowledge of JavaScript, React, HTML, and CSS.Back-End Skills: Experience with server languages like Node.js, Python, or Ruby.Database Knowledge: Familiarity with SQL or NoSQL databases.Tools: Good working knowledge of Git for tracking code changes.Problem-Solving: Strong attention to detail and good communication skills"""
required_skills = extract_skills(text)
print(required_skills)

resume_skills = extract_skills(extracted_txt_from_path)
print(resume_skills)
matched, missing = check_matched(resume_skills=resume_skills, required_skills=required_skills)
print("Matched Skills: ",matched)
print("Missing skills: ",missing)

score = calculate_match_score(matched, required_skills)
print(score)

## Working
