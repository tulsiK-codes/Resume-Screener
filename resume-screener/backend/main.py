from fastapi import FastAPI,Form, File, UploadFile #Core Framework where we'll build our apis
from pydantic import BaseModel
# Pydantic is a Python library used to define data models and validate/parse data using Python type annotations
 #BaseModel helps in data validation and structures and rules for request/response
from typing import List
from fastapi.middleware.cors import CORSMiddleware
from parser import extract_txt_pdf
from analyzer import analyzer_logic

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# app.frontend("/", directory="frontend", fallback="index.html")


# @app.post("/analyze")
# def analyze_endpoint():
#     return {"message": "Resume analysis endpoint working"}

@app.post("/analyze")
async def analyze_resume(
    jobDescription: str = Form(...),
    resumeFile: UploadFile = File(...)
    ): 
    raw_bytes = await resumeFile.read()
    resume_text = extract_txt_pdf(raw_bytes)
    analysis = analyzer_logic(resume_text, jobDescription)
    # analysis = analyse_resume(resume_text, jobDescription) # By mistake I gave the analyzer.py function and the ABOVE ENDPOINT THE SAME NAME, SO I was accidentally calling the async FastAPI endpoint function itself, not the function from analyzer.py 
    return {
        "resumeText" : resume_text,
        "jobDescription": jobDescription,
        "analysis": analysis
        } 

# NO jd.value as it is not javascript
# Just saying a string does not mean an input field from Form thus we specify here str = Form(...) 
#  UploadFile is a datatype, 








# Below we are creating model (in same file for simplicity). Normally we have 2 pydantic models- one for data coming in and other the data sent back

# class Tea(BaseModel): #Tea inherits from BaseModel
#     id: int
#     name: str
#     origin: str

# teas: List[Tea] = [] 
# #teas will hold collection of [id, name, origin] items

# # Decorators give special powers to a function
# @app.get("/")
# def read_root():
#     return {"message": "Welcome to Chai Bar"}

# @app.get("/teas")
# def teas_menu():
#     return teas

# @app.post("/teas")
# def add_tea(tea: Tea):
#     teas.append(tea)
#     return "Tea added successfully"

# @app.put("/teas/{tea_id}")
# # We are passing the tea_id we want to update and also the updated value with which we want to update
# def update_tea(tea_id: int, updated_tea: Tea):
#     for index,tea in enumerate(teas):
#         if tea.id == tea_id:
#             teas[index] = updated_tea
#             return "Tea updated"
#     return {"error": "Tea not found"}
    
# @app.delete("/teas/{tea_id}")
# def del_tea(tea_id: int):
#     for index,tea in enumerate(teas):
#         if tea.id == tea_id:
#             deleted = teas.pop(index)
#             return deleted
#     return {"error": "Tea not found"}