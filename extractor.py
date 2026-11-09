from pypdf import PdfReader
from google import genai
from google.genai import types

# 1. Read the paper
reader = PdfReader("paper.pdf")
full_text = ""
for page in reader.pages:
    full_text += page.extract_text() + "\n"

# 2. The instructions we send to Gemini
prompt = """You are a Computer Science research assistant.
Using ONLY the paper text below, produce these sections:

1. CORE CONCEPT: the problem, the main method, and the key idea,
   in under 300 words, in plain simple language.

2. [FLOWCHART]: a valid Mermaid.js flowchart (graph TD) of the
   system: inputs, components or layers, and outputs.
   Write only the Mermaid text, with no code fences.

3. THREE PROJECT IDEAS for a 3rd-year CS student. For each give:
   the exact extension, the target metric, and the tech stack.

4. Metadata:
     Citations: (the paper text rarely says; write "Not in text")
     Authors: ...
     Publication: ...
     Year: ... (4 digits)
   Never invent values. If something is not in the text, write "Not in text".

PAPER TEXT:
"""

# 3. Call Gemini
client = genai.Client(http_options=types.HttpOptions(timeout=120000))
print("Calling Gemini...")
response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents=prompt + full_text
)

# 4. Save the result
with open("output.md", "w", encoding="utf-8") as f:
    f.write(response.text)
print("Done. Open output.md")