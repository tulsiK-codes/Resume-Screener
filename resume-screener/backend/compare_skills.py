def check_matched(resume_skills, required_skills):
    matched = set()
    missing = set()
    for skill in required_skills:
        if skill in resume_skills:
            matched.add(skill)
        else:
            missing.add(skill)
    # return (matched, missing) or matched, missing
    return [matched, missing]
