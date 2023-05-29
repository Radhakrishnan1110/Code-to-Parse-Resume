import PyPDF2
import json
import re

#Creating dictionary
def extract_resume_data(file_path):
    resume_data = {
        "personal_details": {},
        "education": [],
        "experience": [],
        "projects": [],
        "technical_skills": []
    }

    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = len(pdf_reader.pages)

        # Extracting Personal Details
        page1_text = pdf_reader.pages[0].extract_text()
        personal_details = page1_text.split('\n')
        resume_data["personal_details"]["name"] = personal_details[0].strip()
        details = personal_details[1].strip().split("|")
        linkedin = details[0].split(":")[1].strip()
        phone_no = details[1].split(":")[1].strip()
        gmail = details[2].split(":")[1].strip()

        resume_data["personal_details"]["linkedin"] = linkedin
        resume_data["personal_details"]["phone_no"] = phone_no
        resume_data["personal_details"]["gmail"] = gmail

        # Extracting Education
        education_text = page1_text.split('EDUCATION')[1].split('EXPERIENCE')[0]
        education_details = education_text.split('\n')
        resume_data["education"] = [education.strip() for education in education_details if education.strip()]

        # Extracting Experience
        experience_text = page1_text.split('EXPERIENCE')[1].split('PROJECTS')[0]
        experience_details = experience_text.split('\n')
        resume_data["experience"] = [experience.strip() for experience in experience_details if experience.strip()]

        # Extracting Projects
        projects_text = page1_text.split('PROJECTS')[1]
        #projects_text = page1_text.split('PROJECTS')[1]
        projects_details = projects_text.split('\n')
        resume_data["projects"] = [project.strip() for project in projects_details if project.strip()]

        #Extractiong Technical skills
        skills_text = page1_text.split('TECHNICAL SKILLS')[1]
        skills_lines = skills_text.split('\n')
        resume_data["technical_skills"] = [line.strip() for line in skills_lines if line.strip()]


    return resume_data

# Example usage
file_path = "C:/Users/raman/OneDrive/Desktop/Sem 7/Radha_Krishnan_Resume.pdf"
resume_data = extract_resume_data(file_path)
print(json.dumps(resume_data, indent=5))
