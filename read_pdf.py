from pypdf import PdfReader

reader = PdfReader("paper.pdf")
print("Number of pages:", len(reader.pages))

text = reader.pages[0].extract_text()
print(text[:500])
