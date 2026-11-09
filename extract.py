from pypdf import PdfReader

reader = PdfReader("paper.pdf")

full_text = ""
for page in reader.pages:
    full_text += page.extract_text() + "\n"

print("Pages:", len(reader.pages))
print("Total characters:", len(full_text))