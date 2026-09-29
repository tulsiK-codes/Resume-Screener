from skill_extractor import extract_skills
from compare_skills import check_matched
from calculate_match import calculate_match_score


def analyzer_logic(resume_text, jobDescription):
    resume_skills = extract_skills(resume_text)
    required_skills = extract_skills(jobDescription)
    
    matched_skills, missing_skills = check_matched(
        resume_skills=resume_skills, 
        required_skills=required_skills
        )
    
    score = calculate_match_score(
        matched=matched_skills, required_skills=required_skills
        )
    return {
        "matchPercentage": score,
        "matchedSkills": list(matched_skills),
        "missingSkills": list(missing_skills),
        "resumeSkills": list(resume_skills),
        "requiredSkills": list(resume_skills)
    }