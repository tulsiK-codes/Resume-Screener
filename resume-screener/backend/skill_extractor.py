import re
def extract_skills(text):
    skills = {
        "java",
        "javascript",
        "python",
        "sql",
        "html",
        "css",
        "react",
        "node.js",
        "fastapi",
        "git",
        "github",
        "mongodb",
        "mysql",
        "data structures",
        "machine learning",
        "natural language processing"
    }
    matched_skills = set()

    text = text.lower()

    for skill in skills:
        pattern = r"(?<!\w)" + re.escape(skill) + r"(?!\w)"
        if re.search(pattern, text):
            matched_skills.add(skill)
    return matched_skills

    # for word in text: 
    #     if word in skills:
    #         match_skills.add(word)
    
    # return match_skills
#for word in text: -> This line doesn't give me word from string,it gives one character at a time. Thus, we have the problem  
# Suppose we have
# skill = "java"
# text = "javascript"
# Then: "java" in "javascript" returns true, which is false match

