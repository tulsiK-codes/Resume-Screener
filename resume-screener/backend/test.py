from parser import extract_txt_pdf

pdf_path = r"C:\Users\tulsi\Desktop\TulsiKumari-Documents\TULSI KUMARI-NEW_CV.pdf"

with open(pdf_path, "rb") as file:
    raw_bytes = file.read() # Reads the file as pure binary data
extracted_txt_from_path = extract_txt_pdf(raw_bytes)
print(extracted_txt_from_path)

## Working