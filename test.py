from google import genai
from google.genai import types

client = genai.Client(http_options=types.HttpOptions(timeout=30000))

print("Calling the API...")
response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents="Explain what a research paper abstract is in one sentence."
)
print(response.text)