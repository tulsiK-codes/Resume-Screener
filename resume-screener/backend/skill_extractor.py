import re

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

skill_aliases = {
    "python": ["python"],
    "java": ["java"],
    "javascript": ["javascript", "java script", "js"],
    "c++": ["c++"],
    "c#": ["c#"],
    "html": ["html"],
    "css": ["css"],
    "typescript": ["typescript"],
    "react": ["react", "react.js"],
    "angular": ["angular"],
    "vue.js": ["vue.js", "vue"],
    "node.js": ["node.js", "nodejs"],
    "express.js": ["express.js", "express"],
    "fastapi": ["fastapi"],
    "django": ["django"],
    "sql": ["sql", "structured query language"],
    "mysql": ["mysql"],
    "postgresql": ["postgresql", "postgres"],
    "mongodb": ["mongodb", "mongo db"],
    "git": ["git"],
    "github": ["github"],
    "docker": ["docker"],
    "kubernetes": ["kubernetes", "k8s"],
    "aws": ["aws", "amazon web services"],
    "azure": ["azure", "microsoft azure"],
    "google cloud": ["google cloud", "gcp"],
    "data structures": ["data structures", "dsa"],
    "machine learning": ["machine learning", "ml"],
    "deep learning": ["deep learning", "dl"],
    "pandas": ["pandas"],
    "numpy": ["numpy"],
    "scikit-learn": ["scikit-learn", "sklearn"],
    "tableau": ["tableau"],
    "power bi": ["power bi"],
    "matplotlib": ["matplotlib"],
    "rest api": ["rest api", "restful api"],
    "oop": ["oop", "object-oriented programming"],
}

def extract_skills(text):
    matched_skills = set()

    text = text.lower()

    for skill in skills:
        pattern = r"(?<!\w)" + re.escape(skill) + r"(?!\w)"
        if re.search(pattern, text):
            matched_skills.add(skill)
    return matched_skills

# Expanded skills vocab
def extract_expanded_skills(text):
    text = text.lower()
    matched_skills = set()

    for canonical_skill, aliases in skill_aliases.items():
        for alias in aliases:
            pattern = (
                r"(?<!\w)"
                + re.escape(alias)
                + r"(?!\w)"
            )

            if re.search(pattern, text):
                matched_skills.add(canonical_skill)
                break
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

    