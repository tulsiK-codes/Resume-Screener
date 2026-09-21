import io
from pypdf import PdfReader

def extract_txt_pdf(pdf_bytes):
    """ Process raw PDF bytes and extracts text"""
    pdf_stream = io.BytesIO(pdf_bytes)
    reader = PdfReader(pdf_stream)
    pdf_txt = []
    for page in reader.pages:
        text = page.extract_text()
        if text:
            pdf_txt.append(text)
    return "\n".join(pdf_txt) #If pdf_txt empty then prints "" otherwise all pages with "\n" in between











# pdfPath = r"C:\Users\tulsi\Desktop\TulsiKumari-Documents\TULSI KUMARI-NEW_CV.pdf"
# def extract_text_from_pdf(path):
#     readpdf = PdfReader(path)
#     wholetxt = ""
#     for pgno, page in enumerate(readpdf.pages):
#         txt = page.extract_text()
#         wholetxt += txt + "\n"
#     return wholetxt

# def extract_text_from_pdf(path):
#     reader = PdfReader(path)
#     pages_txt = []
#     for page in reader.pages:
#         txt = page.extract_text()
#         if txt.strip():
#             pages_txt.append(txt)
#     return "\n".join(pages_txt)
# print(extract_text_from_pdf(pdfPath))



# EXPLORATORY CODE
# reader = PdfReader(r"C:\Users\tulsi\Desktop\CV Making Sample\Sample-Resume.pdf")

# print(f"Total Pages: {len(reader.pages)}")

# firstPg = reader.pages[0]
# firstPgText = firstPg.extract_text()
# print("----First Page----")
# print(firstPgText)

# for pageno, page in enumerate(reader.pages):
#     text = page.extract_text()
    # print(f"---Page {pageno + 1}---")
    # print(text)
