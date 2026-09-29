def calculate_match_score(matched, required_skills):
    matches = len(matched)
    tot_skill = len(required_skills)
    try:
        score = (matches/tot_skill) * 100
    except ZeroDivisionError:
        print("Error: Divide vy zero error")
    return score


