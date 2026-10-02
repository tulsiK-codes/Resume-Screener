def calculate_match_score(matched, required_skills):
    if not required_skills:
        return None
    matches = len(matched)
    tot_skill = len(required_skills)
    score = (matches/tot_skill) * 100
    # try:
    #     score = (matches/tot_skill) * 100
    # except ZeroDivisionError:
    #     print("Error: Divide by zero error")
    #     score = 0
    return round(score, 2)


